class Animal:
    def __init__(self, name, type, age) -> None:
        self.name = name
        self.type = type
        self.age = age
    def walk(self):
        print("Walking...")

class Dog(Animal):
    def __init__(self, name, type, age) -> None:
        super().__init__(name, type, age)
    # ghi de phuong thuc (overriding)
    def walk(self):
        print("Dog is walking...")
    def __str__(self) -> str:
        return self.name + ", " + self.type + ", " + str(self.age)

# tao object
dog1 = Dog("kiki", "Chihuahua", 3)
dog1.walk()
print(dog1.__str__())
# dog1.a() # error no attribute

# class Cat: kế thừa từ Animal 
# hàm getName trả về tên của object cat
class Cat(Animal):
    def __init__(self, name, type, age) -> None:
        super().__init__(name, type, age)
        
    def getName(self):
        return self.name
