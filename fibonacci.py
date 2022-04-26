def fib(n):
    a,b = 1,1
    if n==1 or n==2:
        return 1
        
    for i in range(1,n):
        a,b = b, a+b

    return a

a= int(input ("fibonacci number:"))
for i in range (a):
              print(fib(i+1))

print("F",a,"=",fib(a))
