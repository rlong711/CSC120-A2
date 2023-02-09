"""  
Filename: computer.py
Description: Resale Shop Assignment
Part of A2: Object-ification, CSC120: Object-Oriented Programming
Author: Raley Long
Date: 8 February 2023
"""
#This Class sets up and stores the important information required for the inventory list used in the oo_resale_shop file
class Computer:


    #Below lists all the attributes that are going to be used to identify/describe the computer
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    #This code is the constructor for the attributes listed above. 
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
       self.description = description 
       self.processor_type = processor_type 
       self.hard_drive_capacity = hard_drive_capacity 
       self.memory = memory 
       self.operating_system = operating_system 
       self.year_made = year_made 
       self.price = price 

   #This code chunk prints out the details for the computer of interest. 
    def print_details(self): 
        print(self.description)
        print(self.processor_type)
        print(self.hard_drive_capacity)
        print(self.memory)
        print(self.operating_system)
        print(self.year_made)
        print(self.price)

#This gives an example computer (not real) that will be used to test the code/debug it.       
def main(): 
    c = Computer("MacBook", "Core", 120, 32, "Apple", 2012, 950)
    c.print_details()
main()



    

    
    

    
    








    

