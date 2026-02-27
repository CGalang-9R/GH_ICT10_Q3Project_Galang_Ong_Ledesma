from pyscript import display, document

#signup
def signup_complete(e):
    document.getElementById("output-login").innerHTML = ' '
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
