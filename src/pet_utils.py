"""
pet_utils.py
Pet Care Function Library
Author: Amar Hassan
INST326 Project 01

This module contains simple utility functions to support pet care management.
"""

def validate_pet_name(name):
    """Check if a pet name is valid.
    
    Args:
        name (str): The name of the pet.
    
    Returns:
        bool: True if the name is valid, False otherwise.
    
    Raises:
        TypeError: If name is not a string.
    """
    if not isinstance(name, str):
        raise TypeError("Pet name must be a string.")
    return len(name.strip()) > 0

def validate_pet_age(age):
    """Check if a pet age is valid.
    
    Args:
        age (int or float): The age of the pet in years.
    
    Returns:
        bool: True if the age is valid, False otherwise.
    
    Raises:
        TypeError: If age is not a number.
    """
    if not isinstance(age, (int, float)):
        raise TypeError("Age must be a number.")
    return age > 0

def validate_pet_weight(weight):
    """Check if a pet weight is valid.
    
    Args:
        weight (float): The pet's weight in kilograms.
    
    Returns:
        bool: True if the weight is valid, False otherwise.
    
    Raises:
        TypeError: If weight is not a number.
    """
    if not isinstance(weight, (int, float)):
        raise TypeError("Weight must be a number.")
    return 0 < weight < 200

def format_reminder_message(pet_name, task):
    """Format a simple reminder message for a pet care task.
    
    Args:
        pet_name (str): The name of the pet.
        task (str): The task or reminder (e.g., "walk", "feed").
    
    Returns:
        str: A formatted reminder message.
    
    Raises:
        TypeError: If pet_name or task are not strings.
    """
    if not isinstance(pet_name, str) or not isinstance(task, str):
        raise TypeError("Both pet_name and task must be strings.")
    
    pet_name = pet_name.strip().capitalize()
    task = task.strip().lower()
    return f"Reminder: {task} {pet_name} today!"

def convert_minutes_to_hours(minutes):
    """Convert minutes into hours and minutes.

    Args:
        minutes (int): The total number of minutes.

    Returns:
        str: A formatted string representing hours and minutes.
    
    Raises:
        TypeError: If minutes is not an integer.
    """
    if not isinstance(minutes, int):
        raise TypeError("Minutes must be an integer.")
    hours = minutes // 60
    remaining = minutes % 60
    return f"{hours} hr {remaining} min"

def calculate_food_portion(weight, activity_level):
    """Estimate a pet's daily food portion in grams.

    Args:
        weight (float): The pet's weight in kilograms.
        activity_level (str): 'low', 'medium', or 'high'.

    Returns:
        float: The estimated daily food portion in grams.

    Raises:
        ValueError: If activity_level is invalid.
    """
    if not isinstance(weight, (int, float)):
        raise TypeError("Weight must be numeric.")
    if activity_level.lower() not in ["low", "medium", "high"]:
        raise ValueError("Activity level must be 'low', 'medium', or 'high'.")

    base = weight * 30  # base grams per kg
    if activity_level.lower() == "low":
        return base * 0.8
    elif activity_level.lower() == "medium":
        return base
    else:
        return base * 1.2

def calculate_next_vet_visit(last_visit_date):
    """Calculate the next vet visit date (1 year later).

    Args:
        last_visit_date (str): Date in 'YYYY-MM-DD' format.

    Returns:
        str: The next vet visit date.
    """
    from datetime import datetime, timedelta

    try:
        date_obj = datetime.strptime(last_visit_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date must be in 'YYYY-MM-DD' format.")

    next_visit = date_obj + timedelta(days=365)
    return next_visit.strftime("%Y-%m-%d")

def calculate_walk_distance(duration, pace):
    """Estimate walk distance based on time and pace.

    Args:
        duration (float): Duration in minutes.
        pace (float): Average walking speed in km/h.

    Returns:
        float: Estimated distance in kilometers.
    """
    if not all(isinstance(x, (int, float)) for x in [duration, pace]):
        raise TypeError("Both duration and pace must be numeric.")
    hours = duration / 60
    return round(pace * hours, 2)

def filter_pets_by_species(pet_list, species):
    """Return all pets of a given species.

    Args:
        pet_list (list): List of pet dictionaries.
        species (str): Desired species to filter by.

    Returns:
        list: Filtered list of pets.
    """
    if not isinstance(pet_list, list):
        raise TypeError("pet_list must be a list.")
    if not isinstance(species, str):
        raise TypeError("species must be a string.")
    return [pet for pet in pet_list if pet.get("species", "").lower() == species.lower()]

def generate_health_summary(pet_data):
    """Generate a summary of a pet's health data.

    Args:
        pet_data (dict): Contains 'name', 'age', 'weight', 'visits'.

    Returns:
        dict: Summary with basic health indicators.
    """
    if not isinstance(pet_data, dict):
        raise TypeError("pet_data must be a dictionary.")
    
    name = pet_data.get("name", "Unknown")
    age = pet_data.get("age", 0)
    weight = pet_data.get("weight", 0)
    visits = len(pet_data.get("visits", []))

    health_status = "Good"
    if weight <= 0 or age <= 0:
        health_status = "Needs attention"

    return {
        "name": name,
        "age": age,
        "weight": weight,
        "vet_visits": visits,
        "health_status": health_status
    }

def log_care_event(pet_name, event_type, timestamp, notes, log_file="care_log.txt"):
    """Append a care event to a log file.

    Args:
        pet_name (str): Pet's name.
        event_type (str): Type of event.
        timestamp (str): Time of event.
        notes (str): Any notes.
        log_file (str): File path to save the log.
    """
    with open(log_file, "a") as file:
        file.write(f"{timestamp} - {pet_name} - {event_type}: {notes}\n")

def calculate_average_activity(pet_logs):
    """Calculate average activity duration from logs.

    Args:
        pet_logs (list): List of durations in minutes.

    Returns:
        float: Average activity duration.
    """
    if not pet_logs:
        return 0.0
    total = sum(pet_logs)
    return round(total / len(pet_logs), 2)

def send_care_alerts(pet_data):
    """Simulate sending alerts for vet visits or feedings.

    Args:
        pet_data (list): List of dictionaries with pet info.

    Returns:
        list: Messages for each alert.
    """
    alerts = []
    for pet in pet_data:
        name = pet.get("name", "Unknown")
        needs_vet = pet.get("needs_vet", False)
        if needs_vet:
            alerts.append(f"Alert: {name} is due for a vet visit!")
        else:
            alerts.append(f"Reminder: Feed or walk {name} today.")
    return alerts

def export_pet_report(pet_data, output_path="pet_report.txt"):
    """Export a formatted pet report to a text file.

    Args:
        pet_data (list): List of pet dictionaries.
        output_path (str): Path to save the report.
    """
    with open(output_path, "w") as file:
        for pet in pet_data:
            name = pet.get("name", "Unknown")
            age = pet.get("age", "N/A")
            weight = pet.get("weight", "N/A")
            file.write(f"{name}, Age: {age}, Weight: {weight}\n")
