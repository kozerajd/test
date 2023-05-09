import random
# This comment is for testing purposes only!
# target coordinates
target_x = 5
target_y = 5

# radius of the target
target_radius = 1

# number of darts to throw
num_darts = 100000000

# initialize number of darts that hit the target
hits = 0

for i in range(num_darts):
    # generate random x and y coordinates for the dart
    dart_x = random.uniform(0, 10)
    dart_y = random.uniform(0, 10)

    # calculate the distance between the dart and the target
    distance = ((dart_x - target_x) ** 2 + (dart_y - target_y) ** 2) ** 0.5

    # check if the dart hit the target
    if distance <= target_radius:
        hits += 1

# calculate the proportion of darts that hit the target
hit_proportion = hits / num_darts

# calculate the estimate of the area of the target
estimate = hit_proportion * (10 ** 2)

print("Estimate of the area of the target:", estimate)
