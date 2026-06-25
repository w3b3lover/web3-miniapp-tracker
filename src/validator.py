REQUIRED_FIELDS = ["name", "category", "status"]


def validate_miniapp_data(item: dict) -> bool:
    for field in REQUIRED_FIELDS:
        if not item.get(field):
            return False

    return True
