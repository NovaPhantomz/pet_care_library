"""
Pet Care Tracker - Object Oriented System (Project 02)
Author: Amar Hassan

This module provides classes to manage pets, owners, recurring care tasks,
and vet records. It integrates logic from Project 01 by converting standalone
functions into instance methods on the Pet class.
"""

from datetime import date, timedelta
from typing import List, Dict, Optional, Tuple

from pet_utils import (
    validate_pet_age,
    validate_pet_weight,
    calculate_food_portion,
    calculate_walk_distance,
    format_reminder_message,
    log_care_event,
    generate_health_summary,
)


class Owner:
    """Represents a pet owner who can have multiple pets."""

    def __init__(self, name: str, email: Optional[str] = None):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Owner name must be a non-empty string.")
        self._name = name.strip()
        self._email = email
        self._pets: Dict[str, Pet] = {}

    @property
    def name(self):
        return self._name

    @property
    def pets(self) -> Tuple["Pet", ...]:
        return tuple(self._pets.values())

    def add_pet(self, pet: "Pet") -> None:
        if pet.name in self._pets:
            raise ValueError("A pet with this name already exists for this owner.")
        self._pets[pet.name] = pet

    def remove_pet(self, pet_name: str) -> None:
        if pet_name not in self._pets:
            raise ValueError("Pet not found.")
        del self._pets[pet_name]

    def __str__(self):
        return f"{self._name} — {len(self._pets)} pet(s)"

    def __repr__(self):
        return f"Owner(name={self._name!r}, pets={list(self._pets)})"


class VetRecord:
    """Stores vaccination and vet appointment history."""

    def __init__(self):
        self._vaccinations: List[str] = []
        self._appointments: List[str] = []

    def add_vaccination(self, name: str):
        self._vaccinations.append(name)

    def add_appointment(self, note: str):
        self._appointments.append(note)

    @property
    def appointments(self):
        return self._appointments

    def __str__(self):
        return f"{len(self._vaccinations)} vaccinations, {len(self._appointments)} vet visits"


class Schedule:
    """Handles recurrence for care tasks."""

    def __init__(self, every_days: int, start: date):
        if every_days <= 0:
            raise ValueError("Recurrence must be at least 1 day.")
        self._every_days = every_days
        self._start = start
        self._last_completed: Optional[date] = None

    def mark_completed(self, on: date):
        self._last_completed = on

    def next_due(self) -> date:
        base = self._last_completed or self._start
        return base + timedelta(days=self._every_days)

    def is_due(self, on: date) -> bool:
        return on >= self.next_due()

    def __str__(self):
        return f"every {self._every_days} day(s)"


class CareTask:
    """Represents a repeating care task such as feeding or walking."""

    def __init__(self, label: str, schedule: Schedule, notes: str = ""):
        self._label = label
        self._schedule = schedule
        self._notes = notes

    def complete(self, on: date):
        self._schedule.mark_completed(on)

    def is_due(self, on: date):
        return self._schedule.is_due(on)

    def next_due(self):
        return self._schedule.next_due()

    @property
    def label(self):
        return self._label

    def __str__(self):
        return f"{self._label} — next due {self.next_due()}"

    def __repr__(self):
        return f"CareTask({self._label!r})"


class Pet:
    """Represents a pet with tasks and vet records. Integrates Project 01 utilities."""

    def __init__(self, name: str, species: str, breed: str, weight_kg: float, age: float):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Pet must have a name.")
        validate_pet_age(age)
        validate_pet_weight(weight_kg)

        self._name = name.strip()
        self._species = species
        self._breed = breed
        self._age = float(age)
        self._weight_kg = float(weight_kg)

        self._tasks: Dict[str, CareTask] = {}
        self._vet = VetRecord()

    @property
    def name(self):
        return self._name

    @property
    def tasks(self):
        return tuple(self._tasks.values())

    @property
    def vet(self):
        return self._vet

    def add_task(self, task: CareTask):
        if task.label in self._tasks:
            raise ValueError("Task already exists for this pet.")
        self._tasks[task.label] = task

    def due_tasks(self, on: date):
        return [t for t in self._tasks.values() if t.is_due(on)]

    # ✅ Project 01 → now instance methods
    def food_portion(self, activity_level: str) -> float:
        return calculate_food_portion(self._weight_kg, activity_level)

    def walk_distance(self, duration: float, pace: float) -> float:
        return calculate_walk_distance(duration, pace)

    def reminder_message(self, task_label: str) -> str:
        return format_reminder_message(self._name, task_label)

    def log_event(self, event_type: str, notes: str):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        log_care_event(self._name, event_type, timestamp, notes)

    def health_summary(self) -> dict:
        return generate_health_summary(
            {"name": self._name, "age": self._age, "weight": self._weight_kg, "visits": self._vet.appointments}
        )

    def __str__(self):
        return f"{self._name} the {self._breed} ({self._species})"


class Tracker:
    """Manages multiple owners and finds tasks due on a specific day."""

    def __init__(self):
        self._owners: Dict[str, Owner] = {}

    def register_owner(self, owner: Owner):
        self._owners[owner.name] = owner

    def all_due(self, on: date):
        results = []
        for owner in self._owners.values():
            for pet in owner.pets:
                for task in pet.due_tasks(on):
                    results.append((owner.name, pet.name, task.label))
        return results

    def __str__(self):
        return f"Tracker with {len(self._owners)} owner(s)"
