class Nematode:
    def __init__(self, length: float, gender: str, age: str) -> None:
        self.length = length
        self.gender = gender
        self.age = age

    def __repr__(self) -> str:
        return "length in mm: {}, gender: {}, age: {}".format(
            self.length, self.gender, self.age)

    def __str__(self) -> str:
        return "length in mm: {},\ngender: {},\nage: {}".format(
            self.length, self.gender, self.age)
    
