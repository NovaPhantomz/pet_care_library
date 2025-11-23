# 🐾 Pet Care Tracker — Project 03

**Advanced OOP: Inheritance, Polymorphism, Composition**

Author: **Amar Hassan**
Course: **INST326 — Fall 2025**

---

## 📘 Overview

This project builds on Projects 01 and 02 to create a more advanced, object-oriented pet care system.
Project 03 adds:

* Inheritance hierarchies
* Abstract Base Classes (ABC)
* Polymorphic behaviors
* Stronger composition relationships
* A more scalable and clean architecture

The system now models different types of pets (Dog, Cat, Bird) using inheritance while keeping familiar functionality from earlier projects such as owners, tasks, schedules, and vet records.

---

## 🧱 Core Architecture

### ✔️ Inheritance Hierarchy

```
Pet (Abstract Base Class)
 ├── Dog
 ├── Cat
 └── Bird
```

### ✔️ Why This Hierarchy?

The structure reflects natural "is-a" relationships:

* A Dog *is a* Pet
* A Cat *is a* Pet
* A Bird *is a* Pet

The base class `Pet` defines shared attributes and abstract behaviors that all pets must implement.

### ✔️ Abstract Methods in Pet (ABC)

All subclasses must override:

* `daily_food_amount()`
* `daily_exercise_minutes()`
* `sound()`

This enforces a consistent API while still allowing species-specific differences.

---

## 🔄 Polymorphism

Because Dog, Cat, and Bird all inherit from Pet, the system can treat all pets the same while producing different results.

### Example

```python
pets = [
    Dog("Suki", "Pomsky", 13.6, 1.5),
    Cat("Luna", "Siamese", 5, 2),
    Bird("Kiwi", "Parrot", 0.4, 1)
]

for p in pets:
    print(p.name, p.sound(), p.daily_food_amount())
```

Output:

```
Suki Woof! 544.0
Luna Meow! 150.0
Kiwi Chirp! 8.0
```

Same method calls → different behaviors.

---

## 🧩 Composition Relationships

The system heavily uses composition:

* An Owner **has** Pets
* A Pet **has** CareTasks
* A CareTask **has** a Schedule
* A Pet **has** a VetRecord
* A Tracker **has** Owners

These “has-a” relationships keep the design realistic, modular, and easy to maintain.

---

## 📂 Repository Structure

```
/
├── petcare.py              # Main OOP system with ABC + inheritance
├── pet_utils.py            # Project 01 utility functions
├── tests/
│   └── test_petcare.py     # Full Project 03 test suite
├── examples/
│   └── test_script.py      # Example usage script
└── docs/
    └── class_design.md     # Architecture document
```

---

## 💡 Example Usage

```python
from datetime import date
from petcare import Owner, Dog, CareTask, Schedule, Tracker

owner = Owner("Amar", "amar@example.com")

suki = Dog("Suki", "Pomsky", 13.6, 1.5)
owner.add_pet(suki)

task = CareTask("Breakfast", Schedule(1, date.today()))
suki.add_task(task)

tracker = Tracker()
tracker.register_owner(owner)

print(tracker.all_due(date.today()))
```

---

## 🧪 Testing

The test suite verifies:

* Abstract class enforcement (Pet cannot be instantiated)
* Subclass inheritance (Dog, Cat, Bird)
* Polymorphic methods
* Composition relationships
* Tracker functionality

Run tests:

```
python -m unittest tests/test_petcare.py
```

---

## 📝 Project Requirements Checklist

| Requirement               | Status                              |
| ------------------------- | ----------------------------------- |
| Inheritance hierarchy     | ✅ Implemented                       |
| ABC with abstract methods | ✅ Completed                         |
| Polymorphism              | ✅ Demonstrated                      |
| Composition               | ✅ Owner–Pet–Task–Schedule–VetRecord |
| Code quality              | ✅ Clean & organized                 |
| Test suite                | ✅ Included                          |
| Documentation             | ✅ README + architecture doc         |

---

## 🎯 Conclusion

This project demonstrates solid object-oriented design through:

* A meaningful inheritance hierarchy
* Real polymorphic behavior
* Use of abstract base classes
* Clean composition patterns
* A maintainable, extensible architecture

The system now models real-world pet care more accurately and follows the advanced OOP principles expected for Project 03 in INST326.
