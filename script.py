#!/usr/bin/python
import webbrowser
import sys

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)


try:
  index = int(sys.argv[1]) - 1
except:
  print("An exception occurred while getting argument.")



url_list = [
'https://www.youtube.com/watch?v=0BNejY1e9ik', #wimhof
'https://www.youtube.com/watch?v=MPG3kBgz_04&list=PL9QosM48zjjZipe_AWkb6SoJgin4zUf94', #winddown ritual
'https://www.youtube.com/watch?v=5qap5aO4i9A'#lofi
]

# eventually have areas for these

url = url_list[index]
webbrowser.open(url)
