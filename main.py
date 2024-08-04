from datetime import datetime


with open("test.html", mode="w") as test:
    test.write(str(datetime.today().strftime('%Y-%m-%d %H:%M:%S')))
    