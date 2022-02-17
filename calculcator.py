# For the add() function
def add(a, b):
        return a + b

# For the subtract() function
def subtract(a, b):
        return a - b

# For the mulitply() function
def multiply(a, b):
        return a * b

def divide(a, b):
        if a or b == 0:
                print("You can not divide by 0")
        else:
                return a / b

def square(a):
        return a * a 

def power(a):
        return a ** a

def square_root(a):
        list1 = range(a)
        for num in list1:
                if num * num == a:
                        return num

