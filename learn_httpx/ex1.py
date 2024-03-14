import sys
import logging
import httpx
from requests import status_codes
import json

print(sys.platform)

default_site = "https://njrusmc.net" 

def main(site):
    resp = httpx.get(site)
    print(httpx.codes.get_reason_phrase(resp.status_code))
    if httpx.codes.get_reason_phrase(resp.status_code) == "OK": 
        print("Got OK code {}".format(resp.status_code))

    httpx.
def print_status_quote(code):
    return httpx.codes.get_reason_phrase(code)

if __name__ == "__main__":
    print("Main function")
    main(default_site)
