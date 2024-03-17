m=int(input("Enter the first number"))
n=int(input("enter the second number"))
print("Which operation you want to perform \n 1.Sum \n 2.subtraction \n 3.Multiply \n 4.Division")
a=int(input("enter the choice: "))
if a==1:
    print(f"sum of {m} and {n} :{m+n}")
elif a==2:
    print(f"subtraction of {m} and {n} :{m-n}")
elif a==3:
    print(f"Multiplication of {m} and {n} :{m*n}")
elif a==4:
    print(f"Division of {m} and {n} :{m/n}")
