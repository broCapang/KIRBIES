n, m = input().split()
n = int(n)
m = int(m)

if n == m:
  print (n+1)

if n > m:
  for i in range(m+1, n+2):
    print (i)
  
if m > n:
  for i in range(n+1, m+2):
    print (i)