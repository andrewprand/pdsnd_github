import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago','new york city','washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday','all' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=' '

    while True:
           city = str(input('Let\'s choose the city: Chicago, New York City or Washington? \n').lower())
           if city in CITIES:
              break
           else:
              print('\nPlease, check your data and repeat again.\n')

    # get user input for month (all, january, february, ... , june)
    month=' '
    while True:
            month = str(input('\nPlease, choose the month: type \'all\' or  month name \n'\
                  'January, February, March, April, May, June? \n').lower())
            if month  in MONTHS :
                break
            else:
                print('\nPlease, check your data and repeat again.\n')



    # get user input for a day of week (all, monday, tuesday, ... sunday)
    day=' '
    while True:
            day = str(input('\nPlease, choose the day of week.'\
                        ' Type \'all\' or day of week. \n(e.g. all, monday,..friday) \n').title().lower())
            if day  in DAYS  :
                break
            else:
                print('\nPlease, check your data and repeat again.\n')



    print('-'*40)
    return city, month, day

#Loads data for the city and filters with month and day 
def load_data(city, month, day):
    
   df=pd.read_csv(CITY_DATA[city])
   df['Start Time'] = pd.to_datetime(df['Start Time'])
   df['month'] =df['Start Time'].dt.month
   df['day_of_week'] = df['Start Time'].dt.day_name()
   df['hour'] = df['Start Time'].dt.hour

   if month.lower() !='all':
      months = ['january', 'february', 'march', 'april', 'may', 'june']
      imonth = months.index(month) + 1
      df = df.loc[df['month'] == imonth]

   if day.lower() != 'all':
      days = ['monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']
      df = df.loc[df['day_of_week'] == day.title()]

   return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].value_counts().idxmax()
    print("The most common month:", popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day of week:", popular_day)

    # display the most common start hour
    popular_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour:", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #  display most commonly used start station
    df['Start Station'] = df['Start Station'].mode()[0]
    #  display most commonly used end station
    df['End Station']= df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    print(df.groupby(['Start Station', 'End Station']).size())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time:", total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time:", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Counts of user types:")
    print(df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns:
        print('-'*40)
        print("Counts of gender:")
        print(df['Gender'].value_counts())
        print('-'*40)
    else:
       print('Sorry, no data available for this filter...')


    # Display earliest, most recent, and most common year of birth


    if 'Birth Year' in df.columns:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]

        print('The earliest birth year:', earliest)
        print('The most recent birth year:', most_recent)
        print('The most common birth year:', most_common)
    else:
        print('Sorry, no data available for  this filter...')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   
def show_raw_data(df):
    """   Asking about 5 lines of raw data """
    
    line_count = 0
    answer = str(input("\n Would you like to see 5 lines of raw data .Please write 'yes' or 'no' \n" ).lower())
    while True:
        if answer =='yes':
           five_rows = df.iloc[line_count:line_count+5]
           print(five_rows)
           line_count += 5
           #print(df.head(line_count))
           print('-'*40)
           answer = str(input("\n Do you want to see the next 5 rows. Please write 'yes' or 'no' \n").lower())
           continue
        elif answer == 'no':
           break
        else:
           print('-'*40)
           print('\nPlease, check your data and repeat again.\n')
           answer = str(input("\n Please write 'yes' or 'no' \n").lower())
           continue

    print('-'*40)
    

def main():
    """
    Asking about script restarting - yes or no
    """
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = str(input('\nWould you like to restart? Enter yes or no.\n').lower())
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
