# Made by p32929
# My facebook ID: https://www.facebook.com/p32929

import os, smtplib, time
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def send_email(toaddrs, message):
    fromaddr = 'warnerpython@gmail.com'
    SUBJECT = "From Fayaz"
    TEXT = "Down server(s):\n" + message
    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    print("...::: Sending email :::...\n")

    dep1 = 'warnerpython@gmail.com'
    dep2 = '55555666666fay'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(dep1, dep2)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    print("Email sent to %s" % toaddrs)


def check_web(site):
    req = Request(site)
    try:
        response = urlopen(req)
    except HTTPError as e:
        # The server couldn\'t fulfill the request
        # Error code: + e.code
        return False
    except URLError as e:
        # We failed to reach a server
        # Reason: + e.reason
        return False
    else:
        # Website is working fine
        return True


def later():
    count = 0

    email_file = open("email.txt", "r")
    email = email_file.readline()
    email_file.close()

    message = ""

    file = open("URLs.txt", "r")
    print("Checking URLs one by one\n")
    while True:
        var = file.readline()
        if var == "":
            if count != 0:
                message = message.replace("http://", "")
                message = message.replace("https://", "")
                message = message.replace(".com/", " . com / ")
                send_email(email, message)

                # Replacing these characters so that the email provider doesn't consider the email as a SPAM
                
            else:
                print("No warnings :)")
            break
        else:
            print("checking " + var)
            checker = check_web(var)
            if (checker == False):
                count += 1
                print(var + "is down")
                message = message + var

    file.close()
    print("...::: Task completed :::...")
    print("\nWaiting 5 minutes\n")
    time.sleep(300)
    later()


def input_sites_name():
    print("First time running")
    file = open("URLs.txt", "w")
    var = 1
    while (True):
        urls = input("Input URL no %d:(Input 0 when finished)\n" % (var))
        var += 1
        if (urls == "0"):
            print("URL input finished")
            break
        else:
            file.write(urls + "\n")
    file.close()


def input_email():
    file = open("email.txt", "w")
    email = input("Enter an email address(Where the notice will be sent):\n")
    file.write(email)
    file.close()


if os.path.exists("URLs.txt"):
    later()
else:
    input_sites_name()
    input_email()
    later()
