import math

def erlang(A,C):
    L = (A**C) / math.factorial(C)
    sum_concat = 0 
    for n in range(C + 1):
        sum_concat += (A ** n) / math.factorial(n)
    return (L / sum_concat)
    
    
# Cell size = 1.2km2
# 2 Calls per min
# Call duration = 2min
# Number of channels 
blocking_probability_cell_1 = erlang(2 * 1.2 * 2, 13)
print("Blocking probability of cell 1: ", blocking_probability_cell_1)
 
blocking_probability_cell_2 = erlang(4 * 1.2 * 2, 19)
print("Blocking probability of cell 2: ", blocking_probability_cell_2)
 
blocking_probability_cell_3 = erlang(8 * 1.2 * 2, 18)
print("Blocking probability of cell 3: ", blocking_probability_cell_3)
 
blocking_probability_cell_4 = erlang(12 * 1.2 * 2, 17)
print("Blocking probability of cell 4: ", blocking_probability_cell_4)
 
blocking_probability_cell_5 = erlang(10 * 1.2 * 2, 15)
print("Blocking probability of cell 5: ", blocking_probability_cell_5)

overall_blocking_probability = (blocking_probability_cell_1 * 2/36) + (blocking_probability_cell_2 * 4/36) + (blocking_probability_cell_3 *  8/36) + (blocking_probability_cell_4 * 12/36) + (blocking_probability_cell_5 * 10/36)
print("Overall blocking probability: ", overall_blocking_probability)

