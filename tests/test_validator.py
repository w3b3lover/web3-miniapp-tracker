from src.validator import validate_miniapp_data


def test_valid_miniapp_data():
    item = {
        "name": "Startale App",
        "category": "Super App",
        "status": "Testing"
    }

    assert validate_miniapp_data(item) is True


def test_invalid_miniapp_data():
    item = {
        "name": "",
        "category": "Game",
        "status": "Watching"
    }

    assert validate_miniapp_data(item) is False
