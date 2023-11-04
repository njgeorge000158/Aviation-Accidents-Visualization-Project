--******************************************************************************************
--
--  File Name:  Project3Group3FutureCreateTableSchemata.sql
--
--  File Description:
--      This file contains the SQL script for creating the database tables 
--      for the next phase of the Aviation Accident Analysis Project.
--
--
--  Date               Description                              Programmer
--  ---------------    ------------------------------------     ------------------
--  10/24/2023         Initial Development                      N. James George
--
--******************************************************************************************/

-- These statements drop any existing tables in the database.

DROP TABLE IF EXISTS accidents;

DROP TABLE IF EXISTS locations;

DROP TABLE IF EXISTS airports;

DROP TABLE IF EXISTS country;

DROP TABLE IF EXISTS narratives;

DROP TABLE IF EXISTS nature;

DROP TABLE IF EXISTS phase;

DROP TABLE IF EXISTS damage;

DROP TABLE IF EXISTS operator;

DROP TABLE IF EXISTS types;


-- These statements create the database tables for aviation accident information.

CREATE TABLE
    types
        (id_number INTEGER,
         type VARCHAR NOT NULL
            PRIMARY KEY (id_number));

CREATE TABLE
    operators
        (id_number INTEGER,
         operator VARCHAR NOT NULL
            PRIMARY KEY (id_number));

CREATE TABLE
    damage
        (id_number INTEGER,
         damage VARCHAR NOT NULL
            PRIMARY KEY (id_number));

CREATE TABLE
    phase
        (id_number INTEGER,
         phase VARCHAR NOT NULL
            PRIMARY KEY (id_number));

CREATE TABLE
    nature
        (id_number INTEGER,
         damage VARCHAR NOT NULL
            PRIMARY KEY (id_number));

CREATE TABLE
    narratives
        (accident_id VARCHAR,
         narrative VARCHAR NOT NULL
            PRIMARY KEY (accident_id));

CREATE TABLE
    country
        (country_code VARCHAR NOT NULL,
         country_code3 VARCHAR NOT NULL,
         name VARCHAR NOT NULL,
         capital VARCHAR NOT NULL,
         region VARCHAR NOT NULL,
         subregion VARCHAR NOT NULL,
         lat REAL NOT NULL,
         lon REAL NOT NULL
            PRIMARY KEY (country_code));

CREATE TABLE
    airports
        (id_number INTEGER PRIMARY KEY,
         icao VARCHAR NOT NULL,
         iata VARCHAR NOT NULL,
         name VARCHAR NOT NULL,
         state VARCHAR,
         country_code VARCHAR NOT NULL,
         lat REAL NOT NULL,
         lon REAL NOT NULL
            PRIMARY KEY (id_number)
            FOREIGN KEY (country_code) 
                REFERENCES country (country_code));

CREATE TABLE
    locations
        (accident_id VARCHAR,
         airport_id INTEGER
         name VARCHAR NOT NULL,
         city VARCHAR,
         state VARCHAR,
         country_code VARCHAR NOT NULL,
         lat REAL NOT NULL,
         lon REAL NOT NULL
            PRIMARY KEY (accident_id)
            FOREIGN KEY (airport_id) 
                REFERENCES airports (id_number)
            FOREIGN KEY (country_code)
                REFERENCES country (country_code));

CREATE TABLE
    accidents
        (accident_id VARCHAR,
         date VARCHAR NOT NULL,
         year INTEGER NOT NULL,
         type_id INTEGER NOT NULL,
         operator_id INTEGER NOT NULL,
         fatalities INTEGER NOT NULL,
         occupants INTEGER NOT NULL,
         damage_id INTEGER NOT NULL,
         phase_id INTEGER NOT NULL,
         nature_id INTEGER NOT NULL,
         departure_id INTEGER NOT NULL,
         destination_id INTEGER NOT NULL
            PRIMARY KEY (accident_id)
            FOREIGN KEY (accident_id) 
                REFERENCES narratives (accident_id)
            FOREIGN KEY (accident_id) 
                REFERENCES locations (accident_id)
            FOREIGN KEY (type_id) 
                REFERENCES types (id_number)
            FOREIGN KEY (operator_id) 
                REFERENCES operators (id_number)
            FOREIGN KEY (damage_id) 
                REFERENCES damage (id_number)
            FOREIGN KEY (phase_id) 
                REFERENCES phase (id_number)
            FOREIGN KEY (nature_id) 
                REFERENCES nature (id_number)
            FOREIGN KEY (departure_id) 
                REFERENCES airports (id_number)
            FOREIGN KEY (destination_id) 
                REFERENCES airports (id_number));