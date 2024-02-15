my_list = list()
max = None
for i in range(10):
    num = int(input("Enter a number: "))
    if max == None or num > max:
        max = num
    my_list.append(num)
print(f"The largest number in the list: {my_list} is {max}")