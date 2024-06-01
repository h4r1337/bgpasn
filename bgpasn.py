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


def get_ips(ASN, v6=False):
    ASN_URL = URL + ASN.strip()
    page = requests.get(ASN_URL)
    soup = BeautifulSoup(page.content, "lxml")
    ranges = []

    prefixes = soup.find("div", id="prefixes")

    if prefixes:
        prefixes_table = prefixes.find("table", id="table_prefixes4")
        for cidr in prefixes_table.tbody.find_all("a"):
            ranges.append(cidr.text)
            print(cidr.text)

    if v6:
        prefixes6 = soup.find("div", id="prefixes6")
        if prefixes6:
            prefixes_table = prefixes6.find("table", id="table_prefixes6")
            for cidr in prefixes_table.tbody.find_all("a"):
                ranges.append(cidr.text)
                print(cidr.text)
    
    return ranges
    

def main():
    cidrs = []
    parser = argparse.ArgumentParser(
        description="ASN to IP range scraper from bgp.he.net"
    )
    parser.add_argument("-a", type=str, help="ASN")
    parser.add_argument("-v6", action="store_true", help="Include ipv6 ranges in output")
    args = parser.parse_args()

    if args.a:
        try:
            cidrs = get_ips(args.a, args.v6)
            copy_to_clip(cidrs)
        except:
            print("Error")
    elif sys.stdin.isatty():
        parser.print_help()
    else:
        for line in sys.stdin:
            try:
                cidrs = get_ips(line.strip())
                copy_to_clip(cidrs)
            except:
                print("Error")


if __name__ == "__main__":
    main()
