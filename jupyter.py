class Human():
    def __init__(self, name, father_name, cnic):
        self.name = name 
        self.father_name= father_name
        self.cnic = cnic
    def printer(self):
        print('this is a human')

class Student(Human):
        def __init__(self, name, father_name, cnic , rollnumber):
            super().__init__(name, father_name,cnic)
            self.rollnumber = rollnumber
        # def eat(self):
        #     print(self.name, 'Is eating', self.program)
def showdetails(self):
    print ('name',self.name ,'father Name', self.father_name , 'cnic', self.cnic)



class Teacher(Human):
        def __init__(self, name, father_name, cnic , id):
            super().__init__(name, father_name,program)
            self.id = id

class Admin(Human):
        def __init__(self, name, father_name, cnic, designation):
            super().__init__(name, father_name,cnic)
            self.designation = designation

# st = Student('Innam', 'm jaffar','eaing bryani')
# st2 = Student('ali', 'hamza sheikh', 'zinger')
# st3 = Student ('jaish' , 'asad' , 'jelly')
# st.eat()
# st2.eat()
# st3.eat()

st = Student (' jaish', "asad", '42201-32662576-9', 98)