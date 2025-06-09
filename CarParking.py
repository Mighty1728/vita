import heapq

class Car:
    def __init__(self, number, car_type, arrival_time):
        self.number = number
        self.type = car_type
        self.arrival_time = arrival_time

    def __lt__(self, other):
        return self.arrival_time < other.arrival_time

class ParkingCompartment:
    def __init__(self, car_type):
        self.type = car_type
        self.queue = []

    def park_car(self, car):
        if car.type.lower() == self.type.lower():
            heapq.heappush(self.queue, car)
            print(f"Parked {car.number} in {self.type} compartment.")
        else:
            print(f"{car.type} doesn't belong in {self.type} compartment.")

    def show_parked_cars(self):
        print(f"{self.type} Compartment:")
        if not self.queue:
            print("No cars parked.")
        else:
            for car in sorted(self.queue, key=lambda c: c.arrival_time):
                print(f"- {car.number} ({car.type}), Arrival Time: {car.arrival_time}")
        print()

def main():
    mini = ParkingCompartment("Mini")
    sedan = ParkingCompartment("Sedan")
    suv = ParkingCompartment("SUV")

    n = int(input("Enter number of cars: "))

    for i in range(1, n + 1):
        number = input("Enter car number: ")
        car_type = input("Enter car type (Mini/Sedan/SUV): ")

        car = Car(number, car_type, i)

        if car_type.lower() == "mini":
            mini.park_car(car)
        elif car_type.lower() == "sedan":
            sedan.park_car(car)
        elif car_type.lower() == "suv":
            suv.park_car(car)
        else:
            print("Invalid car type. Car not parked.")
        print()

    print("Final Parking Status:")
    mini.show_parked_cars()
    sedan.show_parked_cars()
    suv.show_parked_cars()

if __name__ == "__main__":
    main()
