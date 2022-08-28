def Armstrong(n,o):
    sum = 0
    temp = n
    while temp > 0:
       digit = temp % 10
       sum += digit ** o
       temp = temp//10
    if n == sum:
       print(n,"is an Armstrong number")
       return True
    else:
       print(n,"is not an Armstrong number")
       return False
    
num = int(input("Enter Number: "))
order = len(str(num))
Armstrong(num,order)