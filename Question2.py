import pandas as pd
square1=[]
square2=[]
a=int(input("Enter the number is :"))
for i in range(0,a):
    num=int(input("Enter the square of number:"))
    square1.append(num)
    square2.append(num**2)
    check=pd.Series(square2,index=[square1])
    print(check)