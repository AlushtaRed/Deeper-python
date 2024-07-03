def check_leap_year(year):
    if year >0:
        if year%4 != 0:
            # year = 'Год не високосный'
            return False
        elif year%100 != 0:
            # year = 'Год високосный'
            return True
        elif year%100 == 0 and year%400 ==0:
            # year = 'Год високосный'
            return True
        else: 
            # year = 'Год не високосный'
            return False
    else:
        return False