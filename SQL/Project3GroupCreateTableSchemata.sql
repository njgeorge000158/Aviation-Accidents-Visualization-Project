--******************************************************************************************
--
--  File Name:  Project3Group3CreateTableSchemata.sql
--
--  File Description:
--      This file contains the SQL script for creating the database tables 
--      for the Aviation Accident Analysis Project.
--
--
--  Date               Description                              Programmer
--  ---------------    ------------------------------------     ------------------
--  10/24/2023         Initial Development                      N. James George
--
--******************************************************************************************/

-- These statements drop any existing tables in the database.

DROP TABLE IF EXISTS accidents;

DROP TABLE IF EXISTS departure;

DROP TABLE IF EXISTS destination;

DROP TABLE IF EXISTS airports;

DROP TABLE IF EXISTS country;


-- These statements create the database tables for aviation accident information.
CREATE TABLE
    country
        (id_number INTEGER,
         country VARCHAR NOT NULL,
         country_code VARCHAR NOT NULL,
         country_code3 VARCHAR NOT NULL,
         capital VARCHAR NOT NULL,
         region VARCHAR NOT NULL,
         subregion VARCHAR NOT NULL,
         lat REAL NOT NULL,
         lon REAL NOT NULL
            PRIMARY KEY (id_number));

CREATE TABLE
    airports
        (id_number INTEGER PRIMARY KEY,
         icao VARCHAR NOT NULL,
         iata VARCHAR NOT NULL,
         name VARCHAR NOT NULL,
         state VARCHAR,
         country VARCHAR NOT NULL,
         country_code VARCHAR NOT NULL,
         lat REAL NOT NULL,
         lon REAL NOT NULL
            PRIMARY KEY (id_number));

CREATE TABLE
    destination
        (accident_id VARCHAR,
         date VARCHAR NOT NULL,
         year INTEGER NOT NULL,
         icao VARCHAR NOT NULL,
         iata VARCHAR NOT NULL,
         name VARCHAR NOT NULL,
         state VARCHAR,
         country VARCHAR NOT NULL,
         country_code VARCHAR NOT NULL,
         lat REAL NOT NULL,
         lon REAL NOT NULL
            PRIMARY KEY (accident_id));

CREATE TABLE
    departure
        (accident_id VARCHAR,
         date VARCHAR NOT NULL,
         year INTEGER NOT NULL,
         icao VARCHAR NOT NULL,
         iata VARCHAR NOT NULL,
         name VARCHAR NOT NULL,
         state VARCHAR,
         country VARCHAR NOT NULL,
         country_code VARCHAR NOT NULL,
         lat REAL NOT NULL,
         lon REAL NOT NULL
            PRIMARY KEY (accident_id));

CREATE TABLE 
	accidents
	    (accident_id VARCHAR,
         date VARCHAR NOT NULL,
         year INTEGER NOT NULL,
         type VARCHAR NOT NULL,
         operator VARCHAR NOT NULL,
         fatalities INTEGER NOT NULL,
         occupants INTEGER NOT NULL,
         damage VARCHAR NOT NULL,
         phase VARCHAR NOT NULL,
         nature VARCHAR NOT NULL,
         departure VARCHAR NOT NULL,
         destination VARCHAR NOT NULL,
         locations VARCHAR NOT NULL,
         city VARCHAR NOT NULL,
         state VARCHAR,
         country VARCHAR NOT NULL,
         country_code VARCHAR NOT NULL,
         lat REAL NOT NULL,
         lon REAL NOT NULL,
         narrative TEXT
            PRIMARY KEY (accident_id));
