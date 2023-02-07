class Computer:

    # What attributes will it need?
    year_made: int
    operating_system: str 
    price: int 
    description: str 
    color: str 
    memory_cpacity : str

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, year_made, operating_system, price, description, color, memory_capacity):
       self.year_made = year_made
       self.operating_system = operating_system
       self.price = price
       self.description = description
       self.color = color
       self.memory_capacity = memory_capacity 
    

    # What methods will you need?
    def computer_information(self, year_made, operating_system, price, description, color, memory_capacity): 
        computer_info = (year_made, operating_system, price, description, color, memory_capacity) 
        print(computer_info)





    

