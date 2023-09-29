import time

import requests
import uvicorn
import json
import multiprocessing
from uvicorn import Config, Server
from fastapi import FastAPI
from fastapi.requests import Request


class RestAPI:
    app = FastAPI()

    def __init__(self, database=None):
        self.database = database
        uvicorn_process = multiprocessing.Process(target=self.run_uv_server)
        uvicorn_process.start()
        time.sleep(1)

    def run_uv_server(self):
        config = Config(app=self.app, host="0.0.0.0", port=8000)
        server = Server(config)
        server.run()

    def get(self, url, payload=None):
        request_payload = {
            "database": self.database,
            "payload": payload
        }
        response = requests.get(f"http://localhost:8000{url}", json=request_payload)
        return json.dumps(response.json())

    def post(self, url, payload=None):
        request_payload = {
            "database": self.database,
            "payload": payload
        }
        response = requests.post(f"http://localhost:8000{url}", json=request_payload)
        return json.dumps(response.json())

    @staticmethod
    @app.get("/users")
    async def get_users(request: Request):
        try:
            body = await request.json()
            return body["database"]

        except Exception as error:
            print(error)

    @staticmethod
    @app.post("/add")
    async def add(request: Request):
        try:
            body = await request.json()
            payload = json.loads(body["payload"])

            user_body = {"name": payload["user"], "owes": {}, "owed_by": {}, "balance": 0.0}
            # body["database"]["users"].append(user_body)
            return user_body

        except Exception as error:
            print(error)


if __name__ == "__main__":  # type: ignore
    import uvicorn
