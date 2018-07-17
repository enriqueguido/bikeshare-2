import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def menu():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    menu_option = input('Would you like to see data for Chicago, New York, or Washington? \n')
    while menu_option.lower():
        if menu_option.lower() == 'chicago':
            return 'chicago.csv'
        elif menu_option.lower() == 'new york':
            return 'new_york_city.csv'
        elif menu_option.lower() == 'washington':
            return 'washington.csv'
        else:
            print('Please choose between Chicago, New York, or Washington.')
    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


    # print('-'*40)
    # return city, month, day

def time_frame():
    time_frame_option = input('Would you like to filter the data by month, day, or none')
    while time_frame.lower():
        if time_frame.lower != 'month' or time_frame.lower() != 'day' or time_frame.lower() != 'none':
            print('Please select fromm the options given.')
    return time_frame

def month():
    months_to_choose_dict = {'january': 1,
                            'february': 2,
                            'march':3,
                            'april': 4,
                            'may': 5,
                            'june': 6}

    month_option = input('Please type one of the following months to analyze: \n January, February, March, April, May, June \n')
    while month_option.lower() not in months_to_choose_dict.values():
        if month_option.lower() not in months_to_choose_dict.values():
            print('Please select from the given months to analyze')
    final_month = months_to_choose_dict[month_option.lower()]
    return final_month

def days():
    days_to_choose_dic = {'Monday': 1,
                        'Tuesday': 2,
                        'Wendesday': 3,
                        'Thursday': 4,
                        'Friday': 5,
                        'Saturday': 6,
                        'Sunday': 7}
    days_option = input('Please type a day to analyze \n')
    while days_option.lower() not in days_to_choose_dic.values():
        if days_option.lower() not in days_to_choose_dic.values():
            print('Please select from the given days to analyze')
    final_day = days_to_choose_dic[days_option.lower()]
    return final_day

# def load_data(city, month, day):
#     """
#     Loads data for the specified city and filters by month and day if applicable.
#
#     Args:
#         (str) city - name of the city to analyze
#         (str) month - name of the month to filter by, or "all" to apply no month filter
#         (str) day - name of the day of week to filter by, or "all" to apply no day filter
#     Returns:
#         df - Pandas DataFrame containing city data filtered by month and day
#     """
#
#
#     return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['start_time'].dt.month.mode())
    popular_month = months[index - 1]
    print('The most popular month is {}.'.format(popular_month))

    # display the most common day of week
    common_weeks_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    index = int(df['start_time'].dt.dayofweek.mode())
    popular_day = common_weeks_days[index]
    print('The most popular day of week is {}.'.format(popular_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df.hour.mode()[0]
    print('The most popular hour of the week is {}.'.format(popular_hour) )



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = menu()
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
