from pyscript import document

#  PLAYER DATA 
players = ["Zak", 
           "Koby", 
           "Dwayne",
           "Enzo", 
           "David", 
           "Joaquin"]

# FUNCTION TO SHOW PLAYERS 
def show_players(e=None):
    
    html_list = "<h3>Player List</h3><ol class='list-group list-group-numbered'>"
    
    for player in players: 
        html_list += f"<li class='list-group-item'>{player}</li>"
    
        html_list += "</ol>"
    
        document.getElementById("player-output").innerHTML = html_list
