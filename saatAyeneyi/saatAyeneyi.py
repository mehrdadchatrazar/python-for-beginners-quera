hour, minute = map(int, input().split())

hour = (12 - hour) % 12
minute = (60 - minute) % 60

print(f'{hour:02d}:{minute:02d}')