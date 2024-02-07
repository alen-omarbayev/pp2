class myClass():
    def __init__(self):
        self.s=""
    def get_string(self):
        self.input_str=str(input())
    def print_string(self):
        print(self.input_str.upper())


a=myClass()
a.get_string()
a.print_string()