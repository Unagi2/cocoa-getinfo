from datetime import datetime
import jpholiday


genzai = datetime.now()
DATE = genzai.strftime('%Y%m%d')


def isBizDay(DATE):
    Date = (datetime.strptime(DATE, '%Y%m%d')).date()
    if Date.weekday() >= 5 or jpholiday.is_holiday(Date):
        return 0
    else:
        return 1


if __name__ == "__main__":
    isBizDay(DATE)
