print("Welcome to my first game!")
name = input("What is your name? ")
age =int(input("What is your age? "))

print("Hello", name, "you are", age, "year old.")

health = 10


if age >= 18: 
  print("you are old enough to play!")
  
  wants_to_play = input("Do you want to play? ").lower()
  if wants_to_play == "yes": 
    print("Lets play!")
    print("you are starting with",health, "health")
    print("You open your eyes and suddenly you are standing on a road that divdes into two paths.")

    left_or_right = input("First Choice... Left or Right (Left/Right)? ")
    
    if left_or_right == "left": 
      ans = input("Nice, you follow the path and reach a lake... Do you want to swim across or go around (across/around)? ")

      if ans == "around":
       print("You went around and reached the other side of the lake.")

      elif ans == "across":
       print("You managed to get across, but were bit by a vicious monster fish and lost 5 health.")
       health -= 5

      ans = input("You notice a house and a river, which do you go to (house/river)? ")
      if ans == "house":
         print("You knock on the door and no one answers and out of nowhere you get attecked from behind by a stranger, you lost 5 health")
         health -= 5
         if health <= 0:
          print("You now have 0 health and lost the game...")
         else:
            print("You have survived the attack by stranger and the owner comes and helps you fight off the attacker")
            print("the owner helps you get into a close by village and you find a place to stay for now You Win!")

      else: 
          print("You go to the river and try to go through it, but a bears spots you and you are attacked and lost your life..")
          health -= 10
          if health <= 0:
           print("You have 0 health and lost the game...")

    else: 
      print("You were thinking of going right but out of nowhere you get struck by an arrow to the knee and bleed out alot and lost all of your heatlh.")
      health -= 10
      if health <= 0:
        print("You have 0 health and lost the game...")
  else: 
    print("Ok, Bye...")
else: 
  print("You are not enough to play...")