from pyscript import document

# PLAYER DATA 
players = [
    {"name": "Koby", "section": "RUBY"},
    {"name": "PlACE HOLDER NAME", "section": "EMERALD"},
    {"name": "PlACE HOLDER NAME", "section": "SAPPHIRE"},
    {"name": "PlACE HOLDER NAME", "section": "TOPAZ"},
    {"name": "PlACE HOLDER NAME", "section": "RUBY"},
    {"name": "PlACE HOLDER NAME", "section": "EMERALD"}
]

# FUNCTION TO SHOW PLAYERS 
def show_players(e=None):
    """Use a loop to generate the player list dynamically."""
    html_list = "<h3>Player List</h3><ul class='list-group'>"
    
    for player in players:  # loop through each player
        html_list += f"<li class='list-group-item'>{player['name']} - {player['section']}</li>"
    
    html_list += "</ul>"

    document.getElementById("player-output").innerHTML = html_list

    # Optional: hide button after click
    if e:
        e.target.style.display = "none"
