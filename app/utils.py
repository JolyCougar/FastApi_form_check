import re
from datetime import datetime
from email.utils import parseaddr
from typing import Dict


def is_email(value: str) -> bool:
    return "@" in parseaddr(value)[1]


def is_phone(value: str) -> bool:
    match = re.match(r"^\+7\d{3}\d{3}\d{2}\d{2}$", value)
    if match:
        return True
    else:
        return False


def is_date(value: str) -> bool:
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            datetime.strptime(value, fmt)
            return True
        except ValueError:
            continue
    return False


def determine_field_type(value: str) -> str:
    if is_date(value):
        return "date"
    elif is_phone(value):
        return "phone"
    elif is_email(value):
        return "email"
    else:
        return "text"


def match_template(data: Dict[str, str], templates: list) -> dict:
    best_match = None
    max_matches = 0

    for template in templates:
        match_count = 0
        all_fields_match = True

        for field, field_type in template["fields"].items():
            if field in data and determine_field_type(data[field]) == field_type:
                match_count += 1
            else:
                all_fields_match = False
                break

        if all_fields_match and match_count > max_matches:
            best_match = template
            max_matches = match_count

    return best_match
