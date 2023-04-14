import sys
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
from art import *


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def getLicense():
    # Create an URL object
    url = 'https://www.faa.gov/data_research/commercial_space_data/licenses/'
    # Create object page
    page = requests.get(url)

    # Obtain page's information
    soup = BeautifulSoup(page.text, "html.parser")

    license_table = soup.find('table', id='launch-license-tbl')
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    count1 = 1
    count2 = 1

    # Clearing the Screen Linux and Windows
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

    print(bcolors.WARNING + text2art("Go Starship!"))
    print(bcolors.OKBLUE + "Request completed in " + str(round(page.elapsed.total_seconds() * 100, 2)) + ' ms' + ' at ' + current_time + '\n')

    print(bcolors.HEADER + '-------------- Starship Licenses ----------------\n' + bcolors.ENDC)

    for index, obj in enumerate(license_table.find_all('td')):
        if 'Starship' in obj.text:
            print(
                str(count1) + '. ' + bcolors.UNDERLINE + bcolors.OKGREEN + bcolors.BOLD + license_table.find_all('td')[index].text + bcolors.ENDC + " ("
                + license_table.find_all('td')[index + 1].text + ") - "
                + bcolors.OKCYAN + "expires: " + license_table.find_all('td')[index + 2].text[9:].strip() + bcolors.ENDC)
            print('\n')
            count1 += 1

    print(bcolors.HEADER + '-------------- SpaceX Licenses ----------------\n' + bcolors.ENDC)

    for index, obj in enumerate(license_table.find_all('td')):
        if ('Space Exploration Technologies Corporation' in obj.text) and (not 'Starship' in obj.text):
            print(str(count2) + '. ' + bcolors.UNDERLINE + bcolors.OKGREEN + license_table.find_all('td')[index + 1].text + bcolors.ENDC + " ("
                + license_table.find_all('td')[index + 2].text + ") - "
                + bcolors.OKCYAN + "expires: " + license_table.find_all('td')[index + 3].text[9:].strip() + bcolors.ENDC)
            print('\n')
            count2 += 1

    aprint("random")

if __name__ == '__main__':
    while True:
        getLicense()
        time.sleep(5)




