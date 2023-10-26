class Parent1:
    def method1(self):
        print("Method 1 from Parent1")

class Parent2:
    def method2(self):
        print("Method 2 from Parent2")

class Child(Parent1, Parent2):
    pass


if __name__ == "__main__":
    child = Child()
    child.method1()  # Calls method from Parent1
    child.method2()  # Calls method from Parent2
    print(Child.mro())  # Prints the method resolution order of Child
