class Member:
    """ a member of a university. """
    def __init__(self, name: str, address: str, email: str) -> None:
        """ Create a new member named name, with home and email address """
        self.name = name
        self.address = address
        self.email = email

    def __str__(self) -> str:
        """ return a string rep of this member. """
        return "{}\n{}\n{}".format(self.name, self.address, self.email)


class Faculty(Member):
    """ a faculty member at a university. """
    def __init__(self, name: str, address: str, email: str, faculty_num: str) -> None:
        super().__init__(name, address, email)
        self.faculty_number = faculty_num
        self.courses_teaching = []

    def __str__(self) -> str:
        """ return a string rep of this faculty. """
        member_string = super().__str__()
        return """{}\n{}\nCourses: {}""".format(
            member_string,
            self.faculty_number, " ".join(self.courses_teaching))

class Student(Member):
    """ A student member at a university. """
    def __init__(self, name: str, address: str, email: str, student_num: str) -> None:
        """ create a new student named name, with home and email address,
        student numer student_nu, an empty list of courses taken, and an
        empty list of current_courses
        """

        super().__init__(name, address, email)
        self.student_number = student_num
        self.courses_taken = []
        self.courses_taking = []
