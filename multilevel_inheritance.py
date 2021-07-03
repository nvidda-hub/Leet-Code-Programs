class Student:
    no_of_leaves = 10

    def __init__(self, sname, srole, sage):
        self.name = sname
        self.age = sage
        self.role = srole

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split('-'))

    def print_details(self):
        return f"{self.name}, {self.age} and {self.role}"


class Player(Student):
    no_of_leaves = 15

    def __init__(self, sname, srole, sage, sgame):
        super(Player, self).__init__(sname, srole, sage)
        self.game = sgame

    def print_details(self):
        return f"{self.name}, {self.age} and {self.role}. He playes {self.game}"

class Teacher(Player):
    no_of_leaves = 30
    def __init__(self, sname, sage, srole, sgame, ssubject):
        super(Teacher, self).__init__(sname, sage, srole, sgame)
        self.subject = ssubject

    def print_details(self):
        return f"{self.name}, {self.age} and {self.role}. He playes {self.game}. He teaches {self.subject}"
s1 = Student.from_dash("Narendra-25-student")
p1 = Player.from_dash("Yadav-25-student-Cricket")
t1 = Teacher.from_dash("Basudev-45-teacher-watching TV-Social Science")


print(t1.print_details())

