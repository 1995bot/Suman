def main():
    print('+ for Addition')
    print('- for Subtraction')
    print('* for Multiplication')
    print('/ for Division')
    ch = input("Enter your choice:")
    if ch=='+':
        x=int(input("Enter value of a:"))
        y=int(input("Enter value of b:"))  
        print("Addition:",add(x,y))
    elif ch=='-':
        x=int(input("Enter value of a:"))
        y=int(input("Enter value of b:"))  
        print("Subtraction:",sub(x,y))
    elif ch=='*':
        x=int(input("Enter value of a:"))
        y=int(input("Enter value of b:"))  
        print("Multiplication",mul(x,y))
    elif ch=='/':
        x=int(input("Enter value of a:"))
        y=int(input("Enter value of b:"))  
        print("Division",div(x,y))
    else:
        print("Invalid character")  
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
main()