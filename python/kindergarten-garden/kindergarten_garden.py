import re

students_name = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph",
                 "Kincaid", "Larry"]

plants = {
    "G": "Grass",
    "C": "Clover",
    "R": "Radishes",
    "V": "Violets",
}


class Garden:
    def __init__(self, diagram, students=None):
        if students is None:
            students = students_name
        self.diagram = diagram
        self.students = sorted(students)

    def plants(self, student):
        plants_student = []

        rows = self.diagram.split("\n")
        row1 = re.findall('..', rows[0])
        row2 = re.findall('..', rows[1])

        word = row1[self.students.index(student)] + row2[self.students.index(student)]

        for letter in word:
            plants_student.append(plants[letter])

        return plants_student
