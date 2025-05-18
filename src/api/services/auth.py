from common.config import settings


def get_all_creds():
    creds = []

    admin = {
        "username": settings.admin_username,
        "password": settings.admin_password,
    }

    creds.append(admin)
    return creds
