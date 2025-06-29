class Weather:
    '''Defines weather ofthe city'''

    def __init__(self):
          '''Initializes City,Temp and condition to default value'''
          self.city = " "
          self.temp = 0
          self.condition = " "

    def set_weather(self):
        '''gets weater data from user'''
        self.city = "Mumbai"
        self.temp = 30
        self.condition = "Humid"

    def display_weather(self):
         '''Displays the weather of the city'''
         print(f"City: {self.city}")
         print(f"Temperature: {self.temp}")
         print(f"Condition: {self.condition}")     

city1 = Weather()
city1.set_weather()
city1.display_weather()