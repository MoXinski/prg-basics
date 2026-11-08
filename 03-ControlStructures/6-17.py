time = input('Enter time (24-hour format): ')
hours = int(time.split(':')[0])
minutes = time.split(':')[1]

if hours == 0:
    print(f'Time in 12-hour format: 12:{minutes}am')
elif hours < 12:
    print(f'Time in 12-hour format: {hours}:{minutes}am')
elif hours == 12:
    print(f'Time in 12-hour format: 12:{minutes}pm')
else:
    print(f'Time in 12-hour format: {hours - 12}:{minutes}pm')
