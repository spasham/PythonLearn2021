#check a number is divided by both 2 & 4.

num = int(input('enter a number'))

if num % 2 == 0:
    if num % 4 == 0:
      print ('success')
    else:
      print ('sorry')
else:
    print ('Failed')
