from datetime import date

birth_year = int(input("What's Your Birth Year? (e.g., 2012): "))
birth_month = int(input("What's Your Birth Month? (e.g., 12): "))
birth_day = int(input("What's Your Birth Date? (e.g., 14): "))

today = date.today()

age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))

if today.day >= birth_day:
    month = today.month - birth_month
else:
    month = today.month - birth_month - 1

if month < 0:
    month += 12

if today.day >= birth_day:
    day = today.day - birth_day
else:
    previous_month = today.month - 1 if today.month > 1 else 12
    previous_month_days = (date(today.year if previous_month != 12 else today.year - 1, previous_month + 1, 1) - date(today.year if previous_month != 12 else today.year - 1, previous_month, 1)).days
    day = previous_month_days + today.day - birth_day

print(f"Your Age Is! {age} Years {month} Months {day} Days Old")
