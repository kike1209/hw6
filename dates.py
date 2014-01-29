

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    mo = month.lower()
    if len(month) <= 1:
        return None
    else:
        m = month[0].upper() + mo[1:]
    if m in months:
        return m
    else:
        return None

# valid_month("january") => "January"    
# valid_month("January") => "January"
# valid_month("foo") => None
# valid_month("") => None

print valid_month("Janhh")
print valid_month("j")
print valid_month("marCh")

import math

def valid_day(day):
    if day and day.isdigit(day):
    	d=int(day)
    	if d>0 or d<=31:
        	return d

"""
print valid_day('0')
print valid_day('1')
print valid_day('15') 
print valid_day('500')
# valid_day('0') => None    
# valid_day('1') => 1
# valid_day('15') => 15
# valid_day('500') => None
"""

def valid_year(year):
    if year and year.isdigit():
        y=int(year)
        if y>1899 and y<2021:
            return y
        else:
            return None


# valid_year('0') => None    
# valid_year('-11') => None
# valid_year('1950') => 1950
# valid_year('2000') => 2000