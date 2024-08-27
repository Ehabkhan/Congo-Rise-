import random

def roll_dice(sides, rolls):
    results = []
    for _ in range(rolls):
        result = random.randint(1, sides)
        results.append(result)
    return results

def main():
    sides = int(input("Enter the number of sides on the dice: "))
    rolls = int(input("Enter the number of rolls: "))

    results = roll_dice(sides, rolls)

    print(f"\nRolling a {sides}-sided dice {rolls} times:")
    for i, result in enumerate(results, start=1):
        print(f"Roll {i}: {result}")

if __name__ == "__main__":
    main()
