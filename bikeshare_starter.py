import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input("Enter city name (chicago, new york city, washington): ")
    month = input("Enter month (all, january, february, ... , june): ")
    day = input("Enter day of week (all, monday, tuesday, ... sunday): ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    # Filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month]

    # Filter by day if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Most common month
    common_month = df['month'].mode()[0]
    print(f"Most common month: {common_month.title()}")

    # Most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"Most common day of week: {common_day.title()}")

    # Most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f"Most common start hour: {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(f"Most commonly used start station: {start_station}")

    # Most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f"Most commonly used end station: {end_station}")

    # Most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + " -> " + df['End Station']
    most_common_trip = df['trip'].mode()[0]
    print(f"Most frequent combination trip: {most_common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Total travel time
    total_duration = df['Trip Duration'].sum()
    print(f"Total travel time: {total_duration} seconds")

    # Mean travel time
    mean_duration = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_duration} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:")
    print(user_types.to_string())

    # Counts of gender (if available)
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of gender:")
        print(gender_counts.to_string())
    else:
        print("\nGender data not available for this city.")

    # Earliest, most recent, and most common year of birth (if available)
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nEarliest year of birth: {earliest_year}")
        print(f"Most recent year of birth: {recent_year}")
        print(f"Most common year of birth: {common_year}")
    else:
        print("\nBirth Year data not available for this city.")

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
