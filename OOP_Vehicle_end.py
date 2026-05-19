from OOP_Vehicle import Vehicle, Car, Truck, Motorcycle

car = Car("Toyota", "Camry", 2022, 1500, 4, 5)
truck = Truck("Ford", "F-150", 2021, 2200, 1500, 5000)
motorcycle = Motorcycle("Yamaha", "MT-07", 2023, 180, 2, False)

car.drive()
truck.haul()
motorcycle.ride()

vehicles = [car, truck, motorcycle]
for vehicle in vehicles:
    vehicle.start_engine()