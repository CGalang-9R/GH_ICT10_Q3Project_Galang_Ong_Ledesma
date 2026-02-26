from pyscript import document

#  PLAYER DATA 
players = ["Agena, Vada ","Ala, Zipporah Alvarado","Baring, Jaiyanah ","Baylon, Koby Martin Eusebio","Brodhagen, Alexandria Dominic R.","Cabatingan, Jade Louisse Castro","Cañete, Tarcisius John Coballes","Dimaculangan, Zakari Dwayne U.","Evangelista, Dwayne Kyle Bolante","Galang, Charlize Liana Maceda","Garabiles, Shalanie Lanette Galvez","Gonzales, Amanda Mathea ","Jamet, Frances Hailey Almoro","Ledesma, Aisha Ashley Opallia","Nacino, Samantha Gabrielle Dela Cruz","Nardo, Kaitlyn Francesca Mandia","Oliveros, Joaquin Rafael","Olmedo, Cerinne Kimberlee ","Ong, Raiden Bryce Chan","Rebadulla, Samantha Erin ","Reyes, David Miguel A.","Sangreo, Vanna Marie  - Excused from Physical Activities","Villafuerte, Lauren Mary ","Villegas, Enzo Kelsey ","Yao, Amanda Praise Kho",


]

# FUNCTION TO SHOW PLAYERS 
def show_players(e=None):

    
    html_list = "<h3>Player List</h3><ol class='list-group list-group-numbered'>"
    
    for player in players:  
        html_list += f"<li class='list-group-item'>{player}</li>"
    
    html_list += "</ol>"

    document.getElementById("player-output").innerHTML = html_list

   

