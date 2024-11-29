class Zodiac:
    """Find zodiac sign in birthdays.
    """
    def __init__(key):
        zodiac_list = {'March 21': 'Aries', 'April 20': 'Taurus', 'May 21': 'Gemini', 'June 21': 'Cancer', 'July 23': 'Leo', 'August 23': 'Virgo', 'September 23': 'Libra', 'October 23': 'Scorpio', 'November 22': 'Sagittarius', 'December 22': 'Capricorn', 'January 20': 'Aquarius', 'February 19': 'Pisces'}
        
        zodiac = input("Please input your birthday to find your Zodiac sign.\n")
        value = zodiac_list.get(zodiac, "This is not an inputtable birthday. Please try again.")
        print(value)