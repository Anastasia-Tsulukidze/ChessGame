
def square_check(val):
  while True:
    z = int(input(f'{val}: '))
    if z <= 0 or z > 8:
      print(f'Please enter {val} in range 1-8!')
      continue
    else:
      return z
  
x1 =  square_check('x1')
x2 =  square_check('x2')
y1 =  square_check('y1')
y2 =  square_check('y2')

if(x1 + x2 + y1 + y2) % 2 ==0:
  print("YES")
else: 
  print('NO')
