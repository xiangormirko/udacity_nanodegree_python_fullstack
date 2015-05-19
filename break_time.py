import webbrowser
import time

loops=3
counter=0

print("This program started on "+time.ctime())
while (counter<loops):
    time.sleep(10)
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=Yt0QpQFBWms")

    counter+=1
