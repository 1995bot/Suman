def fibo():
    n=int(input("Enter the number:"))
    a=0
    b=1
    temp=0
    for i in range(0,n):
        temp = a + b
        b = a 
        a= temp
        print(a, end=" ")
        
fibo()      