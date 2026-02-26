from pyscript import document

#  PLAYER DATA 
players = ["(1) Agena, Vada ","(2) Ala, Zipporah Alvarado","(3) Baring, Jaiyanah ","(4) Baylon, Koby Martin Eusebio","(5) Brodhagen, Alexandria Dominic R.","(6) Cabatingan, Jade Louisse Castro","(6) Cañete, Tarcisius John Coballes","(7) Dimaculangan, Zakari Dwayne U.","(8) Evangelista, Dwayne Kyle Bolante","(9) Galang, Charlize Liana Maceda","(10) Garabiles, Shalanie Lanette Galvez","(11) Gonzales, Amanda Mathea ","(12) Jamet, Frances Hailey Almoro","(13) Ledesma, Aisha Ashley Opallia","(14) Nacino, Samantha Gabrielle Dela Cruz","(15) Nardo, Kaitlyn Francesca Mandia","(16) Oliveros, Joaquin Rafael","(17) Olmedo, Cerinne Kimberlee ","(18) Ong, Raiden Bryce Chan","(19) Rebadulla, Samantha Erin ","(20) Reyes, David Miguel A.","(21) Sangreo, Vanna Marie  - Excused from Physical Activities","(22) Villafuerte, Lauren Mary ","(23) Villegas, Enzo Kelsey ","(24) Yao, Amanda Praise Kho",


]

# FUNCTION TO SHOW PLAYERS 
def show_players(e=None):

    
    html_list = "<h3>Player List</h3><ol class='list-group list-group-numbered'>"
    
    for player in players:  
        html_list += f"<li class='list-group-item'>{player}</li>"
    
    html_list += "</ol>"

    document.getElementById("player-output").innerHTML = html_list

   

