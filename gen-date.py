#!/bin/python

from datetime import date, timedelta as td

d1 = date(1900, 1, 1)
d2 = date(2016, 12, 31)

delta = d2 - d1

for i in range(delta.days + 1):
    dta = d1 + td(days=i)
    print (dta.strftime("%d-%m-%Y"))
    print (dta.strftime("%d/%m/%Y"))
    print (dta.strftime("%d.%m.%Y"))
    print (dta.strftime("%d%m%Y"))

    print (dta.strftime("%d-%m-%y"))
    print (dta.strftime("%d/%m/%y"))
    print (dta.strftime("%d.%m.%y"))
    print (dta.strftime("%d%m%y"))

    print (dta.strftime("%Y-%m-%d"))
    print (dta.strftime("%Y/%m/%d"))
    print (dta.strftime("%Y.%m.%d"))
    print (dta.strftime("%Y%m%d"))

    print (dta.strftime("%y-%m-%d"))
    print (dta.strftime("%y/%m/%d"))
    print (dta.strftime("%y.%m.%d"))
    print (dta.strftime("%y%m%d"))