def my_function():
    print("Hello function")

my_function()

# parametres

def fun(y):
    print(y)

fun("Gmail")
fun("Youtube")
fun("Facebook")

# default paramenter value

def my_function(country = "Norway"):
    print("I am from",country)

my_function()
my_function("India")
my_function("USA")

# passsing a list as a parameter

def my_function(fruits):
    for x in fruits:
        print(x)

fruits=["apple", "banana", "mango", "litchi"]

my_function(fruits)

# use of return statement

f = 0
def my_function(x, y):
    return y+x

print(my_function(3, 5))
print(my_function(10, 20))