import time
import webbrowser

total_breaks = 3
break_count = 0

print("This Program Started On: " , time.ctime())       #Current time

while (break_count < total_breaks):                     #Loop For 3 Time
    time.sleep(5)                                       #To Wait 5 Sec
    webbrowser.open("https://www.youtube.com/watch?v=YQHsXMglC9A")
    break_count = break_count + 1
