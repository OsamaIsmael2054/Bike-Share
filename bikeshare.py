import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june',"all"]
days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city do you want to query about?(chicago, new york city, washington)\n").lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("Error city not found")
    # get user input for month (all, january, february, ... , june)

    while True:
        month = str(input("Which month do you want to query about?\n").lower())
        if month in months:
            break
        else:
            print("Error month not found ")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("Which day do you want to query about?\n").lower())
        if day in days:
            break
        else:
            print("Error day not found ")
    print('-'*40)

    return city, month, day

def load_data(city,month,day):
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

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df["hours"] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int

        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        day = days.index(day)
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].value_counts().index[0]
    print('Most Commonly month:', popular_month)
    
    # display the most common day of week
    popular_day = df['day_of_week'].value_counts().index[0]
    print('\nMost Commonly day:', popular_day)
    
    # display the most common start hour
    popular_hour = df["hours"].value_counts().index[0]
    print('\nMost Commonly hour:', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().index[0]
    print('Most Commonly used start station:', popular_start_station)
    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().index[0]
    print('\nMost Commonly used end station:', popular_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', popular_start_station, " & ", popular_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types: ', user_types)
    
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('\nGender Types: ', gender)
    except:
        print("\n No data available")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        print('\nEarliest Year: ', earliest)
        most_recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year: ', most_recent_Year)
        Most_Common_Year = df['Birth Year'].value_counts().index[0]
        print('\nMost Common Year:', Most_Common_Year)
    except:
        print('\n No data available')

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