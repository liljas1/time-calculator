def day_of_week(day, passed):
    days_dict = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7,
    }
    day = day.lower().capitalize()
    num_of_day = days_dict.get(day)
    num_of_added_day = num_of_day + passed
    if num_of_added_day > 7:
        num_of_added_day = num_of_added_day % 7

    for key, value in days_dict.items():
        if value == num_of_added_day:
            return key


def add_time(start, duration, day=None):
    start_time, period = start.split()
    start_time = start_time.split(':')

    start_hour, start_minute = start_time
    start_hour, start_minute = int(start_hour), int(start_minute)
    # print(start_hour, start_minute)

    add_hour, add_minute = duration.split(':')
    add_hour, add_minute = int(add_hour), int(add_minute)
    # print(add_hour, add_minute)

    # transforming into 24h
    if period == 'PM':
        start_hour += 12

    added_hour = start_hour + add_hour
    new_minute = start_minute + add_minute
    if new_minute >= 60:
        new_minute -= 60
        added_hour += 1
    new_minute = str(new_minute)
    if int(new_minute) < 10:
        new_minute += '0'
        new_minute = new_minute[::-1]

    if added_hour % 24 >= 12:
        period = 'PM'
    else:
        period = 'AM'

    new_hour = added_hour % 12
    if new_hour == 0:
        new_hour = 12
    new_hour = str(new_hour)

    days_passed = added_hour // 24
    if day is not None:
        new_time = new_hour + ':' + new_minute + ' ' + period + ', ' + str(day_of_week(day, days_passed))
    else:
        new_time = new_hour + ':' + new_minute + ' ' + period

    if days_passed == 0:
        pass
    elif days_passed == 1:
        days_passed = ' (next day)'
        new_time += days_passed
    else:
        days_passed = f' ({days_passed} days later)'
        new_time += days_passed

    return new_time
