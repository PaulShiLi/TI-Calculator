#Fibonacci Sequence

N = int(input("Enter number of terms: "))
A= 0
B = 1
I = 0
L1 = []
L2 = []

if N <= 0:
  print("Please enter a positive integer")
if N == 1:
  print("Fibonacci sequence upto",N)
else:
  print("Fibonacci sequence:")
  for I in range(N):
      print(A)
      L1.append(I)
      L2.append(A)
      C = A + B
      A = B
      B = C
