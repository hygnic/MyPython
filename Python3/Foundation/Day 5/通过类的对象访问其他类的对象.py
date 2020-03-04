# User: hygnic
# Date: 2018/9/6


class Teacher:
    def __init__(self, name, age):
        self.n = name
        self.a = age


class Course:
    def __init__(self, name, cost, teacher):
        self.n = name
        self.c = cost
        self.t = teacher


t1 = Teacher('lcc', 22)
c1 = Course('lbb', 21, t1)
print(c1.n)
print(c1.t)
print(c1.t.a)
print(c1.t.n)
