from app.models import User

# if a user exists with the given username, return false
def validate_new_username(username):
    user = User.query.filter_by(username=username).first()
    return not user

def validate_username_length(username):
    return len(username) > 4 and len(username) < 21

def validate_password_length(password):
    return len(password) > 4 and len(password) < 21

def validate_register_form(username, password):
    messages = []
    if not validate_new_username(username):
        messages.append("Username is not unique")
    if not validate_username_length(username):
        messages.append("Username must be between 5 and 20 characters")
    if not validate_password_length(password):
        messages.append("Password must be between 5 and 20 characters")
    return messages