from pyscript import document

#  PLAYER DATA 
players = ["(1) Agena, Vada ","(2) Ala, Zipporah Alvarado","(3) Baring, Jaiyanah ","(4) Baylon, Koby Martin Eusebio","(5) Brodhagen, Alexandria Dominic R.","(6) Cabatingan, Jade Louisse Castro","(6) Cañete, Tarcisius John Coballes","(7) Dimaculangan, Zakari Dwayne U.","(8) Evangelista, Dwayne Kyle Bolante","(9) Galang, Charlize Liana Maceda","(10) Garabiles, Shalanie Lanette Galvez",
"(11) Gonzales, Amanda Mathea ",
"Jamet, Frances Hailey Almoro",
"Ledesma, Aisha Ashley Opallia",
"Nacino, Samantha Gabrielle Dela Cruz",
"Nardo, Kaitlyn Francesca Mandia",
"Oliveros, Joaquin Rafael",
"Olmedo, Cerinne Kimberlee ",
"Ong, Raiden Bryce Chan",
"Rebadulla, Samantha Erin ",
"Reyes, David Miguel A.",
"Sangreo, Vanna Marie  - Excused from Physical Activities",
"Villafuerte, Lauren Mary ",
"Villegas, Enzo Kelsey ",
"Yao, Amanda Praise Kho",


]

# FUNCTION TO SHOW PLAYERS 
def show_players(e=None):

    
    html_list = "<h3>Player List</h3><ol class='list-group list-group-numbered'>"
    
    for player in players:  
        html_list += f"<li class='list-group-item'>{player}</li>"
    
    html_list += "</ol>"

    document.getElementById("player-output").innerHTML = html_list

   

