from pyscript import display, document

#signup
def signup_complete(e):
    username = document.querySelector('input[name="username"]').value
    email = document.querySelector('input[name="email"]').value
    password = document.querySelector('input[name="password"]').value
    
    if username.strip() and email.strip() and "@" in email and password.strip() and len(password) > 7:
        document.getElementById("output-login").innerHTML = ''
        display(f'''User is succesfully logged in''', target='output-login')
    else:
        document.getElementById("output-login").innerHTML = ''
        display(f'''Please fill in all required fields correctly. Username must be at least 7 characters long. Password must contain at least one letter and one number, and must be at least 10 characters long.''', target='output-login')
#signup page end
