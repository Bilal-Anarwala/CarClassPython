from Specs import Specs

class Race:
    @staticmethod
    def start_race(car1, car2):
        print("Car 1:")
        print()
        car1.display_car_info()
        print()
        print("Car 2:")
        car2.display_car_info()
        print()

        if car1.get_horsepower() > car2.get_horsepower():
            print(f"The winner is: {car1.get_make()} {car1.get_model()}")
        elif car1.get_horsepower() < car2.get_horsepower():
            print(f"The winner is: {car2.get_make()} {car2.get_model()}")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    bilals_car = Specs("Toyota", "Supra", 1998, "2JZ-GTE", 900)
    drews_car = Specs("Mitsubishi", "Eclipse", 1995, "4G63", 600)
    andrays_car = Specs("BMW", "M335i", 2016, "N55", 620)
    mohammads_car = Specs("Tesla", "Model 3", 2021, "Electric", 450)
    robertos_car = Specs("Nissan", "GTR", 2001, "RB26-DETT", 1000)
    nabeels_car = Specs("Dodge", "Viper ACR", 2016, "EWE", 645)
    tylers_car = Specs("Corvette", "Z06", 2010, "LS7", 505)
    syeds_car = Specs("Mazda", "Miata", 2016, "Skyactive-G", 155)

    cars = [bilals_car, drews_car, andrays_car, mohammads_car, robertos_car,
            nabeels_car, tylers_car, syeds_car]

    print("Available cars:")
    for i, car in enumerate(cars, 1):
        print(f"{i}. {car.get_make()} {car.get_model()}")

    # Get user input to select two cars
    first_choice = int(input(f"Choose the first car (1 to {len(cars)}): ")) - 1
    second_choice = int(input(f"Choose the second car (1 to {len(cars)}): ")) - 1

    # Start the race between the selected cars
    race = Race()
    race.start_race(cars[first_choice], cars[second_choice])
