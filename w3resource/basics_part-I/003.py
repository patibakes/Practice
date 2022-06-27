# Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

# Z biblioteki 'datetime' importuję klasę 'datetime', a w tej klasie są zdefiniowane różne obiekty na których można wykonwyać różne operacje
from datetime import datetime

# Definiuję zmienną 'now' do której przypisuję metodę 'now()' z klasy 'datetime'
now = datetime.now()
print("current date and time", now)