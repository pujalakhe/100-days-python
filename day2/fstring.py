#There are 365 days in a year, 52 weeks in a year and 12 months in a year.
age=input("enter your current age")
age_int=int(age)
years_remaining=90-age_int
days_remaining=years_remaining*365
weeks_remaining=years_remaining*52
month_remaining=years_remaining*12
#use of fstring to covert all integer value into stg at once
msg=f" You have {days_remaining} days, {weeks_remaining} weeks and {month_remaining} months left "
print(msg)