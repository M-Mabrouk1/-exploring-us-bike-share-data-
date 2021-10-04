import time
import pandas as pd


CITY_DATA = {'chicago': 'data/chicago.csv',
             'new york city': 'data/new_york_city.csv',
             'washington': 'data/washington.csv'}
months = ["all", "january", "feburary", "march", "april", "may", "june"]
days = ['all', 'monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday']


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
        city = input(
            "\nPlease enter enter one of three cities Chicago, New York City or Washington: ").lower()
        if city not in CITY_DATA.keys():
            print(
                "Please enter one of the three cities Chicago or New York City or Washington")
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            "\nPlease enter a month from January to June to filter by or all for no filter: ").lower()
        if month not in months:
            print("Please enter a valid month")
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(
            "\nPlease enter a day of a week to filter by or all for no filter: ").lower()
        if day not in days:
            print("Please enter a valid day")
        else:
            break

    print("-"*40)
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
    # read csv into dataframe
    df = pd.read_csv(CITY_DATA[city])
    df.drop("Unnamed: 0", axis=1, inplace=True)
    df.index.rename("Index", inplace=True)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print("Most common month:", popular_month, sep="\n")

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("\nMost common day of week:", popular_day, sep="\n")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Frequent Start Hour:', popular_hour, sep="\n")

    print("\nThis took %.5s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_st = df['Start Station'].mode()[0]
    print("Most common start station:", popular_start_st, sep="\n")

    # display most commonly used end station
    popular_end_st = df['End Station'].mode()[0]
    print("\nMost common End station:", popular_end_st, sep="\n")

    # display most frequent combination of start station and end station trip
    popular_start_end = (df['Start Station'] + "\n" +
                         df['End Station']).mode()[0]
    print("\nMost frequent combination of start station and end station trip:",
          popular_start_end, sep="\n")

    print("\nThis took %.5s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time:\n{} minutes".format(
        round(df["Trip Duration"].sum()/60, 2)), sep="")
    # dispalay average travel time
    print("\nAverage travel time:\n{} minutes".format(
        round(df["Trip Duration"].mean()/60, 2)), sep="")

    print("\nThis took %.5s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df["User Type"].value_counts().to_string()
    print("\nUser Types:", user_types, sep="\n")

    # Display counts of gender
    if "Gender" in df.columns:
        gender = df["Gender"].value_counts().to_string()
        print("\nGender:", gender, sep="\n")
    else:
        print("\nNo gender stats")

    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_year = int(df["Birth Year"].min())
        print("\nEarliest year:", earliest_year)

        most_recent_year = int(df["Birth Year"].max())
        print("\nMost recent year:", most_recent_year)

        most_common_year = int(df["Birth Year"].mode())
        print("\nMost common year:", most_common_year)
    else:
        print("\nNo birth year stats")

    print("\nThis took %.5s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    """Displays sample of raw data if the user wants"""

    start_time = time.time()

    # variable to iterate over index of df
    i = 5
    # ask the user if he/she wants to see a sample of raw data
    while True:
        raw_data = input(
            '\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        
        if raw_data.lower() == "yes":
            print(df[i-5:i])
            i += 5 
        elif raw_data.lower() == "no":
            break
        else:
            print("\nInvalid input, please write yes or no")

    print("\nThis took %.5s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
