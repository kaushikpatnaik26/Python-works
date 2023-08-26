fruit = ['apple','banana','cherry']
print(fruit)

fruit[0]='car'
fruit[1]='bus'
fruit[2]='train'

print(fruit)
print (len(fruit))

fruit.append('mango')
print(fruit)
# append adds element in the last
fruit.insert(1,'coconut')
print(fruit)
# insert adds in specific index
fruit.remove('train')
print(fruit)

fruit.pop()
print(fruit)
fruit.pop(2)
print(fruit)
# pop prints the last element by default or else we can specify the index to print
fruit2=fruit.copy()
print(fruit2)

for element in fruit:
    print(element)
#printing list using for loop

fruit.clear()
print(fruit)    
#clears the list elements only the list format [] stays 