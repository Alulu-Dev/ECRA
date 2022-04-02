from mongoengine import ValidationError

from ..model import User


def create_new_customer(personal_info):
    try:
        print(personal_info)
        new_customer = User()
        new_customer.code_name = personal_info['username']
        new_customer.legal_name = personal_info['full name']
        new_customer.password = personal_info['password']
        
        new_customer.save()

    except ValidationError:
        return "Data cannot be Created", 500


def remove_customer_account(account_id):
    """
    * user can remove their account and
    * admins can remove users when they violate regulations
    will be updated to change status to deleted and once 30 days pass to actually delete the data
    """
    try:
        account = User.objects.get(id=account_id)
        account.delete()
        return True

    except ConnectionError:
        return "Data cannot be Removed", 500


def display_customer_account_details(account_id):
    try:
        account = User.objects.get(id=account_id)
        response = {
            'username': account.code_name,
            'official name': account.legal_name,
        }
        return {'user': response}
    except ValidationError:
        return "Data Couldn't Be Fetched", 500


def update_customer_account_details(account_id, new_data):
    try:
        account = User.objects.get(id=account_id)

        if 'username' in new_data and new_data['username'] != account.code_name:
            account.update(set__code_name= new_data['username'])
        if 'full name' in new_data and new_data['full name'] != account.legal_name:
            account.update(ser__legal_name=new_data['full name'])
        if 'password' in new_data and new_data['password'] != account.password:
            account.update(set__password=new_data['password'])

        display_customer_account_details(account_id)
    except ValidationError:
        return "Data Couldn't Be Fetched", 500
