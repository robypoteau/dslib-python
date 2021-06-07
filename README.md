[![Build Status](https://travis-ci.com/robypoteau/dslib-python.svg?branch=main)](https://travis-ci.com/robypoteau/dslib-python)

# Data Structure and Algorithms

The study and development of the canonical data structures.

# Objects and classes

In software development, one of the major paradigms, i.e., ways of thinking, is called object-oriented programming (OOP). In OOP, things with characteristics and behaviors are objects. These things can be concrete or abstract, including a person, a car, a calendar date, or a thought. Additionally, these objects need to have individuality; one person is different from another, just as one date is to another.

To construct an object in a program, we use a class. A class is a template for creating objects because objects have shared characteristics and shared behaviors. Moving forwards, we'll call these class characteristics properties and the class behaviors, methods.

When you use a class to make an object, this is called instantiation; this is why objects are also called instances [of a class].

# Principles of OOP

There are four principles to objected-oriented programming: 1) abstraction, 2) encapsulation, 3) inheritance, and 4) polymorphism.

Abstraction is about moving away from the details of one particular object and looking at the broader characteristics. For instance, a person might have the name Jennifer, but more generally, the individual has a name, and so do all persons. When you abstract, the goal is to find a model for the objects of interest, not for details specific to an individual. When we abstract, we are not interested in all the features of object, only the ones relevant to our use case.

Encapsulation is about controlling access to the internal elements of a class to prevent unexpected changes to those elements. Additionally, by encapsulating the inner workings of a class, the programmer needs only to focus on the input and the output of a class without needing to know the inner workings of that class.

Inheritance is about reusing code and consistency. Often classes share functionality and features. Instead of rebuilding the wheel, a programmer can "inherit" code from a previously constructed class and extend it if need be. Inheriting code helps prevent developers from updating the same code snippet in various classes and, by extension, helps keep implementation details consistent between similar classes. The class from which I inherit is my parent (or base) class, while the class that inherits from a parent class is called a child (or derived) class.

Polymorphism is about having "many forms" of the same methods. One case would be if two classes inherit from the same parent but have different implementation details for a given parent function. OOP languages have structures that enable you to override and extend functionality acquired from parent classes. Additionally, polymorphism encompasses the concept of overloading, which is when a class contains multiple methods with the same name but different inputs and or outputs.
