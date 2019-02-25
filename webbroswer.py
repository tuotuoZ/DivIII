import webbrowser
import pytz

#
# webbrowser.open("https://www.python.org")
#
help(webbrowser)

ie = webbrowser.get(webbrowser.iexplore)
ie.open('google.com')