year_in = int(input())


def is_year_leap(year_in):
    if year % 4 == 0:
        return True
    else:
        return False


result = is_year_leap(year_in)
print(f'Год {year_in}: {result}')
