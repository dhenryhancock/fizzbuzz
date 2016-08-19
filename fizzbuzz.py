import sys
if len(sys.argv)!=1:
 try:
  upper_limit=int(sys.argv[1])
 except ValueError:
  print("Make it a number ")
  upper_limit=int(input("number please "))
 print("fizzbuzz counting up to {}".format(upper_limit))
 for number in range(1,upper_limit+1):
    if number %5==0 and number %3==0:
     print("fizzbuzz")
    elif number % 3==0:
     print("fizz")
    elif number %5==0:
     print("buzz")
    else:
     print(number)
else:
 try:
  upper_limit=int(input("limit please "))
 except ValueError:
  print("Make it a number ")
  upper_limit=int(input("limit please "))
 print("fizzbuzz counting up to {}".format(upper_limit))
 for number in range(1,upper_limit+1):
    if number %5==0 and number %3==0:
     print("fizzbuzz")
    elif number % 3==0:
     print("fizz")
    elif number %5==0:
     print("buzz")
    else:
     print(number)

 
   