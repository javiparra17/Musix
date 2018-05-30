def ban(musician):
    if not musician.banned:
        musician.banned = True
        musician.save()
    else:
        return "This musician is already banned"

    return musician


def unban(musician):
    if musician.banned:
        musician.banned = False
        musician.save()
    else:
        return "This musician is not banned"

    return musician
