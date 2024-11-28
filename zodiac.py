from tomlkit import value


class Zodiac:
    """Find zodiac sign in birthdays.
    """
    def __init__(key):
        zodiac = {'March 21': 'Aries', 'April 20': 'Taurus', 'May 21': 'Gemini', 'June 21': 'Cancer', 'July 23': 'Leo', 'August 23': 'Leo', 'September 23': 'Libra', 'October 23': 'Scorpio', 'November 22': 'Sagittarius', 'December 22': 'Capricorn', 'January 20': 'Aquarius', 'February 19': 'Pisces'}
        for str in zodiac.keys():
            if " " in str:
                print(zodiac.get(str), end = " ")
        