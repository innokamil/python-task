import json
from typing import Any 
from pathlib import Path

def read_from_json(filename: str | Path) -> None | Any:
    with open(filename, "r") as obj:
        return json.loads(obj.read()) 

def read_from_xml(filename: str | Path) -> None | Any:
    with open(filename, "r") as obj:
        return obj.read()
