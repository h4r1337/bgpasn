#!/bin/python3

import argparse
import sys
import subprocess
import requests
from bs4 import BeautifulSoup

URL = "https://bgp.he.net/"


def copy_to_clip(cidr):
    process = subprocess.Popen(['xsel', '-bi'], stdin=subprocess.PIPE)
    process.communicate(input="\n".join(cidr).encode('utf-8'))


def get_ips(soup):
    ranges = []
    prefixes = soup.find("div", id="prefixes")
    prefixes6 = soup.find("div", id="prefixes6")

    if prefixes:
        for cidr in prefixes.tbody.find_all("a"):
            ranges.append(cidr.text)
            print(cidr.text)

    if prefixes6:
        for cidr in prefixes6.tbody.find_all("a"):
            ranges.append(cidr.text)
            print(cidr.text)
    
    return ranges
    

def main():
    cidrs = []
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(
            description="ASN to IP range scraper from bgp.he.net"
        )
        parser.add_argument("-a", required=True, help="ASN")
        args = parser.parse_args()

        ASN = args.a
        ASN_URL = URL + ASN.strip()
        page = requests.get(ASN_URL)

        soup = BeautifulSoup(page.content, "lxml")

        try:
            cidrs = get_ips(soup)
            copy_to_clip(cidrs)
        except:
            print("Error")
    else:
        for line in sys.stdin:
            ASN_URL = URL + line.strip()
            page = requests.get(ASN_URL)

            soup = BeautifulSoup(page.content, "lxml")

            try:
                cidrs = get_ips(soup)
                copy_to_clip(cidrs)
            except:
                print("Error")


if __name__ == "__main__":
    main()
