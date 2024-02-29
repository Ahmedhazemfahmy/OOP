from datetime import date
#Instance Methods
class Student:
    no_of_students = 0 
    def __init__(self,name , age, courses="none"):
        self.__name = name
        self.__age = age           #(1) here by adding the "__" before the variable it became Encapsulated
        self.__courses = courses   # No change can be done outside the Class except by the getter and setters only. 
        Student.no_of_students += 1

    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    

    def describe(self):
        print(f"My name is {self.__name} and i'm {self.__age} years old")
    
    def maturity(self):
        if self.__age == 30:
            print("Adult")
        elif self.__age < 30:        #That is called Instance Methods and only can take one (__init__)
            print("Student")
        elif self.__age > 30:
            print("ok")
        else:
            return 0


    @classmethod
    def birthyear(cls, name, year):                  #This is called Class Method 
        return cls(name, date.today().year - year)
student1 = Student("ahmed", 28, ['cs', 'html', 'python'])
student2 = Student("medhat", 31, ['Js', 'Angular', 'c#'])
student4 = Student.birthyear("hassa", 1996)


#more explanation over Class Methods 
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def veg(cls):
        return cls(['olives', 'onions', 'tomatos'])
    
    @classmethod
    def marg(cls):
        return cls(['cheese','extra cheese', 'vegetables'])
    def __str__(self):           # that is overridng the print method to be shown in a string rather than memory location
        return f"pizza ingredients are {self.ingredients}" #called Dunder method (double underscore)
pizza1= Pizza.marg()
pizza2= Pizza.veg()


#Static Methods: 
#used by calling the Class name + the method inside.
class Math:
    @staticmethod
    def add(x,y):
        return x+y
    
    @staticmethod
    def add5(num):
        return num +5
    
    @staticmethod
    def add10(num):
        return num+10
    
x = Math.add(5,15)
y = Math.add10(x)
z = Math.add5(y)

print(x,y,z)
