
from django.contrib.auth.models import User

def achievement_user_create_account(user):
    return True


def achievement_user_complete_activity(user):
    activities = user.user_profile.activities.all()
    if activities:
        return True
    return False