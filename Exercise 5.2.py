largest = None
smallest = None
fine = 0
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            num = int(num)
            if smallest is None:
                smallest = num
            elif smallest >= num:
                largest = smallest
                smallest = num
            else:
                if largest is None:
                    largest = num
                elif largest <= num:
                    largest = num
        except:
            fine = -1
if fine == -1:
    print("Invalid input")
print("Maximum is", largest)
print("Minimum is", smallest)
