from astral import Astral
import datetime
now = datetime.datetime.now()


city_name = "Plymouth"
a = Astral()
a.solar_depression = 'civil'
city = a[city_name]
sun = city.sun(date=datetime.date(now.year,now.month,now.day),local=True)

sunset = (sun['sunset'])
time = datetime.datetime.now()


while True:
    if time > sunset:
        print("YEA")
