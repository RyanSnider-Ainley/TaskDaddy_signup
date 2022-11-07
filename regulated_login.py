import hashlib.sha256
import re

def regulate_password_parameter(password):
    return True if re.match('[A-Za-z0-9$&!]+$', password) else False

print(regulate_password_parameter())

