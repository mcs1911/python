def computepay(h, r):
    if h < 40:
        pay = h * r
    elif h > 40:
        pay = (h - 40) * 1.5 * r + (40 * r) 
    return pay

h = int(input('Enter hours: '))
r = float(input('Enter rate: '))
        
p = computepay(h, r)
print("Pay", p)