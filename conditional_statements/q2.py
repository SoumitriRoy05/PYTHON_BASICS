# calculate percentage with pass and fail condition

m1=int(input("Enter the marks of m1:"))
m2=int(input("Enter the marks of m2:"))
m3=int(input("Enter the marks of m3:"))
percentage=(100*(m1+m2+m3))/300
if(percentage>=40 and m1>30 and m2>30 and m3>30):
    print(f"You are passed:{percentage}")
else:
    print(f"You failed:{percentage}")
   