from pyscript import document

#  PLAYER DATA 
players = [
    "Dimaculangan",
    "Baylon",
    "Evangelista",
    "Villegas",
    "Reyes",
    "Gonzales",
     "Yao",
      "Olmedo",
      "Baring",
      "Broadhagen",
      "Canete",
]

# FUNCTION TO SHOW PLAYERS 
def show_players(e=None):

    
    html_list = "<h3>Player List</h3><ol class='list-group list-group-numbered'>"
    
    for player in players:  # loop through each player
        html_list += f"<li class='list-group-item'>{player}</li>"
    
    html_list += "</ol>"

    document.getElementById("player-output").innerHTML = html_list

    # Optional: hide button after click
    if e:
        e.target.style.display = "none"
        e.target.style.display = "none"

