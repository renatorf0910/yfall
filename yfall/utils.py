# Utils def's
import re

def valid_password(senha):
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'
    if re.match(regex, senha):
        return True
    return False
