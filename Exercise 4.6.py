def computepay(h, r):
    h = float(h)
    r = float(r)
    if h <= 40:
        pay = h*r
    if h > 40:
        pay = 40*r + 1.5*r*(h-40)
    return pay

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
p = computepay(hrs, rate)
print("Pay", p)
