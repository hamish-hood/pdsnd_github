import time
import pandas as pd
import numpy as np

city = { 'Chicago': 'chicago.csv',
              'New York city': 'new_york_city.csv',
              'Washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']
day_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']





def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True: 
        city = input('\nWhich city would you like to investigate out of Chicago, New York City or Washington?')
                     if city not in ('Chicago','New York City','Washington'):
                     print ('invalid answer, please try again')
                     continue 
                     else:
                     break
                     
while True:
          month = input('\nWhich month would you like to look at? from January to June, or you can type all)
    if month not in ('january', 'february', 'march', 'april', 'may', 'june','all'):
              print ('invalid answer, please try again')
                     continue
                        else:
                        break
                        
                     
while True:
           day = input('\nAnd finaly which day are you after?, or you can type all)
      if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
      print  ('invalid answer, please try again')
                       continue
                       else:
                       break
                       
    
    
    
    

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

df = pd.read_csv(CITY_DATA[city])
                       
df['start time'] = pd.to_datetime(df['start time'])                  
df['month'] = df.['start time'].dt.month
df['day_of_week'] = df.['start time'].dt.weekday_name
                       
if month != 'all':
      month = months.index(month) +1                 
    df = df[df['month'] == month]                   
                       
if day != 'all':
      df = df[df['days_of_week'] == day.title()]                                     
                       
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour

                       
    popular_month = df['month'].mode()[0]
                       print('most common month:', popular_month)
    popular_day = df['day_of_week'].mode()[0]                   
                       print('most common day:', popular_day)
    df['hour'] = df['start time'].dt.hour
    popular_hour = df['hour'].mode()[0]                  
                       print('most common hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip

start_station = df['start station'].value_counts().idxmax()
         print('most common start station:', start_station)
end_station = df['end station'].value_counts().idxmax()           
         print('most common end station:', end_station)              
                       
combo_station = df.groupby(['start station', 'end station']).conut()              
          print('the most frequent combination of start and end station trips is:', start_station, " and ",end_station              
                       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time

                
   total_travel_time = sum(df['trip duration'])
  print('total travel time:', total_travel_time/86400, 'days')
                
    mean_travel_time = df['trip duration'].mean()
  print('mean travel time:', mean_travel_time/60, 'minutes')              
                
                

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth

     user_types = df['user type'].value_counts()
      print('user types:', user_types)          
                
try which_gender = df['gender'].value_counts()      
     print('which gender:', which_gender)           
     except KeyError: print('which gender has missing data')       
                
try earliest_year = df['birth year'].min()                
     print('earliest year:', earliest_year)     
     except KeyError: print('earliest year has missing data')    
                
try most_recent_year = df['birth year'].max()
     print('most recent year:', most_recent_year)           
     except KeyError: print('most recent year has missing data') 
                
try most_common_year = df['birth year'].value_counts().idxmax()
     print('most common year:', most_common_year)           
     except KeyError: print('most common year has missing data') 
                
                

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
