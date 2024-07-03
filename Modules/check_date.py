from check_leap_year import check_leap_year

def check_date(date):
    short =[4,6,9,11]
    long = [1,3,5,7,8,10,12]
    date = date.split('.')
    date = list(map(lambda x: int(x), date))
    # print(date)
    if date[1] in short and 0<date[0]< 31 and date[2]>0:
        return True
    elif date[1] in long and 0<date[0]< 32 and date[2]>0:
        return True
    elif date[1] == 2:
        if check_leap_year(date[2]) and 0<date[0]< 30:
            return True
        elif not check_leap_year(date[2]) and 0<date[0]< 29 and date[2]>0:
            return True
        else:
            return False
    else:
        return False