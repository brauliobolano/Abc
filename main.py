print("The range is 10")
sum = 0
previous= 0
for current in range (10):
  if current > 0:
    previous = current-1
  sum = current + previous
  print("Current Number: ",current,"Previous Number: ", previous,"Sum: ",sum)