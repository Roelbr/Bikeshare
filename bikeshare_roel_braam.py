"""
This Bikeshare program makes calculations on bikeshare trips to produce statistics from the files from Chicago, New York City and Washington. After the city is selected a time period 'none', 'month' or 'day' is selected. Month selection is on the full month name,
day selection is based on an integer in the range 1-31. After a month or a day is selected a subset of the cityfile of all the months or days  is created as data file and this file is used for further processing in the program.

"""

##  import all necessary packages and functions

import csv
import pprint
import datetime
import time
import collections
from collections import Counter


## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'


def csv_dict_list(city):
    """ Function opens csv based on user input and generates a list with key, value pairs 
     Arg: city file name
    Returns: (list) key, value pairs with the selected city data"""
     
    with open(city) as city_file:
        city_file = [{key: value for key, value in row.items()}
    	for row in csv.DictReader(city_file, skipinitialspace=True)]
    return city_file



def select_month_file(city_file, selected_month):
    """Function  to create a subset of the selected city file data
        Args: city file, selected month based on user input
        Returns: (list) a subset of the cityfile based on selected month
    """

    data  = []
    for i in city_file:
        string_month = datetime.datetime.strptime(i['Start Time'],"%Y-%m-%d %H:%M:%S")
        string_month = string_month.strftime("%B")
        if string_month.lower() == selected_month:
            data.append(i)
    return data    



def select_day_file(city_file, selected_day):
    """ Function  to create a subset of the selected city file data
        Args: city file, selected day based on user input
        Returns: (list)a subset of the cityfile based on selected day
    """

    data = []
    for i in city_file:
        string_day = datetime.datetime.strptime(i['Start Time'],"%Y-%m-%d %H:%M:%S")
        string_day = string_day.strftime("%d")
        if string_day.lower() == selected_day:
            data.append(i)
    return data  




def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    while True:
          city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
       
          if city.lower() not in ('chicago', 'new york', 'washington'):
              print("Please select Chicago, New York or Washington.")
          else:
              if city.lower() == 'new york':
                  city = 'new_york_city'
              return eval(city.lower())
              break  



def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
    (str) The selected full month name to filter the bikeshare data
    '''
    while True:
          selected_month = input('\nWhich month? January, February, March, April, May, or June?\n')
          if selected_month.lower() not in ('january','february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'):   
                  print("Please select a month")
          else:                    
                print ("You selected:  "+str(selected_month))
                return str(selected_month.lower())
                

        

            
def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        (str) Day of the month as a two digit string
    '''

    while True:
        day = int(input('\nWhich day? Please type your response as an integer.\n'))
        if day not in list(range(1,31)):
            print("Please enter a value between 1 and 31")
        else:    
            print( "You selected: " + str(day))
            selected_day = '%02d' % day
            return selected_day
            





def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        (str) For filtering bikeshare data by 'month', 'day'or no filter: 'none
    '''
    while True: 
          time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
          if time_period.lower() not in ('month', 'day', 'none'):
                print("Please select a desired month, day or none if you have no preference")
          else:
                return time_period
                break
            


def popular_stations(data):
    '''
    Question: What is the most popular start station and most popular end station?
    Arg: subsetted data list 
    Returns: (str) 2x with most popular start station and most popular end station
    '''
    
    start_stations = [item['Start Station'] for item in data]
    end_stations = [item['End Station'] for item in data]
    popular_start_station = max(set(start_stations), key=start_stations.count)
    popular_end_station = max(set(end_stations), key=end_stations.count)
    print("The most popular start station is: "+ popular_start_station)
    print("The most popular end station is: " + popular_end_station)    



def popular_trip(data):
    '''
    Question: What is the most popular trip?
    Arg: subsetted data list
    Returns: (str) with most popular trip
    '''
    
    trips = [(item['Start Station'], item['End Station']) for item in data]
    popular_trip = max(set(trips), key=trips.count)
    print ( "The most popular trip is: " + str(popular_trip[0])+", "+ str(popular_trip[1]))




def popular_month(data):
    '''
    Question: What is the most popular month?
    Args: subsetted data list
    Returns: (str) with most popular month
    '''

    start_times = [i['Start Time'] for i in data]
    month_counts = {}
    month_list = [datetime.datetime.strptime(time,"%Y-%m-%d %H:%M:%S").strftime('%B') for time in start_times]
    for month in month_list:
       if month in month_counts:
           month_counts[month] += 1
       else:
           month_counts[month] = 1
    print("The most popular month is: " +  max(month_counts, key = month_counts.get))
    


def popular_day(data):
   '''
   Question: What is the most popular day?
   Args: subsetted data list
   Returns:  (str)  with most popular day
   '''
   
   start_times = [i['Start Time'] for i in data]
   weekday_counts = {}
   weekday_list = [datetime.datetime.strptime(time,"%Y-%m-%d %H:%M:%S").strftime('%A') for time in start_times]
   for week_day in weekday_list:
       if week_day in weekday_counts:
           weekday_counts[week_day] += 1
       else:
           weekday_counts[week_day] = 1
   print("The most popular day is: " + max(weekday_counts, key = weekday_counts.get))




def popular_hour(data):
   '''
   Question: What is the most popular hour of day for start time?
   Args: subsetted data list
   Returns:   (str) with most popular hour
   '''
   
   start_times = [i['Start Time'] for i in data]
   hour_counts = {}
   hour_list = [datetime.datetime.strptime(time,"%Y-%m-%d %H:%M:%S").strftime('%H') for time in start_times]
   for hour in hour_list:
       if hour in hour_counts:
           hour_counts[hour] += 1
       else:
           hour_counts[hour] = 1
   print("The most popular hour is: " + max(hour_counts, key = hour_counts.get))



def trip_duration(data):
    '''
    Question: What is the total trip duration and average trip duration?
    Args: subsetted data list
    Returns:   (str 2x) with total trip duration and average trip duration
    '''
   
    trip_duration = [i['Trip Duration'] for i in data]
    total_duration = sum(list(map(float, trip_duration)))
    average_duration = sum(list(map(float, trip_duration))) / len(trip_duration)
    print ("The total trip duration is: " + (str(round( total_duration,2))) +" minutes")
    print ("The average trip duration is: " + (str(round( average_duration,2))) +" minutes")



def users(data):
    '''
    Question: What are the counts of each user type?
    Args: subsetted data list
    Returns: (str) with key,value with totals of user types
    '''
    
    user_type = [i['User Type'] for i in data]
    counts = Counter(user_type)
    print("The counts of the user types are:")
    for key, value in counts.items():
        print(key, value)
    



def gender(data):
    '''
    Question: What are the counts of gender?
    Args: subsetted data list
    Returns: (str) with key, value with totals of gender. String 'Not provided' added where value is missing.
    '''
    
    gender = [i['Gender'] for i in data]
    gender = ['Not provided' if i not in ('Male', 'Female')  else i for i in gender]
    counts = Counter(gender)
    print("The counts of the genders are:")
    for key, value in counts.items():
        print(key, value)
    



def birth_years(data):
   '''
   Question: What are the earliest, most recent, and most popular birth years?
   Args: subsetted data list
   Returns: (str 3x) with the birth year of the youngest biker, the oldest biker and the birth year with the highest count
   '''
   
   birth_years = [i['Birth Year'] for i in data]
   birth_years = [i for i in birth_years if i]
   most_recent_birth_year = max(birth_years)
   earliest_birth_year = min(birth_years)
   max_counts = max(set(birth_years), key=birth_years.count) 
   print ("The most recent birth year is: " + str(int(float(most_recent_birth_year))))
   print ("The earliest birth year is: " + str(int(float(earliest_birth_year))))
   print ("The most popular birth year is: " + str(int(float( max_counts))))


def print_5_lines(data,city):
    '''
    Sub function for the display-data function to print 5 lines if user requests so.
    Args: subsetted data list and city(needed to provide the right print string with or without gender and birth year.
    Returns: (str 3x) with the birth year of the youngest biker, the oldest biker and the birth year with the highest count.
    ''' 
    count = 0
    while True:
        for row in data:
           if count < 5:
               if city == 'chicago.csv' or city == 'new_york_city.csv':
                   print("Start Time:{0}, End Time:{1}, Trip Duration:{2}, Start Station:{3}, End Station:{4}, User Type:{5}, Gender:{6}, Birth Year:{7}".format(row['Start Time'],
                   row['End Time'], row['Trip Duration'], row['Start Station'], row['End Station'], row['User Type'],row['Gender'], row['Birth Year']))
                   count+=1
               if city == 'washington.csv':
                   print("Start Time:{0}, End Time:{1}, Trip Duration:{2}, Start Station:{3}, End Station:{4}, User Type:{5}".format(row['Start Time'],
                   row['End Time'], row['Trip Duration'], row['Start Station'], row['End Station'], row['User Type']))
                   count+=1 
           else:   
               display = input('Would you like to view 5 more lines?'
                    'Type \'yes\' or \'no\'. ')
                                                
               if display  == 'yes':
                    count = 0
                    continue
               if display == 'no':
                   return
             
                
              

def display_data(data,city):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        Selected data list and city-name
    Returns:
        5 lines of formatted data
    '''
    
    
    display = input('Would you like to view individual trip data?'
                    'Type \'yes\' or \'no\'. ')
    if display not in ('yes', 'no'):
        print("Please enter 'yes' or 'no'")
    else:
        if display == 'yes':
            print_5_lines(data,city) 
       
    print('Printing done!')




def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        the statistics in an interactive experience
    '''

    
    # Filter by city (Chicago, New York, Washington) and retrieve city_file
    city = get_city()
    city_file = csv_dict_list(city)

   
    # Read the selected file and filter by time period (month, day, none)
    time_period = get_time_period()

    if time_period == 'none':
        data = city_file
        
    elif time_period == 'day':
       selected_day = get_day()
       
       data =select_day_file(city_file, selected_day)
      

    elif time_period == 'month':
       selected_month= get_month()
       data = select_month_file(city_file, selected_month)
       
  
    print('Calculating the first statistic...')
    start_time = time.time()

    # What is the most popular month for start time?
    if time_period == 'none':
        popular_month(data)
            
    

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
   
        popular_day(data)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular hour of day for start time?
    
    popular_hour(data)


    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    trip_duration(data)
    

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    popular_stations(data)
    

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    popular_trip(data)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    users(data)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
     
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender(data)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest, most recent, and most popular birth years?
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        birth_years(data)

    print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(data,city)

    # Restart?
    restart = input('Would you like to restart? Type \'yes\' or \'no\'.')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()

	

