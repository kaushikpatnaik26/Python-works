a= int(input("Enter a num: "))

if(a%5==0 & a%8==0):
    print(a,"is divisible by both 5 and 8")
elif(a%5 ==0 & a%8!=0):
    print(a,"is only divisible by 5")
elif(a%5 !=0 & a%8==0):
    print(a,"is only divisible by 8")    
else:
    print("Not divisible by both 5 or 8")    