class Zodiac:
    """Find zodiac sign in birthdays.
    """
    def __init__(key):
        failure_count = 0
        zodiac_list = {'March 21': 'Aries', 'April 20': 'Taurus', 'May 21': 'Gemini', 'June 21': 'Cancer', 'July 23': 'Leo', 'August 23': 'Virgo', 'September 23': 'Libra', 'October 23': 'Scorpio', 'November 22': 'Sagittarius', 'December 22': 'Capricorn', 'January 20': 'Aquarius', 'February 19': 'Pisces'}
        while True:
            zodiac = input("Please input your birthday to find your Zodiac sign.\n")
            if zodiac in zodiac_list:
                value = zodiac_list.get(zodiac)
                print(value + "\n")
                break
            else:
                failure_count += 1
                if failure_count > 4:
                    print("Fuck off")
                    break
                else:
                    print("This is not an inputtable birthday. Please try again.\n")
                    continue