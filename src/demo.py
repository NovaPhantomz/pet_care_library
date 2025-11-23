from datetime import date
from petcare import Owner, Dog, CareTask, Schedule

owner = Owner("Amar", "amar@example.com")

# Create a Dog (Pet is now abstract)
suki = Dog("Suki", "Pomsky", 13.6, 1.5)
owner.add_pet(suki)

task = CareTask("Breakfast", Schedule(every_days=1, start=date.today()))
suki.add_task(task)

print(owner)
print(suki)
print(task)
print("Due today? →", task.is_due(date.today()))
