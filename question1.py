user1=int(input("Enter the User1 input:"))
user2=int(input("Enter the User2 input:"))
user3=int(input("Enter the User3 input:"))
user4=int(input("Enter the User4 input:"))
user5=int(input("Enter the User5 input:"))
if (user1>0 and user2>0 and user3>0 and user4>0 and user5>0):
    total=user1+user2+user3+user4+user5
    x=open('myoutput.txt','a') 
    print("myoutput for question1",file=x)
    print(total,file=x)
else:
    x=open('myoutput.txt','a') 
    print("User Entered the Negative Number",file=x)

# x=open("question1.txt","a")
# print("my output",assignment1=x)
# x.close()
# file=open('question1.txt','r')
# for line in question1:
#     print(line)
#print(file.read())1
