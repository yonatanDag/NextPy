def gen_secs():
    # generator for seconds(0 to 59)
    return (sec for sec in range(0, 60))


def gen_minutes():
    # generator for minutes(0 to 59)
    return (minute for minute in range(0, 60))


def gen_hours():
    # generator for hours(0 to 23)
    return (hour for hour in range(0, 24))


def gen_time():
    # generator for all possible times in a day (hh:mm:ss)
    for hour in gen_hours():
        for minutes in gen_minutes():
            for seconds in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minutes, seconds)


# for gt in gen_time():
#     print(gt)


def gen_years(start=2024):
    # generator for years starting from a given year (default 2024 - the current year)
    while True:
        yield start
        start += 1


def gen_months():
    # generator for months(1 to 12)
    return (month for month in range(1, 13))


def gen_days(month, leap_year=True):
    # generator for days in a given month, accounting for leap years if applicable
    if month == 1:
        return (day for day in range(1, 32))
    elif month == 2:
        if leap_year:
            return (day for day in range(1, 30))
        else:
            return (day for day in range(1, 29))
    elif month == 3:
        return (day for day in range(1, 32))
    elif month == 4:
        return (day for day in range(1, 31))
    elif month == 5:
        return (day for day in range(1, 32))
    elif month == 6:
        return (day for day in range(1, 31))
    elif month == 7:
        return (day for day in range(1, 32))
    elif month == 8:
        return (day for day in range(1, 32))
    elif month == 9:
        return (day for day in range(1, 31))
    elif month == 10:
        return (day for day in range(1, 32))
    elif month == 11:
        return (day for day in range(1, 31))
    elif month == 12:
        return (day for day in range(1, 32))


def gen_date():
    # generator for complete date and time strings (dd/mm/yyyy hh:mm:ss)
    for year in gen_years():
        for month in gen_months():
            # determine if the current year is a leap year
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                leap_year = True
            else:
                leap_year = False
            # generate days for the current month
            for day in gen_days(month, leap_year):
                for gt in gen_time():
                    yield ("%02d/%02d/%04d" % (day, month, year)) + " " + gt


counter = 0
date_generations = gen_date()

# continuously generate and print the date after every 1,000,000 iterations
while True:
    current_date = next(date_generations)
    if counter % 1000000 == 0 and counter != 0:
        print(current_date)
    counter += 1
