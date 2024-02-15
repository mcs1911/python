hours = float(input("Enter Hours: "))
rate = float(input('Enter rate: '))
             
if hours <= 40.0:
    pay = hours * rate
    print(f'Pay: {pay}')
else:
    pay = (hours - 40) * (1.5 * rate) + (40 * rate) 
    print(pay)