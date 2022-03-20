from flask_restx import Namespace, Resource
from flask_login import login_required

from API.core.sessionAccessControl import user_login, user_logout

api = Namespace('session', description="Endpoint to control system session")


@api.route('/login/<user_id>/<passcode>/')
class LoginSystems(Resource):
    @api.doc("Login external users")
    def post(self, system_id, passcode):
        return user_login(system_id, passcode)


@api.route('/logout/')
class LogoutSystems(Resource):
    @api.doc("Logout external users")
    @login_required
    def post(self):
        return user_logout
