import datetime
 
aries_start = datetime.date(2000, 3, 21)
aries_end = datetime.date(2000, 4, 19)
list = []
delta = datetime.timedelta(days=1)
 
# iterate over range of dates
while (aries_start <= aries_end):
    list.append(aries_start.strftime("%B %d"))
    aries_start += delta

tuple = tuple(list)
zodiac_list = {tuple: 'Aries'}
