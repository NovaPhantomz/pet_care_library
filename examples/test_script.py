import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))





from src.pet_utils import (
    validate_pet_name,
    validate_pet_age,
    validate_pet_weight,
    format_reminder_message,
    convert_minutes_to_hours,
    calculate_food_portion,
    calculate_next_vet_visit,
    calculate_walk_distance,
    filter_pets_by_species,
    generate_health_summary,
    log_care_event,
    calculate_average_activity,
    send_care_alerts,
    export_pet_report,
)

print("=== SIMPLE FUNCTIONS ===")
print(validate_pet_name("Suki"))                  # True
print(validate_pet_age(3))                        # True
print(validate_pet_weight(25))                    # True
print(format_reminder_message("luna", "feed"))    # Reminder: feed Luna today!
print(convert_minutes_to_hours(130))              # 2 hr 10 min

print("\n=== MEDIUM FUNCTIONS ===")
print(calculate_food_portion(10, "medium"))       # about 300.0
print(calculate_next_vet_visit("2024-10-12"))     # 2025-10-12
print(calculate_walk_distance(60, 5))             # 5.0
pets = [
    {"name": "Suki", "species": "dog"},
    {"name": "Luna", "species": "cat"},
    {"name": "Max", "species": "dog"},
]
print(filter_pets_by_species(pets, "dog"))        # [{'name': 'Suki', ...}, {'name': 'Max', ...}]

print("\n=== COMPLEX FUNCTIONS ===")
pet_data = {"name": "Suki", "age": 3, "weight": 15, "visits": ["2024-01-01", "2025-01-01"]}
print(generate_health_summary(pet_data))          # summary dict

log_care_event("Luna", "feeding", "2025-10-12 08:00", "Fed half portion")
print("Logged a care event.")

activity_logs = [20, 30, 40, 50]
print(calculate_average_activity(activity_logs))  # 35.0

pet_list = [
    {"name": "Suki", "needs_vet": True},
    {"name": "Luna", "needs_vet": False},
]
print(send_care_alerts(pet_list))                 # alert list

export_pet_report(pets)
print("Pet report exported to pet_report.txt")
