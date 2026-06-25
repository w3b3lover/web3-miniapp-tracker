import json
from pathlib import Path

from src.models import MiniApp


def load_miniapps(file_path: str):
    path = Path(file_path)

    if not path.exists():
        return []

    data = json.loads(path.read_text(encoding="utf-8"))

    apps = []

    for item in data:
        apps.append(
            MiniApp(
                name=item.get("name", ""),
                category=item.get("category", ""),
                status=item.get("status", ""),
                ecosystem=item.get("ecosystem", ""),
                website=item.get("website", ""),
                notes=item.get("notes", ""),
                tags=item.get("tags", [])
            )
        )

    return apps
