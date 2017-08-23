import webbrowser
import time


total_break=3
break_count=0
print "this program start on"+time.ctime()
while break_count<total_break:
	time.sleep(2*60*60)
	webbrowser.open("https://www.youtube.com/watch?v=NucJk8TxyRg")

