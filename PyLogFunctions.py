#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyLogFunctions.py
 #
 #  File Description:
 #      This Python script, PyLogFunctions.py, contains generic Python functions
 #      for writing information to log files.  Here is the list:
 #
 #      ReturnCurrentDateAsString
 #      ReturnCurrentTimestampAsString
 #      DebugReturnObjectWriteObject
 #      ReturnTimePointMessage
 #      ReturnImageFilePathString
 #      ReturnStylerObjectSavePNGImage
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/24/2023      Initial Development                     N. James George
 #  09/22/2023      Added ReturnStylerObjectSavePNGImage    N. James George
 #
 #******************************************************************************************/

import PyLogConstants as log_constant

import dataframe_image as dfi

from datetime import date
from datetime import datetime


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyLogFunctions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnCurrentDateAsString
 #
 #  Function Description:
 #      This function returns the current date as a formatted string for the names
 #      of log files.
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
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnCurrentDateAsString():
    
    todayDateObject \
        = date \
            .today()

    return \
        todayDateObject \
            .strftime('%Y%m%d')


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnCurrentTimestampAsString
 #
 #  Function Description:
 #      This function returns the current date and time as a formatted string
 #      for timepoint entries in log files.
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
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnCurrentTimestampAsString():
    
    nowDateTimeObject \
        = datetime \
            .now()
    
    return \
        nowDateTimeObject \
            .strftime \
                ('%m/%d/%Y %H:%M:%S')


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  DebugReturnObjectWriteObject
 #
 #  Function Description:
 #      This function takes an object as a parameter, and, if the global debug flag is true, 
 #      writes it to a debug file before returning the object to the caller.
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
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DebugReturnObjectWriteObject \
        (inputObjectParameter):
    
    messageStringVariable \
        = f'\n\n' + str(inputObjectParameter) + f'\n\n'
    
    if log_constant.DEBUG_FLAG == True:
        
        log_constant \
            .debugTxtFile \
                .write \
                    (messageStringVariable)
            
        return \
            inputObjectParameter
    
    elif log_constant.LOG_FLAG == True:
        
        log_constant \
            .logTxtFile \
                .write \
                    (messageStringVariable)


# In[6]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnTimePointMessage
 #
 #  Function Description:
 #      This function takes a message, formats it with a timestamp, and returns it 
 #      to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          messageStringParameter
 #                          This parameter is the message that the function formats 
 #                          with a timestamp.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnTimePointMessage \
        (messageStringParameter \
            = ''):
    
    currentTimeStampStringVariable \
        = ReturnCurrentTimestampAsString()
    
    timePointMessageStringVariable \
        = f'\nTimepoint: {currentTimeStampStringVariable}\n'
    
    timePointMessageStringVariable \
        = timePointMessageStringVariable \
          + messageStringParameter \
          + '\n\n'
    
    return \
        timePointMessageStringVariable


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnImageFilePathString
 #
 #  Function Description:
 #      This function takes a captions for a matplotlib plot and returns 
 #      the image file path.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          captionStringParameter
 #                          This parameter is the plot title.
 #  String
 #          imageFormatStringParameter
 #                          This parameter is the image format file suffix.    
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/27/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnImageFilePathString \
        (captionStringParameter \
            = 'test',
         imageFormatStringParameter \
            = ''):
    
    tempCaptionStringVariable \
        = ''.join(filter(str.isalnum, captionStringParameter))
    
    
    imageFilePathStringVariable \
        = log_constant.IMAGES_DIRECTORY_PATH \
            + '/' \
            + log_constant.PROGRAM_DESIGNATION \
            + tempCaptionStringVariable
    
    
    if imageFormatStringParameter != '' \
        and imageFormatStringParameter != None:
    
        imageFilePathStringVariable \
            = imageFilePathStringVariable \
              + '.' \
              + imageFormatStringParameter
    
    return \
        imageFilePathStringVariable


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnStylerObjectSavePNGImage
 #
 #  Function Description:
 #      This function takes a captions for a matplotlib plot and returns 
 #      the image file path.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          captionStringParameter
 #                          This parameter is the plot title.
 #  String
 #          imageFormatStringParameter
 #                          This parameter is the image format file suffix.    
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/27/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnStylerObjectSavePNGImage \
        (inputStylerObject,
         captionString):
    
    try:
        
        if log_constant.IMAGE_FLAG == True:

            imageFilePathStringVariable \
                = ReturnImageFilePathString \
                    (captionString,
                        'png')
        
            dfi \
                .export \
                    (inputStylerObject, 
                     imageFilePathStringVariable)
        
        return \
            inputStylerObject
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnObjectSaveImage, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'cannot save an image of a DataFrame or StylerObject ' \
                 + 'then return it to the caller.')
        
        return \
            None

