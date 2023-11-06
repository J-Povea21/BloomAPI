def read_user_response(db_user):
    message = 'User found!' if db_user else 'User not found'
    return {'user': db_user, 'message': message}

def user_added_response(userCreated):
    message = 'User added!' if userCreated else 'The username is already taken'
    return {'status': userCreated, 'message': message}