def calculate_xp(action: str, karma: int = 0) -> int:
    xp_map = {
        "create": 5,
        "accept": 10,
        "complete": 20,
        "thumbs_up": 5,
        "quest_complete": 50
    }
    return xp_map.get(action, 0) + karma
