start = int(input("Give me a starting number: "))
end = int(input("Give me a number to end before: "))
inc = int(input("How much to increase each time? "))
for i in range (start, end, inc):
  print(i)