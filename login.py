from pyscript import display, document

#signup
def signup_complete(e):
    username = document.querySelector('input[name="username"]').value
    email = document.querySelector('input[name="email"]').value
    password = document.querySelector('input[name="password"]').value
    if username.strip() and email.strip() and "@" in email and password.strip() and password > 7:
        document.getElementById("output-login").innerHTML = ''
        display(f'''Is this information correct?
                Username: {username}, Email: {email}
                <input type="button" py-click="signup_confirm" value="Login">''', target='output-login')
    else:
        document.getElementById("output-login").innerHTML = ''
        display(f'''Please fill in all required fields correctly.
                    1. All fields are required,
                    2. Valid email,
                    3. Password is ≥8 characters.''', target='output-login')

def signup_confirm(e):
    document.getElementById("output-login").innerHTML = ''
    display(f'User is succesfully logged in. Proceed to the next section.', target='output-login')
#signup page end
