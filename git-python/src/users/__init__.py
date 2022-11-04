import logging


USERS_MAP = {
}


def map_user(email):
    if email in USERS_MAP:
        return USERS_MAP[email]
    logging.error('User %s not found' % email)
    return email