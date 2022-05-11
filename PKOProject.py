import tkinter
from tkinter import *
from tkinter import messagebox

"""
This is for creating new players, initialize the values with
name, knocks, bounty, and earnings.
"""
class createPlayer:
    def __init__(self, name, knocks, bounty, earnings, status):
        self.name = name
        self.knocks = knocks
        self.bounty = bounty
        self.earnings = earnings
        self.status = status

"""
The GUI itself and other functions:
"""
class pokerGUI:
    def __init__(self, root):
        self.master = root
        self.master.title("PKO Tournament Organizer")
        # Initialize variables that we need:
        self.entryFee = DoubleVar()  # Store the entry fee in this variable
        self.playerName = StringVar()  # Store the player name in this variable
        self.playerNameList = []  # Store the names of the players
        self.initCount = IntVar()  # Store the count of player initialization
        self.hBounty = DoubleVar()  # Store the highest bounty in here
        self.playerInfo = [] # Store the player information in this variable
        self.loserBountyKeep = DoubleVar()
        self.hBountyName = StringVar()
        self.hBountyNameKeep = StringVar()
        self.hBountyKeep = DoubleVar()
        # Creating the GUI widgets:
        self.entryFeeTitle = Label(self.master, text="Entry fee:")
        self.entryFeeTitle.grid(row=0, column=0, sticky=N, padx=20)
        self.entryFeeEntry = Entry(self.master, width=26)
        self.entryFeeEntry.grid(row=1, column=0, sticky=N, padx=20)
        self.entryFeeButton = Button(self.master, text="Set the entry fee", command=self.setFee, width=22)
        self.entryFeeButton.grid(row=2, column=0, sticky=N, padx=20)
        self.entryFeeChange = Button(self.master, text="Change the entry fee", command=self.changeFee, width=22)
        self.entryFeeChange.grid(row=3, column=0, sticky=N, padx=20)

        self.enterName = Label(self.master, text="Enter name:")
        self.enterName.grid(row=0, column=1, sticky=N)
        self.enterNameEntry = Entry(self.master, width=26)
        self.enterNameEntry.grid(row=1, column=1, sticky=N)
        self.enterNameButton = Button(self.master, text="Set the player name", command=self.setName, width=21)
        self.enterNameButton.grid(row=2, column=1, sticky=N)
        self.initPlayersButton = Button(self.master, text="Initialize players", command=self.initPlayerValues, width=21)
        self.initPlayersButton.grid(row=3, column=1, sticky=N)

        self.prizePoolTitle = Label(self.master, width=17, text="Current Prize Pool:")
        self.prizePoolTitle.grid(row=0, column=3, sticky=W, padx=10)
        self.prizePoolEntry = Entry(self.master)
        self.prizePoolEntry.grid(row=1, column=3, sticky=W, padx=10)
        self.prizePoolEntry['state'] = 'disabled'

        self.highestBountyTitle = Label(self.master, width=17, text="Highest Bounty:")
        self.highestBountyTitle.grid(row=2, column=3, sticky=W, padx=10)
        self.highestBountyEntry = Entry(self.master)
        self.highestBountyEntry.grid(row=3, column=3, sticky=W, padx=10)
        self.highestBountyEntry['state'] = 'disabled'

        self.knockOutButton = Button(self.master, text="Knockout", command=self.keepTrackWindow,width=11)
        self.knockOutButton.grid(row=0, column=4, sticky=W)
        self.rebuyPlayerButton = Button(self.master, text="Rebuy", command=self.rebuy,width=11)
        self.rebuyPlayerButton.grid(row=1, column=4, sticky=W)
        self.addNewPlayer = Button(self.master, text="New player", command=self.newPlayer, width=11)
        self.addNewPlayer.grid(row=2, column=4, sticky=W)
        self.removePlayer = Button(self.master, text="Remove player", command=self.deletePlayer, width=11)
        self.removePlayer.grid(row=3, column=4, sticky=W)
        self.endGameButton = Button(self.master, text= "End game", command=self.endGame,width=11)
        self.endGameButton.grid(row=4, column=4, sticky=W)
        # Text Box for output:
        self.outputInfoTitle = Label(self.master, text="Game information:")
        self.outputInfoTitle.grid(row=5, column=1, sticky=N)
        self.outputInfo = Text(self.master, width=90, height=24)
        self.outputInfo.grid(row=6, columnspan=5, sticky=W, padx=40, pady=5)
        # Player list box:
        self.playerBoxTitle = Label(self.master, text= "Player list:")
        self.playerBoxTitle.grid(row=5, column=6, sticky=N)
        self.playerBox = Text(self.master, width=40, height=24)
        self.playerBox.grid(row=6, column = 6,sticky=W)

    def endGame(self): # Function to end the game
        self.inCount = IntVar() # Count the amount of players in

        # Get the amount of "In" players:
        for x in self.playerInfo:
            if x.status == "In":
                self.inCount.set(self.inCount.get()+1)

        if self.inCount.get() == 1: # There's only 1 person left
            newWindow5  = Toplevel(pokerRoot)

            self.final = Text(newWindow5, width=150, height=50)
            self.final.grid(row=0, column=0)

            for x in self.playerInfo:
                if x.status == "In":
                    self.final.insert(tkinter.END, x.name + " has won $" + str(x.bounty+x.earnings+((self.entryFee.get() / 2.0) * len(self.playerNameList))) + " | ($" + str(x.bounty) + " was from bounties, $" + str(x.earnings) + " was from earnings, $" + str((self.entryFee.get() / 2.0)*len(self.playerNameList)) + " was from the total prize pool.)\n")
                else:
                    self.final.insert(tkinter.END, x.name + " has won $" + str(x.bounty+x.earnings) + " | ($" + str(x.bounty) + " was from bounties, $" + str(x.earnings) + " was from earnings.)\n")

    def deletePlayer(self): # Function to create a window to delete a player from the pre-game list
        newWindow4 = Toplevel(pokerRoot)
        newWindow4.geometry("280x90")

        self.getName = StringVar()
        # Getting the player information:
        self.label = Label(newWindow4, text="What's the name of the player you want to remove?")
        self.label.grid(row=0, column=0)
        self.entry = Entry(newWindow4, textvariable=self.getName)
        self.entry.grid(row=1, column=0)
        # Button
        self.button = Button(newWindow4, text="Submit name", command=self.deleteFromList)
        self.button.grid(row=4, column=0)

    def deleteFromList(self): # Function to delete a player from the pre-game list
        if self.initCount.get() == 0:
            if self.getName.get() != "":  # Check if blank entries are being put in
                if self.getName.get() in self.playerNameList:
                    self.playerNameList.remove(self.getName.get())

                    self.playerBox.delete('1.0', END)
                    for x in self.playerNameList:
                        self.playerBox.insert(tkinter.END, x + "\n")
                else:
                    messagebox.showerror("Error!", "This name does not exist in the player name list. Try again.")
            else:
                messagebox.showerror("Error!", "Please put a name into this field. Try again.")
        else:
            messagebox.showerror("Error!", "The game has already started. You can no longer remove players.")

    def newPlayer(self): # Function to create a window to create a new player
        newWindow3 = Toplevel(pokerRoot)
        newWindow3.geometry("195x90")

        self.getName = StringVar()
        # Getting the player information:
        self.label = Label(newWindow3, text="What's the name of the new player?")
        self.label.grid(row=0, column=0)
        self.entry = Entry(newWindow3, textvariable=self.getName)
        self.entry.grid(row=1, column=0)
        # Button
        self.button = Button(newWindow3, text="Submit name", command=self.newPlayerInit)
        self.button.grid(row=4, column=0)

    def newPlayerInit(self): # Function to create a new player mid-game
        if self.initCount.get() == 1:
            if self.getName.get() != "":  # Check if blank entries are being put in
                if self.getName.get() in self.playerNameList:
                    messagebox.showerror("Error!", "This player name already exists in the list of players.")
                else:
                    self.playerNameList.append(self.getName.get()) # Make sure for other functions that utilize the name list to input the new player's name
                    self.newList = []
                    self.cP = createPlayer(self.getName.get(), self.newList, (self.entryFee.get() / 2.0), 0.0, "In")
                    self.playerInfo.append(self.cP)  # Push the new player into the list of player objects

                    # Output the prize pool to the box:
                    self.prizePoolEntry['state'] = 'normal'
                    self.prizePoolEntry.delete(0, END)
                    self.prizePoolEntry.insert(0, (self.entryFee.get() / 2.0) * len(self.playerNameList))
                    self.prizePoolEntry['state'] = 'disabled'


                    self.playerBox.delete('1.0', END)
                    for x in self.playerNameList:
                        self.playerBox.insert(tkinter.END, x + "\n")

                    self.outputNewTable() # Show the new table
            else:
                messagebox.showerror("Error!", "Please input a name into the field. Try again.")
        else:
            messagebox.showerror("Error!", "You cannot add new players like this before the game starts.")

    def rebuy(self):
        newWindow2 = Toplevel(pokerRoot)  # A separate window needs to be defined using the parent root, pokerRoot.
        newWindow2.geometry("250x90")

        self.getRebuy = StringVar()
        # Getting the player information:
        self.label = Label(newWindow2, text="What's the name of the player who rebuying?")
        self.label.grid(row=0, column=0)
        self.entry = Entry(newWindow2, textvariable=self.getRebuy)
        self.entry.grid(row=1, column=0)
        # Button
        self.button = Button(newWindow2, text="Submit name", command=self.reInit)
        self.button.grid(row=4, column=0)

    def reInit(self): # Function that allows the user to let people back into the game.
        if self.getRebuy.get() != "": # Check if blank entries are being put in
            if self.getRebuy.get() in self.playerNameList: # Check if the players exist
                self.rebuyIndex = self.playerNameList.index(self.getRebuy.get())

                if self.playerInfo[self.rebuyIndex].status == "Out":
                    self.playerInfo[self.rebuyIndex].status = "In"
                    self.playerInfo[self.rebuyIndex].bounty = (self.entryFee.get()/2.0)
                    self.outputNewTable()
                else:
                    messagebox.showerror("Error!", "This player is still in.")
            else:
                messagebox.showerror("Error!", "The name does not exist in the list of players. Try again.")
        else:
            messagebox.showerror("Error!", "Please input a name into the field. Try again.")

    def setFee(self):  # Function to set the fee value
        if self.initCount.get() == 1:
            messagebox.showerror("Error!", "You can not change the entry fee anymore.")
        else:
            if self.entryFeeEntry.get() == "":
                messagebox.showerror("Error!", "Please enter an entry fee amount.")
            else:
                self.entryFee.set(float(self.entryFeeEntry.get()))
                self.entryFeeEntry[
                    'state'] = 'disabled'  # We do not want to be able to change the fee amount after setting it.

    def changeFee(self):  # Function to restore the state of the set fee entry box
        if self.initCount.get() == 1:
            messagebox.showerror("Error!", "You can not change the entry fee anymore.")
        else:
            self.entryFeeEntry['state'] = 'normal'

    def setName(self):  # Function to set the name of a player
        if self.initCount.get() == 1:
            messagebox.showerror("Error!", "You can not input anymore names.")
        else:
            if self.enterNameEntry.get() == "":
                messagebox.showerror("Error!", "Please enter a name.")
            else:
                self.playerName.set(self.enterNameEntry.get())
                self.playerNameList.append(self.playerName.get())
                self.enterNameEntry.delete(0, END)

                self.playerBox.delete('1.0', END)
                for x in self.playerNameList:
                    self.playerBox.insert(tkinter.END, x + "\n")

    def initPlayerValues(self):  # Function to initialize the default values for players given the entry fee:
        if len(self.playerNameList) == 0:
            messagebox.showerror("Error!", "There are no players to initialize.")
        else:
            if self.initCount.get() == 1:
                messagebox.showerror("Error!", "You cannot initialize the list of players again!")
            else:
                for name in self.playerNameList:
                    self.newList = []
                    self.cP = createPlayer(name, self.newList, (self.entryFee.get() / 2.0), 0.0, "In")
                    self.playerInfo.append(self.cP)  # Push the new player into the list of player objects

                self.initCount.set(
                    self.initCount.get() + 1)  # Set the initialization count to 1 to indicate the players are set

                self.enterNameEntry['state'] = 'disabled'
                # Output the prize pool to the box:
                self.prizePoolEntry['state'] = 'normal'
                self.prizePoolEntry.insert(0, (self.entryFee.get() / 2.0) * len(self.playerNameList))
                self.prizePoolEntry['state'] = 'disabled'
                # Output the highest bounty to the box:
                self.hBountyName.set("Several people: ")
                self.hBountyNameKeep.set("Several people: ")
                self.highestBountyEntry['state'] = 'normal'
                self.highestBountyEntry.insert(0, self.hBountyNameKeep.get() + str(self.entryFee.get() / 2.0))
                self.hBounty.set(self.entryFee.get()/2.0)
                self.highestBountyEntry['state'] = 'disabled'

                self.outputNewTable()  # Output the table

    def keepTrackWindow(self):  # Function to create a separate window to keep track of player actions:
        newWindow = Toplevel(pokerRoot)  # A separate window needs to be defined using the parent root, pokerRoot.
        newWindow.geometry("290x140")
        self.getLoser = StringVar()  # String variable that will hold the name of the player that was knocked
        self.getWinner = StringVar()  # String variable that will hold the name of the player that knocked

        # Getting the player information:
        self.label = Label(newWindow, text="What's the name of the player who was knocked out?")
        self.label.grid(row=0, column=0)
        self.entry = Entry(newWindow, textvariable=self.getLoser)
        self.entry.grid(row=1, column=0)

        self.label2 = Label(newWindow, text="What's the name of the player who knocked")
        self.label2.grid(row=2, column=0)
        self.entry2 = Entry(newWindow, textvariable=self.getWinner)
        self.entry2.grid(row=3, column=0)

        self.button = Button(newWindow, text="Submit names", width=15,command=self.keepTrack)
        self.button.grid(row=4, column=0)
        self.button2 = Button(newWindow, text="Undo last entry",width=15, command=self.undo)
        self.button2.grid(row=5, column=0)

    """
    Use this for reference on the undo button:
    Things that get changed are:
        - Knocks
        - Bounty
        - Status
    """
    def undo(self): # Function will undo the actions of the Knockout function
        # Get the indexes of the last loser/winner and undo everything
        # Loser:
        self.playerInfo[self.loserIndex].bounty = self.loserBountyKeep.get()
        self.playerInfo[self.loserIndex].status = "In"

        # Winner:
        self.playerInfo[self.winnerIndex].bounty -= (self.playerInfo[
                                                         self.loserIndex].bounty) / 2.0
        self.playerInfo[self.winnerIndex].earnings -= (self.playerInfo[
                                                           self.loserIndex].bounty) / 2.0
        self.playerInfo[self.winnerIndex].knocks.remove(" " + self.playerInfo[self.loserIndex].name + " ")

        # Undo any changes to highest bounty
        self.hBounty.set(self.hBountyKeep.get())
        self.highestBountyEntry['state'] = 'normal'
        self.highestBountyEntry.delete(0, END)
        self.highestBountyEntry.insert(0, self.hBountyNameKeep.get() + ": $" + str(self.hBountyKeep.get()))
        self.highestBountyEntry['state'] = 'disabled'

        self.outputNewTable()  # Output the new table

    def keepTrack(self):  # Function to keep track of the players in the game
        if self.getLoser.get() or self.getWinner.get() != "":  # Check if blank entries are being put in
            if self.getLoser.get() in self.playerNameList and self.getWinner.get() in self.playerNameList:  # Check if the players exist
                if self.getLoser.get() != self.getWinner.get():  # Check if the same inputs are being put in
                    # Get the indexes of the "loser" and the "winner":
                    self.loserIndex = self.playerNameList.index(self.getLoser.get())
                    self.winnerIndex = self.playerNameList.index(self.getWinner.get())
                    # Check the status of the players to see if their actions are valid or not:
                    if self.playerInfo[self.loserIndex].status == "Out" or self.playerInfo[
                        self.winnerIndex].status == "Out":
                        messagebox.showerror("Error!", "This player is already out.")
                    else:
                        # Save information just incase we have to undo:
                        self.loserBountyKeep.set(self.playerInfo[self.loserIndex].bounty)
                        self.hBountyKeep.set(self.hBounty.get())
                        self.hBountyNameKeep.set(self.hBountyName.get())

                        # Winner:
                        self.playerInfo[self.winnerIndex].bounty += (self.playerInfo[
                                                                            self.loserIndex].bounty) / 2.0
                        self.playerInfo[self.winnerIndex].earnings += (self.playerInfo[
                                                                              self.loserIndex].bounty) / 2.0
                        self.playerInfo[self.winnerIndex].knocks.append(" " + self.playerInfo[self.loserIndex].name + " ")

                        # Loser:
                        self.playerInfo[self.loserIndex].bounty = 0.0
                        self.playerInfo[self.loserIndex].status = "Out"

                        self.highestBounty()  # Output the newest highest bounty out
                        # Refresh the boxes with the new data:
                        self.entry.delete(0, END)
                        self.entry2.delete(0, END)
                        self.outputNewTable()  # Output the new table
                else:
                    messagebox.showerror("Error!", "A player cannot knock themselves out.")
            else:
                messagebox.showerror("Error!", "One of the names do not exist in the list of players. Try again.")
        else:
            messagebox.showerror("Error!", "Please input a name into both fields. Try again.")

    def highestBounty(self):  # Function to check for the highest bounty
        for x in self.playerInfo:  # For all the player objects in the list
            if x.bounty > self.hBounty.get():  # Check for the highest bounty
                self.hBounty.set(x.bounty)  # Set the new bounty
                self.hBountyName.set(x.name) # Set the name of the person with the new bounty

                # State the new bounty leader:
                self.highestBountyEntry['state'] = 'normal'
                self.highestBountyEntry.delete(0, END)
                self.highestBountyEntry.insert(0, x.name + ": $" + str(self.hBounty.get()))
                self.highestBountyEntry['state'] = 'disabled'

    def outputNewTable(self):  # Function to show the new updated table every round
        self.outputInfo.delete('1.0', END)

        self.outputInfo.insert(tkinter.END, "Format - " +  " Player " + " Knocks " + " Bounty " + " Earnings " + " Status " + "\n")
        for x in self.playerInfo:  # For all the player objects in the list
            # Output them in a: name, [ knocks ], bounty, and status format:
            self.outputInfo.insert(tkinter.END, "          " + x.name + " | [")

            for y in x.knocks:
                self.outputInfo.insert(tkinter.END,
                                       y)
            # end of knock is self.width-1 ( 9-1)
            self.outputInfo.insert(tkinter.END,
                                   "] | " + str(x.bounty) + " | " + str(x.earnings)+ " | " + str(x.status) + "\n")

        self.outputInfo.insert(tkinter.END, "\n")

# =================================================================
if __name__ == '__main__':
    pokerRoot = Tk()
    poker_GUI = pokerGUI(pokerRoot)
    #pokerRoot.configure(background='#2B2726')
    pokerRoot.geometry("1170x550")  # Window size, x/y
    pokerRoot.mainloop()