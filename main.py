from pyscript import display, document

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