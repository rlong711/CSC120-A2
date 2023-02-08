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
    
    
    

def main(): 
    my_store = ResaleShop()
    print(my_store.inventory)
    
    

    

   




