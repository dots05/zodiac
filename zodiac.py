import calendar

class Zodiac:
    """Find zodiac sign in birthdays.
    """
    def __init__(key):
        print("List of zodiacs:")
        zodiac_list = {'March 21': 'Aries', 'April 20': 'Taurus', 'May 21': 'Gemini', 'June 21': 'Cancer', 'July 23': 'Leo', 'August 23': 'Virgo', 'September 23': 'Libra', 'October 23': 'Scorpio', 'November 22': 'Sagittarius', 'December 22': 'Capricorn', 'January 20': 'Aquarius', 'February 19': 'Pisces'}
        for str in zodiac_list.keys():
            if " " in str:
                print(zodiac_list.get(str), end = "\n")
                
        zodiac = input("Please input your birthday to find your Zodiac sign.\n")
        
        match zodiac:
            case "March 21":
                print("Aries")
            case "April 20":
                print("Taurus")
            case "May 21":
                print("Gemini")
            case "June 21":
                print("Cancer")
            case "July 23":
                print("Leo")
            case "August 23":
                print("Virgo")
            case "September 23":
                print("Libra")
            case "October 23":
                print("Scorpio")
            case "November 22":
                print("Sagittarius")
            case "December 22":
                print("Capricorn")
            case "January 20":
                print("Aquarius")
            case "February 19":
                print("Pisces")
            case _:
                print("Not an inputtable birthday. Come again later!")