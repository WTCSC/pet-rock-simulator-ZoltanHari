[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/3zOHVIfr)
# Pet Rock Simulator 

This pet rock simulator is a game where you need to take care of a rock by making sure that it stays happy and healthy for as long as you can 
The rock dies when anyone of the stats go under 0 except for the money and food stats and when the rock is angry at the end of the day  
Try to Find the Secret Code When Telling Your Rock What to Do  
Hint: Contra

## Requirements
Python 3.8 or higher

## Installation

1. Clone the Repository

git clone https://github.com/WTCSC/life-decision-simulator-ZoltanHari.git

2. Open the Cloned Repository

cd pet-rock-simulator-ZoltanHari

## Usage 

1. Run **`pet_rock.py`** with the command python3 pet_rock.py in the terminal

2. Name Your Rock and Read Through the Options

3. Type Out an Option to Make the Rock Do It

4. Keep the Rock Alive for as Long a Your Can

### Usage Example

![](https://s1.ezgif.com/tmp/ezgif-18b5cfa490095b.gif)

## Path Modification  

To Edit Existing Options or Add New Ones, Open the **`pet_rock.py`** File and use the Following Format inside the While Loop
```python
action = input("What Will You Do to Take Care of Him?\nEat, Nap, Play, Bath, Work, Shop, or Option 1\n").lower().strip()
match action:
        case "option1":
        stat 1 += 1
        stat 2 -= 2
        print(f"{name} Did Option 1\n+1 Stat 1,-2 stat 2)
```

### Path Modification Example
```python
action = input("What Will You Do to Take Care of Him?\nEat, Nap, Play, Bath, Work, Shop, or Touch Grass\n").lower().strip()
match action:
        case "touchgrass":
        emotion_index -= 1
        energy += 3
        health -= 2
        print(f"{name} Decided to Touch Grass\n- Emotion, +3 Energy,-2 Health)
```

## Flow Chart

https://docs.google.com/drawings/d/1nJ73kJCfmJgfucUXss6C60Y7Sp7FC-rKVFuOCWWh_tg/edit?usp=sharing