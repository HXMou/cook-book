import random

num_skiers = int(input("number of skiers: "))
total_ski_pairs = 0
current_ski_pairs = 0
gondola_count = 1
for i in range(num_skiers):
    ski_pairs = random.randint(1, 3)
    print(f"Skier numbe {i+1} has {ski_pairs} pairs of ski, entering gondola number {gondola_count}") #cuz for loop starts from 0

    total_ski_pairs += ski_pairs

    if current_ski_pairs + ski_pairs > 10:
        print(f"Gondola is full with {gondola_count} gondolas, with {current_ski_pairs} ski pairs")
        gondola_count += 1
        current_ski_pairs = ski_pairs
    else:
        current_ski_pairs += ski_pairs

print(f"total number of ski pairs: {total_ski_pairs}")