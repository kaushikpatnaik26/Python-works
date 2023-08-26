# termed as dict
# {} dictonary format

Dict = {}
# empty dictonary
print(Dict)

Dict = {1:'C',2:'Python',3:'Java'}
#left of colon(:) is the key right to colon is the value
print(Dict)

#creating a dictonary using dict() method
name = dict({1:'car', 2:'bus',3:'train'})
print(name)

#creating a dictonary with each item as a pair
Dict = dict([(1, 'java'), (2, 'python'), (3, 'C'), (4, 'php')])
print('\nDictonary with each item as a pair')

#replacing value
Dict[1]='dog'
print(Dict)
#using for loop to get only keys of the dictonary
for x in Dict.keys():
    print(x)

#using for loop to get only values of the dictonary
for x in Dict.values():
    print(x)

#using for loop for getting both keys and values
for x, y in Dict.items():
    print(x, y)

#nested dictonary

myfamily={
    'child1':{'name':'emily', 'year':2003},
    'child2':{'name':'josh', 'year':2004},
    'child3':{'name':'matt', 'year':2005}
}
print(myfamily)

