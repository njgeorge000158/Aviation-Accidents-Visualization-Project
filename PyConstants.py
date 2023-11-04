#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyConstants.py
 #
 #  File Description:
 #      This Python script, PyFunctions.py, contains generic Python constants
 #      for completing common tasks.
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/20/2023      Initial Development                     N James George
 #
 #******************************************************************************************/


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyConstants.py'


# In[3]:


# This is a global constant for setting coefficient precision for equations.
EQUATION_COEFFICIENT_PRECISION \
    = 4


# These constants are generic formats for Strings.
GENERAL_TEXT_FORMAT \
    = '{:}'

INTEGER_FORMAT \
    = '{:,}'

FLOAT_FORMAT \
    = '{:,.2f}'

FLOAT_AS_INTEGER_FORMAT \
    = '{:,.0f}'

CURRENCY_INTEGER_FORMAT \
    = '$' + INTEGER_FORMAT

CURRENCY_FLOAT_FORMAT \
    = '$' + FLOAT_FORMAT

CURRENCY_FLOAT_AS_INTEGER_FORMAT \
    = '$' + FLOAT_AS_INTEGER_FORMAT

PERCENT_FLOAT_FORMAT \
    = FLOAT_FORMAT + '%'

PERCENT_INTEGER_FORMAT \
    = INTEGER_FORMAT + '%'

TEMPERATURE_FLOAT_FORMAT \
    = FLOAT_FORMAT +'° F'

