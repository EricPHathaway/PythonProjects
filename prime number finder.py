while True:
  num_i = int(input('Enter a number: '))

  import math
  num_i_s = int(math.sqrt(num_i))

  for i in range(2, num_i_s+1):
    test = num_i % i
    if (test == 0):
      num_i = str(num_i)
      print(i)
      print (num_i + ' is not prime.')
      break
  else:
    if(num_i<=1):
      num_i = str(num_i)
      print(num_i + ' is not prime.')
    else:
      num_i = str(num_i)
      print(num_i + ' is prime.')
      print(i)
