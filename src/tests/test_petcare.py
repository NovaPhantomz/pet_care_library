import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from datetime import date, timedelta

from petcare import (
    Pet,
    Dog,
    Cat,
    Bird,
    Owner,
    CareTask,
    Schedule,
    Tracker
)

class TestPetInheritance(unittest.TestCase):

    def test_dog_inherits_pet(self):
        d = Dog("Rex", "Husky", 20, 2)
        self.assertIsInstance(d, Pet)

    def test_cat_inherits_pet(self):
        c = Cat("Luna", "Tabby", 5, 3)
        self.assertIsInstance(c, Pet)

    def test_bird_inherits_pet(self):
        b = Bird("Sky", "Parrot", 1.2, 4)
        self.assertIsInstance(b, Pet)

class TestPolymorphism(unittest.TestCase):

    def test_polymorphic_sounds(self):
        pets = [
            Dog("A", "Breed", 5, 1),
            Cat("B", "Breed", 4, 2),
            Bird("C", "Breed", 1, 1)
        ]
        sounds = [p.sound() for p in pets]
        self.assertEqual(sounds, ["Woof!", "Meow!", "Chirp!"])

    def test_polymorphic_food_amounts(self):
        d = Dog("Suki", "Pomsky", 13, 2)
        c = Cat("Luna", "Tabby", 7, 3)

        # dogs eat more than cats (different calculate_food_portion results)
        self.assertNotEqual(d.daily_food_amount(), c.daily_food_amount())

class TestComposition(unittest.TestCase):

    def test_owner_stores_pet(self):
        owner = Owner("Amar", "amar@example.com")
        dog = Dog("Suki", "Pomsky", 13.6, 1.5)

        owner.add_pet(dog)
        self.assertIn(dog, owner.pets)

    def test_tracker_finds_due_tasks(self):
        owner = Owner("Amar")
        dog = Dog("Suki", "Pomsky", 13.6, 1.5)

        # Start date = today → due today
        task = CareTask("Breakfast", Schedule(every_days=1, start=date.today()))
        dog.add_task(task)
        owner.add_pet(dog)

        tracker = Tracker()
        tracker.register_owner(owner)

        due = tracker.all_due(date.today())

        # should include exactly 1 entry: ("Amar", "Suki", "Breakfast")
        self.assertEqual(len(due), 1)
        self.assertEqual(due[0][2], "Breakfast")

class TestSchedule(unittest.TestCase):

    def test_schedule_due_on_start_date(self):
        s = Schedule(every_days=1, start=date.today())
        self.assertTrue(s.is_due(date.today()))

    def test_schedule_due_on_next_cycle(self):
        yesterday = date.today() - timedelta(days=1)
        s = Schedule(every_days=1, start=yesterday)

        # after implementing "start date = first due", this works cleanly
        self.assertTrue(s.is_due(date.today()))

    def test_schedule_not_due_if_future(self):
        tomorrow = date.today() + timedelta(days=1)
        s = Schedule(every_days=2, start=tomorrow)
        self.assertFalse(s.is_due(date.today()))

class TestCareTask(unittest.TestCase):

    def test_task_due_today(self):
        task = CareTask("Walk", Schedule(1, date.today()))
        self.assertTrue(task.is_due(date.today()))

    def test_task_due_after_complete(self):
        task = CareTask("Feed", Schedule(1, date.today()))
        today = date.today()
        task.complete(today)

        # next due = today + 1
        self.assertFalse(task.is_due(today))
        self.assertTrue(task.is_due(today + timedelta(days=1)))

class TestPetMethods(unittest.TestCase):

    def test_pet_food_portion(self):
        dog = Dog("Suki", "Pomsky", 10, 2)
        self.assertGreater(dog.daily_food_amount(), 0)

    def test_pet_reminder(self):
        dog = Dog("Suki", "Pomsky", 10, 2)
        msg = dog.reminder_message("feed")
        self.assertIn("Reminder:", msg)
        self.assertIn("Suki", msg)

if __name__ == "__main__":
    unittest.main()
