values = {
    0: {
        "keys": "A, E, I, O, U, L, N, R, S, T",
        "value": 1
    },
    1: {
        "keys": "F, H, V, W, Y",
        "value": 4
    },
    2: {
        "keys": "B, C, M, P",
        "value": 3
    },
    3: {
        "keys": "Q, Z ",
        "value": 10
    },
    4: {
        "keys": "D, G",
        "value": 2
    },
    5: {
        "keys": "J, X",
        "value": 8
    },
    6: {
        "keys": "K",
        "value": 5
    },
}


def score(word):
    total_value = 0
    for letter in word:
        for key in values.keys():
            keys = list(map(str.strip, values[key]["keys"].split(',')))

            if letter.upper() in keys:
                total_value += values[key]["value"]

    return total_value
