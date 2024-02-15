x= int(input("Enter a number of repetitions: "))


# Write your decorator here
def hello_repeat(f):
    def wrapper():
     for i in range(x):
         f()
    return wrapper

@hello_repeat
def hello():
       print ('Hello')
hello()
