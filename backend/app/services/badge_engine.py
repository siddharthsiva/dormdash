def get_badge(xp: int, karma: int):
    if xp > 100 and karma > 50:
        return "Campus Hero"
    elif karma > 30:
        return "Reliable Rider"
    elif xp > 50:
        return "Speed Demon"
    return "Newbie"
