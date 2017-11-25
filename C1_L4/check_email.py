#Using Python 2.7 Not 3 [ex: python check_email.py -NOT- python3 check_email.py]
import urllib

def open_File():
    opfile = open("/home/gemy/Desktop/Nanodegree/C1_L4/Clear_Words.txt")
    connection = opfile.read()
    print(connection)
    opfile.close()
    check_words(connection)

def check_words(Check):
    Checking = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + Check) #Site For Checking [wdylike = what do you like]
    result = Checking.read()
    print(result)
    Checking.close()
    if "true" in result:
        print("This Email Has Curse Words")
    elif "false" in result:
        print("This Email Has No Curse Words")

open_File()
