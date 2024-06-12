print("This is a practice command")

def fib(a):
    if a==0:
        return 0
    elif a==1:
        return 1
    else:
        return fib(a-1)+fib(a-2)
    
terms=int(input("Enter the number of terms: "))
if terms<=0:
    print("Enter a positive number")
else:
    for z in range(terms):
        print(fib(z),end=" ")