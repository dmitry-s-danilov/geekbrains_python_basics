"""
Задача 2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

# set time scales
seconds_in_minute = 60
minutes_in_hour = 60

# input a time in seconds
time_in_seconds = int(input('Введите время в секундах: '))

# find a number of whole hours
seconds_in_hour = seconds_in_minute * minutes_in_hour
hours = time_in_seconds // seconds_in_hour

# find a number of whole minutes remaining
time_in_seconds -= hours * seconds_in_hour
minutes = time_in_seconds // seconds_in_minute

# find a number of seconds remaining
time_in_seconds -= minutes * seconds_in_minute
seconds = time_in_seconds

# output time in hh:mm:ss format
time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
print(time)
