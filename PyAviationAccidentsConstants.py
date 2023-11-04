#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyAviationAccidentsConstants.py
 #
 #  File Description:
 #      This Python script, PyAviationAccidentsConstants.py, contains generic Python 
 #      constants for completing common tasks for the Aviation Accidents Project.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  10/05/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyAviationAccidentsWebScrapeAndAPIConstants.py'


# In[3]:


BEGIN_YEAR \
    = 1970

END_YEAR \
    = 2022


AVIATION_SAFETY_NET_MAIN_URL \
    = 'https://aviation-safety.net'

AVIATION_SAFETY_NET_DATABASE_PRIMARY_URL \
    = '/database/year/'


AVIATION_ACCIDENTS_DATA_ONE_CSV_FILE \
    = './Resources/AviationAccidentsData1.csv'

AVIATION_ACCIDENTS_NARRATIVE_ONE_CSV_FILE \
    = './Resources/AviationAccidentsNarratives1.csv'


AVIATION_UPDATED_ACCIDENTS_DATA_CSV_FILE \
    = './Resources/UpdatedAviationAccidentsData.csv'

AVIATION_UPDATED_ACCIDENTS_NARRATIVE_CSV_FILE \
    = './Resources/UpdatedAviationAccidentsNarratives.csv'

AVIATION_DEPARTURE_AIRPORTS_CSV_FILE \
    = './Resources/DepartureAirports.csv'

AVIATION_DESTINATION_AIRPORTS_CSV_FILE \
    = './Resources/DestinationAirports.csv'

AVIATION_ACCIDENT_LOCATIONS_CSV_FILE \
    = './Resources/AccidentLocations.csv'


AVIATION_ACCIDENTS_DATABASE_TABLE_CSV_FILE \
    = './Resources/DatabaseTableAviationAccidents.csv'

COUNTRY_DATABASE_TABLE_CSV_FILE \
    = './Resources/DatabaseTableCountry.csv'

AIRCRAFT_TYPES_DATABASE_TABLE_CSV_FILE \
    = './Resources/DatabaseTableAircraftTypes.csv'

AIRCRAFT_OPERATORS_DATABASE_TABLE_CSV_FILE \
    = './Resources/DatabaseTableAircraftOperators.csv'

AIRCRAFT_DAMAGE_DATABASE_TABLE_CSV_FILE \
    = './Resources/DatabaseTableAircraftDamage.csv'

FLIGHT_PHASE_DATABASE_TABLE_CSV_FILE \
    = './Resources/DatabaseTableFlightPhase.csv'

NATURE_OF_FLIGHT_DATABASE_TABLE_CSV_FILE \
    = './Resources/DatabaseTableNatureOfFlight.csv'

AIRPORTS_DATABASE_TABLE_CSV_FILE \
    = './Resources/DatabaseTableAirports.csv'

DEPARTURE_AIRPORTS_DATABASE_TABLE_CSV_FILE \
    = './Resources/DatabaseTableDepartureAirports.csv'

DESTINATION_AIRPORTS_DATABASE_TABLE_CSV_FILE \
    = './Resources/DatabaseTableDestinationAirports.csv'


SQLITE_DATABASE \
    = 'sqlite:///Visualization/AviationAccidentsDatabase.sqlite'

SQLITE_DATABASE_PATH \
    = './Visualization/AviationAccidentsDatabase.sqlite'


bearingDictionary \
    = {'N': 0.0,
       'NNE': 22.5,
       'NE': 45.0,
       'ENE': 67.5,
       'E': 90.0,
       'ESE': 112.5,
       'SE': 135.0,
       'SSE': 157.5,
       'S': 180.0,
       'SSW': 202.5,
       'SW': 225.0,
       'WSW': 247.5,
       'W': 270.0,
       'WNW': 292.5,
       'NW': 315.0,
       'NNW': 337.5}


# In[ ]:




