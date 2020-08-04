class CoffeeMachine:
    def __init__(self):
        self.milk = 1000
        self.water = 400
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.water_supply = 0
        self.milk_supply = 0
        self.beans_supply = 0
        self.water_supply = 0
        self.cups_supply = 0

    def main(self):
        action = input("Write action(buy, fill, take, remaining, exit):")
        if action == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            choice = input()
            if choice == "1":
                CoffeeMachine.check(self, 1)
            elif choice == "2":
                CoffeeMachine.check(self, 2)
            elif choice == "3":
                CoffeeMachine.check(self, 3)
            else:
                CoffeeMachine.main(self)
        elif action == "fill":
            CoffeeMachine.fill(self)
        elif action == "take":
            CoffeeMachine.take(self)
        elif action == "remaining":
            CoffeeMachine.remaining(self)
        elif action == "exit":
            return

    def buy(self, coffee_type):
        if coffee_type == 1:
            self.water -= 250
            self.beans -= 16
            self.money += 4
            self.cups -= 1
            CoffeeMachine.good(self)

        elif coffee_type == 2:
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.money += 7
            self.cups -= 1
            CoffeeMachine.good(self)

        elif coffee_type == 3:
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.money += 6
            self.cups -= 1
            CoffeeMachine.good(self)

    def fill(self):
        self.water_supply = int(input("Write how many ml of water do you want to add:\n"))
        self.water += self.water_supply
        self.milk_supply = int(input("Write how many ml of milk do you want to add:\n"))
        self.milk += self.milk_supply
        self.beans_supply = int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.beans += self.beans_supply
        self.cups_supply = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.cups += self.cups_supply
        CoffeeMachine.main(self)

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        CoffeeMachine.main(self)

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")
        CoffeeMachine.main(self)

    def check(self, coffee_type):
        if coffee_type == 1:
            if self.water < 250:
                print("Sorry, not enough water")
                CoffeeMachine.main(self)
            elif self.beans < 16:
                print("Sorry, not enough coffee beans")
                CoffeeMachine.main(self)
            elif self.cups < 1:
                print("Sorry, not enough disposable cups")
                CoffeeMachine.main(self)
            else:
                CoffeeMachine.buy(self, 1)
        elif coffee_type == 2:  # water = 350, milk = 75, beans = 20,
            if self.water < 350:
                print("Sorry, not enough water")
                CoffeeMachine.main(self)
            elif self.milk < 75:
                print("Sorry, not enough milk")
                CoffeeMachine.main(self)
            elif self.beans < 20:
                print("Sorry, not enough beans")
                CoffeeMachine.main(self)
            elif self.cups < 1:
                print("Sorry, not enough disposable cups")
                CoffeeMachine.main(self)
            else:
                CoffeeMachine.buy(self, 2)
        elif coffee_type == 3:  # water = 200, milk = 100, beans = 12
            if self.water < 200:
                print("Sorry, not enough water")
                CoffeeMachine.main(self)
            elif self.milk < 100:
                print("Sorry, not enough milk")
                CoffeeMachine.main(self)
            elif self.beans < 12:
                print("Sorry, not enough beans")
                CoffeeMachine.main(self)
            elif self.cups < 1:
                print("Sorry, not enough disposable cups")
                CoffeeMachine.main(self)
            else:
                CoffeeMachine.buy(self, 3)

    def good(self):
        print("I have enough resources, making you a coffee!")
        CoffeeMachine.main(self)


instance = CoffeeMachine()
instance.main()
