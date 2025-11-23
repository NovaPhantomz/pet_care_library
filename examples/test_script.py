# Simple demo script for Project 03

from datetime import date
from petcare import Owner, Dog, CareTask, Schedule, Tracker

# Create an owner
owner = Owner("Amar", email="amar@example.com")

# Create a pet (use Dog/Cat/Bird instead of Pet)
suki = Dog("Suki", "Pomsky", 13.6, 1.5)
owner.add_pet(suki)

# Add a recurring task
feed = CareTask("Breakfast", Schedule(every_days=1, start=date.today()), notes="Purina Pro")
suki.add_task(feed)

# Register the owner in the tracker
tracker = Tracker()
tracker.register_owner(owner)

# Print details
print("=== OWNER ===")
print(owner)

print("\n=== PET ===")
print(suki)
print("Daily food amount:", suki.daily_food_amount())
print("Daily exercise needed:", suki.daily_exercise_minutes())
print("Sound:", suki.sound())

print("\n=== TASK ===")
print(feed)
print("Due today? →", feed.is_due(date.today()))

print("\n=== TRACKER OUTPUT ===")
print(tracker.all_due(date.today()))
