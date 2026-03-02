import random

num_skiers = int(input("number of skiers: "))
total_ski_pairs = 0
current_ski_pairs = 0
gondola_count = 1
max_ski_pair = 1
gondola_with_max_skis = 0

for i in range(num_skiers):
    ski_pairs = random.randint(1, 3)
    print(f"Skier numbe {i+1} has {ski_pairs} pairs of ski, entering gondola number {gondola_count}") #cuz for loop starts from 0

    total_ski_pairs += ski_pairs

    if current_ski_pairs + ski_pairs > 10:
        print(f"Gondola is full with {gondola_count} gondolas, with {current_ski_pairs} ski pairs")

        if current_ski_pairs > max_ski_pair:
            max_ski_pair = current_ski_pairs
            gondola_with_max_skis = gondola_count

        gondola_count += 1
        current_ski_pairs = ski_pairs
    else:
        current_ski_pairs += ski_pairs

print(f"total number of ski pairs: {total_ski_pairs}")
print(f"Gondola with the most skis: {gondola_with_max_skis}")
print(f"Max ski pairs in a gondola: {max_ski_pair}")