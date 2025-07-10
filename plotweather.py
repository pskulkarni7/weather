import matplotlib.pyplot as plt
#This script plots the weather forecast for three cities: Lisbon, New York, and Tokyo.
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
temperatures = [[22, 24, 19, 23, 25], [30, 32, 31, 29, 28], [18, 20, 19, 21, 22]]
# Lisbon, New York, and Tokyo temperatures for the week               

plt.figure(figsize=(10, 6))
Lisbon_temperatures = temperatures[0]  # Lisbon data
Newyork_temperatures = temperatures[1]  # New York data 
Tokyo_temperatures = temperatures[2]  # Tokyo data
plt.plot(days, Lisbon_temperatures, marker='o', linestyle='-', color='b')
plt.plot(days, Newyork_temperatures, marker='o', linestyle='-', color='r')
plt.plot(days, Tokyo_temperatures, marker='o', linestyle='-', color='g')
plt.legend(['Lisbon', 'New York', 'Tokyo'])
plt.title('Weather Forecast for the Week')
plt.xlabel('Days of the Week')
plt.ylabel('Temperature (°C)')
plt.show()

