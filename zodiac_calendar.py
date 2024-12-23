# add imports
import datetime

#initialize variables
start = datetime.date(1999, 3, 21)
end = datetime.date(2000, 3, 20)
date_list = []
zodiac_list = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
delta = datetime.timedelta(days=1)

# iterate over range of dates
while (start <= end):
    date_list.append(start.strftime("%B %d"))
    start += delta
    
#convert date_tuple to date_lust
date_tuple = tuple(date_list)
birthday_list = {date_tuple: zodiac_list}
