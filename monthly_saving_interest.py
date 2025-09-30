import numpy as np

initial_savings = 1000
monthly_deposits = 500
months = 12
interest = 0.02
time = np.arange(0, months +1)

savings = []
balance = initial_savings

for m in time:
    balance += monthly_deposits
    balance += balance * interest
    savings.append(balance)
    
savings = np.array(savings)

for m, b in zip(time, savings): 
 print(f"Month {m} : ${b:.2f}")
