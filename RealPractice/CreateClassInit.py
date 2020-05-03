class StudentClassInit:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def print_data(self):
        print("The name of student is ", self.name)
        print("The branch of student is ", self.branch)

s1 = StudentClassInit("Suman", "MSIT")
s1.print_data()
