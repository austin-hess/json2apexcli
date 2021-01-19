import cProfile
import merge_objs
import random
import time

random.seed(time.time())
letters = 'abcde'
input_arr = []
arr_size = 10000
element_length = 25

for _ in range(arr_size):
    input_arr.append(''.join(random.choice(letters) for _ in range(element_length)))

with cProfile.Profile() as pr:
    for _ in range(100):
        pr.runcall(merge_objs.getDistinctItemsSet, input_arr)
    pr.print_stats()
    for _ in range(100):
        pr.runcall(merge_objs.getDistinctItemsArray, input_arr)
    pr.print_stats()