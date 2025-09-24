def show_stats():
    global energy, hunger, cleanliness, health, money, food, emotion_index
    energy = min(max(energy, 0), 5)
    health = min(max(health, 0), 5)
    hunger = min(max(hunger, 0), 5)
    cleanliness = min(max(cleanliness, 0), 5)
    if emotion_index < 0:
        emotion_index = 0
    elif emotion_index > len(emotions) - 1:
        emotion_index = len(emotions) - 1
    print(f"Time of Day: {current_time}\nEmotion: {emotions[emotion_index]}\nHealth: {health}\nEnergy: {energy}\nHunger: {hunger}\nCleanliness: {cleanliness}\nMoney: {money}\nFood: {food}")

emotions = ["Happy", "Neutral", "Sad", "Angry"]
emotion_index = 1
time_of_day = ["Morning", "Noon", "Afternoon", "Night"]
time_index = 3
energy = 5
health = 5 
hunger = 5
cleanliness = 5
money = 4
food = 2
food_cost = 2
emotion = "Neutral"
name = input("Please Name Your Rock\n")
print(f"This Is Your Pet Rock,{name}\n🪨\nAnd You Need to Take Care of Him")
while True:
    time_index = (time_index + 1) % len(time_of_day)
    current_time = time_of_day[time_index]
    if time_index == 0:
        energy += 5
        print(f"{name} Has Slept and Feel Refreshed")
    show_stats()   
    if energy == 0:
        print(f"{name} Has Died Of Exhaustion, Give It A Break Next Time")
        break
    elif health == 0:
        print(f"{name} Has Lost Too Much Sediment and Has Died, Next Time Heal It")
        break
    elif hunger == 0:
        print(f"{name} Has Died Of Hunger, Next Time Feed It")
        break
    elif cleanliness == 0: 
        print(f"{name} Has Died Due To Poor Hygiene, Next Time Clean It")
        break
    elif time_index == 0 and emotion_index == 3:
        print(f"{name} Got Too Angry At You and Killed You in Your Sleep, Next Time Make Sure It's Happy")
    action = input("What Will You Do to Take Care of Him?\nEat, Nap, Play, Bath, Work, or Shop\n").lower().strip()
    match action:
        case "eat":
            if food > 0:
                hunger += 3
                energy += 1
                cleanliness -= 2
                health += 1
                food -= 1
                print(f"{name} Has Eaten Food!\n+3 Hunger,-1 Energy,-1 Cleanliness,+1 Health,-1 Food")
            else:
                print("You Have No Food! Go Buy Some!")
        case "nap":
            energy += 3
            hunger -= 2
            cleanliness -= 1
            print(f"{name} Has Taken A Nap\n+3 Energy,-2 Hunger,-1 Cleanliness")
        case "play":
            emotion_index -= 1
            energy -= 2
            cleanliness -= 3
            health -= 2
            hunger -= 2
            print(f"{name} Has Played\n+Emotion,-2 Energy,-2 Cleanliness,-2 Health,-2 Hunger")
        case "bath":
            cleanliness += 5
            energy += 1
            health += 2
            hunger -= 1
            print(f"{name} Has Taken A Bath\n+5 Cleanliness,+1 Energy,+2 Health,-1 Hunger")
        case "work":
            emotion_index += 1
            energy -= 1
            money += 1
            hunger -= 1
            print(f"{name} Has Gone to Work\n- Emotion,+1 Energy,+1 Money, -1 Hunger")
        case "shop":
            emotion_index += 1
            energy -= 1
            hunger -= 1
            buy_food = input("Would You Like to Buy Food?\n Yes or No").strip().lower()
            if buy_food == "yes":
                if money >= FOOD_COST:
                    food += 1
                    money -= FOOD_COST
                    print("You Bought Some Food")
                else:
                    print("You Don't Have Enough Money to Buy Food")
                elif buy_food == "no":
                    print("You Didn't Buy Any Food")
            print(f"{name} Has Gone to the Store\n+ Food,-Emotion,-1 Energy,-1 Hunger")

        case "upupdowndownleftrightleftrightba":
            emotion_index = 0
            energy = 5
            health = 5 
            hunger = 5
            cleanliness = 5
            money = 999999999
            food = 9999999999
            print("Konami Code Activated! All States Maxed!")