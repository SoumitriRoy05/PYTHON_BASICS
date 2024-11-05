# to check whether it is a spam comment or not

s1="make a lot of money"
s2="buy now"
s3="subscribe this"
s4="click this"
msg=input("Enter the comment:")
if((s1 is msg) or (s2 is msg) or (s3 is msg) or (s4 is msg)):
    print("This is a spam comment")
else:
    print("This is not a spam comment")