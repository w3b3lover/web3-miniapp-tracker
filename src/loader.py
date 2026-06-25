import json
from pathlib import Path

from src.models import MiniApp
from src.validator import validate_miniapp_data


def load_miniapps(file_path: str):
    path = Path(file_path)

    if not path.exists():
        return []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    apps = []

    for item in data:
        if not validate_miniapp_data(item):
            continue

        apps.append(
            MiniApp(
                name=item.get("name", ""),
                category=item.get("category", ""),
                status=item.get("status", ""),
                ecosystem=item.get("ecosystem", ""),
                website=item.get("website", ""),
                notes=item.get("notes", ""),
                score=item.get("score", 0),
                tags=item.get("tags", [])
            )
        )

    return apps
