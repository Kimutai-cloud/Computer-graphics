import json
from typing import List, Dict, Any

def read_jsonline(FILEPATH: str) -> List[dict[str, Any]]:
    shape_coords = []

    with open(FILEPATH, 'r') as file:
        for line in file:
            try:
                data:json.loads(line)
                shape_coords.append(data)
                break
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON line: {e}")
                continue

    return shape_coords
