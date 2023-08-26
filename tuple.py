x = ('1', '2', '3', '4')
y = (('a', 'b', 'c', 'd'))

if (len(x)==len(y)):
    res=dict(zip(x,y))

print("Dictonary constructed from tuples:"+str(res))

my_tuple = 1 , "hello" , 2.5
print(my_tuple)

a, b, c = my_tuple
print(a)
print(b)
print(c)

#creating a tuple with one element

my_tuple = 'hello'
print(my_tuple)
print(type(my_tuple))

my_tuple = 'hello',
print(my_tuple)
print(type(my_tuple))

# how to acccess tuple elements

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-3])#negative indexing 

my_tuple = ('h', 'e', 'l', 'l', 'o')
print(my_tuple[0])
print(my_tuple[-4])
#start counting from right to left with most right one index= -1

n_tuple = ('mouse', [8,4,6], (1,2,3))
print(n_tuple[0][-1])#nested indexing >>> -1 index of the 0th index
print(n_tuple[1][1])# 1st index of 1st index
print(n_tuple[2][-3])

#range indexing/ slicing
thistuple('facebook', 'google', 'yahoo', 'gmail', 'twitter', 'reddit')
print(thistuple[2:5])#it will print from index 2 to index 5-1
print(thistuple[-4:-1])#it will print from index -4 to index -1-1

#changing tuple values
y= list(thistuple)
print(y)
y[1]='instagram'
print(thistuple)

#loop through tuple
for x in thistuple:
    print(x)

#tuple length
print(len(thistuple))

# + operator
tuple1 = ('a','b','c')
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)

#count method
thistuple = ('g','o','o','g','l','e')
x = thistuple.count('o')
print(x)

element = ('a', ('a','b'))

