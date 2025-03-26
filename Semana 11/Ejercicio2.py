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
            print (f'Se subio pasajero: {person.name}')
        else:
            print (f'Este pasajero no cabe: {person.name}')
        
    def drop_off_passenger (self, person):
        eliminated = False
        for index, item in enumerate (self.passenger):
            if item == person:
                self.passenger.pop(index)
                eliminated = True
                print (f'Se bajo pasajero: {person.name}')
        if eliminated == False :
            print (f'Pasajero no esta en el bus')

passenger1 = Person('Pedro')
passenger2 = Person('Juan')
passenger3 = Person('Brayan')

Bus1 = Bus(2) # se indica numero maximo de pasajeros

# se suben pasajeros

Bus1.add_passenger(passenger1) 
Bus1.add_passenger(passenger2)
Bus1.add_passenger(passenger3)

# se bajan pasajeros

Bus1.drop_off_passenger(passenger2)

# se indican los pasajeros finales
print ('Pasajeros en el bus:')
for item in Bus1.passenger:
    print (f'{item.name}')