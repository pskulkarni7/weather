import csv
# Write a CSV file with city weather data
with open('temperatures.csv', 'a', newline = "") as file:
    writer = csv.writer(file)

    writer.writerow(['\nNew York', 'Sunny', 25])
    writer.writerow(['Los Angeles', 'Cloudy', 22])
    writer.writerow(['Chicago', 'Rainy', 18])
    writer.writerow(['Houston', 'Sunny', 30])
    writer.writerow(['Phoenix', 'Sunny', 35])