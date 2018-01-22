def collatz(n):
  result = []
  while (n != 1):
      if n % 2 == 0:
          result.append(n)
          n = n / 2
      else:
          result.append(n*3+1)
          n = n*3 + 1
      
  return len(result) + 1

"""
test.assert_equals(collatz(20), 8)
test.assert_equals(collatz(15), 18)
"""
