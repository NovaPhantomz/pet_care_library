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
