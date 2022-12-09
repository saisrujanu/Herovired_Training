# #if else loop
# n=int(input("Enter the number:"))
# if (n<=0):
#     print("Lessthan zero")
# elif (n<=5):
#     print("Number is lessthan five")
# else:
#     print("greater than ten")

# name=input("enter the college:")
# rollno=input("enter the rollno:")
# college1={name:rollno}
# print(college1)
    
product_1=int(input('quantity of first product:'))
product_2=int(input('quantity of first product:'))
product_3=int(input('quantity of first product:'))
product_4=int(input('quantity of first product:'))
product_5=int(input('quantity of first product:'))
amountforp1=product_1*100
amountforp2=product_2*200
amountforp3=product_3*300
amountforp4=product_4*400
amountforp5=product_5*500

#Using the List
l=[product_1,product_2,product_3,product_4,product_5]
#using the loops
for i in l:
    print(i)
#using the if-else statements
if((product_1<=0)or (product_1<=0)or(product_3<=0)or(product_4<=0)or(product_5<=0)):
    print('please enter a positive value')
else:
    totalAmount=amountforp1+amountforp2+amountforp3+amountforp4+amountforp5
    entries={product_1:100,product_2:200,product_3:300,product_4:400,product_5:500} 
    x=open('mydata.txt','a') 
    print("the amount of all products",entries,"/n","Total price of ech product:",file=x)
    # x.close()  
    entries1={product_1:amountforp1,product_2:amountforp2,product_3:amountforp3,product_4:amountforp4,product_5:amountforp5}
    for k,v in entries.items():
        print([k,v],sep=":",end=" ")
        print(k,v,file=x)
        print("\n",entries1)
    print('the amount that you need to pay is:')
    print("The amount that you need to pay",totalAmount,file=x)
total=product_1*300 +product_2*400 +product_3*500 +product_4*600+product_5*7000
# print(total)
# print(total,file=x)
