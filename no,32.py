unit=int(input("enter unit"))
if unit>=1 and unit<=100:
    print("no charge")
elif unit>=101 and unit<=200:
    bill=unit*5
    print(bill,bill) 
elif unit>=200:
    a=unit-100
    b=100*5
    bill=a*10-b
    print("bill",bill) 
else:
    print("none")
              