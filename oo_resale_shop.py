#This class below alters the inventory list depending on what has been bought, sold, changed, etc.
from computer import *
class ResaleShop:

    #This sets up the attribute inventory that will be used later for buying/selling/refurbishing/etc.
    inventory = list
    


    #This is a constructor for the attribute needed for this code. 
    def __init__(self):
        self.inventory = []
    

        

    #This method sets up the "buying" function of the resale shop by appending information about each computer to the inventory every time a new computer is added. 
    def buy(self, c: Computer): 
        self.inventory.append(c)
   
   #This method sets up the "selling" function of the resale shop by removing a computer from the inventory list with the condition that the computer has to already be in the inventory.
    def sell(self, c: Computer): 
        if c in self.inventory: 
            self.inventory.remove(c)
        else: 
            print("Computer not in this inventory")
    
    #This method changes the price of a computer in the inventory if the price is over 2000. The computer will be 200 dollars off for a special Valentine's Day Sale (or any other promotional marketing) we will be doing this year!!
    def price_change(self, c: Computer):
        if c[6] >= 2000:
            c[6] -= 200
            print("Congratulations! Your computer is a part of our fun sale! Enjoy 200 dollars off your computer")
            print(c[6])
        else: 
            print("So sorry! That computer is not a part of our sale, but make sure to look at others where the sale applies before you leave us.")
        
    
    
#This creates the sample computer used for this coding assignment and calls the relevant functions/methods.
def main(): 
    my_store = ResaleShop()
    c = Computer(["MacBook", "Core", 120, 32, "Apple", 2012, 950])
    my_store.buy(c)
    my_store.sell(c)
    my_store.price_change(c)

main()
    

    

   




