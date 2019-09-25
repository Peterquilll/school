def work(month):
    nextMonth = ""

    if month == "jan":
        nextMonth = "feb"
    elif month == "feb":
        nextMonth = "mar"
    elif month == "mar":
        nextMonth = "apr"
    elif month == "apr":
        nextMonth = "may"
    elif month == "may":
        nextMonth = "jun"
    elif month == "jun":
        nextMonth = "jul"
    elif month == "jul":
        nextMonth = "aug"
    elif month == "aug":
        nextMonth = "sep"
    elif month == "sep":
        nextMonth = "oct"
    elif month == "oct":
        nextMonth = "nov"
    elif month == "nov":
        nextMonth = "dec"
    elif month == "dec":
        nextMonth = "jan"
    else:
        print('Please enter a valid month')
    return nextMonth

def days_in_month(year, month):
    is_leap_year = False

    leap = year % 4
    if year == 0 & year % 100 != 0:
        is_leap_year = True
    elif year == 0 or year % 400 == 0:
        is_leap_year = True

    if month in ("jan", "mar", "may", "jul", "aug", "oct", "dec"):
        days_in_month = 31
    elif month == "feb":
        if is_leap_year == True:
            days_in_month = 29
        else:
            days_in_month = 28
    else:
        days_in_month = 30

    return days_in_month

def days_added(day, days_in_month, month, next_month, year):
    if day <= 27 and days_in_month == 28:
        day += 1
    elif day <= 28 and days_in_month == 20:
        day += 1
    elif day <= 29 and days_in_month == 30:
        day += 1
    elif day <= 30 and days_in_month == 31:
         day += 1
    else:
        if day == days_in_month and month == "dec":
            month = next_month
            day = 1
            year = year + 1
        elif day == days_in_month:
            month = next_month
            day = 1

    print ("The next day is: ", month, day, year)



def main():
    year = int(input("Enter a year: "))
    month = str(input("Enter a month: "))
    day = int(input("Enter a day:"))
    months = work(month)
    day_in = days_in_month(year, month)
    day_add = days_added(day, day_in, month, months,year)


if __name__ == '__main__':
    main()
