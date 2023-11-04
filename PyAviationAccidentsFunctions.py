#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyAviationAccidentsFunctions.py
 #
 #  File Description:
 #      This Python script, PyAviationAccidentsFunctions, contains generic Python
 #      functions for extracting, transforming, loading and analyzing aviation 
 #      accidents. Here is a list of the functions:
 #
 #      ReturnHtmlElementTextFromList
 #      ReturnDateTimeFromString
 #      ReturnFatalitiesAndOccupantsFromString
 #      ReturnFormattedAccidentLocationString
 #      ReturnClassificationsListFromHTML
 #      ReturnCleanAircraftOperators
 #      ReturnCleanAircraftTypes
 #      ReturnRenamedAirport
 #      ReturnParsedLocationInformation
 #      ReturnAirportsDictionaryFromModule
 #      ReturnAirportsDictionaryFromMapQuest
 #      ReturnGeocodeDataFrameForAirports
 #      ReturnRenamedLocation
 #      ReturnLocationDictionaryFromString
 #      ReturnLocationDictionaryNearWithinLocation
 #      ReturnLocationDictionaryOfOffFromLocation
 #      ReturnLocationDictionaryLocation
 #      ReturnGeocodeDataFrameForAccidents
 #      ReturnNewGeoCoordinates
 #      ReturnCountryDataFrame
 #      ReturnStandardizedCountryNames
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  10/17/2023      Initial Development                     N. James George
 #
 #******************************************************************************************/

import PyLogFunctions as log_function
import PyLogSubRoutines as log_subroutine
import PyAviationAccidentsConstants as local_constant

from PyAviationAccidentsConfig import mapquest_api_key

from datetime import datetime as dt
from math import asin, atan2, cos, degrees, radians, sin
from countryinfo import CountryInfo

import airportsdata
import country_converter
import random
import re
import requests

import pandas as pd

countryConverterObject \
    = country_converter.CountryConverter()


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyAviationAccidentsFunctions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnHtmlElementTextFromList
 #
 #  Function Description:
 #      This function returns the text from an HTML element specified by the parameters.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List of Strings
 #          textElementsStringList
 #                          This parameter is a List of HTML elements from a webpage.
 #  String
 #          criteriaString
 #                          This parameter is the search criteria for the webpage.
 #  Boolean
 #          allTextFlagBoolean
 #                          This parameter specifies that the result must be all text.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnHtmlElementTextFromList \
        (textElementsStringList,
         criteriaString,
         allTextFlagBoolean \
            = None):
    
    try:
        
        if criteriaString == 'Time:' \
            or criteriaString == 'First flight:' \
            or criteriaString == 'MSN:':
            
            defaultString = 'Unknown'
            
        else:
            
            defaultString = 'None'
        
        
        tempString = 'n/a'
        
        matchingStringList \
            = [s for s in textElementsStringList if criteriaString in s]
        
          
        if len(matchingStringList) > 0:
        
            criteriaWithSpaceString = criteriaString + ' '
                
            matchingString \
                = matchingStringList[0]
                
            if len(matchingString) == len(criteriaString):
                    
                tempString \
                    = defaultString
                
            elif criteriaWithSpaceString in matchingString:
                    
                if len(matchingString) == len(criteriaWithSpaceString):
                        
                    tempString \
                        = defaultString
                        
                else:
                        
                    tempString \
                        = matchingString[len(criteriaWithSpaceString):]
                    
            else:
                    
                tempString \
                    = matchingString[len(criteriaString):]
            
            
            if allTextFlagBoolean == True \
                and any(c.isalpha() for c in tempString) == False \
                and (criteriaString != 'Registration:' and criteriaString != 'MSN:'):
                        
                tempString = defaultString
                
            if criteriaString == 'Time:' and tempString != 'Unknown':
                
                colonIndexInteger = tempString.index(':')
                
                if colonIndexInteger == 1:
                    
                    tempString = tempString[0:4]
                
                elif colonIndexInteger == 2:
                    
                    tempString = tempString[0:5]
                    
                else:
                    
                    startIndexInteger = colonIndexInteger - 2
                    
                    endIndexInteger = colonIndexInteger + 3
                    
                    if endIndexInteger > len(tempString) - 1:
                        
                        endIndexInteger = len(tempString) - 1
                    
                    tempString = tempString[startIndexInteger:endIndexInteger]
             
        else:
                
            tempString = defaultString
        
        
        return \
            tempString
        
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnHtmlElementTextFromList, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return the requested text from a List '
                 + 'of HTML elements.')
        
        return \
            'n/a'


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnDateTimeFromString
 #
 #  Function Description:
 #      This function returns a datetime object from a date object a time String.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Date
 #          dateObject
 #                          This parameter is the input Date object.
 #  String
 #          timeString
 #                          This parameter is the input time as a String.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnDateTimeFromString \
        (dateObject,
         timeString):
    
    try:

        if timeString != 'Unknown':
            
            tempTimeString \
                = timeString
                    
        else:
                
            tempTimeString \
                = '00:00'
                
        timeObject \
            = dt.strptime \
                    (tempTimeString, '%H:%M') \
                .time()
            
        tempDateTime \
            = dt.combine \
                    (dateObject, 
                     timeObject)
        
        return \
            tempDateTime
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnDateTimeFromString, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a datetime object from a date object'
                 + 'and time String.')
        
        return \
            '00:00'


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnFatalitiesAndOccupantsFromString
 #
 #  Function Description:
 #      This function returns the numbers of fatalaties and occupants from a String.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          informationString
 #                          This parameter is the String containing the information.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnFatalitiesAndOccupantsFromString \
        (informationString):
    
    try:
        
        informationStringList \
            = informationString.split(' ')

        if len(informationStringList) < 5:
            
            return \
                [0, 0]
                   
        if any(c.isnumeric() for c in informationStringList [1]) \
            == True:
                
            fatalitiesInteger \
                = int(informationStringList [1])
                
        else:
                
            fatalitiesInteger \
                = 0
                
                
        if any(c.isnumeric() for c in informationStringList [4]) \
            == True:
        
            occupantsInteger \
                = int(informationStringList [4])
                
        else:
                
            occupantsInteger \
                = 0
        
        
        resultsIntegerList \
            = []
        
        resultsIntegerList \
            .append \
                (fatalitiesInteger)
        
        resultsIntegerList \
            .append \
                (occupantsInteger)   
        
        
        return \
            resultsIntegerList
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnFatalitiesAndOccupantsFromString, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a fatalities and occupants from a String.')
        
        return \
            [0, 0]


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnFormattedAccidentLocationString
 #
 #  Function Description:
 #      This function returns a formatted location String for the accident.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          informationString
 #                          This parameter is the String containing the information.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnFormattedAccidentLocationString \
        (informationString):
    
    try:
        
        tempInformationString \
            = informationString.strip()
                
        informationStringList \
            = tempInformationString.split(' ')
        
        formattedString \
            = tempInformationString
            
            
        for index, element in enumerate(informationStringList):
                
            element = element.strip()
                
            if len(element) > 0:
                    
                if index == 0:
                    
                    formattedString = element
                
                elif lastElementString == '(':
                    
                    formattedString += element
                    
                else:
                
                    formattedString = formattedString + ' ' + element
                    
                    
                lastElementString = element

                
        return \
            formattedString
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnFormattedAccidentLocationString, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a fatalities and occupants from a String.')
        
        return \
            None


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnClassificationsListFromHTML
 #
 #  Function Description:
 #      This function returns a formatted list of classifications from a list 
 #      of HTML elements.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String List
 #          classificationsHtmlList
 #                          This parameter is the String containing the information.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnClassificationsListFromHTML \
        (classificationsHtmlList):
    
    try:
        
        classificationsStringList \
            = []
        
        
        for classification in classificationsHtmlList:

                classificationsStringList \
                    .append \
                        (classification.text.strip())
      
        
        for index, classification in enumerate (classificationsStringList):

            if len(classification) == 0:

                del classificationsStringList[index]
    
        for index, classification in enumerate (classificationsStringList):

            if classification == '':

                classificationsStringList.remove(classificationsStringList[index])

        
        return \
            classificationsStringList
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnFormattedAccidentLocationString, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a fatalities and occupants from a String.')
        
        return \
            [] 


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnCleanAircraftOperators
 #
 #  Function Description:
 #      This function returns a clean Series of aircraft operators.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          initialInputSeries
 #                          This parameter is the input Series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnCleanAircraftOperators \
        (initialInputSeries):
    
    try:
        
        inputSeries \
            = initialInputSeries.copy()

        for index, aircraftOperator in inputSeries.items():
            
            tempString = aircraftOperator.lower()
            
            if tempString == 'aerolift company':
                
                inputSeries \
                    [index] \
                        = 'Aerolift'
                
            elif tempString == 'air north queensland':
             
                inputSeries \
                    [index] \
                        = 'Airnorth'
                
            elif tempString == 'air serv limited' \
                    or tempString == 'air services limited - asl':
                
                inputSeries \
                    [index] \
                        = 'Air Services Limited'    
                
            elif tempString == 'eagle aviation ?':
            
                inputSeries \
                    [index] \
                        = 'Eagle Aviation'   
                
            elif tempString == 'malaysian airlines system - mas':
                
                inputSeries \
                    [index] \
                        = 'Malaysia Airlines'
                
            elif tempString == 'millon air':
                
                inputSeries \
                    [index] \
                        = 'Million Air'                
                
            elif tempString == 'phoenix':
                
                inputSeries \
                    [index] \
                        = 'Phoenix Air'
                
            elif tempString == 'star jet':
                
                inputSeries \
                    [index] \
                        = 'Starjet Inc.'
                
            elif tempString == 'tropicair':
                
                inputSeries \
                    [index] \
                        = 'Tropic Air'    
                
            elif tempString == 'zip':
                
                inputSeries \
                    [index] \
                        = 'ZIPAIR'                   
            
            elif 'aeroflot' in tempString:
                
                inputSeries \
                    [index] \
                        = 'Aeroflot'
            
            elif 'air north' in tempString:
                
                inputSeries \
                    [index] \
                        = "Air North, Yukon's Airline"
                
            elif 'caac' in tempString:
                
                inputSeries \
                    [index] \
                        = 'CAAC'
                
            elif 'conair' in tempString:
                
                inputSeries \
                    [index] \
                        = 'Conair Group'
                
            elif 'crystal' in tempString:
                
                inputSeries \
                    [index] \
                        = 'Crystal Air'    
                
            elif 'dosaaf' in tempString:
                
                inputSeries \
                    [index] \
                        = 'DOSAAF'                 

            elif 'fedex' in tempString:
                
                inputSeries \
                    [index] \
                        = 'Federal Express'
                
            elif 'frontier air' in tempString:
                
                inputSeries \
                    [index] \
                        = 'Frontier Airlines'
                
            elif 'jetcraft aviation' in tempString:
                
                inputSeries \
                    [index] \
                        = 'Jetcraft'
                
            elif 'korean air' in tempString:
                
                inputSeries \
                    [index] \
                        = 'Korean Air'
                
            elif 'markair' in tempString:
                
                inputSeries \
                    [index] \
                        = 'MarkAir'
                
            elif '(pan am)' in tempString:
                
                inputSeries \
                    [index] \
                        = 'Pan Am' 
                
            elif 'safe air' in tempString \
                    and tempString != 'safe air cargo':
                
                inputSeries \
                    [index] \
                        = 'SAFE Air'
                
            elif 'southwest air' in tempString \
                    and tempString != 'southwest airlift':
                
                inputSeries \
                    [index] \
                        = 'Southwest Air'
                
            elif 'sydney skydivers' in tempString:
                
                inputSeries \
                    [index] \
                        = 'Sydney Skydivers'
                
            elif 'utair' in tempString:
                
                inputSeries \
                    [index] \
                        = 'Utair' 
                
                
        return \
            inputSeries
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnCleanAircraftOperators, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a clean Series of aircraft operators.')
        
        return \
            inputSeries


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnCleanAircraftTypes
 #
 #  Function Description:
 #      This function returns a clean Series of aircraft types.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          initialInputSeries
 #                          This parameter is the input Series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnCleanAircraftTypes \
        (initialInputSeries):
    
    try:
        
        inputSeries \
            = initialInputSeries.copy()
        
        
        for index, aircraftType in inputSeries.items():

            if 'Consolidated PBY-5A Catalina' in aircraftType:
                
                inputSeries \
                    [index] \
                        = 'Consolidated PBY-5A Catalina'

                continue
                
            elif 'BAC One-Eleven' in aircraftType:
                
                inputSeries \
                    [index] \
                        = 'BAC One-Eleven'

                continue

            elif 'Consolidated PB4Y-2 Privateer' in aircraftType:
                
                inputSeries \
                    [index] \
                        = 'Consolidated PB4Y-2 Privateer'

                continue
                
            elif 'DC-3' in aircraftType:
                
                inputSeries \
                    [index] \
                        = 'Douglas DC-3'

                continue
                
            elif 'VFW/Fokker VFW.614' in aircraftType:
                
                inputSeries \
                    [index] \
                        = 'VFW-Fokker 614'

                continue 
                
            elif 'Lockheed 18-56-24 Lodestar' in aircraftType:
                
                inputSeries \
                    [index] \
                        = 'Lockheed Model 18 Lodestar'

                continue
                
            elif 'Martin 4-0-4' in aircraftType:
                
                inputSeries \
                    [index] \
                        = 'Martin 4-0-4'

                continue    
                
            elif 'Pilatus Britten Norman BN2' in aircraftType:
                
                inputSeries \
                    [index] \
                        = 'Pilatus Britten-Norman BN-2'

                continue  
            
            elif 'Shorts SC.7' in aircraftType:
                
                inputSeries \
                    [index] \
                        = 'Shorts SC.7 Skyvan'

                continue
                
            elif 'Vickers 952 Vanguard' in aircraftType:
                
                inputSeries \
                    [index] \
                        = 'Vickers Vanguard'

                continue             
            

            aircraftTypeString \
                = ''  
            
            lastTokenString \
                = ''
            
            tempTokenString \
                = ''
            
            
            tempStringList \
                = aircraftType.split(' ')
        
            for listIndex, listElement in enumerate(tempStringList):

                tempElement \
                    = re.sub \
                        ('[/-]', '', listElement)

                if tempElement.isalpha() == True:
                    
                    aircraftTypeString \
                        += (listElement + ' ')
                    
                else:
                    
                    tempTokenString \
                        = tempStringList \
                            [listIndex] \
                                .replace \
                                    ('.', '-')
                    
                    break
                
            
            if 'de Havilland' in aircraftTypeString:
                
                aircraftTypeString \
                    = 'de Havilland Canada '
                

            if aircraftTypeString == inputSeries[index]:

                continue
            
          
            if len(tempTokenString) > 0:
                
                if tempTokenString[0].isalpha() == True:

                    switchTypeFlagBoolean \
                        = False 
                    
                    for tokenIndex, token in enumerate(tempTokenString):
                    
                        if switchTypeFlagBoolean == False:
                            
                            if token.isalpha() == True:
                                
                                lastTokenString \
                                    += token.upper()
                                
                            else:
                                
                                lastTokenString \
                                    += token
                                
                                switchTypeFlagBoolean \
                                    = True
                                
                        else:
            
                            if token.isnumeric() == True:
                                
                                lastTokenString \
                                    += token
                                
                            else:
                                
                                break
    
                                
                elif tempTokenString[0].isnumeric() == True:
                    
                    switchTypeFlagBoolean \
                        = False 
                    
                    for tokenIndex, token in enumerate(tempTokenString):
                    
                        if switchTypeFlagBoolean == False:
                            
                            if token.isnumeric() == True:
                                
                                lastTokenString \
                                    += token
                                
                            else:
                                
                                break
                                
            
            aircraftTypeString \
                += lastTokenString
            
            aircraftTypeString \
                = aircraftTypeString.strip()
            
            if aircraftTypeString[-1] == '-':
                
                aircraftTypeString \
                    = aircraftTypeString[:-1]

            inputSeries \
                [index] \
                    = aircraftTypeString

        
        log_function \
            .DebugReturnObjectWriteObject \
                (inputSeries)
        
        return \
            inputSeries
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnCleanAircraftTypes, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a clean Series of aircraft types.')
        
        return \
            initialInputSeries


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnRenamedAirport
 #
 #  Function Description:
 #      This function returns a renamed airport.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          airportNameString
 #                          This parameter is the original airport name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnRenamedAirport \
        (airportNameString):
    
    try:
        
        tempAirportNameString \
            = '' + airportNameString
        
        tempAirportNameString \
            = tempAirportNameString \
                .replace \
                    ('AB',
                     'Air Base')
                
        tempAirportNameString \
            = tempAirportNameString \
                .replace \
                    ('AFB',
                     'Air Force Base')
                
        tempAirportNameString \
            = tempAirportNameString \
                .replace \
                    ('NAS',
                     'Naval Air Station')
                
        tempAirportNameString \
            = tempAirportNameString \
                .replace \
                    ('SPB',
                     'Seaplane Base')
        
        
        log_function \
            .DebugReturnObjectWriteObject \
                (tempAirportNameString)
        
        return \
            tempAirportNameString
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnRenamedAirport, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a renamed airport.')
        
        return \
            airportNameString


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnParsedLocationInformation
 #
 #  Function Description:
 #      This function parses out name, icao, iata, state and country information
 #      from the input String.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          airportString
 #                          This parameter is the input String.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnParsedLocationInformation \
        (airportString):
    
    try:
        
        tempDictionary \
            = {'icao': '',
               'iata': '',
               'name': '',
               'state': '',
               'country': '',
               'country_code': '',
               'lat': 0,
               'lon': 0}
        

        if 'Congo (Democratic Republic)' in airportString:
            
            airportString \
                = airportString \
                    .replace \
                        ('Congo (Democratic Republic)', 
                         'Democratic Republic of the Congo')

                
        if '(' in airportString and ')' in airportString:
                    
            startIndexInteger \
                = airportString.rindex('(')
                
            endIndexInteger \
                = airportString.rindex(')')
                  
        else:
                  
            startIndexInteger \
                = 0
                
            endIndexInteger \
                = 0
                
                
        icaoIdentifierString \
            = 'xxxx'
                
        iataIdentifierString \
            = 'xxx'
            
            
        substringLengthInteger \
            = endIndexInteger - startIndexInteger
            
  
        if '(' in airportString \
            and ')' in airportString \
            and '/' in airportString:
                    
            if substringLengthInteger == 4:
                    
                icaoIdentifierString \
                    = 'xxxx'
                    
                iataIdentifierString \
                    = airportString \
                        [startIndexInteger+1:endIndexInteger]
                    
            elif substringLengthInteger == 5:
                
                icaoIdentifierString \
                    = airportString \
                        [startIndexInteger+1:endIndexInteger]
                
                iataIdentifierString \
                    = 'xxx'
                    
            elif substringLengthInteger == 9:
                                    
                iataIdentifierString \
                    = airportString \
                        [startIndexInteger+1:startIndexInteger+4]
                
                icaoIdentifierString \
                    = airportString \
                        [endIndexInteger-4:endIndexInteger]
                            
        elif '(' in airportString \
            and ')' in airportString \
            and '/' not in airportString:
                
            if substringLengthInteger == 4:
                    
                icaoIdentifierString \
                    = 'xxxx'
                    
                iataIdentifierString \
                    = airportString \
                        [startIndexInteger+1:endIndexInteger]
                    
            elif substringLengthInteger == 5:
                
                icaoIdentifierString \
                    = airportString \
                        [startIndexInteger+1:endIndexInteger]
                
                iataIdentifierString \
                    = 'xxx'
          
        
        if icaoIdentifierString != 'xxxx' \
            or iataIdentifierString != 'xxx':
            
            tempAirportNameString \
                = airportString \
                    [0:startIndexInteger]
            
            tempAirportNameString \
                = tempAirportNameString \
                    .strip()
            
            stateNameString \
                = ''

            if ',' in tempAirportNameString:
               
                firstCommaIndexInteger \
                    = tempAirportNameString \
                        .index(',')

                stateNameString \
                    = tempAirportNameString \
                        [firstCommaIndexInteger+2:len(tempAirportNameString)]
                
                tempAirportNameString \
                    = tempAirportNameString \
                        [0:firstCommaIndexInteger]

    
            airportNameString \
                = ReturnRenamedAirport \
                    (tempAirportNameString)
                
            countryNameString \
                = airportString \
                    [endIndexInteger+3:len(airportString)] \
                        .strip()
            
        else:
                
            if 'entvid pri Sticni Airfield, Slovenia' in airportString:
                    
                tempAirportNameString \
                    = 'Sentvid Pri Sticni Field Airport, Slovenia'
                    
            elif 'Kleins Camp Airstrip, Tanzania' in airportString:
                    
                tempAirportNameString \
                    = "andBeyond Klein's Camp, Tanzania"           
                
            else:
                    
                tempAirportNameString \
                    = airportString
                    
                    
            tempAirportNameString \
                = ReturnRenamedAirport \
                    (tempAirportNameString)

            if ',' in tempAirportNameString:
                    
                firstCommaIndexInteger \
                    = tempAirportNameString \
                        .index(',')
                    
                lastCommaIndexInteger \
                    = tempAirportNameString \
                        .rindex(',')
                    
                if firstCommaIndexInteger == lastCommaIndexInteger \
                    or 'Air Base,' in tempAirportNameString:
                        
                    airportNameString \
                        = tempAirportNameString \
                            [0:lastCommaIndexInteger] \
                                .strip()
                        
                    stateNameString \
                        = ''
                        
                    countryNameString \
                        = tempAirportNameString \
                            [lastCommaIndexInteger+2:len(tempAirportNameString)]
                        
                else:
                        
                    airportNameString \
                        = tempAirportNameString \
                            [0:firstCommaIndexInteger]
                        
                    stateNameString \
                        = tempAirportNameString \
                            [firstCommaIndexInteger+2:lastCommaIndexInteger]
                        
                    countryNameString \
                        = tempAirportNameString \
                            [lastCommaIndexInteger+2:len(tempAirportNameString)] 
        
        
        tempDictionary \
            ['icao'] \
                = icaoIdentifierString
        
        tempDictionary \
            ['iata'] \
                = iataIdentifierString    
        
        tempDictionary \
            ['name'] \
                = airportNameString 

        tempDictionary \
            ['state'] \
                = stateNameString   

        tempDictionary \
            ['country'] \
                = countryNameString
        
        tempDictionary \
            ['country_code'] \
                = countryConverterObject.convert(names=countryNameString, to='ISO2')  
        
        
        return \
            tempDictionary
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnParsedLocationInformation, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return parsed airport information.')
        
        return \
            tempDictionary


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnAirportsDictionaryFromModule
 #
 #  Function Description:
 #      This function returns a completed airport Dictionary with geocoordinates
 #      using the airportsdata module.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary List
 #          airportsIcaoDictionaryList
 #                          This parameter is an airports data set indexed with icao.
 #  Dictionary List
 #          airportsIataDictionaryList
 #                          This parameter is an airports data set indexed with iata.
 #  Dictionary
 #          airportsDictionary
 #                          This parameter is an Dictionary for the current airport.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnAirportsDictionaryFromModule \
        (airportsIcaoDictionaryList,
         airportsIataDictionaryList,
         airportDictionary):
    
    try:
 
        tempDictionary \
            = airportsIcaoDictionaryList \
                [airportDictionary['icao']]
       
    except:

        tempDictionary \
            = None


    if tempDictionary == None:

        try:
                    
            tempDictionary \
                = airportsIataDictionaryList \
                    [airportDictionary['iata']]
                    
        except:
                    
            tempDictionary \
                = None
            
            
    if tempDictionary != None:
        
        airportDictionary['lat'] \
            = tempDictionary['lat']
        
        airportDictionary['lon'] \
            = tempDictionary['lon']
        
        return \
            airportDictionary \
                .copy()
        
    else:

        return \
            tempDictionary


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnAirportsDictionaryFromMapQuest
 #
 #  Function Description:
 #      This function returns a completed airport Dictionary with geocoordinates 
 #      using the Mapquest API.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary
 #          airportsDictionary
 #                          This parameter is an Dictionary for the current airport.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnAirportsDictionaryFromMapQuest \
        (airportDictionary):
    
    try:
        
        if len(airportDictionary['state']) == 0:

            locationString \
                = airportDictionary['name'] \
                    + ', ' \
                    + airportDictionary['country']

        else:
                
            locationString \
                = airportDictionary['name'] \
                    + ', ' \
                    + airportDictionary['state'] \
                    + ', ' \
                    + airportDictionary['country']
            
        baseURLString \
            = 'https://www.mapquestapi.com/geocoding/v1/address'

        parameterDictionary \
            = {'key': mapquest_api_key,
               'location': locationString}

        responseJSONObject \
            = requests \
                .get \
                    (baseURLString, 
                     params = parameterDictionary) \
                        .json()

        if responseJSONObject['results'][0]['locations'][0]['adminArea1'] \
            != airportDictionary['country_code']:
        
            parameterDictionary \
                = {'key': mapquest_api_key,
                   'location': airportDictionary['country']}

            responseJSONObject \
                = requests \
                    .get \
                        (baseURLString, 
                         params = parameterDictionary) \
                            .json()
                  
        airportDictionary['lat'] \
            = responseJSONObject \
                ['results'][0] \
                ['locations'][0] \
                ['latLng'] \
                ['lat']
        
        airportDictionary['lon'] \
            = responseJSONObject \
                ['results'][0] \
                ['locations'][0] \
                ['latLng'] \
                ['lng']
        
        
        return \
            airportDictionary \
                .copy()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnAirportsDictionaryFromMapQuest, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a complete airport Dictionary.')
        
        return \
            airportDictionary


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnGeocodeDataFrameForAirports
 #
 #  Function Description:
 #      This function returns a completed airport DataFrame with geocoordinates 
 #      from a Series of text Strings.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          initialInputSeries
 #                          This parameter is an input Series of text Strings.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnGeocodeDataFrameForAirports \
        (initialInputSeries):
    
    try:
        
        inputSeries \
            = initialInputSeries.copy()
        
        
        airportDictionaryList \
            = []
        
        
        airportsIcaoDictionaryList \
            = airportsdata \
                .load()

        airportsIataDictionaryList \
            = airportsdata \
                .load('iata')
        

        for airport in inputSeries:

            initialAirportDictionary \
                = ReturnParsedLocationInformation \
                    (airport)

            airportDictionary \
                = ReturnAirportsDictionaryFromModule \
                    (airportsIcaoDictionaryList,
                     airportsIataDictionaryList,
                     initialAirportDictionary)

            
            if airportDictionary == None:
                
                airportDictionary \
                    = ReturnAirportsDictionaryFromMapQuest \
                        (initialAirportDictionary)
                    
            
            airportDictionaryList \
                .append(airportDictionary)
            
        
        return \
            pd.DataFrame \
                .from_dict \
                    (airportDictionaryList)
            
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnGeocodeDataFrameForAirports, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a complete airport DataFrame.')
        
        return \
            None


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnRenamedLocation
 #
 #  Function Description:
 #      This function returns a completed airport DataFrame with geocoordinates 
 #      from a Series of text Strings.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          locationNameString
 #                          This parameter is an String holding the location.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnRenamedLocation \
        (locationNameString):
    
    try:
        
        tempString \
            = ' ' + locationNameString
        
        
        if ' ca ' in tempString:
            
            tempString \
                = tempString \
                    .replace \
                        ('ca ', 
                         '')
        
        tempString \
            = tempString \
                .replace \
                    ('(Atlantic Ocean)',  
                     '')
        
        tempString \
            = tempString \
                .replace \
                    ('(Indian Ocean)',  
                     '')
        tempString \
            = tempString \
                .replace \
                    ('(Pacific Ocean)',  
                     '')
        
        tempString \
            = tempString \
                .replace \
                    ('(Southern Ocean)',  
                     '')
        
        tempString \
            = tempString \
                .replace \
                    ('[Gulf of Mexico]',  
                     '')
        
        tempString \
            = tempString \
                .replace \
                    ('[Gulf of Sivash]',  
                     '')
        
        tempString \
            = tempString \
                .replace \
                    ('[Black Sea]',  
                     '')
        
        tempString \
            = tempString \
                .replace \
                    ('[Baltic Sea]',  
                     '')

        
        tempString \
            = tempString \
                .replace \
                    ('0km ', 
                     '0 km ')
        
        tempString \
            = tempString \
                .replace \
                    ('1km ', 
                     '1 km ')
        
        tempString \
            = tempString \
                .replace \
                    ('2km ', 
                     '2 km ')
        
        tempString \
            = tempString \
                .replace \
                    ('3km ', 
                     '3 km ')
        
        tempString \
            = tempString \
                .replace \
                    ('4km ', 
                     '4 km ')
        
        tempString \
            = tempString \
                .replace \
                    ('5km ', 
                     '5 km ')
        
        
        tempString \
            = tempString \
                .replace \
                    ('(Amerin',  
                     '(American')
            
        tempString \
            = tempString \
                .replace \
                    (' Ri)', 
                     ' Rica)')
            
        tempString \
            = tempString \
                .replace \
                    (' Afri)',  
                     ' Africa)')
            
        tempString \
            = tempString \
                .replace \
                    ('Ameri)',  
                     ' America)')
        
            
        tempString \
            = tempString \
                .replace \
                    ('Congo (Democratic Republic)', 
                     'Democratic Republic Congo')
        
        tempString \
            = tempString \
                .replace \
                    (' USA ',  
                     ' (United States) ')
        
        tempString \
            = tempString \
                .replace \
                    ('United States of America',  
                     'United States')
        
        tempString \
            = tempString \
                .replace \
                    ('St. Johns, NL, Canada',  
                     'St. Johns, NL, (Canada)')
        
        tempString \
            = tempString \
                .replace \
                    ('Newfoundland, Canada',  
                     'Newfoundland (Canada)')
        
        
        tempString \
            = tempString \
                .replace \
                    ('off Alaska',  
                     '320 km (198.8 mls) SE of Anchorage, AK (United States)')
        
        tempString \
            = tempString \
                .replace \
                    ('off Nassau, Bahamas',  
                     '18 km (11.2 mls) N of Nassau (Bahamas)')
        
        tempString \
            = tempString \
                .replace \
                    ('between Santa Barbara, CA and Kahului, HI',  
                     '1600 km (994.2 mls) WSW of Santa Barbara, CA (United States)')
        
        tempString \
            = tempString \
                .replace \
                    ('off Alexandria, Egypt (Mediterranean Sea)',  
                     '18 km (11.2 mls) N of Alexandria (Egypt)')   
        
        
        tempString \
            = tempString \
                .replace \
                    ('Abitibi Canyon near Fraserdale, ON (Canada)',  
                     'near Abitibi Canyon, Cochrane District, ON (Canada)')  
        
        tempString \
            = tempString \
                .replace \
                    ('Keflavik, Iceland',  
                     'Keflavik (Iceland)')
        
        tempString \
            = tempString \
                .replace \
                    ('Klaipeda, Lithuania',  
                     'Klaipeda (Lithuania)') 
       
        
        if 'near Hawaii' == tempString.strip():
        
            tempString \
                = 'near Honolulu, HI, (United States)'     
       
        elif 'off Hawaii, ' in tempString:
            
            tempString \
                = tempString \
                    .replace \
                        ('off Hawaii, ',
                         'off Honolulu, HI, ')
        elif 'North Atlantic' == tempString.strip():
            
            tempString \
                = '3200 km (1988.4 mls) W of Paris (France)'
            
        if 'Cape Hatteras, NC' in tempString \
            and 'United States' not in tempString:
            
            tempString \
                = tempString \
                    .replace \
                        ('Cape Hatteras, NC',
                         'Cape Hatteras, NC (United States)')
        
        
        tempString \
            = tempString \
                .strip()
            
        log_function \
            .DebugReturnObjectWriteObject \
                (tempString)
        
        return \
            tempString
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnRenamedLocation, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a renamed location String.')
        
        return \
            locationString


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnLocationDictionaryFromString
 #
 #  Function Description:
 #      This function returns a location Dictionary based on a String.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary List
 #          airportsIcaoDictionaryList
 #                          This parameter is a Dictionary List holding airport data
 #                          indexed by icao identifier.
 #  Dictionary List
 #          airportsIataDictionaryList
 #                          This parameter is a Dictionary List holding airport data
 #                          indexed by iata identifier.
 #  String
 #          locationString
 #                          This parameter is an String holding the location.
 #  String
 #          displacementString
 #                          This parameter is an String holding the displacement
 #                          information for latitude and longitude.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnLocationDictionaryFromString \
        (airportsIcaoDictionaryList,
         airportsIataDictionaryList,
         locationString,
         displacementString):
    
    try:
        
        tempString \
            = '' + locationString

        initialLocationDictionary \
            = ReturnParsedLocationInformation \
                (tempString)

        locationDictionary \
            = ReturnAirportsDictionaryFromModule \
                (airportsIcaoDictionaryList,
                 airportsIataDictionaryList,
                 initialLocationDictionary)

        
        if locationDictionary == None:
   
            locationDictionary \
                = ReturnAirportsDictionaryFromMapQuest \
                    (initialLocationDictionary)
    
    
        if locationDictionary['name'] == 'xxxx' \
            or len(locationDictionary['name']) == 0:
            
            locationDictionary['name'] \
                = locationDictionary['country']
            
      
        if len(displacementString) > 0:

            displacementString \
                = displacementString \
                    .strip()
            
            displacementStringList \
                = displacementString \
                    .split(' ')
            
            
            distanceFloat \
                = float \
                    (displacementStringList[0])
            
            bearingString \
                = displacementStringList \
                    [len(displacementStringList)-1]
            
            
            bearingFlagBoolean \
                = False
            
            for bearing in local_constant.bearingDictionary.keys():
                
                    if bearingString == bearing:
                        
                        bearingFlagBoolean \
                            = True
                        
                        break
            
            
            if bearingFlagBoolean == False:
                
                bearingIndexInteger \
                    = random \
                        .randint \
                            (0, len(local_constant.bearingDictionary)-1)
                
                bearingString \
                    = list \
                        (local_constant.bearingDictionary) \
                            [bearingIndexInteger]
            
            locationDictionary['lat'], locationDictionary['lon'] \
                = ReturnNewGeoCoordinates \
                    (locationDictionary['lat'], 
                     locationDictionary['lon'], 
                     distanceFloat, 
                     local_constant.bearingDictionary[bearingString])
            
        return \
            locationDictionary
        
    except:

        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnLocationDictionaryFromString, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a location Dictionary from a String.')
        
        return \
            None


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnLocationDictionaryNearWithinLocation
 #
 #  Function Description:
 #      This function returns a location Dictionary based on a String with near/within
 #      as key words.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary List
 #          airportsIcaoDictionaryList
 #                          This parameter is a Dictionary List holding airport data
 #                          indexed by icao identifier.
 #  Dictionary List
 #          airportsIataDictionaryList
 #                          This parameter is a Dictionary List holding airport data
 #                          indexed by iata identifier.
 #  String
 #          locationString
 #                          This parameter is an String holding the location.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnLocationDictionaryNearWithinLocation \
        (airportsIcaoDictionaryList,
         airportsIataDictionaryList,
         locationString):
    
    try:

        tempString \
            = '' + locationString
        
        tempString \
            = tempString \
                .replace \
                    (' within ',
                     ' near ') \
                .strip()

        tempString \
            = tempString \
                [len('near')+1:len(tempString)]

        
        firstIndexInteger \
            = tempString \
                .rindex('(')
            
        lastIndexInteger \
            = tempString \
                .rindex(')')
  

        countryString \
            = tempString \
                [firstIndexInteger+1:lastIndexInteger]

    
        tempString \
            = tempString \
                [0:firstIndexInteger-1]
           
        tempString \
            = tempString \
                + ', ' \
                + countryString
 

        locationDictionary \
            = ReturnLocationDictionaryFromString \
                (airportsIcaoDictionaryList,
                 airportsIataDictionaryList,
                 tempString, '')
            
        return \
            locationDictionary
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnLocationDictionaryNearWithinLocation, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a location Dictionary with near/within' \
                 + ' as key words.')
        
        return \
            None


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnLocationDictionaryOfOffFromLocation
 #
 #  Function Description:
 #      This function returns a location Dictionary based on a String with of/off/from
 #      as key words.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary List
 #          airportsIcaoDictionaryList
 #                          This parameter is a Dictionary List holding airport data
 #                          indexed by icao identifier.
 #  Dictionary List
 #          airportsIataDictionaryList
 #                          This parameter is a Dictionary List holding airport data
 #                          indexed by iata identifier.
 #  String
 #          locationString
 #                          This parameter is an String holding the location.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnLocationDictionaryOfOffFromLocation \
        (airportsIcaoDictionaryList,
         airportsIataDictionaryList,
         locationString):
    
    try:
        
        tempString \
            = '' + locationString
        
        
        firstIndexInteger \
            = tempString \
                .rindex \
                    ('(')
        
        lastIndexInteger \
            = tempString \
                .rindex \
                    (')')
        
        
        countryString \
            = tempString \
                [firstIndexInteger+1:lastIndexInteger]
        
        
        tempString \
            = tempString \
                [0:firstIndexInteger] \
                    .strip()
        
        if ' of ' in tempString:
            
            firstIndexInteger \
                = tempString \
                    .index \
                        (' of ')
            
            
            displacementString \
                = tempString \
                    [0:firstIndexInteger] \
                        .strip()
            
            displacementString \
                = displacementString \
                    .replace \
                        (',',
                         '.')
            
            
            if ' km' not in displacementString.lower() \
                and ' mls' not in displacementString.lower():
                
                displacementString \
                    = ''
            
            
            tempString \
                = tempString \
                    [firstIndexInteger+4:len(tempString)] \
                        .strip()
            
        elif ' off ' in tempString:
            
            firstIndexInteger \
                = tempString \
                    .index \
                        (' off ')
            
            
            if firstIndexInteger == 1 or firstIndexInteger == 0:
                
                displacementString \
                    = ''
                
            else:
                
                displacementString \
                    = tempString \
                        [0:firstIndexInteger] \
                            .strip()
            
                displacementString \
                    = displacementString \
                        .replace \
                            (',',
                             '.')
            
                if ' km' not in displacementString.lower() \
                    and ' mls' not in displacementString.lower():
                
                    displacementString \
                        = ''
            
            tempString \
                = tempString \
                    [firstIndexInteger+5:len(tempString)] \
                        .strip()
            
        elif ' from ' in tempString:
            
            firstIndexInteger \
                = tempString \
                    .index \
                        (' from ')
            
            displacementString \
                = tempString \
                    [0:firstIndexInteger] \
                        .strip()
            
            displacementString \
                = displacementString \
                    .replace \
                        (',',
                         '.')
            
            if ' km' not in displacementString.lower() \
                and ' mls' not in displacementString.lower():
                
                displacementString \
                    = ''
                
            tempString \
                = tempString \
                    [firstIndexInteger+6:len(tempString)] \
                        .strip()       
            
        elif 'off ' in tempString:
                
            firstIndexInteger \
                    = tempString \
                        .index \
                            ('off ')
            
            tempString \
                = tempString \
                    [firstIndexInteger+4:len(tempString)] \
                        .strip()
            
            displacementString \
                = ''
        
        
        if tempString[-1] == ',':
            
            tempString \
                = tempString[:-1]
        
        
        if countryString == 'United States of America':
            
            countryString \
                = 'United States'
            
        elif countryString == 'Democratic Republic Congo':
            
            countryString \
                = 'Democratic Republic of the Congo'
            
        
        tempString \
            = tempString \
                + ', ' \
                + countryString
 
        
        locationDictionary \
            = ReturnLocationDictionaryFromString \
                (airportsIcaoDictionaryList,
                 airportsIataDictionaryList,
                 tempString,
                 displacementString)
            
        return \
            locationDictionary
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnLocationDictionaryOfOffFromLocation, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a location Dictionary with of/off/from' \
                 + ' as key words.')
        
        return \
            None


# In[19]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnLocationDictionaryLocation
 #
 #  Function Description:
 #      This function returns a location Dictionary based on a String with no key words.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary List
 #          airportsIcaoDictionaryList
 #                          This parameter is a Dictionary List holding airport data
 #                          indexed by icao identifier.
 #  Dictionary List
 #          airportsIataDictionaryList
 #                          This parameter is a Dictionary List holding airport data
 #                          indexed by iata identifier.
 #  String
 #          locationString
 #                          This parameter is an String holding the location.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnLocationDictionaryLocation \
        (airportsIcaoDictionaryList,
         airportsIataDictionaryList,
         locationString):
    
    try:
        
        tempString \
            = '' + locationString
        
        
        firstIndexInteger \
            = tempString \
                .rindex \
                    ('(')
        
        lastIndexInteger \
            = tempString \
                .rindex \
                    (')')
        
        
        countryString \
            = tempString \
                [firstIndexInteger+1:lastIndexInteger] \
                    .strip()
        
        
        tempString \
            = tempString \
                [0:firstIndexInteger] \
                    .strip()
        
        tempString \
            = tempString \
                + ', ' \
                + countryString

        
        locationDictionary \
            = ReturnLocationDictionaryFromString \
                (airportsIcaoDictionaryList,
                 airportsIataDictionaryList,
                 tempString, '')
            
        return \
            locationDictionary
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (locationString)
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'\nThe function, ReturnLocationDictionaryLocation, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a location Dictionary with no key words.')
        
        return \
            None 


# In[20]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnGeocodeDataFrameForAccidents
 #
 #  Function Description:
 #      This function returns a geocoded DataFrame for aviation accident locations.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          initialInputSeries
 #                          This parameter is Series of location Strings.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnGeocodeDataFrameForAccidents \
        (initialInputSeries):
    
    try:
        
        inputSeries \
            = initialInputSeries.copy()
        
        
        airportsIcaoDictionaryList \
            = airportsdata \
                .load()

        airportsIataDictionaryList \
            = airportsdata \
                .load('iata')
        
        
        locationDictionaryList \
            = []
        
        
        for location in inputSeries:

            tempString \
                = ReturnRenamedLocation \
                    (location)

            tempString \
                = ' ' + tempString

            if ' near ' in tempString.lower() \
                or ' within ' in tempString.lower():

                locationDictionary \
                    = ReturnLocationDictionaryNearWithinLocation \
                        (airportsIcaoDictionaryList,
                         airportsIataDictionaryList,
                         tempString)
                      
            elif (' of ' in tempString.lower()) \
                or ' off ' in tempString.lower() \
                or ' from ' in tempString.lower():

                locationDictionary \
                    = ReturnLocationDictionaryOfOffFromLocation \
                        (airportsIcaoDictionaryList,
                         airportsIataDictionaryList,
                         tempString)
                
            else:

                locationDictionary \
                    = ReturnLocationDictionaryLocation \
                        (airportsIcaoDictionaryList,
                         airportsIataDictionaryList,
                         tempString)
            
            
            locationDictionaryList \
                .append \
                    (locationDictionary)
            
            
        tempDataFrame \
            = pd.DataFrame \
                .from_dict \
                    (locationDictionaryList)

        
        return \
            tempDataFrame
            
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (locationString)
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnGeocodeDataFrameForAccidents, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a DataFrame for accident locations.')
       
        return \
            None


# In[21]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnNewGeoCoordinates
 #
 #  Function Description:
 #      This function returns a geocoordinates based on the parameters.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Float
 #          latitudeFloat
 #                          This parameter is original latitude.
 #  Float
 #          longitudeFloat
 #                          This parameter is original longitude.
 #  Float
 #          distanceFloat
 #                          This parameter is distance from the original position 
 #                          in kilometers.
 #  Float
 #          bearingDegreesFloat
 #                          This parameter is distance from the bearing in degrees.
 #  Float
 #          radiusOfSphereFloat
 #                          This parameter is mean radius of the Earth in kilometers.  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnNewGeoCoordinates \
        (latitudeFloat, 
         longitudeFloat, 
         distanceFloat, 
         bearingDegreesFloat, 
         radiusOfSphereFloat \
             = 6371.0):
    
    try:
        
        latitudeFloat \
            = radians \
                (latitudeFloat)
        
        longitudeFloat \
            = radians \
                (longitudeFloat)
        
        bearingRadiansFloat \
            = radians \
                (bearingDegreesFloat)
        
        finalLatitudeFloat \
            = asin \
                (sin(latitudeFloat) 
                 * cos(distanceFloat / radiusOfSphereFloat) \
                 + cos(latitudeFloat) \
                 * sin(distanceFloat / radiusOfSphereFloat) \
              * cos(bearingRadiansFloat))
        
        finalLongitudeFloat \
            = longitudeFloat \
              + atan2 \
                    (sin(bearingRadiansFloat) \
                     * sin(distanceFloat / radiusOfSphereFloat) \
                     * cos(latitudeFloat),
                     cos(distanceFloat / radiusOfSphereFloat) \
                     - sin(latitudeFloat) \
                     * sin(longitudeFloat))
    
        return \
            (degrees(finalLatitudeFloat), 
             degrees(finalLongitudeFloat))

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnNewGeoCoordinates, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return new geocoordinates.')
        
        return \
            (0.0, 0.0)


# In[22]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnNewGeoCoordinates
 #
 #  Function Description:
 #      This function returns a a DataFrame with information for all countries.
 #
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

def ReturnCountryDataFrame():
    
    try:

        countryInfoObject \
            = CountryInfo()

        allCountryInfoDictionary \
            = countryInfoObject.all()
     
        allCountryDictionary \
            = {'country': [],
               'country_code': [],
               'country_code3': [],
               'capital': [],
               'region': [],
               'subregion': [],
               'lat': [],
               'lon': []}
       
        
        for country in allCountryInfoDictionary.keys():

            if country != 'scotland' \
                and country != 'wales' \
                and country != 'macau' \
                and country != 'heard island and mcdonald islands' \
                and country != 'hong kong':

                allCountryDictionary \
                    ['country'] \
                        .append \
                            (allCountryInfoDictionary \
                                [country] \
                                ['name'])

                if country != 'namibia':
                
                    allCountryDictionary \
                        ['country_code'] \
                            .append \
                                (allCountryInfoDictionary \
                                    [country] \
                                    ['ISO'] \
                                    ['alpha2'])
                
                else:
                    
                    allCountryDictionary \
                        ['country_code'] \
                            .append \
                                ('NA')
                    

                allCountryDictionary \
                    ['country_code3'] \
                        .append \
                            (allCountryInfoDictionary \
                                [country] \
                                ['ISO'] \
                                ['alpha3'])
          
                allCountryDictionary \
                    ['capital'] \
                        .append \
                            (allCountryInfoDictionary \
                                [country] \
                                ['capital'])
     
                allCountryDictionary \
                    ['region'] \
                        .append \
                            (allCountryInfoDictionary \
                                [country] \
                                ['region'])
       
                allCountryDictionary \
                    ['subregion'] \
                        .append \
                            (allCountryInfoDictionary \
                                [country] \
                                ['subregion'])
       
                allCountryDictionary \
                    ['lat'] \
                        .append \
                            (allCountryInfoDictionary \
                                [country] \
                                ['capital_latlng'][0])
         
                allCountryDictionary \
                    ['lon'] \
                        .append \
                            (allCountryInfoDictionary \
                                [country] \
                                ['capital_latlng'][1])

                
        tempDataFrame \
            = pd.DataFrame \
                .from_dict \
                    (allCountryDictionary)
        
        
        return \
            tempDataFrame
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnCountryDataFrame, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot return a country DataFrame.')
        
        return \
            None


# In[23]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnStandardizedCountryNames
 #
 #  Function Description:
 #      This function returns a DataFrame with standardized country names based on country
 #      codes.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrame
 #                          This parameter is the input DataFrame.
 #  DataFrame
 #          countryDataFrame
 #                          This parameter is the DataFrame with the country information.
 #  String
 #          countryCodeColumnString
 #                          This parameter is the name of the country code column.
 #  String
 #          countryNameColumnString
 #                          This parameter is the name of the country name column. 
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  10/18/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnStandardizedCountryNames \
        (inputDataFrame,
         countryDataFrame,
         countryCodeColumnString,
         countryNameColumnString):
    
    try:
        
        tempDataFrame \
            = inputDataFrame \
                .copy()
        
        
        for i, row in tempDataFrame.iterrows():
            
            for j, country in countryDataFrame.iterrows():
                
                if tempDataFrame[countryCodeColumnString][i] \
                    == countryDataFrame[countryCodeColumnString][j]:
                    
                    tempDataFrame[countryNameColumnString] \
                        = tempDataFrame \
                            [countryNameColumnString] \
                                .str.replace \
                                    (tempDataFrame[countryNameColumnString][i], 
                                     countryDataFrame[countryNameColumnString][j])
                    
        return \
            tempDataFrame
        
    except:
      
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnStandardizedCountryNames, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot standardize country names in a DataFrame.')
        
        return \
            None

