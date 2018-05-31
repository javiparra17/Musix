def edit_profile(musician, name, surname, description, photo, phone,
                 gender, country, city):
    user = musician.user
    user.firs_name = name
    user.last_name = surname

    user.save()

    musician.description = description
    musician.photo = photo
    musician.phone = phone
    musician.gender = gender
    musician.country = country
    musician.city = city

    musician.save()

    return musician


def change_password(musician, new_password):
    user = musician.user

    user.set_password(new_password)
    user.save()

    musician.user = user
    musician.save()

    return musician
