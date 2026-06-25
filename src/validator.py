from src.status import is_known_status

REQUIRED_FIELDS = ["name", "category", "status"]


def validate_miniapp_data(item: dict) -> bool:
    for field in REQUIRED_FIELDS:
        if not item.get(field):
            return False

    if not is_known_status(item.get("status", "")):
        return False

    return True
