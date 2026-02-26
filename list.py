from pyscript import document

# PLAYER DATA
players = [
    {"name": "Koby", "section": },
    {"name": "Enzo", "section": },
    {"name": "Dwayne", "section": },
    {"name": "Zak", "section": },
    {"name": "David", "section": },
    {"name": "Joaquin", "section": }
]

# FUNCTION TO SHOW PLAYERS USING A LOOP
def show_players(event=None):
    html = "<h3>Player List</h3>"
    html += "<ul class='list-group'>"

    # LOOP through players with numbering
    for index, player in enumerate(players, start=1):
        html += f"<li class='list-group-item'>"
        html += f"{index}. {player['name']} - {player['section']}"
        html += "</li>"

    html += "</ul>"

    document.getElementById("player-output").innerHTML = html

    if event:
        event.target.style.display = "none"
