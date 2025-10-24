def check_badges(user):
    badges = []
    if user.karma >= 100:
        badges.append("Karma King")
    if user.xp >= 500:
        badges.append("XP Master")
    # Add more badge logic here
    return badges
