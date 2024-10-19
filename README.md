# CarClassPython

## Introduction

This project is an exact copy of my CarClass that I did only now it is written in Python. I wanted practice OOP on Python and wanted to see if I could replicate my Java project onto Python and was able to do so successfully.
## Project Structure

The project is organized into three main Python classes, each representing a key component of the car racing system:

1. `Cars.py`: The base class representing basic car information.
2. `Specs.py`: An extended class of Cars, adding specific performance details.
3. `Race.py`: The main class that runs the racing simulation and user interaction.


## Object-Oriented Programming Concepts Showcase

This project demonstrates several key OOP concepts:

1. **Inheritance**: The Specs class extends the Cars class, inheriting its properties and methods.

2. **Encapsulation**: Both Cars and Specs classes use private attributes with public getters and setters.

3. **Method Overriding**: The Specs class overrides the `displayCarInfo()` method from the Cars class.

4. **Polymorphism**: The Race class uses Specs objects, which are also Cars objects due to inheritance.

5. **Object Composition**: The Race class creates and manages multiple car objects.

6. **Access Modifiers**: Proper use of private and public access modifiers to control access to class members.

7. **Constructor Chaining**: The Specs class constructor calls the superclass constructor using `super()`.


# Note

I do NOT condone any sort of car racing especially on public roads. Save that for the track/dragstrip :)
