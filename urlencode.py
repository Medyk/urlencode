import urllib
import sys

if len(sys.argv) >= 1:
    txt = ' '.join(sys.argv[1:])
    if len(txt) > 0:
        print(urllib.quote(txt))
        exit(0)

exit(1)
