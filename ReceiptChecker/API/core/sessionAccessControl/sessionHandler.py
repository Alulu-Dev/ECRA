from flask_login import logout_user, login_user, current_user

from ..model import User


def login(name, passcode):
    """
        logging in user into the system
        """
    try:
        user = User.objects.get(code_name=name)
        # check user status before letting them log in
        if user.status == "Blocked":
            return "This account is blocked! please contact system Admins", 403
        elif user.status == "Deleted":
            return "This account no longer exists", 401
        elif user.password == passcode:
            login_user(user)

            return current_user.system_name
        else:
            raise ConnectionError

    except ConnectionError:
        return "Invalid login detail", 401


def logout():
    logout_user()
    return "user logged out", 202
