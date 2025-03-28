class Person():
	def __init__(self, name):
		self.name = name



class Bus:

    def __init__ (self, max_passengers):
        self.max_passengers = max_passengers
        self.passenger = []

    def qty_passenger(self):
        return len(self.passenger)
    
    def add_passenger(self, person):
        if self.qty_passenger() < self.max_passengers:
            self.passenger.append (person)
            print (f'The passenger named {person.name} got on')
        else:
            print (f'There is no space for: {person.name}')
        
    def drop_off_passenger (self, person):
        eliminated = False
        for index, item in enumerate (self.passenger):
            if item == person:
                self.passenger.pop(index)
                eliminated = True
                print (f'The passenger named {person.name} got off')
        if eliminated == False :
            print (f'This person is not on the bus')

passenger1 = Person('Pedro')
passenger2 = Person('Juan')
passenger3 = Person('Brayan')

Bus1 = Bus(2) # The maximum number of passenger is indicated

# Passenger got on

Bus1.add_passenger(passenger1) 
Bus1.add_passenger(passenger2)
Bus1.add_passenger(passenger3)

# Passenger got off

Bus1.drop_off_passenger(passenger2)

# Final passengers on the bus are indicated
print ('Passengers on the bus:')
for item in Bus1.passenger:
    print (f'{item.name}')