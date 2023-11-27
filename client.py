#!/usr/bin/env python3
import argparse
import logging
import os
import requests


# Set logger
log = logging.getLogger()
log.setLevel('INFO')
handler = logging.FileHandler('books.log')
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

# Read env vars related to API connection
FLIGHTS_API_URL = os.getenv("FLIGHTS_API_URL", "http://localhost:8000")



def list_flights():
    suffix = "/flights/list_flights"
    endpoint = FLIGHTS_API_URL + suffix
    response = requests.get(endpoint)
    if response.ok:
        json_resp = response.json()
        for flight in json_resp:
            print(f"-> Flight from: {flight['from_location']} to: {flight['to_location']}")
        
        return json_resp
    else:
        print(f"Error: {response}")

def month_mapper(int_month):
    months = {
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }

    return months.get(str(int_month), None)

def recommended_ag():
    suffix = "/flights/most_recurred_months"
    endpoint = FLIGHTS_API_URL + suffix
    response = requests.get(endpoint)
     #import pdb; pdb.set_trace()
    if response.ok:
        json_resp = response.json()       
        for max_months in json_resp:
            month = month_mapper(max_months['month']) # month key
            print(f"{month} -> Number times visited: {max_months['count']}") 

    else:
        print(f"Error: {response}")


def get_most_recurred_months():
    res = list_flights()
    if not res:
        print("No flights could be listed")

    # group by months
    output = {}
    for flight in res:
        month = flight['month']
        if not month in output:
            output[month] = 0
        
        output[month] += 1
    
    # sort by values
    output = dict(sorted(output.items(), key=lambda item: -int(item[1])))

    return output


def main():
    log.info(f"Welcome to flights research service. App requests to: {FLIGHTS_API_URL}")

    parser = argparse.ArgumentParser()

    list_of_actions = ["list", "recommended", "recommended-ag"]
    parser.add_argument("action", choices=list_of_actions,
            help="Action to be user for the books library")
    args = parser.parse_args()

    if args.action == "list":
        list_flights()
    elif args.action == "recommended":
        output = get_most_recurred_months()
        for key in output.keys():
            month = month_mapper(key)
            print(f"{month} -> Number times visited: {output[key]}")
    
    elif args.action == "recommended-ag":
        recommended_ag()
        

if __name__ == "__main__":
    main()