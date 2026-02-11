import random
randomNumber = random.randint(1,100)
count = 0
while True:
  guess = int(input("Enter your guess:"))
  count+=1
  if guess < randomNumber:
    print("Too Low!")
  elif guess > randomNumber:
    print("Too High!")
  else:
    print("Congratulations! You got the number right.")
    print(f"It took you {count} attempts to get it right")
    break
