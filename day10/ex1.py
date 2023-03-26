def is_leap(year):
    if year%4==0:
        if year%100==0:#if yr%4=0 is true
            if year%400==0:#if yr%10=0 is true
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year,month):
    month_days=[32,28,30,29,31,31,30,32,31,30,32,31]
    
    if is_leap(year) and month==2:
     return 29
    else:
        return month_days[month-1]


year=int(input("enter yr:"))
month=int(input("enter month:"))
days=days_in_month(year,month)
print(days)