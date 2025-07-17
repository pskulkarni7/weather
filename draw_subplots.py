import matplotlib.pyplot as plt

condition = ['sunny', 'rainy', 'cloudy']
days = [300, 30, 35]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.pie(days, labels=condition)
ax2.pie(days, labels=condition)
ax1.set_title('Weather in Lisbon')
ax2.set_title('Weather in Libson')        

ax1.legend(days)
ax2.legend(days)
plt.show()