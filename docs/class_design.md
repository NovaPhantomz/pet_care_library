# Class Design Document — Pet Care Tracker (Project 02)

**Author:** Amar Hassan
**Course:** INST326 — Fall 2025

## Overview

This project takes the pet care function library from Project 01 and turns it into a full object-oriented program. Instead of having separate functions, the program now uses classes that keep data and related actions together. This setup makes more sense because in real life, owners care for pets, pets have tasks, and those tasks happen on schedules.

## Class Responsibilities

| Class         | What It Does                                                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Owner**     | Stores owner information and manages one or more pets.                                                                                     |
| **Pet**       | Holds pet attributes (name, species, breed, age, weight), manages care tasks, and tracks vet history. Also uses Project 01 care functions. |
| **CareTask**  | Represents recurring tasks like feeding, walking, or giving medication.                                                                    |
| **Schedule**  | Calculates when a task is next due based on how often it repeats.                                                                          |
| **VetRecord** | Stores vaccination records and past vet appointment history.                                                                               |
| **Tracker**   | Coordinates multiple owners and lists tasks that are due across the system.                                                                |

## Encapsulation and Validation

Most attributes are stored as private variables (for example, `_name` and `_weight_kg`) to prevent unwanted changes. Properties are used to safely access and update values. The `Pet` class also reuses validation functions from Project 01, like checking that age and weight are reasonable, which keeps things consistent.

## Project 01 Integration

Key functions from Project 01 are now instance methods inside the `Pet` class:

| Project 01 Function         | New Method                          | Purpose                                              |
| --------------------------- | ----------------------------------- | ---------------------------------------------------- |
| `calculate_food_portion()`  | `pet.food_portion(activity_level)`  | Uses the pet's actual weight to estimate daily food. |
| `calculate_walk_distance()` | `pet.walk_distance(duration, pace)` | Estimates walk distance based on time and pace.      |
| `format_reminder_message()` | `pet.reminder_message(task_label)`  | Creates friendly reminder messages.                  |
| `log_care_event()`          | `pet.log_event(event_type, notes)`  | Logs pet-related events with timestamps.             |
| `generate_health_summary()` | `pet.health_summary()`              | Provides a quick health overview for the pet.        |

This shows a clear shift from **function-based code to object-based code**, which is the main goal of Project 02.

## Future Extensions (Project 03 Preparation)

This system is ready to be expanded in Project 03 using inheritance and polymorphism. Possible extensions include:

* Subclasses like `Dog(Pet)` and `Cat(Pet)`
* Specialized tasks like `MedicationTask(CareTask)`
* Custom `__str__()` output for different pet types

The current structure allows new features to be added without rewriting the entire system.
