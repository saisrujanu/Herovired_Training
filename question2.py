dict='car'
Brandname=input("Enter the Brand-Name:")
color=input("Enter the Car-Color:")
car={Brandname:color}
x=open('myoutput.txt','a')
print("myoutput for question2",file=x)
print(car,file=x)