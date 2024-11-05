#to find greatest among 4

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
d=int(input("Enter a number:"))
if(a>b and a>c and a>d):
    print(f"A is the greatest:{a}")
elif(b>a and b>c and b>d):
    print(f"B is the greatest:{b}")
elif(c>a and c>b and c>d):
    print(f"C is the greatest:{c}")
elif(d>a and d>b and d>c):
    print(f"D is the greatest:{d}")