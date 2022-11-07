age = int(input("What's your age? "))

unit = input("Please choose time unit: Months, Weeks, Days, Hours, Minutes, Seconds. \nNote: You can write the first letter or the full name of the time unit. ").strip().lower()


months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60


if unit == 'months' or unit == 'm':
    print(f'You lived for {months:,} Months')

elif unit == 'weeks' or unit == 'w':
    print(f'You lived for {weeks:,} Weeks')

elif unit == 'days' or unit == 'd':
    print(f'You lived for {days:,} Days')

elif unit == 'hours' or unit == 'H':
    print(f'You lived for {hours:,} Hours')

elif unit == 'minutes' or unit == 'm':
    print(f'You lived for {minutes:,} Minutes')

elif unit == 'seconds' or unit == 's':
    print(f'You lived for {seconds:,} Seconds')

else:
    print('Your choice is not available')
