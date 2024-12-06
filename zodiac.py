from zodiac_calendar import zodiac_list, tuple

class Zodiac:
    """Find the zodiac sign that aligns with your birthday.
    """
    def __init__(key):
        failure_count = 0
        while True:
            zodiac = input("Please input your birthday to find your Zodiac sign.\n")
            if tuple in zodiac_list:
                if zodiac in tuple:
                    value = zodiac_list.get(tuple)
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
