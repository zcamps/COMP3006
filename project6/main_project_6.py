#Zackary Campbell
#COMP 3006 Project 6
#Reads CSV file then calculates soem statistics and retrurns a .txt with
#statistics and sample rows



import pandas as pd
import numpy as np
import statistics


df = pd.read_csv('players.csv', header = [1])                     #gets the data from csv in data frame with header names

sampledf = df.loc[3:5]

#I could probably calculate all of these in a loop but honestly it's kinda nice typing them all out
#It feels therapeutic so I decided to do it this way
a_mean = statistics.mean(df['age'])
a_mode = statistics.mode(df['age'])
a_stdev = statistics.stdev(df['age'])
a_median = statistics.median(df['age'])                            #calculates mean, mode, stdev, and median for the age column.


h_mean = statistics.mean(df['height(in)'])
h_mode = statistics.mode(df['height(in)'])
h_stdev = statistics.stdev(df['height(in)'])
h_median = statistics.median(df['height(in)'])                    #calculates same statistics but for height


w_mean = statistics.mean(df['weight(lbs)'])
w_mode = statistics.mode(df['weight(lbs)'])
w_stdev = statistics.stdev(df['weight(lbs)'])
w_median = statistics.median(df['weight(lbs)'])                    #calculates for weight


v_mean = statistics.mean(df['vertical(in)'])
v_mode = statistics.mode(df['vertical(in)'])
v_stdev = statistics.stdev(df['vertical(in)'])
v_median = statistics.median(df['vertical(in)'])                   #calculates for vertical


b_mean = statistics.mean(df['bench(reps@225)'])
b_mode = statistics.mode(df['bench(reps@225)'])
b_stdev = statistics.stdev(df['bench(reps@225)'])
b_median = statistics.median(df['bench(reps@225)'])                 #calculates for bench


f_mean = statistics.mean(df['40 yd dash'])
f_mode = statistics.mode(df['40 yd dash'])
f_stdev = statistics.stdev(df['40 yd dash'])
f_median = statistics.median(df['40 yd dash'])                    #calculates for 40-yd dash


s_mean = statistics.mean(df['shoe size'])
s_mode = statistics.mode(df['shoe size'])
s_stdev = statistics.stdev(df['shoe size'])
s_median = statistics.median(df['shoe size'])                       #calculates for shoe size


ws_mean = statistics.mean(df['wingspan(in)'])
ws_mode = statistics.mode(df['wingspan(in)'])
ws_stdev = statistics.stdev(df['wingspan(in)'])
ws_median = statistics.median(df['wingspan(in)'])                     #calculates for wingspan


sh_mean = statistics.mean(df['shuttle'])
sh_mode = statistics.mode(df['shuttle'])
sh_stdev = statistics.stdev(df['shuttle'])
sh_median = statistics.median(df['shuttle'])                       #calculate for shuttle


iq_mean = statistics.mean(df['iq'])
iq_mode = statistics.mode(df['iq'])
iq_stdev = statistics.stdev(df['iq'])
iq_median = statistics.median(df['iq'])                        #calculate for iq

A = np.array([['category', 'mean', 'mode', 'stdev', 'median'],['Age', a_mean, a_mode, a_stdev, a_median], ['height', h_mean, h_mode, h_stdev, h_median],
              ['weight', w_mean, w_mode, w_stdev, w_median], ['vertical', v_mean, v_mode, v_stdev, v_median],
              ['bench', b_mean, b_mode, b_stdev, b_median], ['40 yd dash', f_mean, f_mode, f_stdev, f_median],
              ['shoesize', s_mean, s_mode, s_stdev, s_median], ['wingspan', ws_mean, ws_mode, ws_stdev, ws_median],
              ['shuttle', sh_mean, sh_mode, sh_stdev, sh_median], ['iq', iq_mean, iq_mode, iq_stdev, iq_median]])


#the above array has all of the calculated statistics put in rows and columns. Rows represent the catgery and the columns are the various stats

newdf = pd.DataFrame(A)
print(newdf)
print(sampledf)


#takes our outputs and puts them in a .txt
newdf.to_json('playerText', orient= 'index')
sampledf.to_json('playerText', orient= 'index')










