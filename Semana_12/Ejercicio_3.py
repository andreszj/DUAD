class ElectricCar:

    def __init__ (self, battery, range_wlpt, *args, **kwargs):
        self.battery = battery
        self.range_wlpt = range_wlpt
        super().__init__(*args, **kwargs)
    def charge_system (self):
        print ('This car is charging...')
class DriveMode:

    def __init__ (self, drive_mode, *args, **kwargs):
        self.drive_mode = drive_mode
        super().__init__(*args, **kwargs)
    def active_drive_mode(self,drive_mode):
        modes = {1: "ECO", 2: "SPORT", 3: "AUTO"}
        self.drive_mode = drive_mode
        print (f'{modes[drive_mode]} mode is activated')

class Drivetrain:

    def __init__ (self, drive_system, *args, **kwargs):
        self.drive_system = drive_system
        super().__init__(*args, **kwargs)
    def active_drive_system(self):
        print (f'This car has an  {self.drive_system} drive system')

class ElectricSUV (ElectricCar, DriveMode, Drivetrain):

    def __init__ (self, battery, range_wlpt, drive_mode, drive_system, brand):
        self.brand = brand
        super().__init__ (battery,range_wlpt, drive_mode, drive_system) 
        
        # It is no necessary used because super () with arguments:

        # DriveMode.__init__ (self, drive_mode)
        # Drivetrain.__init__ (self, drive_system) 

    def car_info (self):
        print (f'This car is a {self.brand}, with a {self.battery} KWh Battery, {self.range_wlpt} km of range, and an {self.drive_system} drive system')
        self.active_drive_mode(self.drive_mode)

my_car = ElectricSUV (80, 450, 1, 'AWD', 'BYD') #Starting on ECO mode

my_car.car_info()

my_car.active_drive_mode (2) #Switch to SPORT mode
my_car.charge_system() # Charging Battery
print (f'Current Drive Mode: {my_car.drive_mode}') # New Drive mode
