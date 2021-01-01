import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import math

dataset =pd.read_csv("Ads_CTR_Optimisation.csv")


#REINFORCEMENT LEARNING(UCB AND THOMPSON ALGORITHM)
#UPPER CONFIDENCE BOUND
d = 10
N=10000
ads_selected =[]
number_of_selection = [0]*d
sum_of_reward=[0]*d
total_reward = 0
for n in range(0,N):
    ad =0
    max_upper = 0
    for i in range(0,d):
        if (number_of_selection[i] > 0):
            average_reward = sum_of_reward[i]/number_of_selection[i]
            delta_i = math.sqrt(1.5*math.log(n+1)/number_of_selection[i])
            upper_bound = average_reward + delta_i
        else:
            upper_bound  = 1000000000
            
        if (upper_bound > max_upper ):
            max_upper = upper_bound
            ad = i
    ads_selected.append(ad)
    sum_of_reward[ad] += dataset.values[n,ad]
    number_of_selection[ad] += 1 
    total_reward += dataset.values[n,ad]
    
#Visualizing the result on Histogram on UCB   
plt.hist(ads_selected) 
plt.title("Histogram of ads selection using Upper Confidence Bound")
plt.xlabel("Ads ")
plt.ylabel("Number of selection using UCB")
plt.show()        
        
        
# THOMPSON ALGORITHM
import random
ad_selected = []
number_of_reward_1 = [0]*d
number_of_reward_0 = [0]*d
total_rewards = 0
for n in range (0,N):
    max_random = 0
    ads =0
    for i in range (0,d):
        upper_rad = random.betavariate(number_of_reward_1[i] +1, number_of_reward_0[i] + 1)
        if upper_rad > max_random:
            max_random = upper_rad 
            ads = i
    ad_selected.append(ads)
    reward = dataset.values[n,ads]
    total_rewards += reward
    if reward == 0 :
        number_of_reward_0[ads] += 1
    else:
        number_of_reward_1[ads] += 1
    
#Visualizing the result on Histogram for Thompson  Sampling 
plt.hist(ad_selected) 
plt.title("Histogram of ads selection using Thompson sampling ")
plt.xlabel("Ads ")
plt.ylabel("Number of selection")
plt.show()     
    







