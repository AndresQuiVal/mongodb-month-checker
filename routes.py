#!/usr/bin/env python3
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from model import Flight, FlightCount

router = APIRouter()

@router.post("/{city_name}", response_description="Post a new flight from a city specified", status_code=status.HTTP_201_CREATED, response_model=Flight)
def create_flight(city_name: str, request: Request, flight: Flight = Body(...)):
    # import pdb; pdb.set_trace()
    flight_dict = jsonable_encoder(flight)
    # get city name to post
    if (city := request.app.database['cities'].find_one({"city_name" : city_name})) is not None:
        city['airport']['flights'].append(flight_dict)

        request.app.database['cities'].replace_one({"city_name" : city_name}, city) 
        return flight_dict
    
    raise HTTPException(status_code=404, detail=f"City {city_name} not found")
    

@router.get("/most_recurred_months", response_description="Get most recurred months", response_model=List[dict])
def most_recurred_months(request: Request):
    cursor = request.app.database['cities'].aggregate([
        {"$unwind": "$airport.flights"},
        {"$group": {"_id": "$airport.flights.month", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$project": {"_id": 0, "month": "$_id", "count": 1}},
    ])

    result = []
    for item in cursor:
        result.append(item)

    return result


   
@router.get("/list_flights", response_description="Get all created flights", response_model=List[Flight])
def list_flights(request: Request):
    all_flights = []

    r = list(request.app.database['cities'].find())
    for item in r:
        item['_id'] = str(item['_id'])
        print(item)

        if len(item['airport']['flights']) > 0:
            all_flights.extend(item['airport']['flights'])

    return all_flights


@router.get("/list_flights", response_description="Get all created flights", response_model=List[Flight])
def list_flights(request: Request):
    all_flights = []

    r = list(request.app.database['cities'].find())
    for item in r:
        item['_id'] = str(item['_id'])
        print(item)

        if len(item['airport']['flights']) > 0:
            all_flights.extend(item['airport']['flights'])

    return all_flights