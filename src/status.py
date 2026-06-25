KNOWN_STATUSES = [
    "Testing",
    "Reviewing",
    "Watching",
    "Researching",
    "Learning",
    "Archived"
]


def normalize_status(status: str) -> str:
    return status.strip().title()


def is_known_status(status: str) -> bool:
    return normalize_status(status) in KNOWN_STATUSES
