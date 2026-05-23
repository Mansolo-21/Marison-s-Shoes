def is_main_owner(user):

    return (
        user.is_authenticated and
        user.profile.role == 'owner'
    )


def is_side_owner(user):

    return (
        user.is_authenticated and
        user.profile.role == 'side_owner'
    )