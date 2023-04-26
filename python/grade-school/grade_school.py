class School:
    def __init__(self):
        self.classe = {}
        self.all_students = []

    def add_student(self, name, grade):
        student = {
            "name": name,
            "grade": grade
        }
        self.all_students.append(name)

        if grade in self.classe.keys():
            self.classe[grade].append(student)

        self.classe[grade] = []
        self.classe[grade].append(student)

    def roster(self):
        return sorted(self.all_students)

    def grade(self, grade_number):
        students_name = []
        for students in self.classe[grade_number]:
            students_name.append(self.classe[grade_number][students]["name"])
        return students_name
