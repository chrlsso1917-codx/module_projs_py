# Step 1 — Print a welcome header
# Step 2 — Ask for character name, age, height, weight
# Step 3 — Calculate power level
# Step 4 — Display a clean character card
# Step 5 — Ask to create another character, loop if yes.

print("Hi there! Welcome to the...")
print("=" * 29)
print("  CHARACTER PROFILE CREATOR ")
print("=============================")

while True:
    name = input("Enter character name: ")
    while True:
        try:
            age = int(input("Enter age: "))
            break
        except ValueError:
            print("Invalid data type!")
    while True:
        try:
            height = float(input("Enter height: "))
            break
        except ValueError:
            print("Invalid data type!")
    while True:
        try:
            weight = float(input("Enter weight: "))
            break 
        except ValueError:
            print("Invalid data type!")
 # formula
    power = (age * 20) + (height * 25) - (weight * 2)
    print("=" * 29)
    print("     CHARACTER PROFILE  ")
    print("=" * 29)
    print("Name:       ", name)
    print("Age:        ", age)
    print("Height:     ", height)
    print("Weight:     ", weight)
    print("Power Level:", power)
    print("=" * 29)
    choice = input("Create another character?\n")
    print("=" * 29)
    if choice.lower() == "yes":
        continue
    else:
        break


