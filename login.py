from pyscript import display, document

#signup
def signup_complete(e):
    username = document.querySelector('input[name="username"]').value
    email = document.querySelector('input[name="email"]').value
    password = document.querySelector('input[name="password"]').value
    alpha = password.isalpha()
    num = password.isdigit()

    if len(username) < 7:
        display(f'Your username is too short. Please add more characters.', target='output-login')
    
    elif len(password) < 10:
        display(f'Your password is too short. Please add more characters.', target='output-login')

    elif alpha == True:
        display(f'Your password must contain at least one number.', target='output-login')

    elif num == True:
        display(f'Your password must contain at least one letter.', target='output-login')

    else:
        display(f'User is succesfully logged in', target='output-login')
    
    #if (username.strip() and email.strip() and "@" in email and password.strip() and len(password) > 6 and len(username) > 9 and not alpha and not num):
        #document.getElementById("output-login").innerHTML = ''
        #display(f'''User is succesfully logged in''', target='output-login')
    #else:
        #document.getElementById("output-login").innerHTML = ''
        #display(f'''Please fill in all required fields correctly. Username must be at least 7 characters long. Password must contain at least one letter and one number, and must be at least 10 characters long.''', target='output-login')
#signup page end
