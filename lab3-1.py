dict = dict()
while True:
    choice = input("To continue press enter,to quit enter (No): ")
    if choice.lower() == "no":
        break;
    name = input("Enter the employee's name: ")
    salary = int(input("Enter the employee's salary: "))
    dict[name] = salary

print(dict)