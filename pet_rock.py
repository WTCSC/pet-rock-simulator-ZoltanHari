def show_stats():
    global energy, hunger, cleanliness, health, money, food, emotion_index
    if energy > 5:
        energy = 5
    if hunger > 5:
        hunger = 5
    if cleanliness > 5:
        cleanliness = 5
    if health > 5:
        health = 5
    if money > 5:
        money = 5
    if hunger > 5:
        hunger = 5
    if emotion_index < 0:
        emotion_index = 0
    elif emotion_index > len(emotions) - 1:
        emotion_index = len(emotions) - 1
    print(f"\n---Rock Stats---\nEmotion: {emotions[emotion_index]}\nHealth: {health}\nEnergy: {energy}\nHunger: {hunger}\nCleanliness: {cleanliness}\nMoney: {money}\nFood: {food}")

emotions = ["Happy", "Neutral", "Sad", "Angry"]
emotion_index = 1
time_of_day = ["Morning", "Noon", "Afternoon", "Night"]
time_index = 0
energy = 5
health = 5 
hunger = 5
cleanliness = 5
money = 4
food = 2
food_cost = 2
emotion = "Neutral"
current_time = time_of_day[time_index]
time_index = (time_index + 1) % len(time_of_day)
if time_index == 0:
    energy += 5
name = input("Please Name Your Rock")
print(f"This Is Your Pet Rock, {name}\n🪨\nAnd You Need to Take Care of Him")
while True:
    show_stats()
    action = input("What Will You Do to Take Care of Him?\nEat, Nap, Play, Bath, Work, or Shop\n").lower()
    match action:
        case "eat":
            if food > 0:
                hunger += 3
                energy -= 1
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
            if emotion_index < len(emotions) + 1:
                emotion_index -= 1
            energy -= 2
            cleanliness -= 3
            health -= 2
            print(f"{name} Has Played\n+Emotion,-2 Energy,-2 Cleanliness,-2 Health")
        case "bath":
            cleanliness += 5
            energy += 1
            health += 2
            print(f"{name} Has Taken A Bath\n+5 Cleanliness,+1 Energy,+2 Health,-1 Hunger")
        case "work":
            if emotion_index > 0:
                emotion_index += 1
            energy += 1
            money += 1
            print(f"{name} Has Gone to Work\n-Emotion,+1 Energy,+1 Money")
        case "shop":
            if emotion_index > 0:
                emotion_index += 1
            energy -= 1
            buy_food = input("Would You Like to Buy Food?\n Yes or No").lower()
            if buy_food == "yes":
                if money >= FOOD_COST:
                    food += 1
                    money -= FOOD_COST
            print(f"{name} Has Gone to the Store\n -Emotion,-1 Energy,+ Food")