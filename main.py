from pyscript import display, document

#signup
def signup_complete(e):
    username = document.querySelector('input[name="username"]').value
    email = document.querySelector('input[name="email"]').value
    password = document.querySelector('input[name="password"]').value
    if username.strip() and email.strip() and "@" in email and password.strip() and password >= 8:
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

def intrams(e):
    document.getElementById('output').innerHTML = ' '

    reg = document.querySelector('input[name="registration"]:checked').value
    cle = document.querySelector('input[name="clearance"]:checked').value
    gr = document.getElementById('grade').value
    sct = document.getElementById('section').value.upper()

    if reg == 'No':
        display(f'Please register online to be able to join the Intramurals.', target='output')
    
    elif cle == 'No':
        display(f'Please get a medical clearance from the clinic to be able to join the Intramurals.', target='output')

    
    elif sct == 'RUBY':
        display(f'Congratulations! You are part of the Blue Bears!', target='output')
        document.getElementById("image").innerHTML = "<img src= 'blue_bears.jpg'height='300' width='300'>"

    elif sct == 'EMERALD':
        display(f'Congratulations! You are part of the Yellow Tigers!', target='output')
        document.getElementById("image").innerHTML = "<img src= 'yellow_tigers.jpg' height='300' width='300'>"

    elif sct == 'SAPPHIRE':
        display(f'Congratulations! You are part of the Red Bulldogs!', target='output')
        document.getElementById("image").innerHTML = "<img src= 'red_bulldogs.jpg' height='300' width='300'>"

    elif sct =='TOPAZ':
        display(f'Congratulations! You are part of the Green Hornets!', target='output')
        document.getElementById("image").innerHTML = "<img src= 'green_hornets.jpg' height='300' width='300'>"

    else:
        display(f'Please double check your inputs and try again.', target='output')
