def Fibonacci(n):
   if n <= 1:
       return n
   else:
       return (Fibonacci(n - 1) + Fibonacci(n - 2))

n = int(input("Enter the Value of n: "))

# take input from the user

print("Fibonacci series :")
for i in range(n):
   print(Fibonacci(i),end=" ")
