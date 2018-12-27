from datetime import date
from dataclasses import dataclass


@dataclass
class Person:

    first_name: str
    last_name: str
    birthday: date

