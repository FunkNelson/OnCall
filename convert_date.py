import sys

month = int(sys.argv[1])
day = int(sys.argv[2])

months = [(1, "January"), (2, "February"), (3, "March"), (4, "April"),
          (5, "May"), (6, "June"), (7, "July"), (8, "August"), (9, "September"),
          (10, "October"), (11, "November"), (12, "December")]

def convert_date(month, day):
    
    month_string = months[(month) - 1][1]
       
    if day in [1, 21, 31]:
        day_string = "st"
    elif day in [2, 22]:
        day_string = "nd"
    elif day in [3, 23]:
        day_string = "rd"
    else:
        day_string = "th"

    
    date_string = month_string + " " + str(day) + day_string
    return date_string
    
print convert_date(month, day)

