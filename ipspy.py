#!/usr/bin/python3
import sys, os
import json
import random
import socket
from termcolor import colored, cprint
from urllib.request import urlopen

appVer  = "0.1"
appDate = "16/11/16"

def main():
    # check if data is piped to script
    if not os.isatty(0):
        ipAddress = sys.stdin.read()
        ipAddress = ipAddress.replace('\n', ' ').replace('\r', '') # remove newline
    else:
        if len(sys.argv) > 1:
            ipAddress = sys.argv[1]
        else:
            print ("Usage: ipspy.py [ip]")
            sys.exit(2)

    # get json data from function
    jsonData = json.loads(phraseJson(ipAddress))

    # clear terminal
    os.system("clear")

    # print logo and credits
    cprint (getLogo(), "red")
    print ("")
    cprint ("ipspy version: " + appVer + " (" + appDate + ")", "red")
    cprint ("By: Mathias S.", "red")
    print ("")

    # check if the request was successful
    if (jsonData['status'] != "success"):
        cprint ("ipspy failed with error message: " + jsonData['message'] + ". Request IP: " + jsonData['query'], "red")
        sys.exit(2)

    # make sure zip is not empty..
    if (jsonData['zip'] == ""):
        jsonData['zip'] = "None"

    # get ip if hostname was entered
    if (not ipAddress.isnumeric()):
        try:
            ipAddress = str(socket.gethostbyname(ipAddress))
        except:
            print (" [!] Failed to get IP Address from hostname..")

    # request was a success, prepare to print
    cprint ("---------------------------------------", "red")
    cprint (" [!] TARGET IP: " + ipAddress, "red")
    cprint ("---------------------------------------", "red")
    cprint (" [+] ORG: " + jsonData['org'], "green")
    cprint (" [+] ISP: " + jsonData['isp'], "green")
    cprint (" [+] AS: " + jsonData['as'], "green")
    #cprint (" [+] Hostname: " + str(socket.gethostbyaddr(ipAddress)[0]), "green")
    cprint (" [+] City: " + jsonData['city'], "green")
    cprint (" [+] Zip: " + jsonData['zip'], "green")
    cprint (" [+] Region: " + jsonData['regionName'] + " " + "(" + jsonData['region'] + ")", "green")
    cprint (" [+] Country: " + jsonData['country'] + ", " + jsonData['countryCode'], "green")
    cprint (" [+] GeoLoc: " + "Lat: " + str(jsonData['lat']) + " Lon: " + str(jsonData['lon']), "green")
    cprint (" [+] GMaps: " + "https://maps.google.com/maps?q=" + str(jsonData['lat']) + "," + str(jsonData['lon']), "green")
    cprint (" [+] Timezone: " + jsonData['timezone'], "green")
    cprint (" [+] Status: " + jsonData['status'], "green")
    print ("")

def phraseJson(ip):
    jRead = urlopen('http://ip-api.com/json/' + ip)
    return (jRead.read().decode('utf-8'))

def getLogo():
    # define our logo array
    logoArray = []

    ipspyLogo1 = """
        ██╗██████╗     ███████╗██████╗ ██╗   ██╗
        ██║██╔══██╗    ██╔════╝██╔══██╗╚██╗ ██╔╝
        ██║██████╔╝    ███████╗██████╔╝ ╚████╔╝
        ██║██╔═══╝     ╚════██║██╔═══╝   ╚██╔╝
        ██║██║         ███████║██║        ██║
        ╚═╝╚═╝         ╚══════╝╚═╝        ╚═╝
    """
    ipspyLogo2 = """
        ██▓ ██▓███       ██████  ██▓███ ▓██   ██▓
        ▓██▒▓██░  ██▒   ▒██    ▒ ▓██░  ██▒▒██  ██▒
        ▒██▒▓██░ ██▓▒   ░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░
        ░██░▒██▄█▓▒ ▒     ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░
        ░██░▒██▒ ░  ░   ▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░
        ░▓  ▒▓▒░ ░  ░   ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒
        ▒ ░░▒ ░        ░ ░▒  ░ ░░▒ ░     ▓██ ░▒░
        ▒ ░░░          ░  ░  ░  ░░       ▒ ▒ ░░
        ░                    ░           ░ ░
                                         ░ ░
    """
    ipspyLogo3 = """
        ▄█ █ ▄▄         ▄▄▄▄▄   █ ▄▄ ▀▄    ▄
        ██ █   █       █     ▀▄ █   █  █  █
        ██ █▀▀▀      ▄  ▀▀▀▀▄   █▀▀▀    ▀█
        ▐█ █          ▀▄▄▄▄▀    █       █
        ▐  █                    █    ▄▀
           ▀                    ▀
    """
    ipspyLogo4 = """
               _ . - = - . _
          . "  \  \   /  /  " .
        ,  \                 /  .
      . \   _,.--~=~"~=~--.._   / .
     ;  _.-"  / \ !   ! / \  "-._  .
    / ,"     / ,` .---. `, \     ". /
   /.'   `~  |   /:::::\   |  ~`   './
   \`.  `~   |   \:::::/   | ~`  ~ .'/
    \ `.  `~ \ `, `~~~' ,` /   ~`.' /
     .  "-._  \ / !   ! \ /  _.-"  .
      ./    "=~~.._  _..~~=`"    \.
        ,/         ""          \,
          . _/             \_ .
             " - ./. .\. - "
    """

    # add all the logos to the array
    logoArray.extend([ipspyLogo1, ipspyLogo2, ipspyLogo3, ipspyLogo4])

    # get random logo from array and return it
    rnd = random.randrange(len(logoArray))
    return logoArray[rnd]

if __name__ == "__main__":
    main()
