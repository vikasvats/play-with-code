# write a code to check the n number of fibonacchi sequence


def fib():
   n = int(input("Write your number:"))
   a,b=0,1
   for _ in range(n):
      print(a)
      a,b =b,a + b

fib()