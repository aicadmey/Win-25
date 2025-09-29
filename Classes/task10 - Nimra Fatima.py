#class
#Example1:
class University:
    def __init__(self, name, locations):
        self.name = None
        self.locations = None
    
    class Depart:
            def __init__(self):
                self.room = None
                self.location = None 
            
# create an object
my_uni = University.Depart()
my_uni.location = 12
print(my_uni.room)
print(my_uni.location)
#Example2:
class PGC:
    def __init__(self,name, location):
        self.name = None
        self.location = None
    class Girls_compus:
            def __init__(self):
                self.name = None
                self.location = None
            class Boys_compus:
                  def __init__(self):
                      self.name = None
                      self.location = None         
# create an object
my_uni = PGC.Girls_compus.Boys_compus()
my_uni.location = 12
print(my_uni.name)
print(my_uni.location) 

class Superior_collage:
    def __init__(self,name, location):
        self.name = None
        self.location = None
    class Girls_compus:
            def __init__(self):
                self.name = None
                self.location = None
            class Boys_compus:
                  def __init__(self):
                      self.name = None
                      self.location = None         
# create an object
my_uni = Superior_collage.Girls_compus.Boys_compus()
my_uni.location = 12
print(my_uni.name)
print(my_uni.location) 

#Example3:
class Web_development:
    def __init__(self,skill):
        self.skill = None
    class Front_end_development:
        def __init__(self):
            self.skill = None
            self.front_page = None 
        class Back_end_development:
            def __init__(self): 
                self.skill = None
                self.back_page = None 
            class Full_stack_development:
                 def __init__(self): 
                    self.skill = None
                    self.full_page = None  
# create an object
my_uni = Web_development.Front_end_development.Back_end_development.Full_stack_development()
my_uni.full_page = 10
print(my_uni.full_page)
print(my_uni.skill)  

class Artifical_intelligence:
    def __init__(self,skill):
        self.skill = None
    class Machine_learning:
        def __init__(self):
            self.skill = None
            self.language = None 
        class Deep_learning:
            def __init__(self): 
                self.skill = None
                self.Architecture = None 
            class Robotics:
                 def __init__(self): 
                    self.skill = None
                    self.movement = None  
# create an object
my_uni = Artifical_intelligence.Machine_learning.Deep_learning.Robotics()
my_uni.movement = 11
print(my_uni.movement)
print(my_uni.skill) 

class Information_technology:
    def __init__(self,skill):
        self.skill = None
    class Software_engineering:
        def __init__(self):
            self.skill = None
            self.process = None 
        class Networking:
            def __init__(self): 
                self.skill = None
                self.module = None 
            class Security:
                 def __init__(self): 
                    self.skill = None
                    self.safety = None  
# create an object
my_uni = Information_technology.Software_engineering.Networking.Security()
my_uni.safety = 9
print(my_uni.safety)
print(my_uni.skill)
#Example4:
class Computer:
    def __init__(self,model):
        self.name = None
        self.model = None
    class PC:
        def __init__(self):
            self.model = None
            self.design = None
        class Laptop:
            def __init__(self):
                self.model = None
                self.touchpad = None 
            class Tablet:
                def __init__(self): 
                    self.model = None
                    self.notebook_type = None   
                class Analog_computer:
                    def __init__(self):
                        self.model = None
                        self.electronic_computer = None   
# create one object
com = Computer.PC.Laptop.Tablet.Analog_computer()
com.electronic_computer = 14
print(com.electronic_computer)
print(com.model)

class Mobile_phone:
    def __init__(self,model):
        self.name = None
        self.model = None
    class Smartphone:
        def __init__(self):
            self.model = None
            self.design = None
        class OPPA:
            def __init__(self):
                self.model = None
                self.Samsung_Mobiles = None 
            class Realme:
                def __init__(self): 
                    self.model = None
                    self.Chinese_company = None   
                class IOS:
                    def __init__(self):
                        self.model = None
                        self.device = None   
# create one object
com = Mobile_phone.Smartphone.OPPA.Realme.IOS()
com.device = 15
print(com.device)
print(com.model)

class Television:
    def __init__(self):
        self.name = None
        self.model = None
    class LCD:
        def __init__(self):
            self.model = None
            self.size = None
        class LED:
            def __init__(self):
                self.model = None
                self.size = None
            class plasma:
                def __init__(self):
                    self.model = None
                    self.tiny_gas_plasma = None
                class Smart_Tv:
                    def __init__(self):
                        self.model = None
                        self.flat_screen = None
# create one object
tel = Television.LCD.LED.plasma.Smart_Tv()
tel.flat_screen = 9
print(tel.flat_screen)


class Internet:
    def __init__(self):
        self.speed = None
        self.quailty = None
    class Fiber:
        def __init__(self):
            self.speed = None
            self.reliable = None
        class Cable:
            def __init__(self):
                self.speed = None
                self.peak_uasge = None
            class Fixed_wireless:
                def __init__(self):
                     self.speed = None
                     self.radio_signal = None
                class FTP:
                    def __init__(self):
                          self.speed = None
                          self.upload_web_pages = None
Inter = Internet.Fiber.Cable.Fixed_wireless.FTP()
Inter.upload_web_pages = 7
print(Inter.upload_web_pages)

#Example5:
class Car:
    def __init__(self):
        self.name = None
        self.model = None
    class Sedan:
        def __init__(self):
            self.model = None
            self.design = None
        class Limousine:
            def __init__(self):
                self.model = None
                self.size = None
            class Sport_car:
                def __init__(self):
                    self.model = None
                    self.speed = None
                class SUV:
                    def __init__(self):
                        self.model = None
                        self.capability = None
                    class jeep:
                        def __init__(self):
                            self.model = None
                            self.built = None
ca = Car.Sedan.Limousine.Sport_car.SUV.jeep()
ca.built = 10
print(ca.built)

class Buses:
    def __init__(self):
        self.name = None
        self.model = None
    class Coach_buses:
        def __init__(self):
            self.name = None
            self.clear_distance = None
        class Motorcoach:
            def __init__(self):
                self.name = None
                self.reliable = None
            class School_van:
                def __init__(self):
                    self.name = None
                    self.safely = None
                class Suttle:
                    def __init__(self):
                          self.name = None
                          self.easy = None
                    class Minibus:
                        def __init__(self):
                             self.name = None
                             self.size = None
Bus = Buses.Coach_buses.Motorcoach.School_van.Suttle.Minibus()
Bus.size = 5
print(Bus.size)  

class Truck:
    def __init__(self):
        self.name = None
        self.model = None
    class Box_truck:
        def __init__(self):
            self.model = None
            self.speed = None
        class Tow_truck:
            def __init__(self):
                self.model = None
                self.size = None
            class Firetruck:
                def __init__(self):
                     self.model = None
                     self.power = None 
                class Heavy_truck:
                    def __init__(self):  
                         self.model = None
                         self.heavy = None 
                    class Tank_truch:
                        def __init__(self):
                             self.model = None
                             self.heavy = None     
tur = Truck.Box_truck.Tow_truck.Firetruck.Heavy_truck.Tank_truch()
tur.heavy = 5
print(tur.heavy)

class Motorcycle:
    def __init__(self):
        self.name = None
        self.model = None
    class sport_biker:
        def __init__(self):
            self.name = None
            self.speed = None  
        class scooter:
            def __init__(self):
                self.name = None
                self.heavy = None  
            class Bobber:
                def __init__(self):
                   self.name = None
                   self.hard = None
                class Off_road:
                    def __init__(self):
                       self.name = None
                       self.light = None  
                    class Cafe_Racer:
                        def __init__(self):
                           self.name = None
                           self.rider = None  
cycle = Motorcycle.sport_biker.scooter.Bobber.Off_road.Cafe_Racer()
cycle.rider = 5
print(cycle.rider)

class Motorbikes:
    def __init__(self):
        self.name = None
        self.model = None
    class Standard:
        def __init__(self):
            self.model = None
            self.design = None  
        class Sport_bike:
            def __init__(self):
                 self.model = None
                 self.sport = None
            class Snowmobile:
                def __init__(self):
                     self.model = None
                     self.Snow = None 
                class Enclosed:
                    def __init__(self):
                        self.model = None
                        self.Enclose = None 
                    class Touring_bike:
                        def __init__(self):
                             self.model = None
                             self.tour = None   
bike = Motorbikes.Standard.Sport_bike.Snowmobile.Enclosed.Touring_bike()
bike.tour = 5
print(bike.tour)                            