#Inheritence Examples.
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f"His name is {self.name} and he is {self.age} years old"
    
class Man(Human):
    gender = 'Male'
    no_of_men = 0

    def __init__(self, name, age, voice):
        super().__init__(name, age)
        self.voice = voice
        Man.no_of_men += 1
    
    def display(self):        #polymorphism
        string = super().display()
        return string + f" and his voice would be {self.voice} Which is defined as a {self.gender}"
    


someone = Man("Ahmed", 28, "hard")
print(someone.display())