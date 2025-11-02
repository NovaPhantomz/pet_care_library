# 🐾 Pet Care Tracker — Object-Oriented System (Project 02)

**Author:** Amar Hassan
**Course:** INST326 — Fall 2025

## 📘 Overview

This project evolves the Project 01 function library into a fully object-oriented system. Instead of using standalone functions to manage pets and care tasks, the system now uses classes that bundle data and behavior together.

The design focuses on:

* Encapsulation of pet and care task data
* Validation of input values
* Reuse of the Project 01 utility functions
* Clean class interactions for scheduling and reminders

## 🐶 Core Classes

| Class       | Responsibility                                           |
| ----------- | -------------------------------------------------------- |
| `Owner`     | Holds owner info and manages multiple pets               |
| `Pet`       | Stores pet attributes and provides care-related behavior |
| `CareTask`  | Represents recurring care tasks (feeding, walks, etc.)   |
| `Schedule`  | Calculates next due dates for recurring tasks            |
| `VetRecord` | Tracks vaccinations and vet appointments                 |
| `Tracker`   | Top-level manager for owners, pets, and tasks            |

## 🔄 Project 01 Integration

Logic from **Project 01** has been directly reused in instance methods of `Pet`, such as:

* Food portion calculation
* Walk distance estimation
* Reminder message formatting
* Event logging
* Health summary generation

This ensures clear continuity and demonstrates understanding of how functions translate to methods.

## 🧩 Example Usage

```python
from datetime import date
from petcare import Owner, Pet, CareTask, Schedule, Tracker

owner = Owner("Amar", email="amar@example.com")
suki = Pet("Suki", "dog", "Pomsky", weight_kg=13.6, age=1.5)
owner.add_pet(suki)

feed = CareTask("Breakfast", Schedule(every_days=1, start=date.today()), notes="Purina Pro")
suki.add_task(feed)

tracker = Tracker()
tracker.register_owner(owner)

print(tracker.all_due(date.today()))
```

## 📂 Repository Structure

```
/ (root)
├── petcare.py        # Main OOP class system
├── pet_utils.py      # Project 01 function library (reused)
├── docs/
│   └── class_design.md
└── README.md
```

## ✅ Status

Ready for use and extension in **Project 03** (Inheritance + Polymorphism).
