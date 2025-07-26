temperatures = [10, 12, 14, 15]

# Print the list
print("Temperatures:", temperatures)
# Modify an existing temperature
temperatures[2] = 16
# Print the modified item
print("Modified temperature at index 2:", temperatures[2])
# Add a temperature to the list
temperatures.append(18)
# Print the the newly added item
print("Newly added temperature:", temperatures[-1])


forecast = {
  "Monday": { "temperature": 21, "condition": "Rainy"},
  "Tuesday": { "temperature": 20, "condition": "Sunny"},
  "Wednesday": { "temperature": 23, "condition": "Cloudy"},
  "Thursday": { "temperature": 24, "condition": "Sunny"},
}

# Print the dictionary
print("Weather Forecast:", forecast)    
# Modify Wednesdays temperature to 25 and Sunny
forecast["Wednesday"]["temperature"] = 25
# Print Wednedays temperature
print("Wednesday's temperature:", forecast["Wednesday"]["temperature"])
# Add forecast for Friday, 27, Cloudy
forecast["Friday"] = {"temperature": 27, "condition": "Cloudy"}
# Print Friday temperature such as "Friday's temperature will be 27 degrees and cloudy
print("Friday's temperature will be", forecast["Friday"]["temperature"], "degrees and", forecast["Friday"]["condition"].lower())