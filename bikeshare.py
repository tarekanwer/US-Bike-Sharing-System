import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
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
    while True:
        city = input('Enter the city name : ')
        if city in CITY_DATA.keys():
            break
        else:
            print('Enter a valid name about data provided')
    
    if city == 'washington':
        tri = 1
    else:
        tri = 0
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter the month name : ')
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter the day name : ')


    print('-'*40)
    return city, month, day ,tri


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] =  df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    common_month = df['Start Time'].dt.month.mode()[0]
    print('the most common month is {}'.format(common_month))
    


    # TO DO: display the most common day of week
    common_day =  df['Start Time'].dt.day_name().mode()[0]
    print('The most common day of the week is {}'.format(common_day))
    


    # TO DO: display the most common start hour
    common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is {}'.format(common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(common_start_station))


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(common_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    
    df['trip'] = 'From ' + df['Start Station'] +' to '+ df['End Station']
    common_com = df['trip'].mode()[0]
    print('The most frequent combination is {}'.format(common_com))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    
    
    total_travel_time = df['Trip Duration'].sum()
    
    print('Total travel time is {} days'.format(total_travel_time/(24*3600)))


    # TO DO: display mean travel time
    
    mean_travel_time = df['Trip Duration'].mean()
    
    print('the mean travel time is {} minutes'.format(mean_travel_time/60))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,tri):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    if tri == 0:
        # TO DO: Display counts of gender
        gen_types = df['Gender'].value_counts()
        print(gen_types)
    
    
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common = df['Birth Year'].mode()[0]
        
        print('the earliest year of birth is {}'.format(earliest_year))
        print('the most recent year of birth is {}'.format(recent_year))
        print('the most common year of birth is {}'.format(common))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day , tri = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,tri)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
