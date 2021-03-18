#Zackary Campbell
#COMP 3006 Project 6
#This script generates a 1000x10 array of data


import numpy as np
import pandas as pd




persons = np.array(['age', 'height(in)', 'weight(lbs)', 'vertical(in)', 'bench(reps@225)', '40 yd dash', 'shoe size', 'wingspan(in)', 'shuttle', 'iq'])

count = 0

for i in range(0,1000):                             #creates fake data at random
    count += 1
    p_age = np.random.randint(0,6) + 19
    p_height = np.random.randint(0,13) + 70
    p_weight = np.random.randint(0,190) + 160
    p_vertical = np.random.randint(0,20) + 24
    p_bench = np.random.randint(0,22) + 4
    p_40 = np.random.random() + 4.1
    p_shoe = np.random.randint(0,7) + 10
    p_wingspan = p_height + np.random.randint(-7, 7)
    p_shuttle = np.random.uniform(4.1, 4.9)
    p_iq = np.random.randint (70, 130)

    player = np.array([p_age, p_height, p_weight, p_vertical, p_bench, p_40, p_shoe, p_wingspan, p_shuttle, p_iq])
#above row puts fake data in an array
    persons = np.vstack((persons, player))              #stacks the new row at the bottom of our big array

df = pd.DataFrame(persons)                              #converts the array to a dataframe

df.to_csv('players.csv')                                #writes dataframe to csv


print(p_shuttle)
print(persons)




