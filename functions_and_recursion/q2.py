# greatest among three numbers

def number(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
print(f"Greatest Number among {a,b,c} is:{number(a,b,c)}")