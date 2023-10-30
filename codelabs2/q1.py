import json #This module is used to work with JSON data

#The typing library is used to provide type hints for varibales, function parameters and return values. Usefull fro:  Code Readability, Enhanced IDE support and Static analysis.

from typing import List # To specify the return value as a list of dictionaries 
from typing import Dict # To specify the list contains dictionaries
from typing import Any # to specify that the dictionary can contain values of any type

def read_jsonline(FILEPATH: str) -> List[Dict[str, Any]]:
    shape_coords = []

    with open(FILEPATH, 'r') as file:
        for line in file:
            try:
                data:json.loads(line)
                shape_coords.append(data)
                break
            except json.JSONDecodeError as e: #Errors possible are FileNotFoundError, PermissionError and OSError as an invalid file path error.
                print(f"Error parsing JSON line: {e}")
                continue

    return shape_coords
