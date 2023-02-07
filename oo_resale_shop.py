from computer import *
class ResaleShop:

    # What attributes will it need?
    inventory = list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

        

    # What methods will you need?
    def buy(self, c: Computer): 
        self.inventory.append(c)
   
    def sell(self, c: Computer): 
        if c in self.inventory: 
            self.inventory.remove(c)
        else: 
            print("Computer not in this inventory")
    
    
    

def main(): 
    my_store = ResaleShop()
    print(my_store.inventory)
    
    

    

   




