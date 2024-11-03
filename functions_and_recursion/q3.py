# FAHRENHEIT TO CELCIUS

def convert(f):
    return 5*(f-32)/9
f=int(input("Enter tempertaure:"))
print(f"THE TEMPERATURE IN CELCIUS IS: {convert(f)}")