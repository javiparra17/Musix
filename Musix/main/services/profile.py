def edit_profile(musician, name, surname, username, description, photo, phone,
                 gender, country, city):
    user = musician.user
    user.firs_name = name
    user.last_name = surname
    user.username = username

    user.save()

    musician.description = description
    musician.photo = photo
    musician.phone = phone
    musician.gender = gender
    musician.country = country
    musician.city = city

    musician.save()

    return musician
