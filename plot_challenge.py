import matplotlib.pyplot as plt

years = [2000, 2005, 2010, 2015, 2020]
temp_anomalies = [0.8, 0.9, 1.0, 1.2, 1.3]  # °C deviation from a baseline
co2_emissions = [25, 30, 35, 40, 45]  # in billions of metric tons

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.plot(years, temp_anomalies, marker='o', linestyle='-', color='b')
ax2.bar(years, co2_emissions, color='r', width=0.8)
ax1.set_title('Global Temperature Anomalies Over Years')
ax2.set_title('Global CO2 Emissions Over Years')        
ax1.set_xlabel('Year')
ax2.set_xlabel('Year') 
ax1.set_ylabel('Temperature Anomaly (°C)')
ax2.set_ylabel('CO2 Emissions (billion metric tons)')  
ax1.legend(['Temperature Anomaly'], loc='upper left')
ax2.legend(['CO2 Emissions'], loc='upper left')
plt.tight_layout()
plt.savefig('climate_change_analysis.png')
plt.show()           