import time
import pandas as pd
import numpy as np

CITY_DATA = { 'new york city': 'new_york_city.csv', 'chicago': 'chicago.csv', 'washington': 'washington.csv' }
cities=['new york city','chicago','washington']
months=['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December','All']
days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Welcome to my humble code!!! Let\'s start by exploring some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('Select a city from the following: New York City, Chicago and Washington. \n')).lower()
        if city not in cities:
            print('Please enter a valid city name')
        else:
            break
    # get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Would you like to sort by month? If yes, then type the month. If not, type all\n')).title()
        if month not in months:
            print('Please type a month name that is correct')
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('Would you like to sort by day? If yes, then type the day. If not, type all\n')).title()
        if day not in days:
            print('Please choose a valid day')
        else:
            break


    print('*'*60)
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
	# load data into a df, so it can be used in the code
    df = pd.read_csv(CITY_DATA[city])
    # convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # create new columns for month and day
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filtering using months
    if month != 'All':
        month = months.index(month) + 1
        df = df[df['month'] == month]
    # filtering using days
    if day != 'All':
        df = df[df['day_of_week'] == day]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # Most common month
    month_mode = df['month'].mode()[0]
    print('The most common month is: {}'.format(months[month_mode-1]))
    # Most common day of week
    print('The most common day is: {}'.format(df['day_of_week'].mode()[0]))
    # Most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: {}'.format(df['hour'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*60)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # Most commonly used start station
    print('The most common start station is: {}'.format(df['Start Station'].mode()[0]))
    # Most commonly used end station
    print('The most common end station is: {}'.format(df['End Station'].mode()[0]))
    # Most frequent combination of start station and end station trip
    most_common_c = df['Start Station'].map(str) + ' to ' + df['End Station']
    print('The most popular combination is: {}'.format(most_common_c.mode()[0]))  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*60)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""  
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # Total travel time
    minutes, sec = divmod(df['Trip Duration'].sum(), 60)
    hours, minutes = divmod(minutes, 60)
    print ('The total travel time is: ',hours,' hours, ', minutes,' minutes, and ', sec,' seconds.')
    # Mean travel time
    mean_minutes, mean_sec = divmod(df['Trip Duration'].mean(), 60)
    mean_hours, mean_minutes = divmod(mean_minutes, 60)
    print ('The mean travel time is: ',mean_hours,' hours, ', mean_minutes,' minutes, and ', mean_sec,' seconds.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*60)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Counts of user types
    print('The user can be seen as \n{}'.format(df['User Type'].value_counts()))
    # Counts of gender
    if('Gender' not in df):
        print('Sorry! Gender data are unavailable for Washington')
    else:
        print('The genders are \n{}'.format(df['Gender'].value_counts()))
    # Earliest, most recent, and most common year of birth
    if ('Birth Year' not in df):
        print('Sorry! Birth year data are unavailable for Washington')
    else:
        by = int(df['Birth Year'].min())
        print('The earliest birth year is:', by)
        bry = int(df['Birth Year'].max())
        print('The most recent birth year is:', bry)
        bcy = int(df['Birth Year'].mode()[0])
        print('The most common birth year is:', bcy)
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*60)

def view_data(df):
    start=0
    more=input('\nDo you want to view the data? Enter yes or no.\n')
    while more=='yes':
        try:
            num = int(input('Enter the number of rows to view\n'))
            num = start+num
            print(df[start:num])
            more = input('More rows? Enter yes or no.\n')
            start = num
        except ValueError:
            print('Enter an integer value')    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)    
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
