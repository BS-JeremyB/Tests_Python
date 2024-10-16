import re
def email_valide(email):
    regex_email = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(regex_email, email)