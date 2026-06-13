while True:
    name=input("What's your first name? : ").strip()
    if name=="":
        print("The name cannot be empty.")
    else:
        if name.isalpha():
            break
        else:
            print("Insert only letters with no space.")

while True:
    try:
        age = int(input("How old are you? : "))
        break 
    except ValueError:
        print("That's not a valid age.")

while True:
    town=input("Which town do you live in? : ")
    if town:
        break   
    else:
        print("The town cannot be empty.")

print()
print(f"Name: {name}.\n"
      f"Age: {age}.\n"
      f"Town: {town}.")
