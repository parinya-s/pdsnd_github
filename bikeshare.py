import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    city = input('Would you like to see data for Chicago, New York City, or Washington?  ')
    city = city.lower()
    while city not in CITY_DATA:
        city = input('Not a valid name! Try again!')
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month? January, February, March, April, May, or June? Type "all" for all months  ')
    month = month.lower()
    while month not in months:
        if month == 'all':
            break
        else:
            month = input('Not a valid month! Try again!')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day of week? Type "all" for every weekday  ')
    day = day.lower()
    while day not in days:
        if day == 'all':
            break
        else:
            day = input('Not a valid day! Try again!')
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
                     month = months.index(month) + 1
                     df = df[df['Month'] == month]
    if day != 'all':
                     df = df[df['Day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if len(df['Month'].unique()) != 1:
        a = df['Month'].mode()[0]
        print('The most popular month:  ', a)

    # TO DO: display the most common day of week
    if len(df['Day_of_week'].unique()) != 1:
        b = df['Day_of_week'].mode()[0]
        print('The most popular day:  ', b)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    c = df['Hour'].mode()[0]
    print('The most popular hour:  ', c)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    d = df['Start Station'].mode()[0]
    print('Most commonly used start station:  ', d)
    # TO DO: display most commonly used end station
    e = df['End Station'].mode()[0]
    print('Most commonly used end station:  ', e)
    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station'] + " to " + df['End Station']
    f = df['start_end_station'].mode()[0]
    print('Most frequent start station and end station trip:  ', f)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    g = df['Trip Duration'].sum()
    h = df['Trip Duration'].count()
    print('Total travel time:  ',g)
    print('Count:  ', h)
    # TO DO: display mean travel time
    i = df['Trip Duration'].mean()
    print('Average travel time:  ', i)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    j = df['User Type'].value_counts()
    print('What is the breakdown of users\n', j)
    print()
    # TO DO: Display counts of gender
    k = df['Gender'].value_counts()
    print('What is the breakdown of genders?\n', k)
    print()
    # TO DO: Display earliest, most recent, and most common year of birth
    l = df['Birth Year'].max()
    m = df['Birth Year'].min()
    n = df['Birth Year'].mode()[0]
    print('What is the oldest, youngest, and most popular year of birth, respectively?')
    print(int(l), int(m), int(n))

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
