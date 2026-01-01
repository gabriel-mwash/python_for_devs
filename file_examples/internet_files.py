import urllib.request
url = "https://robjhyndman.com/tsdldata/ecology1/hopedale.dat"
with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode("utf-8")
        print(line)

# observe the difference in the code, one has an header one doesn't
# websites can sometimes refuse request from an unknown source hence the header

import urllib.request
url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'

headers = {
    "User-Agent" : "Mozilla/5.0"
    }

request = urllib.request.Request(url, headers=headers)

with urllib.request.urlopen(request) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        print(line)
