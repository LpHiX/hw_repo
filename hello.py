class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Teacher(Human):
    def __init__(self, name, age, subject):
        Human.__init__(self, name, age)
        self.subject = subject

    def get_subject(self):
        return self.subject

    jugador = "It worked!"


test = Teacher(1, 2, 3)
print(test.get_subject())
print(test.jugador)