import random

def randomizer():
    if fp == 1:
        print(sweetArr[random.randint(0, len(sweetArr) - 1)])
    elif fp == 2:
        print(tropicalArr[random.randint(0, len(tropicalArr) - 1)])
    elif fp == 3:
        print(fruityArr[random.randint(0, len(fruityArr) - 1)])


# Flavor Profile Arrays
sweetArr = ["Vanilla", "Cookie Butter", "Almond", "Salted Caramel", "Chocolate Macadamia Nut", "Toasted Marshmallow"]
tropicalArr = ["Pomegranate", "Passion Fruit", "Coconut", "Kiwi", "Pineapple", "Banana", "Guava"]
fruityArr = ["Strawberry", "Watermelon", "Blue Ras", "Blackberry", "Orange", "Peach"]

print("Barista Roulette")
print("----------------")
print()
print("Flavor Profiles")
print("----------------")
print("1. Sweet")
print("2. Tropical")
print("3. Fruity")
print("4. Candy")
print()

fp = int(input("Enter your choice: "))
flavorAmount = int(input("Enter your flavor amount: "))

while (fp < 1 or fp > 4):
    print()
    print("Please enter a valid choice!")
    fp = int(input("Enter your choice: "))

for i in range (flavorAmount):
    randomizer()
