a= int(input("Enter total units: "))

if(a<=100):
    print("NO Charge")
elif(a>100 & a<=200):
    bill=(a-100)*5 
if(a>200):
    bill=(a-200)*10+500  

print("Bill:",bill)