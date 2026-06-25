from dataclasses import dataclass, field


@dataclass
class MiniApp:
    name: str
    category: str
    status: str
    ecosystem: str = ""
    website: str = ""
    notes: str = ""
    score: int = 0
    tags: list[str] = field(default_factory=list)
