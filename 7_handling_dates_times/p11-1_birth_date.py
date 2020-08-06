#!/usr/bin/env python3

from datetime import datetime, timedelta

def get_birth_date():
    birth_date_str = input("Enter birthday (MM/DD/YY): ")    
    birth_date = datetime.strptime(birth_date_str, "%m/%d/%y")

    # if necessary, subtract 100 to fix birth year
    current_year = datetime.now().year
    if birth_date.year > current_year:
        fixed_birth_year = birth_date.year-100
        birth_date = datetime(fixed_birth_year, birth_date.month,
                              birth_date.day)
    return birth_date

def main():
    print("Birthday Calculator")
    print()

    while True:
        name = input("Enter name: ")
        birth_date = get_birth_date()
        current_date = datetime.now()
        
        print("Birthday: " + birth_date.strftime("%A, %B %d, %Y"))
        print("Today:    " + current_date.strftime("%A, %B %d, %Y"))
        
        # calculate person's age
        time_span = current_date - birth_date
        days = time_span.days
        if days > 730:
            years = days // 365
            print(name, "is", years, "years old.")
        else:
            print(name, "is", days, "days old.")

        # calculate days until birthday
        birth_date_this_year = \
            datetime(current_date.year, birth_date.month, birth_date.day)
        time_span = birth_date_this_year - current_date
        days = time_span.days + 1
        if days == 0:
            print(name + "'s birthday is today!")
        elif days == 1:
            print(name + "'s birthday is tomorrow!")
        elif days == -1:
            print(name + "'s birthday was yesterday!")
        elif days > 1:
            print(name + "'s birthday is in", days, "days.")
        elif days < -1:
            print(name + "'s birthday is in", 365-(days*-1), "days.")

        # ask if user wants to continue
        print()
        result = input("Continue? (y/n): ")
        print()
        if result.lower() != "y":
            print("Bye!")
            break      

if __name__ == "__main__":
    main()
