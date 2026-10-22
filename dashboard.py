from blessed import Terminal
import time,random

t= Terminal()

with t.fullscreen():
     for i in range(20):
          print (t.home + t.clear)
          print (t.center(t.cyan_bold("PYTHON DASHBOARD")))
          print(t.center(f" progress:{i*5}% "))
          print(t.center(f"CPU: {random.randint(20,90)}% "))
          print(t.center("$" * i + "$" * (19-i)))
          time.sleep(0.2)