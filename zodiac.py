from zodiac_calendar import birthday_list, date_tuple

class Zodiac:
    """Find the zodiac sign that aligns with your birthday.
    """
    def __init__(self):
        failure_count = 0
        while True:
            zodiac = input("Please input your birthday to find your Zodiac sign.\n")
            if zodiac in date_tuple:
                dates = birthday_list.get(date_tuple)
                match zodiac:
                    case zodiac if zodiac in date_tuple[0:30]:
                        print(dates[0])
                    case zodiac if zodiac in date_tuple[31:60]:
                        print(dates[1])
                    case zodiac if zodiac in date_tuple[61:90]:
                        print(dates[2])
                    case zodiac if zodiac in date_tuple[91:120]:
                        print(dates[3])
                    case zodiac if zodiac in date_tuple[121:151]:
                        print(dates[4])
                    case zodiac if zodiac in date_tuple[152:181]:
                        print(dates[5])
                    case zodiac if zodiac in date_tuple[182:212]:
                        print(dates[6])
                    case zodiac if zodiac in date_tuple[213:242]:
                        print(dates[7])
                    case zodiac if zodiac in date_tuple[243:273]:
                        print(dates[8])
                    case zodiac if zodiac in date_tuple[274:303]:
                        print(dates[9])
                    case zodiac if zodiac in date_tuple[304:334]:
                        print(dates[10])
                    case zodiac if zodiac in date_tuple[335:365]:
                        print(dates[11])
                break
            else:
                failure_count += 1
                if failure_count > 4:
                    print("Fuck off")
                    break
                else:
                    print("This is not an inputtable birthday. Please try again.\n")
                    continue
