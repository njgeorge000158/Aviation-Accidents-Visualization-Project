#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyAviationAccidentFlaskAPI.py
 #
 #  File Description:
 #      This interactive Python notebook, PyAviationAccidentFlaskAPI.ipynb, uses
 #      various methods to retrieve information from a SQLite database using a
 #      Flask API.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  10/24/2023      Initial Development                     N. James George 
 #
 #******************************************************************************************/

import PyAviationAccidentsConstants as local_constant

import numpy as np

from flask import Flask, jsonify, request
from flask_cors import CORS

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyAviationAccidentFlaskAPI'


# In[3]:


# This line of code generates the engine for the SQLite database.
engineSQLAlchemyEngineObject \
    = create_engine \
        (local_constant.SQLITE_DATABASE)


# This line of code sets up an existing database schema for reflection 
# into a new model.
baseSQLAlchemyDeclarativeMetaObject \
    = automap_base()


# This line of code reflects the database tables.
baseSQLAlchemyDeclarativeMetaObject \
    .prepare \
        (engineSQLAlchemyEngineObject, 
         reflect \
             = True)

# These lines of code save the references to the required database 
# tables.
accidentsSQLAlchemyDeclarativeMetaObject \
    = baseSQLAlchemyDeclarativeMetaObject \
        .classes \
            .accidents

departureDeclarativeMetaObject \
    = baseSQLAlchemyDeclarativeMetaObject \
        .classes \
            .departure

destinationDeclarativeMetaObject \
    = baseSQLAlchemyDeclarativeMetaObject \
        .classes \
            .destination

airportsDeclarativeMetaObject \
    = baseSQLAlchemyDeclarativeMetaObject \
        .classes \
            .airports

countryDeclarativeMetaObject \
    = baseSQLAlchemyDeclarativeMetaObject \
        .classes \
            .country

# Each function correctly creates and binds the session 
# between the python app and database (see below).


# In[4]:


#################################################
# Flask Setup
#################################################
appFlaskAppObject = Flask(__name__)

appFlaskAppObject.json.sort_keys = False

CORS(appFlaskAppObject)


# In[5]:


#################################################
# Flask Routes
#################################################


# In[6]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  years
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the stations URL, '/api/v1.0/years'; the route returns to the 
 #      caller the JSON representation of an ordered List of years in the 
 #      aviation accidents data set.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/24/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

@appFlaskAppObject.route('/api/v1.0/years')

def years():
    
    sessionSQLAlchemySessionObject \
        = Session \
            (engineSQLAlchemyEngineObject)

    
    yearListOfSQLAlchemyEngineRowObject \
        = sessionSQLAlchemySessionObject \
            .query \
                (accidentsSQLAlchemyDeclarativeMetaObject \
                    .year) \
            .order_by \
                ((accidentsSQLAlchemyDeclarativeMetaObject \
                    .year) \
                    .asc()) \
            .distinct() \
            .all()

    
    sessionSQLAlchemySessionObject \
        .close()

    
    yearIntegerList \
        = list \
            (np.ravel \
                (yearListOfSQLAlchemyEngineRowObject))
    
    yearStringList \
        = [str(x) for x in yearIntegerList]
    
    
    return \
        jsonify \
            (yearStringList)


# In[7]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  accident_id_list
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the stations URL, '/api/v1.0/accident_id_list'; the route returns to the 
 #      caller the JSON representation of an ordered List of accident ids in the 
 #      aviation accidents data set.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/24/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

@appFlaskAppObject.route('/api/v1.0/accident_id_list/<int:startYearInteger>/<int:endYearInteger>')

def accident_id_list \
        (startYearInteger,
         endYearInteger):
    
    sessionSQLAlchemySessionObject \
        = Session \
            (engineSQLAlchemyEngineObject)

    
    accidentIDListOfSQLAlchemyEngineRowObject \
        = sessionSQLAlchemySessionObject \
            .query \
                (accidentsSQLAlchemyDeclarativeMetaObject \
                    .accident_id) \
            .filter \
                (accidentsSQLAlchemyDeclarativeMetaObject \
                     .year >= startYearInteger) \
            .filter \
                (accidentsSQLAlchemyDeclarativeMetaObject \
                     .year <= endYearInteger) \
            .order_by \
                ((accidentsSQLAlchemyDeclarativeMetaObject \
                    .date) \
                    .asc()) \
            .all()

    
    sessionSQLAlchemySessionObject \
        .close()

    
    accidentIDStringList \
        = list \
            (np.ravel \
                (accidentIDListOfSQLAlchemyEngineRowObject)) 
    
    return \
        jsonify \
            (accidentIDStringList)


# In[8]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  accident_by_id
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives 
 #      at the stations URL, '/api/v1.0/accident_id_list'; the route returns to the 
 #      caller the JSON representation of an ordered List of accident ids in the 
 #      aviation accidents data set.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/24/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

@appFlaskAppObject.route('/api/v1.0/accident_by_id/<accidentIDString>')

def accident_by_id \
        (accidentIDString):
    
    sessionSQLAlchemySessionObject \
        = Session \
            (engineSQLAlchemyEngineObject)

    
    accidentsSQLAlchemyEngineRowObject \
        = sessionSQLAlchemySessionObject \
            .query \
                (accidentsSQLAlchemyDeclarativeMetaObject.accident_id,
                 accidentsSQLAlchemyDeclarativeMetaObject.date,
                 accidentsSQLAlchemyDeclarativeMetaObject.type,
                 accidentsSQLAlchemyDeclarativeMetaObject.operator,
                 accidentsSQLAlchemyDeclarativeMetaObject.fatalities,
                 accidentsSQLAlchemyDeclarativeMetaObject.occupants,
                 accidentsSQLAlchemyDeclarativeMetaObject.damage,
                 accidentsSQLAlchemyDeclarativeMetaObject.phase,
                 accidentsSQLAlchemyDeclarativeMetaObject.nature,
                 accidentsSQLAlchemyDeclarativeMetaObject.departure,
                 accidentsSQLAlchemyDeclarativeMetaObject.destination,
                 accidentsSQLAlchemyDeclarativeMetaObject.location,
                 accidentsSQLAlchemyDeclarativeMetaObject.country,
                 accidentsSQLAlchemyDeclarativeMetaObject.lat,
                 accidentsSQLAlchemyDeclarativeMetaObject.lon) \
            .filter \
                (accidentsSQLAlchemyDeclarativeMetaObject \
                     .accident_id == accidentIDString) \
            .first()

    
    sessionSQLAlchemySessionObject \
        .close()
    
    
    accidentsDictionary \
        = {'type':'feature',
           'properties': 
                {'accident_id': accidentsSQLAlchemyEngineRowObject['accident_id'],
                 'date': accidentsSQLAlchemyEngineRowObject['date'],
                 'type': accidentsSQLAlchemyEngineRowObject['type'],
                 'operator': accidentsSQLAlchemyEngineRowObject['operator'],
                 'fatalities': int(accidentsSQLAlchemyEngineRowObject['fatalities']),
                 'occupants': int(accidentsSQLAlchemyEngineRowObject['occupants']),
                 'damage': accidentsSQLAlchemyEngineRowObject['damage'],
                 'phase': accidentsSQLAlchemyEngineRowObject['phase'],
                 'nature': accidentsSQLAlchemyEngineRowObject['nature'],
                 'departure': accidentsSQLAlchemyEngineRowObject['departure'],
                 'destination': accidentsSQLAlchemyEngineRowObject['destination'],
                 'location': accidentsSQLAlchemyEngineRowObject['location'],
                 'country': accidentsSQLAlchemyEngineRowObject['country']},
           'geometry': 
                {'type': 'Point',
                 'coordinates': [accidentsSQLAlchemyEngineRowObject['lat'], 
                                 accidentsSQLAlchemyEngineRowObject['lon']]}}

    
    return \
        jsonify \
            (accidentsDictionary)


# In[9]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  categories
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives at the
 #      start/end URL, '/api/v1.0/categories/<category>/<start_year>/<end_year>'; 
 #      the route returns an ordered JSON list of category values for a 
 #      specified date range from the aviation accidents data set.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          categoryString
 #                          This input parameter is the category of the query.
 #  Integer
 #          startYearInteger
 #                          This input parameter is the start year of the query.
 #  Integer
 #          endYearInteger
 #                          This input parameter is the end year of the query.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/24/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

@appFlaskAppObject.route('/api/v1.0/categories/<categoryString>' \
                         + '/<int:startYearInteger>/<int:endYearInteger>')

def categories \
        (categoryString,
         startYearInteger, 
         endYearInteger):
    
    if categoryString == 'type':
        
        accidentsColumnSQLAlchemyDeclarativeMetaObject \
            = accidentsSQLAlchemyDeclarativeMetaObject \
                .type
        
    elif categoryString == 'operator':
        
        accidentsColumnSQLAlchemyDeclarativeMetaObject \
            = accidentsSQLAlchemyDeclarativeMetaObject \
                .operator
        
    elif categoryString == 'damage':
        
        accidentsColumnSQLAlchemyDeclarativeMetaObject \
            = accidentsSQLAlchemyDeclarativeMetaObject \
                .damage
        
    elif categoryString == 'phase':
        
        accidentsColumnSQLAlchemyDeclarativeMetaObject \
            = accidentsSQLAlchemyDeclarativeMetaObject \
                .phase

    elif categoryString == 'nature':
        
        accidentsColumnSQLAlchemyDeclarativeMetaObject \
            = accidentsSQLAlchemyDeclarativeMetaObject \
                .nature
        
    elif categoryString == 'country':
        
        accidentsColumnSQLAlchemyDeclarativeMetaObject \
            = accidentsSQLAlchemyDeclarativeMetaObject \
                .country
        
    else:
        
        return \
            None
    
    
    sessionSQLAlchemySessionObject \
        = Session \
            (engineSQLAlchemyEngineObject)

    
    categoryListOfSQLAlchemyEngineRowObject \
        = sessionSQLAlchemySessionObject \
            .query \
                (accidentsColumnSQLAlchemyDeclarativeMetaObject) \
            .order_by \
                ((accidentsColumnSQLAlchemyDeclarativeMetaObject) \
                    .asc()) \
            .filter \
                (accidentsSQLAlchemyDeclarativeMetaObject \
                     .year >= startYearInteger) \
            .filter \
                (accidentsSQLAlchemyDeclarativeMetaObject \
                     .year <= endYearInteger) \
            .order_by \
                ((accidentsColumnSQLAlchemyDeclarativeMetaObject) \
                     .asc()) \
            .distinct() \
            .all()

    
    sessionSQLAlchemySessionObject \
        .close()
    
        
    categoryStringList \
        = list \
            (np.ravel \
                (categoryListOfSQLAlchemyEngineRowObject))
    
    
    return \
        jsonify \
            (categoryStringList)


# In[10]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  accidents
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives at the
 #      start/end URL, '/api/v1.0/accidents/<start_year>/<end_year>'; the route
 #      returns an ordered JSON list of accident records.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Integer
 #          startYearInteger
 #                          This input parameter is the start year of the query.
 #  Integer
 #          endYearInteger
 #                          This input parameter is the end year of the query.
 #  String
 #          types
 #                          This input parameter is the aircraft type.     
 #  String
 #          operators
 #                          This input parameter is the aircraft operators.   
 #  String
 #          damage
 #                          This input parameter is the aircraft damage.
 #  String
 #          phase
 #                          This input parameter is the flight phase.
 #  String
 #          nature
 #                          This input parameter is the nature of the flight.   
 #  String
 #          country
 #                          This input parameter is the country where the accident 
 #                          occurred.   
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/24/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

@appFlaskAppObject.route('/api/v1.0/accidents/<int:startYearInteger>/<int:endYearInteger>' \
                         + '/<typeString>/<operatorString>/<damageString>/<phaseString>' \
                         + '/<natureString>/<countryString>')

def accidents \
        (startYearInteger, 
         endYearInteger,
         typeString,
         operatorString,
         damageString,
         phaseString,
         natureString,
         countryString):

    defaultString = 'N/A'
    
    
    if typeString.lower() == 'aircraft type':
        
        typesConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.type != defaultString
        
    else:
        
        typesConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.type == typeString
        
    
    if operatorString.lower() == 'aircraft operator':
        
        operatorsConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.operator != defaultString
        
    else:
        
        operatorsConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.operator == operatorString
        
    
    if damageString.lower() == 'aircraft damage':
        
        damageConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.damage != defaultString
        
    else:
        
        damageConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.damage == damageString
        
    
    if phaseString.lower() == 'flight phase':
        
        phaseConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.phase != defaultString
        
    else:
        
        phaseConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.phase == phaseString
        
    
    if natureString.lower() == 'nature of flight':
        
        natureConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.nature != defaultString
        
    else:
        
        natureConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.nature == natureString
        
        
    if countryString.lower() == 'location (country)':
        
        countryConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.country != defaultString
        
    else:
        
        countryConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.country == countryString
        

    sessionSQLAlchemySessionObject \
        = Session \
            (engineSQLAlchemyEngineObject)

    
    accidentsListOfSQLAlchemyEngineRowObject \
        = sessionSQLAlchemySessionObject \
            .query \
                (accidentsSQLAlchemyDeclarativeMetaObject.accident_id,
                 accidentsSQLAlchemyDeclarativeMetaObject.date,
                 accidentsSQLAlchemyDeclarativeMetaObject.year,
                 accidentsSQLAlchemyDeclarativeMetaObject.type,
                 accidentsSQLAlchemyDeclarativeMetaObject.operator,
                 accidentsSQLAlchemyDeclarativeMetaObject.fatalities,
                 accidentsSQLAlchemyDeclarativeMetaObject.occupants,
                 accidentsSQLAlchemyDeclarativeMetaObject.damage,
                 accidentsSQLAlchemyDeclarativeMetaObject.phase,
                 accidentsSQLAlchemyDeclarativeMetaObject.nature,
                 accidentsSQLAlchemyDeclarativeMetaObject.departure,
                 accidentsSQLAlchemyDeclarativeMetaObject.destination,
                 accidentsSQLAlchemyDeclarativeMetaObject.location,
                 accidentsSQLAlchemyDeclarativeMetaObject.country,
                 accidentsSQLAlchemyDeclarativeMetaObject.lat,
                 accidentsSQLAlchemyDeclarativeMetaObject.lon) \
            .filter \
                (accidentsSQLAlchemyDeclarativeMetaObject \
                     .year >= startYearInteger) \
            .filter \
                (accidentsSQLAlchemyDeclarativeMetaObject \
                     .year <= endYearInteger) \
            .filter \
                (typesConditionalObject) \
            .filter \
                (operatorsConditionalObject) \
            .filter \
                (damageConditionalObject) \
            .filter \
                (phaseConditionalObject) \
            .filter \
                (natureConditionalObject) \
            .filter \
                (countryConditionalObject) \
        .order_by \
            ((accidentsSQLAlchemyDeclarativeMetaObject \
                .date) \
                .asc()) \
        .all()

    
    sessionSQLAlchemySessionObject \
        .close()
    
        
    accidentsListOfDictionaries \
        = []
    
    
    for accident_id, date, year, types, operator, fatalities, occupants, \
            damage, phase, nature, departure, destination, \
            location, country, lat, lon \
        in accidentsListOfSQLAlchemyEngineRowObject:
        
        accidentsDictionary \
            = {'type':'feature',
               'properties': 
                  {'accident_id': '',
                   'date': '',
                   'year': '',
                   'type': '',
                   'operator': '',
                   'fatalities': 0,
                   'occupants': 0,
                   'damage': '',
                   'phase': '',
                   'nature': '',
                   'departure': '',
                   'destination': '',
                   'location': '',
                   'country': ''},
               'geometry': 
                  {'type': 'Point',
                   'coordinates': []}}
                
        accidentsDictionary \
            ['properties'] \
            ['accident_id'] \
                = accident_id
        
        accidentsDictionary \
            ['properties'] \
            ['date'] \
                = date

        accidentsDictionary \
            ['properties'] \
            ['year'] \
                = year
        
        accidentsDictionary \
            ['properties'] \
            ['type'] \
                = types
        
        accidentsDictionary \
            ['properties'] \
            ['operator'] \
                = operator
        
        accidentsDictionary \
            ['properties'] \
            ['fatalities'] \
                = fatalities
        
        accidentsDictionary \
            ['properties'] \
            ['occupants'] \
                = occupants

        accidentsDictionary \
            ['properties'] \
            ['damage'] \
                = damage
        
        accidentsDictionary \
            ['properties'] \
            ['phase'] \
                = phase
        
        accidentsDictionary \
            ['properties'] \
            ['nature'] \
                = nature
        
        accidentsDictionary \
            ['properties'] \
            ['departure'] \
                = departure
        
        accidentsDictionary \
            ['properties'] \
            ['destination'] \
                = destination
        
        accidentsDictionary \
            ['properties'] \
            ['location'] \
                = location
        
        accidentsDictionary \
            ['properties'] \
            ['country'] \
                = country
        
        accidentsDictionary \
            ['geometry'] \
            ['coordinates'] \
                .append \
                    (lat)
        
        accidentsDictionary \
            ['geometry'] \
            ['coordinates'] \
                .append \
                    (lon)
        
        
        accidentsListOfDictionaries \
            .append \
                (accidentsDictionary \
                     .copy())
        
    geoJSONDictionary \
        = {'type': 'FeatureCollection',
           'features': accidentsListOfDictionaries}
        

    return \
        jsonify \
            (geoJSONDictionary)


# In[11]:


#*******************************************************************************************
 #
 #  Flask API Route Name:  airports
 #
 #  Flask API Route Description:
 #      This function is a Flask API route that occurs when the user arrives at the
 #      start/end URL, '/api/v1.0/airports/<category>/<start_year>/<end_year>'; the
 #      route returns an ordered JSON list of airport information.
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Integer
 #          startYearInteger
 #                          This input parameter is the start year of the query.
 #  Integer
 #          endYearInteger
 #                          This input parameter is the end year of the query.
 #  String
 #          types
 #                          This input parameter is the aircraft type.     
 #  String
 #          operators
 #                          This input parameter is the aircraft operators.   
 #  String
 #          damage
 #                          This input parameter is the aircraft damage.
 #  String
 #          phase
 #                          This input parameter is the flight phase.
 #  String
 #          nature
 #                          This input parameter is the nature of the flight.   
 #  String
 #          country
 #                          This input parameter is the country where the accident 
 #                          occurred.   
 #  String
 #          category
 #                          This input parameter is the type of airport 
 #                          (departure/destination).
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/24/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

@appFlaskAppObject.route('/api/v1.0/airports/<int:startYearInteger>/<int:endYearInteger>' \
                         + '/<typeString>/<operatorString>/<damageString>/<phaseString>' \
                         + '/<natureString>/<countryString>/<categoryString>')

def airports \
        (startYearInteger,
         endYearInteger,
         typeString,
         operatorString,
         damageString,
         phaseString,
         natureString,
         countryString,
         categoryString):

    defaultString = 'N/A'
    
    
    if typeString.lower() == 'aircraft type':
        
        typesConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.type != defaultString
        
    else:
        
        typesConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.type == typeString
        
    
    if operatorString.lower() == 'aircraft operator':
        
        operatorsConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.operator != defaultString
        
    else:
        
        operatorsConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.operator == operatorString
        
    
    if damageString.lower() == 'aircraft damage':
        
        damageConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.damage != defaultString
        
    else:
        
        damageConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.damage == damageString
        
    
    if phaseString.lower() == 'flight phase':
        
        phaseConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.phase != defaultString
        
    else:
        
        phaseConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.phase == phaseString
        
    
    if natureString.lower() == 'nature of flight':
        
        natureConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.nature != defaultString
        
    else:
        
        natureConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.nature == natureString
        
        
    if countryString.lower() == 'location (country)':
        
        countryConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.country != defaultString
        
    else:
        
        countryConditionalObject \
            = accidentsSQLAlchemyDeclarativeMetaObject.country == countryString
    
    
    sessionSQLAlchemySessionObject \
        = Session \
            (engineSQLAlchemyEngineObject)
    
    
    accidentsListOfSQLAlchemyEngineRowObject \
        = sessionSQLAlchemySessionObject \
            .query \
                (accidentsSQLAlchemyDeclarativeMetaObject.accident_id) \
            .filter \
                (accidentsSQLAlchemyDeclarativeMetaObject \
                     .year >= startYearInteger) \
            .filter \
                (accidentsSQLAlchemyDeclarativeMetaObject \
                     .year <= endYearInteger) \
            .filter \
                (typesConditionalObject) \
            .filter \
                (operatorsConditionalObject) \
            .filter \
                (damageConditionalObject) \
            .filter \
                (phaseConditionalObject) \
            .filter \
                (natureConditionalObject) \
            .filter \
                (countryConditionalObject) \
        .order_by \
            ((accidentsSQLAlchemyDeclarativeMetaObject \
                .accident_id) \
                .asc()) \
        .all()
    
    
    sessionSQLAlchemySessionObject \
        .close()
    
    
    accidentIDStringList \
        = []
    
    for accident_id in accidentsListOfSQLAlchemyEngineRowObject:

        accidentIDStringList \
            .append \
                (accident_id[0])    
    

    if categoryString == 'departure':
        
        airportDeclarativeMetaObject \
            = departureDeclarativeMetaObject
        
    elif categoryString == 'destination':
        
        airportDeclarativeMetaObject \
            = destinationDeclarativeMetaObject
        
    else:
        
        return \
            None    
    
    
    sessionSQLAlchemySessionObject \
        = Session \
            (engineSQLAlchemyEngineObject)
    
    
    airportsListOfDictionaries \
        = []
    
    for accident_id in accidentIDStringList:

        airportsSQLAlchemyEngineRowObject \
            = sessionSQLAlchemySessionObject \
                .query \
                    (airportDeclarativeMetaObject.accident_id,
                     airportDeclarativeMetaObject.name,
                     airportDeclarativeMetaObject.country,
                     airportDeclarativeMetaObject.icao,
                     airportDeclarativeMetaObject.iata,
                     airportDeclarativeMetaObject.lat,
                     airportDeclarativeMetaObject.lon) \
                .filter \
                    (airportDeclarativeMetaObject \
                         .accident_id == accident_id) \
                .first()
        
        
        if len(airportsSQLAlchemyEngineRowObject) > 0:
            
            airportsDictionary \
                = {'type':'feature',
                   'properties': 
                      {'accident_id': '',
                       'name': '',
                       'country': '',
                       'icao': '',
                       'iata': ''},
                   'geometry': 
                      {'type': 'Point',
                       'coordinates': []}}
            
            airportsDictionary \
                ['properties'] \
                ['accident_id'] \
                    = airportsSQLAlchemyEngineRowObject \
                        ['accident_id']
            
            airportsDictionary \
                ['properties'] \
                ['name'] \
                    = airportsSQLAlchemyEngineRowObject \
                        ['name']
        
            airportsDictionary \
                ['properties'] \
                ['country'] \
                    = airportsSQLAlchemyEngineRowObject \
                        ['country']
        
            airportsDictionary \
                ['properties'] \
                ['icao'] \
                    = airportsSQLAlchemyEngineRowObject \
                        ['icao']
        
            airportsDictionary \
                ['properties'] \
                ['iata'] \
                    = airportsSQLAlchemyEngineRowObject \
                        ['iata']
   
            airportsDictionary \
                ['geometry'] \
                ['coordinates'] \
                    .append \
                        (airportsSQLAlchemyEngineRowObject \
                            ['lat'])
        
            airportsDictionary \
                ['geometry'] \
                ['coordinates'] \
                    .append \
                        (airportsSQLAlchemyEngineRowObject \
                             ['lon'])
        
        
            airportsListOfDictionaries \
                .append \
                    (airportsDictionary \
                         .copy())
            
        
    sessionSQLAlchemySessionObject \
        .close()

    
    geoJSONDictionary \
        = {'type': 'FeatureCollection',
           'features': airportsListOfDictionaries}

    
    return \
        jsonify \
            (geoJSONDictionary)


# In[ ]:


if __name__ == '__main__': 
    
    appFlaskAppObject.run \
        (port = 5000, 
         debug = False)


# In[ ]:




