def add_time(start, duration, day=None):
    # Split the start time into hours and minutes
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Calculate the new time
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute
    days_passed = 0
    while new_minute >= 60:
        new_hour += 1
        new_minute -= 60
    
    while new_hour >= 12:
        if new_hour == 12:
            if period == 'AM':
                period = 'PM'
                break
            else:
                period = 'AM'
                days_passed += 1
                break
        elif new_hour > 12:
            if period == 'AM':
                period = 'PM'
            else:
                period = 'AM'
                days_passed += 1
            new_hour -= 12
        
    
    new_time = f'{new_hour}:{new_minute:02d} {period}'
    if day:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        day_index = days.index(day.capitalize())
        new_day_index = (day_index + days_passed) % 7
        new_day = days[new_day_index]
        new_time += f', {new_day}'

    if days_passed >= 1:
        if days_passed == 1:
            new_time += ' (next day)'
        else:
            new_time += f' ({days_passed} days later)'

    return new_time


#testing calculator
print(add_time("3:00 PM", "3:10"))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('11:43 AM', '00:20'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 PM', '24:20', 'tueSday'))
print(add_time('6:30 PM', '205:12'))
