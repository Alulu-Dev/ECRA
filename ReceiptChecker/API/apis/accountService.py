from flask import request
from flask_restx import Namespace, Resource, fields
from werkzeug.utils import secure_filename
from tempfile import TemporaryDirectory
from flask_login import current_user, login_required

from ..core.userControl import (user_signup, delete_account,
                                get_customer, update_customer)

api = Namespace('account', description="Endpoint to create, update and delete accounts on the system")

profile_input = {
    'username': fields.String,
    'full name': fields.String,
    'password': fields.String,
}

profile_form = api.model('User', profile_input)



@api.route('/signup/user/')
class RegisterNewCustomer(Resource):
    @api.expect(profile_form)
    def post(self):
        """
        Create a system user account 
        """
        return user_signup(request), 201


@api.route('/user/')
class UserAccountControl(Resource):
    @api.doc("Get account details")
    @login_required
    def get(self):
        """
        Get account details
        """
        return get_customer(current_user.id)

    @api.doc("Remove account from the system by setting it's status to removed and "
             "deleting it after 30 days with all it's data")
    @login_required  # will be replaced by login_required
    def delete(self):
        """
        Remove account from the system
        """
        if delete_account(current_user.id):
            return "Account Deleted", 200
        else:
            return False, 400

    @api.doc("Update account details")
    @api.expect(profile_form)
    @login_required
    def put(self):
        """
        Modify account details
        """
        return update_customer(current_user.id, request.json), 400

