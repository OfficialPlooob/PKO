3-6-2022

Currently as this program stands, it is fully functional to keep track of a Progressive Knockout Tournament game. However, there might be some slight qualify of life issues (like lack of labels provided in the table to know what each value is) or needed adjustment in some of the code to run perfectly (might not be the perfect logic in the function to check for valid name inputs; program still works but inputting a name for the top box and not the bottom doesn't spit the right error message). 

Aside from that, the description for each function will be listed here: 

Fee Entry:
    Input the entry fee into the entry box provided under the label and clicking 'Set the entry fee' will lock in the desired entry fee as a double variable. If you accidentally made a mistake, you can always change it using 'Change the entry fee'
    
Enter Name:
    Input the names of every player participating into the entry box provided under the label and clicking 'Set the player name', this will put the player into a list of player names. If you think you have all the players for the game, then clicking 'Initialize players' will create player objects holding their name, knocks, bounty, earnings, and status.
    
    The format of player information will look like this:
        ex. 
            "John" [   ] 50.0 0.0 "In"
            

In order to keep track of the game actions, clicking 'Start the game' will allow you to keep track of who got knocked out and who knocked the player out. Each input of the names will adjust the highest bounty amount and update the table created below.
    
4-5-2022

Once again, the program is functional. However, there is a slight issue on formatting the table. I can't figure out how to get the 
formatting to work like the setwidth() function in C++. 


Explanation for buttons:
  Knockout - Input two names, for who got knocked out and who did it. 
  Rebuy - Allow someone to rejoin the game when they got knocked out.
  New Player - Add in a new player mid-game.
  Remove Player - Remove a player from the player name list before the game starts (just in-case you input a name wrong). 
  
  Set the player name - Input a name into the list of players before the game.
  Initialize players - Create the list of initial players (core members of the game). 
  
  Set the entry fee - Set the entry fee/buy-in for the tournament.
  Change the entry fee - Change the entry fee/buy-in before the tournament begins. 


    

