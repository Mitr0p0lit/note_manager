created_date = "23-12-2024"
issue_date = "23-12-2025"
day_created_date, month_created_date, year_created_date = created_date.split(sep="-", maxsplit=-1)
day_issue_date, month_issue_date, year_issue_date = issue_date.split(sep="-", maxsplit=-1)
print(day_created_date, month_created_date, year_created_date)
print(day_issue_date, month_issue_date, year_issue_date)