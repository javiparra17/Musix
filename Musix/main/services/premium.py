def become_premium(musician):
    if not musician.premium:
        musician.premium = True

        musician.save()
