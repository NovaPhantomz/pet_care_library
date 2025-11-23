# 📄 **Project 03 — Architecture & Design Document**

**Pet Care Tracker — Advanced OOP (Inheritance, Polymorphism, Composition)**
Author: **Amar Hassan**
Course: **INST326 — Fall 2025**

---

## 🧱 **1. Overview**

This document explains the object-oriented architecture of the Pet Care Tracker system as redesigned for Project 03.
The system builds on previous work by introducing:

* **Inheritance hierarchies**
* **Abstract Base Classes (ABC)**
* **Polymorphism**
* **Meaningful “has-a” composition relationships**
* **Modular class design that scales**

The goal was to transform the simpler Project 02 system into a richer, extensible OOP architecture while keeping the core functionality (tasks, schedules, owners, care events) intact.

---

## 🐾 **2. Inheritance Hierarchy**

Project 03 introduces the following inheritance structure:

```
Pet (Abstract Base Class)
 ├── Dog
 ├── Cat
 └── Bird
```

### ✔️ Why this hierarchy works

This hierarchy follows natural real-world relationships:

* A **Dog is a Pet**
* A **Cat is a Pet**
* A **Bird is a Pet**

The base `Pet` class defines shared attributes:
name, breed, weight, age, tasks, veterinarian record.

It also defines abstract behaviors that *all* pets must implement, but in different ways.

---

## 🧩 **3. Abstract Base Class (Pet)**

The `Pet` class is an **ABC** using Python’s `abc` module.
It enforces a common interface through abstract methods:

```python
@abstractmethod
def daily_food_amount(self): ...

@abstractmethod
def daily_exercise_minutes(self): ...

@abstractmethod
def sound(self): ...
```

### Purpose of abstraction

* Ensures all pets provide these behaviors
* Guarantees polymorphic method calls work
* Prevents direct instantiation of `Pet`
* Provides a common parent type for collections

This enforces clean and consistent API design across all pet subclasses.

---

## 🐶 **4. Subclasses: Dog, Cat, Bird**

Each subclass inherits attributes from `Pet` but **overrides the abstract methods** to implement species-specific logic:

### Example differences

* **Dog** requires more exercise and more food
* **Cat** requires moderate exercise and less food
* **Bird** requires minimal exercise and very small portions
* Each produces a different `sound()` output

### Why these overrides matter

This creates **real polymorphic behavior**, allowing the system to treat all pets the same while still producing unique results for each species.

---

## 🔄 **5. Polymorphism**

Because Dog, Cat, and Bird all inherit from Pet and override the same methods, any code that uses a `Pet` reference can call:

* `daily_food_amount()`
* `daily_exercise_minutes()`
* `sound()`

…without knowing which specific subclass it is.

### Example

```python
pets = [Dog(...), Cat(...), Bird(...)]
for p in pets:
    print(p.sound(), p.daily_food_amount())
```

This produces different results even though the interface is identical — a key demonstration of polymorphism for the project.

---

## 🏗️ **6. Composition Relationships**

Project 03 also uses strong, meaningful composition:

### Owner → Pet

An owner “has” pets.
Owners store pets in an internal dictionary for quick lookup.

### Pet → CareTask

Pets “have” tasks such as feeding, walking, grooming.

### CareTask → Schedule

Tasks include a Schedule object that determines recurrence.

### Pet → VetRecord

Each pet “has” a personal veterinarian record.

### Tracker → Owner

The top-level system aggregates multiple owners to find due tasks.

### Why composition instead of inheritance?

* Owners are not pets
* Tasks are not pets
* Schedules are not tasks
* Vet records are not pets

Using composition avoids forced or illogical inheritance structures and keeps responsibilities focused.

---

## 📊 **7. Class Responsibilities Overview**

### **Pet (Abstract)**

* Shared data fields: name, breed, weight, age
* Stores tasks and vet record
* Defines abstract behaviors
* Integrates Project 01 utility functions

### **Dog / Cat / Bird**

* Concrete implementations of Pet
* Food, exercise, and sound behavior

### **Owner**

* Manages one or more pets
* Accessor to view all pets

### **CareTask**

* Represents a recurring pet care task
* Delegates scheduling to Schedule

### **Schedule**

* Recurrence: every N days
* Tracks last completion date
* Calculates next due date

### **VetRecord**

* Tracks vaccinations and appointments

### **Tracker**

* Holds multiple owners
* Retrieves all tasks due on a given day

---

## 🧪 **8. Testing Strategy (Summary)**

Your test suite verifies:

* Pet cannot be instantiated (ABC enforcement)
* Dog/Cat/Bird correctly inherit from Pet
* Polymorphism: each species returns different outputs
* Owner–Pet–Task–Schedule composition functions
* Tracker still returns correct due tasks

This ensures correctness and alignment with INST326 Project 03 requirements.

---

## 📐 **9. Design Justification**

### Why Inheritance?

* Natural “is-a” model
* Encourages code reuse
* Abstract methods force consistent behavior
* Supports polymorphism cleanly

### Why Polymorphism?

* Allows unified handling of different pets
* Reduces branching logic
* Makes the system extensible (add new animals easily)

### Why Composition?

* Models realistic relationships
* Keeps classes small and single-responsibility
* Prevents unnatural inheritance (e.g., Schedule ≠ Pet)

### Why ABCs?

* Prevents misuse of the base class
* Enforces consistent subclass behavior
* Encourages safe extension of the system

---

## 🧭 **10. Conclusion**

Project 03 transforms the Pet Care Tracker from a basic object system into a robust, extensible architecture using:

* **Abstract base classes**
* **Inheritance**
* **Polymorphism**
* **Composition**
* **Clean separation of responsibilities**
