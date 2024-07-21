# the real right answer =.=
#from datetime import datetime, timedelta
#
## min drive to annar
#drive_to_annar = int(input())
## min drive to cinema
#drive_to_cinema = int(input())
## time of day of movie start
#movie_start = str(input())
#
#movie_start_time = datetime.strptime(movie_start,'%H%M')
#minutes_to_drive = drive_to_annar + drive_to_cinema
#
#total_drive_time = timedelta(minutes=minutes_to_drive)
#latest_time = movie_start_time - total_drive_time
#latest_time = datetime.strftime(latest_time, '%H%M')
#print(latest_time)

# what they wanted lul
# min drive to annar
drive_to_annar = int(input())
# min drive to cinema
drive_to_cinema = int(input())
# time of day of movie start
movie_start = int(input())

total_minutes = drive_to_annar + drive_to_cinema
latest_time = movie_start - total_minutes
print(latest_time)
