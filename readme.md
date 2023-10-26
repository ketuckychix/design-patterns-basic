# Introduction
This is a repo for the design patterns video tutorial (https://www.youtube.com/watch?v=vNHpsC5ng_E&list=PLF206E906175C7E07)

The video is more for Java students, but the basic patterns apply cross languages.

# oop1.py (Inheritance, Encapsulation)
- cover basic Object Oriented Programming
-  when to use inheritance:
    - Is "className" a "super class"?
        - Example: Is a "Dog" an "Animal"?
    - Does "className" shares attribute with "Super class" 
        - Example: "Does "Dog" have a attribute called "name","height", "weight" with "Animal"?
- Don'ts: Do not use inheritance just to reuse code, or they don't have a superclass r/s.

# oop2.py
Polymporphism allows you to write methods that don't need to change if new subclasses are created.

- From ChatGPT:
    > Polymorphism is a concept in object-oriented programming that allows objects of different classes to be treated as if they were objects of the same class. This means that a method can be written to accept an object of a certain class, and it will work correctly when passed an object of any subclass of that class. This allows for more flexible and modular code, as new subclasses can be added without needing to modify existing code.

# mro.py
This python file is just to demonstrate multiple inheritance and its order.Also to introduce the mro() function that dictates the order of method resolution. This allows predictable and consistent order. 

Change the order of Parent1 and Parent2 in the class parameters to and compare the mro method difference!

You will see the following

Before: 
- [<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>]

After reodering to [Parent2, Parent1]
- [<class '__main__.Child'>, <class '__main__.Parent2'>, <class '__main__.Parent1'>, <class 'object'>]


# TODO:
- Strategy Design Pattern
- Observer Design Pattern
- Factory Design Pattern
- Abstract Factory Design Pattern
- Singleton Design Pattern
- Builder Design Pattern
- Prototype Design Pattern
- Decorator Design Pattern
- Command Design Pattern