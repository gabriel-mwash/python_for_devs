class Member:
    def __init__(self, name: str, email: str, address: str):
        self.name = name
        self.email = email
        self.address = address

    def __repr__(self):
        return "name: {}, email: {}, address: {}".format(
            self.name, self.email, self.address)



class Student(Member):
    def __init__(self, name: str, address: str, email: str, student_num: str) -> None:
        super().__init__(name, email, address)
        self.student_num = student_num
        self.courses_taken = []
        self.courses_taking = []

    def __str__(self):
        return "stud_name : {}, stud_address : {}\n, \
student_email: {}\n, stud_num: {}\n, courses_taken: {}\n,\
courses_taking: {}\n".format(self.name, self.address, self.email, self.student_num,
                             self.courses_taken, self.courses_taking)
    def __repr__(self):
        return "name: {}, email: {}, address: {}, student_num: {}, courses_taken: {}, courses_taking: {}".format(
            self.name, self.email, self.address, self.student_num, self.courses_taken,
            self.courses_taking)


class Faculty(Member):
    def __init__(self, name: str, address: str, email: str, faculty_num: str) -> None:
        super().__init__(name, email, address)
        self.faculty_num = faculty_num
        self.courses_teaching = []
        
    def __repr__(self):
        return "name: {}, email: {}, address: {}, faculty_number: {}, courses_teaching: {}".format(
            self.name, self.email, self.address, self.faculty_num,
            self.courses_teaching)
