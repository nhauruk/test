from datetime import datetime

def days_difference(date1, date2):
    if not isinstance(date1, str) or not isinstance(date2, str):
        print("Ожидаются строки в формате YYYY-MM-DD")
        return

    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
    except ValueError:
        print("Ожидаются строки в формате YYYY-MM-DD")
        return

    ts1 = d1.timestamp()
    ts2 = d2.timestamp()
    diff_days = abs((ts2 - ts1) / 86400)

    print("Разница между датами:", diff_days)
