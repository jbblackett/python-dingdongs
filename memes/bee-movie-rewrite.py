import random
lines = open("buzz.txt", "r").read().splitlines()
for i in range(4000):
  myline = random.choice(lines)
  if myline != "\n":
    print(myline)
