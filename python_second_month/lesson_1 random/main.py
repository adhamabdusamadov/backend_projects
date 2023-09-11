# my_set = {0}

# for i in range(1, 101):
#     if i % 10 == 0:
#         i = str(i)
#         for a in i:
#             i = int(i)
#             if a in '2468':
#                 my_set.add(i)
# print(my_set)

import random
numbers = []
for i in range(10):
    numbers.append(random.randint(1, 5))

print(numbers)