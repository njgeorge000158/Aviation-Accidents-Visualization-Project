#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PyFunctions.py
 #
 #  File Description:
 #      This Python script, PyFunctions.py, contains generic Python functions
 #      for completing common tasks.  Here is the list:
 #
 #      ReturnCSVFileAsDataFrame
 #      ReturnMergedDataFrame
 #
 #      ReturnStylerObjectStandardFormat
 #      ReturnStylerObjectPercentChangeStandardFormat
 #      ReturnStylerObjectBackgroundGradientFormat
 #
 #      ReturnNumberOfUniqueElementsInColumn
 #      ReturnDuplicateRowsAsDataFrame
 #      ReturnDataFrameRowsWithValue
 #      ReturnDataFrameRowsWithoutValue
 #
 #      ReturnSummaryStatisticsAsDataFrame
 #      ReturnRegressionModelEquationList
 #      ReturnPolynomialLineSeries
 #      ReturnRSquaredValue
 #      ReturnEquationAsString
 #      ReturnPearsonCorrelation
 #
 #      ConvertSeriesValuesToPercentChange
 #      ConvertSeriesFromDateStringsToDateObjects
 #
 #      ReturnNumberOfRedundanciesInSeries
 #      DisplaySummaryStatistics
 #      ReturnCorrelationTableStandardFormat
 #      DisplayHVPlotFromDataFrame
 #      ReturnSeriesWithDateObjectIndices
 #      ReturnSeriesWithUniqueIndicesLastValues
 #      ReturnFormattedStatisticsDataFrameFromSeries
 #      ReturnDateFromOneYearPriorAsString 
 #      ReturnFormattedRowsAsStylerObject
 #      ReturnStylerObjectStandardFormatForSeries
 #      ReturnExcelFileAsDataFrame
 #      DisplayDataFrameDescription
 #      DisplayDataFrameMemoryUsage
 #      DisplayDataFrameDataTypes
 #      ReturnFormattedStatisticsDataFrameFromDataFrameList
 # 
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/20/2023      Initial Development                     N. James George
 #  09/06/2023      Added returnFormattedStatisticsDataFrameFromSeries
 #                                                          N. James George
 #  09/06/2023      Added ReturnDateFromOneYearPriorAsString 
 #                                                          N. James George
 #  09/13/2023      Added ReturnStylerObjectStandardFormatForSeries
 #                                                          N. James George
 #  09/17/2023      Added title to plot for DisplayHVPlotFromDataFrame
 #                                                          N. James George
 #  09/21/2023      Added ReturnExcelFileAsDataFrame,       N. James George
 #                        DisplayDataFrameDescription,
 #                        DisplayDataFrameMemoryUsage,
 #                        DisplayDataFrameDataTypes
 #  09/29/2023      Added ReturnFormattedStatisticsDataFrameFromDataFrameList
 #                                                          N. James George
 #  09/29/2023      Added parameter to ReturnFormattedStatisticsDataFrameFromSeries
 #                                                          N. James George
 #
 #******************************************************************************************/

import PyConstants as constant
import PyLogSubRoutines as log_subroutine

import PyLogConstants as log_constant

import hvplot.pandas
import numpy as np
import pandas as pd

from datetime import timedelta
from datetime import datetime as dt
from pathlib import Path


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PyFunctions.py'


# In[3]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnCSVFileAsDataFrame
 #
 #  Function Description:
 #      This function receives a file path to a csv file as a parameter, 
 #      reads the csv file into a DataFrame, and returns the DataFrame
 #      to the caller.  If the operation fails, the function returns
 #      None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String or IOString
 #          filePathStringParameter
 #                          The parameter is name of the path to the csv file.
 #                          (i.e., './Resources/input.csv') or an IOString Object.
 #  Boolean
 #          stringFlagBooleanParameter
 #                          This parameter indicates whether the first parameter
 #                          is a String variable or an IOString object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnCSVFileAsDataFrame \
        (filePathStringParameter,
         indexNameStringParameter
          = None,
         stringFlagBooleanParameter \
            = True):
    
    try:
        
        if stringFlagBooleanParameter == True:
            
            pathObject \
                = Path \
                    (filePathStringParameter)
            
        else:
            
            pathObject \
                = filePathStringParameter
            
            
        if indexNameStringParameter == None:
            
            return \
                pd \
                    .read_csv \
                        (pathObject)
            
        else:
        
            return \
                pd \
                    .read_csv \
                        (pathObject,
                         index_col \
                            = indexNameStringParameter)
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnCSVFileAsDataFrame, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return0 a CSV file as a DataFrame, '
                 + f'{filePathStringParameter}.')
    
        return \
            None


# In[4]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnMergedDataFrame
 #
 #  Function Description:
 #      This function receives two DataFrames, merges them into one based 
 #      on a key, index, list of keys, or list of indices and returns the 
 #      merged DataFrame.  If the operation fails, the function returns
 #      None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          firstDataFrameParameter
 #                          This parameter is the first DataFrame
 #  DataFrame
 #          secondDataFrameParameter
 #                          This parameter is the first DataFrame
 #  String
 #          howStringParameter
 #                          This parameter specifies type of merge to be 
 #                          performed {‘left’, ‘right’, ‘outer’, ‘inner’, 
 #                          ‘cross’}. 
 # String or List
 #          onStringOrListParameter
 #                          This parameter is the column key(s) or index name(s)
 #                          to join on.  This parameter can be None, a string, 
 #                          or a list.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnMergedDataFrame \
        (firstDataFrameParameter,
         secondDataFrameParameter,
         howStringParameter,
         onStringOrListParameter):
    
    try:
        firstDataFrame \
            = firstDataFrameParameter.copy()
    
        secondDataFrame \
            = secondDataFrameParameter.copy()
    
   
        return \
            pd \
                .merge \
                    (firstDataFrame,
                     secondDataFrame,
                 how \
                     = howStringParameter,
                 on \
                     = onStringOrListParameter)
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, returnMergedDataFrame, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to merge two Dataframes.')
        
        return \
            None


# In[5]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnStylerObjectStandardFormat
 #
 #  Function Description:
 #      This function receives a DataFrame, formats it (standard), and returns 
 #      the Styler Object to the caller.  If the operation fails, the function 
 #      returns None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #  Integer
 #          precisionIntegerParameter
 #                          This optional parameter is the decimal place 
 #                          precision of the displayed numbers
 #  Boolean
 #          hideFlagBooleanParameter
 #                          This optional parameter indicates whether the
 #                          index column is hidden or not.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnStylerObjectStandardFormat \
        (inputDataFrameParameter,
         captionStringParameter,
         precisionIntegerParameter = 2,
         hideFlagBooleanParameter = True):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter \
                .copy()
        
        if hideFlagBooleanParameter == True:
            
            return \
                inputDataFrame \
                    .style \
                    .set_caption \
                        (captionStringParameter) \
                    .set_table_styles \
                        ([dict \
                             (selector = 'caption',
                              props = [('color', 'black'),
                                       ('font-size', '20px'),
                                       ('font-style', 'bold'),
                                       ('text-align', 'center')])]) \
                    .set_properties \
                         (**{'text-align':
                            'center',
                            'border':
                            '1.3px solid red',
                            'color':
                            'blue'}) \
                    .format \
                        (precision \
                            = precisionIntegerParameter, 
                         thousands \
                            = ',', 
                         decimal \
                            = '.') \
                    .hide()
        
        else:
            
            return \
                inputDataFrame \
                    .style \
                    .set_caption \
                        (captionStringParameter) \
                    .set_table_styles \
                        ([dict \
                             (selector = 'caption',
                              props = [('color', 'black'),
                                       ('font-size', '20px'),
                                       ('font-style', 'bold'),
                                       ('text-align', 'center')])]) \
                    .set_properties \
                         (**{'text-align':
                            'center',
                            'border':
                            '1.3px solid red',
                            'color':
                            'blue'}) \
                    .format \
                        (precision \
                            = precisionIntegerParameter, 
                         thousands \
                            = ',', 
                         decimal \
                            = '.')
        
        
    except:
            
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, returnStylerObjectStandardFormat, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to format a DataFrame as a Styler object.')
        
        return \
            None


# In[6]:


#********************************************************************************************
 #
 #  Function Name:  ReturnStylerObjectPercentChangeStandardFormat
 #
 #  Function Description:
 #      This function receives a DataFrame with percent values, formats a copy
 #      of it as a Styler Object, and returns it to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          This parameter is the table title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 
    
def ReturnStylerObjectPercentChangeStandardFormat \
        (inputDataFrameParameter,
         captionStringParameter):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter \
                .copy()
        
        inputDataFrame \
            .index \
                .name \
                    = None
        
        return \
            inputDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([dict \
                         (selector = 'caption',
                          props = [('color', 'black'),
                                 ('font-size', '20px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')])]) \
                .set_properties \
                    (**{'text-align':
                            'center',
                        'border':
                        '1.3px solid red',
                        'color':
                        'blue'}) \
                .format \
                    ('{:.2f}%') \
                .highlight_min \
                    (color \
                        = 'yellow') \
                .highlight_max \
                    (color \
                        = 'lime')
        
    except:
            
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ReturnStylerObjectPercentChangeStandardFormat, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to format a DataFrame with percent values '
                 + 'as a Styler object.')
        
        return \
            None


# In[7]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnStylerObjectBackgroundGradientFormat
 #
 #  Function Description:
 #      This function receives a DataFrame, formats it (background gtadient), and
 #      returns the Styler Object to the caller.  If the operation fails, the
 #      function returns None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #  Integer
 #          precisionIntegerParameter
 #                          This optional parameter is the decimal place 
 #                          precision of the displayed numbers
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnStylerObjectBackgroundGradientFormat \
        (inputDataFrameParameter,
         captionStringParameter,
         precisionIntegerParameter = 2):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter \
                .copy()
        
        return \
            inputDataFrame \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([dict \
                         (selector = 'caption',
                          props = [('color', 'black'),
                                 ('font-size', '20px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')])]) \
                .set_properties \
                    (**{'text-align':
                            'center'}) \
                .format \
                    (precision \
                        = 2, 
                     thousands \
                        = ',', 
                     decimal \
                        = '.') \
                .background_gradient()
        
    except:
            
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnStylerObjectBackgroundGradientFormat, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to format a DataFrame as a Styler object.')
        
        return \
            None


# In[8]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnNumberOfUniqueElementsInColumn
 #
 #  Function Description:
 #      This function calculates and returns the number of unique elements 
 #      in a DataFrame column.  If the operation fails, the function returns 
 #      None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          keyNameStringParameter
 #                          The parameter is the column key's name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnNumberOfUniqueElementsInColumn \
    (inputDataFrameParameter,
     keyNameStringParameter):
    
    try:
        
        return \
            inputDataFrameParameter \
                [keyNameStringParameter] \
            .nunique()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, returnNumberOfUniqueElementsInColumnFunction, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to calculate the unique number of elements '
                 + f'in a DataFrame column.')
        
        return \
            None


# In[9]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnDuplicateRowsAsDataFrame
 #
 #  Function Description:
 #      This function return duplicate rows in a DataFrame based on the
 #      particular column(s) key(s).  If the operation fails, the function 
 #      returns None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String or List
 #          criteriaStringorListParameter
 #                          The parameter is the DataFrame's column name(s) 
 #                          used as criteria for the process.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnDuplicateRowsAsDataFrame \
        (inputDataFrameParameter,
         criteriaStringorListParameter):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter.copy()
    
        return \
            inputDataFrame \
                [inputDataFrame.duplicated \
                    (subset \
                        = criteriaStringorListParameter)]
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, returnDuplicateRowsAsDataFrame, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return duplicate rows from a DataFrame.')
        
        return \
            None


# In[10]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnDataFrameRowsWithValue
 #
 #  Function Description:
 #      This function returns rows in a DataFrame with the specified value(s) in
 #      the particular column of the particular column(s).  If the operation
 #      fails, the function returns None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          keyNameStringVariable
 #                          The parameter is the DataFrame column key of interest 
 #  List
 #          criteriaListParameter
 #                          The parameter is a list of the values from the column
 #                          used as criteria in the process.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnDataFrameRowsWithValue \
        (inputDataFrameParameter,
         keyNameStringVariable,
         criteriaListParameter):
        
    try:
        
        inputDataFrame \
            = inputDataFrameParameter.copy()
    
        return \
           inputDataFrame \
                .apply \
                    (lambda row: \
                         row \
                             [inputDataFrame \
                                  [keyNameStringVariable] \
                             .isin \
                                  (criteriaListParameter)])
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnDataFrameRowsWithValue, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return rows with specified value(s).')
        
        return \
            None


# In[11]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnDataFrameRowsWithoutValue
 #
 #  Function Description:
 #      This function returns rows in a DataFrame without the specified value(s)
 #      in the particular column of the particular column(s).  If the operation
 #      fails, the function returns None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          keyNameStringVariable
 #                          The parameter is the name of the DataFrame column 
 #                          of interest 
 #  List
 #          criteriaListParameter
 #                          The parameter is a list of the values from the column
 #                          used as criteria in the process.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnDataFrameRowsWithoutValue \
        (inputDataFrameParameter,
         keyNameStringVariable,
         criteriaListParameter):
        
    try:
        
        inputDataFrame \
            = inputDataFrameParameter.copy()
    
        return \
           inputDataFrame \
                .apply \
                    (lambda row: \
                         row \
                             [~inputDataFrame \
                                  [keyNameStringVariable] \
                             .isin \
                                  (criteriaListParameter)])
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnDataFrameRowsWithoutValue, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return rows without specified value(s).')
        
        return \
            None


# In[12]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnSummaryStatisticsAsDataFrame
 #
 #  Function Description:
 #      This function returns summary statistics for a box plot from a Series of values.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          dataSeriesParameter
 #                          The parameter is the input Series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/19/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnSummaryStatisticsAsDataFrame \
        (dataSeriesParameter):

    try:
        
        # This line of code allocates the distribution for the quartiles.
        quartilesSeries \
            = dataSeriesParameter \
                .quantile \
                    ([0.25,
                      0.50,
                      0.75])
    

        # These lines of code establish the lower quartile and the upper quartile.
        lowerQuartileFloatVariable \
            = quartilesSeries \
                [0.25]

        upperQuartileFloatVariable \
            = quartilesSeries \
                [0.75]
    
 
        # This line of code calculates the interquartile range (IQR).
        interquartileRangeFloatVariable \
            = upperQuartileFloatVariable - lowerQuartileFloatVariable


        # These line of code calculate the lower bound and upper bound 
        # of the distribution.
        lowerBoundFloatVariable \
            = lowerQuartileFloatVariable - (1.5*interquartileRangeFloatVariable)
    
        upperBoundFloatVariable \
            = upperQuartileFloatVariable + (1.5*interquartileRangeFloatVariable)
    
   
        # This line of code establishes a list of outliers.
        outliersSeries \
            = dataSeriesParameter \
                .loc[(dataSeriesParameter < lowerBoundFloatVariable) \
                      | (dataSeriesParameter > upperBoundFloatVariable)]
        
        
        # This line of code finds the number of outliers.
        numberOfOutliersIntegerVariable \
            = len(outliersSeries)
  

        # These lines of code create a list of all the summary statistics and store
        # the data in a DataFrame.
        summaryStatisticsList \
            = [{'Lower Quartile':
                    lowerQuartileFloatVariable,
                'Upper Quartile':
                    upperQuartileFloatVariable,
                'Interquartile Range':
                    interquartileRangeFloatVariable,
                'Median':
                    quartilesSeries[0.5],
                'Lower Boundary':
                    lowerBoundFloatVariable,
                'Upper Boundary':
                    upperBoundFloatVariable,
                'Number of Outliers':
                    numberOfOutliersIntegerVariable}]
  
                
        return \
            pd \
                .DataFrame \
                    (summaryStatisticsList)
        
    except:
            
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnSummaryStatisticsAsDataFrame, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to calculate summary statistics for '
                 + f'a Series of values.')
            
        return \
            None


# In[13]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnRegressionModelEquationList
 #
 #  Function Description:
 #      This function receives a two Series for an x-y equation and the polynomial 
 #      degree for the regression and returns a list of equation coefficients.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          xSeriesParameter
 #                          This parameter is the Series used as x-axis 
 #                          values.
 #  Series
 #          ySeriesParameter
 #                          This parameter is the Series used as y-axis 
 #                          values.
 #  Integer
 #          degreeIntegerParameter
 #                          This parameter is degree of the polynomial 
 #                          regression.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnRegressionModelEquationList \
        (xSeriesParameter, 
         ySeriesParameter,
         degreeIntegerParameter):
    try:
        
        equationList \
            = np.poly1d \
                (np.polyfit \
                     (xSeriesParameter,
                      ySeriesParameter,
                      degreeIntegerParameter))

    
        return \
            equationList
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnRegressionModelEquationList, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return polynomial regression equation coefficients.')
        
        return \
            None


# In[14]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnPolynomialLineSeries
 #
 #  Function Description:
 #      This function receives a two Series for an x-y equation and returns a series 
 #      of y-ccordinates for the polynomial line.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          xSeriesParameter
 #                          This parameter is the Series used as x-axis 
 #                          values.
 #  Series
 #          ySeriesParameter
 #                          This parameter is the Series used as y-axis 
 #                          values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnPolynomialLineSeries \
        (xSeriesParameter, 
         ySeriesParameter):
       
    try:
        sampleNumberIntegerVariable \
            = abs \
                (int \
                     ((xSeriesParameter.max() - ySeriesParameter.min()) \
                      / 2))

        return \
            np \
                .linspace \
                    (xSeriesParameter.min(), 
                     xSeriesParameter.max(), 
                     sampleNumberIntegerVariable)
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnPolynomialLineSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return a polynomial regression line Series.')
        
        return \
            None


# In[15]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnRSquaredValue
 #
 #  Function Description:
 #      This function receives a two Series for an x-y equation and the polynomial 
 #      degree for the regression and returns the r-squared value.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          xSeriesParameter
 #                          This parameter is the Series used as x-axis 
 #                          values.
 #  Series
 #          ySeriesParameter
 #                          This parameter is the Series used as y-axis 
 #                          values.
 #  Integer
 #          degreeIntegerParameter
 #                          This parameter is degree of the polynomial 
 #                          regression.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnRSquaredValue \
        (xSeriesParameter, 
         ySeriesParameter, 
         degreeIntegerParameter):
    
    try:
        
        coefficientsFloatArray \
            = np \
                .polyfit \
                    (xSeriesParameter, 
                     ySeriesParameter, 
                     degreeIntegerParameter)

        pPoly1D \
            = np \
                .poly1d \
                    (coefficientsFloatArray)
    
    
        yhatList \
            = pPoly1D \
                (xSeriesParameter)
    
        ybarFloatVariable \
            = ySeriesParameter.sum() \
              / len(ySeriesParameter)
    
    
        ssregFloatVariable \
            = ((yhatList-ybarFloatVariable)**2) \
              .sum()
    
        sstotFloatVariable \
            = ((ySeriesParameter - ybarFloatVariable)**2) \
              .sum()
    
    
        resultsFloatVariable \
            = ssregFloatVariable \
              / sstotFloatVariable
    
    
        return \
             resultsFloatVariable
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnRSquaredValue, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return the r-squared value.')
        
        return \
            None


# In[16]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnEquationAsString
 #
 #  Function Description:
 #      This function receives a List of equation coefficients and returns the equation
 #      as a String.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List of Float
 #          modelEquationListParameter
 #                          This parameter is the list of equation coefficients
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnEquationAsString \
        (modelEquationListParameter):
   
    try:
        
        tempDegreeIntegerVariable \
            = len \
                (modelEquationListParameter)

        equationStringVariable \
            = ''
    
    
        for index, term in enumerate(modelEquationListParameter):
            
            tempStringVariable \
                = str(round(float(term), constant.EQUATION_COEFFICIENT_PRECISION))
            
            
            if tempDegreeIntegerVariable > 1:
                
                tempStringVariable \
                    = tempStringVariable \
                        + 'x' \
                        + '^' \
                        + str \
                            (tempDegreeIntegerVariable)
                
            elif tempDegreeIntegerVariable == 1:
                
                tempStringVariable \
                    = tempStringVariable + 'x'
          
    
            if tempDegreeIntegerVariable == len(modelEquationListParameter):
            
                equationStringVariable \
                    = tempStringVariable
            
            else:
            
                equationStringVariable \
                    = equationStringVariable \
                      + ' + ' \
                      + tempStringVariable
                
            
            tempDegreeIntegerVariable \
                -= 1
        
        
        equationStringVariable \
            = 'y = ' \
              + equationStringVariable
        
        
        return \
            equationStringVariable
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnEquationAsString, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return the regression line as a String.')
    
        return \
            None


# In[17]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnPearsonCorrelation
 #
 #  Function Description:
 #      This function receives a two Series for an x-y equation returns the 
 #      Pearson correlation.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          xSeriesParameter
 #                          This parameter is the Series used as x-axis 
 #                          values.
 #  Series
 #          ySeriesParameter
 #                          This parameter is the Series used as y-axis 
 #                          values.
 #  Integer
 #          degreeIntegerParameter
 #                          This parameter is degree of the polynomial 
 #                          regression.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnPearsonCorrelation \
            (xSeriesParameter, 
             ySeriesParameter):
    
    try:
       
        return \
            xSeriesParameter \
                .corr \
                    (ySeriesParameter, 
                     method \
                         = 'pearson')
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnPearsonCorrelation, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return the Pearson correlation.')
    
        return \
            None


# In[18]:


#*******************************************************************************************
 #
 #  Function Name:  ConvertSeriesValuesToPercentChange
 #
 #  Function Description:
 #      This function receives a Series, converts its values to percent change values,
 #      and returns the new Series to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is input Series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 
    
def ConvertSeriesValuesToPercentChange \
        (inputSeriesParameter):

    try:
        
        inputSeries \
            = inputSeriesParameter.copy()
    
        finalSeries \
            = inputSeries * 0.0
        
        
        for index, value in enumerate(inputSeries):
        
            if index >= len(inputSeries):
            
                continue
            
            elif index > 0:
            
                if inputSeries[ index - 1 ] != 0:
        
                    finalSeries[ index ] \
                        = ((value - inputSeries[ index - 1 ]) \
                           / inputSeries[ index - 1 ]) \
                          * 100
            
            else:
                
                finalSeries[ index ] = 0.0
    
    
        finalSeries \
            .drop \
                (finalSeries \
                     .index \
                         [0], 
                 inplace \
                     = True)
      
        
        return \
            finalSeries
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ConvertSeriesValuesToPercentChange, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to convert the values in a Series '
                 + 'to percent change values.\n')
        
        return \
            None


# In[19]:


#******************************************************************************************
 #
 #  Function Name:  ConvertSeriesTimestampIndexesToDateObjects
 #
 #  Function Description:
 #      This function receives a Series, converts its timestamp indexes values into
 #      Date objects.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is input Series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 
    
def ConvertSeriesTimestampIndexesToDateObjects \
        (inputSeries):
    
    try:

        datesList \
            = []

        for tStamp in inputSeries.index:
        
            tempTimestampVariable \
                = pd \
                    .Timestamp \
                        (tStamp)
            
            tempTimestampVariable \
                .to_pydatetime()
            
            tempDateVariable \
                = tempTimestampVariable.date()
        
            datesList \
                .append \
                    (tempDateVariable)
        
        return \
            pd \
                .Series \
                    (datesList, 
                     index \
                         = inputSeries.index)
    
    except:
        
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ConvertSeriesTimestampIndexesToDateObjects, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to convert the timestamp indices in a Series '
                 + 'to date objects.\n')
        
        return \
            None


# In[20]:


#******************************************************************************************
 #
 #  Function Name:  ConvertSeriesFromDateStringsToDateObjects
 #
 #  Function Description:
 #      This function receives a Series and date format, converts the date Strings
 #      in the Series to Date objects, and returns the new Series to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the input Series.
 #  String
 #          dateFormatStringParameter
 #                          This parameter is date String format of the input Series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 
    
def ConvertSeriesFromDateStringsToDateObjects \
        (inputSeriesParameter,
         dateFormatStringParameter):
    
    try:
        
        return \
             inputSeriesParameter \
                .apply \
                    (lambda x: dt.strptime(x,'%Y-%m-%d').date())   
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ConvertSeriesFromDateStringsToDateObjects, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to convert the date Strings in a Series '
                 + 'to date objects.\n')
        
        return \
            None


# In[21]:


#******************************************************************************************
 #
 #  Function Name:  ReturnNumberOfRedundanciesInSeries
 #
 #  Function Description:
 #      This function receives a Series, calculates the number of redundancies, and
 #      returns the value to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the input Series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnNumberOfRedundanciesInSeries \
        (inputSeriesParameter):
    
    try:
        
        return \
            inputSeriesParameter.count() - inputSeriesParameter.nunique()
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, NumberOfRedundanciesInSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to calculate the number of redundancies '
                 + 'in a Series.\n')
        
        return \
            None


# In[22]:


#******************************************************************************************
 #
 #  Function Name:  DisplaySummaryStatistics
 #
 #  Function Description:
 #      This function receives a DataFrame and displays the statistics summary in a table.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/14/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def DisplaySummaryStatistics \
        (inputDataFrameParameter,
         captionStringParameter):
        
    inputDataFrame \
        = inputDataFrameParameter \
            .copy()
    
    inputDataFrame \
        .index \
        .name \
            = None

    
    return \
        inputDataFrame \
            .style \
            .set_caption \
                (captionStringParameter) \
            .set_table_styles \
                ([{'selector': 
                       'caption', 
                   'props':
                        [('color', 
                              'black'), 
                         ('font-size', 
                              '16px'),
                         ('font-style', 
                              'bold'),
                         ('text-align', 
                              'center')]}]) \
            .set_properties \
                (**{'text-align':
                        'center',
                    'border':
                        '1.3px solid red',
                    'color':
                        'blue'}) \
            .format({'Industry':
                            constant.GENERAL_TEXT_FORMAT, 
                     'Lower Quartile':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                     'Upper Quartile':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT,   
                     'Interquartile Range':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                     'Lower Boundary':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                     'Upper Boundary':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                     'Mean':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                     'Median':
                            constant.CURRENCY_FLOAT_AS_INTEGER_FORMAT, 
                     'Number of Companies':
                            constant.INTEGER_FORMAT, 
                     'Number of Outliers':
                            constant.INTEGER_FORMAT}) \
            .highlight_max \
                (subset \
                    = ['Lower Quartile',
                       'Upper Quartile',
                       'Interquartile Range',
                       'Lower Boundary',
                       'Upper Boundary',
                       'Mean',
                       'Median',
                       'Number of Companies',
                       'Number of Outliers'],
                 color='lime') \
            .highlight_min \
                (subset \
                    = ['Lower Quartile',
                       'Upper Quartile',
                       'Interquartile Range',
                       'Lower Boundary',
                       'Upper Boundary',
                       'Mean',
                       'Median',
                       'Number of Companies',
                       'Number of Outliers'],
                 color='yellow') \
            .hide()


# In[23]:


#******************************************************************************************
 #
 #  Function Name:  ReturnCorrelationTableStandardFormat
 #
 #  Function Description:
 #      This function receives a DataFrame and displays a formatted correlation table.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame
 #  String
 #          captionStringParameter
 #                          This parameter is the table's title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/22/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnCorrelationTableStandardFormat \
        (inputDataFrameParameter,
         captionStringParameter):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter.copy()
        
        return \
            inputDataFrame \
                .corr() \
                .style \
                .set_caption \
                    (captionStringParameter) \
                .set_table_styles \
                    ([dict \
                        (selector \
                             = 'caption',
                         props \
                             = [('color', 'black'),
                                ('font-size', '20px'),
                                ('font-style', 'bold'),
                                ('text-align', 'center')])]) \
                .set_properties \
                    (**{'text-align':
                     'center',
                     'border':
                     '1.3px solid red',
                     'color':
                     'blue'}) \
                .format \
                    (precision \
                        = 6, 
                     thousands \
                        = ',', 
                     decimal \
                        = '.')
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, DisplayFormattedCorrelationTableStandardFormat, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to display a formatted correlation table.')
        
        return \
            None


# In[24]:


#******************************************************************************************
 #
 #  Function Name:  DisplayHVPlotFromDataFrame
 #
 #  Function Description:
 #      This function receives a DataFrame and displays a formatted correlation table.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame
 #  String
 #          captionStringParameter
 #                          This parameter is the plot's title.
 #  String
 #          colorKeyStringParameter
 #                          This parameter is the key to the DataFrame column 
 #                          of colors.
 #  String
 #          sizeKeyStringParameter
 #                          This parameter the key to the DataFrame column of 
 #                          marker sizes.
 #  Tuple of Integers
 #          xlimitTupleParameter
 #                          This parameter the HVPlot limits for the x-axis.
 #  Tuple of Integers
 #          ylimitTupleParameter
 #                          This parameter the HVPlot limits for the y-axis.
 #  Float
 #          alphaFloatParameter
 #                          This parameter the alpha value (transparency level) 
 #                          for the markers.
 #  String
 #          tilesStringParameter
 #                          This parameter indicates the type of map (OSM, ESRI, etc.).
 #  List of Strings
 #          hoverColumnsListOfStringsParameter
 #                          This parameter is the list of column names 
 #                          for the hover message.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/25/2023           Initial Development                         N. James George
 #  9/17/2023           Added title to plot                         N. James George
 #
 #******************************************************************************************/

def DisplayHVPlotFromDataFrame \
        (inputDataFrameParameter,
         captionStringParameter,
         colorKeyStringParameter,
         sizeKeyStringParameter,
         xlimitTupleParameter \
            = (-180, 180), 
         ylimitTupleParameter \
            = (-55, 75),
         alphaFloatParameter \
            = 0.7,
         tilesStringParameter \
            = 'OSM',
         hoverColumnsListOfStringsParameter \
            = None):
    
    try:

        inputDataFrame \
            = inputDataFrameParameter.copy()
        

        if hoverColumnsListOfStringsParameter == None:

            hvPlotOverlayObject \
                = inputDataFrame \
                    .hvplot \
                    .points \
                        ('Longitude', 
                         'Latitude',
                         xlabel = '', 
                         ylabel = '',
                         geo \
                            = True, 
                         color \
                            = colorKeyStringParameter, 
                         size \
                            = sizeKeyStringParameter,
                         xlim \
                            = xlimitTupleParameter, 
                         ylim \
                            = ylimitTupleParameter,
                         alpha \
                            = alphaFloatParameter, 
                         tiles \
                            = tilesStringParameter,
                         title \
                            = captionStringParameter)
       
        else:

            hvPlotOverlayObject \
                = inputDataFrame \
                    .hvplot \
                    .points \
                        ('Longitude', 
                         'Latitude',
                         xlabel = '', 
                         ylabel = '',
                         geo \
                            = True, 
                         color \
                            = colorKeyStringParameter, 
                         size \
                            = sizeKeyStringParameter,
                         xlim \
                            = xlimitTupleParameter, 
                         ylim \
                            = ylimitTupleParameter,
                         alpha \
                            = alphaFloatParameter, 
                         tiles \
                            = tilesStringParameter,
                         title \
                            = captionStringParameter,
                         hover_cols \
                            = hoverColumnsListOfStringsParameter)
    
    
        log_subroutine \
            .SaveHVPlotImageToPNGFile \
                (hvPlotOverlayObject,
                 captionStringParameter)

    
        return \
            hvPlotOverlayObject
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, DisplayHVPlotFromDataFrame, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to display a formatted HVPlot.')
        
        return \
            None


# In[25]:


#******************************************************************************************
 #
 #  Function Name:  DisplayHVPlotFromDataFrame
 #
 #  Function Description:
 #      This function receives a Series with timestamps for indices, converts those
 #      timestamps to dat object, and returns the new Series.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the input Series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/31/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnSeriesWithDateObjectIndices \
        (inputSeriesParameter):
    
    try:

        indexList \
            = ConvertSeriesTimestampIndexesToDateObjects \
                    (inputSeriesParameter) \
                .tolist()
  
        valuesList \
            = inputSeriesParameter \
                .tolist()
   
        return \
            pd \
                .Series \
                    (valuesList, 
                     index \
                         = indexList)
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnSeriesWithDateObjectIndices, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return a Series with Date Objects as the indices.')
        
        return \
            None


# In[26]:


#******************************************************************************************
 #
 #  Function Name:  ReturnSeriesWithUniqueIndicesLastValues
 #
 #  Function Description:
 #      This function receives a Series and removes all redundant rows with the same index
 #      but leaves one instance of that index with the last value.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the input Series.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/31/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnSeriesWithUniqueIndicesLastValues \
        (sharesSeriesParameter):
    
    try:
        sharesSeries \
            = sharesSeriesParameter.copy()
    
        sharesSeries \
            .dropna \
                (inplace \
                     = True)
    
    
        lastIndexIntegerVariable \
            = len \
                (sharesSeries) - 1
    
    
        indexList \
            = []
    
        valueList \
            = []
    
        for sharesIndex, shares in enumerate(sharesSeries):
        
            if sharesIndex < lastIndexIntegerVariable:
            
                if (sharesSeries.index[sharesIndex]).date() != (sharesSeries.index[sharesIndex+1]).date():
            
                    indexList \
                        .append \
                            (sharesSeries \
                                 .index \
                                     [sharesIndex])
            
                    valueList \
                        .append \
                            (sharesSeries[sharesIndex])
        
            elif sharesIndex == lastIndexIntegerVariable:
            
                if (sharesSeries.index[sharesIndex]).date() != (sharesSeries.index[sharesIndex-1]).date():
                
                    indexList \
                        .append \
                            (sharesSeries \
                                 .index \
                                     [sharesIndex])
            
                    valueList \
                        .append \
                            (sharesSeries \
                                 [sharesIndex])
    
    
        return \
            pd \
                .Series \
                    (valueList, 
                     index \
                         = indexList)         

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnSeriesWithUniqueIndicesLastValues, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return a Series with last values from unique indices.')
        
        return \
            None


# In[27]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnFormattedStatisticsDataFrameFromSeries
 #
 #  Function Description:
 #      This function receives a Series, calculates its statistical values, places them
 #      in a DataFrame, and returns the formatted DataFrame to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #  String
 #          columnNameString
 #                          The parameter is the name of the column holding data.
 #  Integer
 #          precisionIntegerParameter
 #                          This optional parameter is the decimal place 
 #                          precision of the displayed numbers
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/06/2023          Initial Development                         N. James George
 #  09/29/2023          Added columnNameString parameter            N. James George
 #
 #******************************************************************************************/

def ReturnFormattedStatisticsDataFrameFromSeries \
        (inputSeriesParameter,
         captionStringParameter \
             = '',
         columnNameString \
             = '',
         precisionIntegerParameter \
            = 4):
    
    try:
        
        inputSeries \
            = inputSeriesParameter.copy()
        
        
        indexList \
            = ['Mean', 
               'Median', 
               'Mode', 
               'Variance', 
               'Std Dev', 
               'SEM', 
               'Minimum', 
               '25%', 
               '50%', 
               '75%', 
               'Maximum', 
               'Count']

        valueList \
            = [inputSeries.mean(),
               inputSeries.median(),
               inputSeries.mode()[0],
               inputSeries.var(),
               inputSeries.std(),
               inputSeries.sem(),
               inputSeries.min(),
               inputSeries.describe().loc['25%'],
               inputSeries.describe().loc['50%'],
               inputSeries.describe().loc['75%'],
               inputSeries.max(),
               inputSeries.count()]
        
        
        statisticsDataFrame \
            = pd \
                .DataFrame \
                    (valueList, 
                     columns \
                         = [columnNameString], 
                     index \
                         = indexList)
    
    
        formattersDictionary \
            = {'Mean': lambda x: f'{x:.4f}',
               'Median': lambda x: f'{x:.4f}',
               'Mode': lambda x: f'{x:.4f}',
               'Variance': lambda x: f'{x:.4f}',
               'Std Dev': lambda x: f'{x:.4f}',
               'SEM': lambda x: f'{x:.4f}',
               'Minimum': lambda x: f'{x:.2f}',
               '25%': lambda x: f'{x:.2f}',
               '50%': lambda x: f'{x:.2f}',
               '75%': lambda x: f'{x:.2f}',
               'Maximum': lambda x: f'{x:.2f}',
               'Count': lambda x: f'{x:.0f}'}

        statisticsStylerObject \
            = ReturnFormattedRowsAsStylerObject \
                (statisticsDataFrame.style, 
                 formattersDictionary)
        
        
        statisticsStylerObject \
            .set_caption \
                (captionStringParameter) \
            .set_table_styles \
                ([{'selector': 
                        'caption', 
                   'props':
                        [('color', 
                              'black'), 
                         ('font-size', 
                              '16px'),
                         ('font-style', 
                              'bold'),
                         ('text-align', 
                              'center')]}]) \
            .set_properties \
                (**{'text-align':
                        'center',
                    'border':
                        '1.3px solid red',
                    'color':
                        'blue'})
            
            
        return \
            statisticsStylerObject
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, returnFormattedStatisticsDataFrameFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return a formatted statistics DataFrame from a Series.')
        
        return \
            None


# In[28]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnDateFromOneYearPriorAsString
 #
 #  Function Description:
 #      This function receives a Series, calculates its statistical values, places them
 #      in a DataFrame, and returns the formatted DataFrame to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          currentDateStringParameter
 #                          The parameter is the input date.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/06/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def ReturnDateFromOneYearPriorAsString \
    (currentDateStringParameter):
    
    
    try:

        mostRecentDateTimeObject \
            = dt \
                .strptime \
                    (currentDateStringParameter, 
                        '%Y-%m-%d')


        if mostRecentDateTimeObject.year % 4 != 0:
    
            daysInYearIntegerVariable \
                = 365
   
        else:
    
            daysInYearIntegerVariable \
                = 366
  
        oneYearPriorToMostRecentDateTimeObject \
            = mostRecentDateTimeObject \
                .date() \
              - timedelta \
                    (days \
                        = daysInYearIntegerVariable)

    
        return \
            dt \
                .strftime \
                    (oneYearPriorToMostRecentDateTimeObject, 
                     '%Y-%m-%d') 
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnDateFromOneYearPriorAsString, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return the date from one year prior.')
        
        return \
            None


# In[29]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnFormattedRowsAsStylerObject
 #
 #  Function Description:
 #      This function formats the rows in a Styler Object and returns the Styler Object.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #  Integer
 #          precisionIntegerParameter
 #                          This optional parameter is the decimal place 
 #                          precision of the displayed numbers
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/07/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnFormattedRowsAsStylerObject \
        (inputStylerObjectParameter, 
         formatterDictionaryParameter):
    
    try:
    
        for row, rowFormatter in formatterDictionaryParameter.items():
        
            rowNumber \
                = inputStylerObjectParameter \
                    .index \
                    .get_loc \
                        (row)

            for columnNumber in range(len(inputStylerObjectParameter.columns)):
            
                inputStylerObjectParameter._display_funcs[(rowNumber, columnNumber)] \
                    = rowFormatter
            
            
        return \
            inputStylerObjectParameter

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnFormattedRowsAsStylerObject, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return the date from one year prior.')
        
        return \
            None


# In[30]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnStylerObjectStandardFormatForSeries
 #
 #  Function Description:
 #      This function formats a Series and returns a Styler Object in standard format.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          The parameter is the input Series.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #  String
 #          indexNameStringParameter
 #                          The parameter is the name for Styler Object's index.
 #  String
 #          columnNameStringParameter
 #                          The parameter is the name for Styler Object's column name.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/13/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnStylerObjectStandardFormatForSeries \
        (inputSeriesParameter,
         captionStringParameter,
         indexNameStringParameter,
         columnNameStringParameter):
    
    try:
        
        inputSeries \
            = inputSeriesParameter.copy()
        
        
        displayDataFrame \
            = pd \
                .DataFrame \
                    (inputSeries \
                        .tolist(), 
                     columns \
                         = [columnNameStringParameter],
                     index \
                         = inputSeries \
                            .index \
                                .tolist())
        
        displayDataFrame \
            .index \
                .name \
                    = indexNameStringParameter

        return \
            ReturnStylerObjectStandardFormat \
                (displayDataFrame,
                 captionStringParameter, 
                 hideFlagBooleanParameter \
                     = False)

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnStylerObjectStandardFormatForSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return a formatted Series for display.')
        
        return \
            None


# In[31]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnExcelFileAsDataFrame
 #
 #  Function Description:
 #      This function receives a file path to an Excel file as a parameter, 
 #      reads the Excel file into a DataFrame, and returns the DataFrame
 #      to the caller.  If the operation fails, the function returns
 #      None.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          filePathString
 #                          The parameter is name of the path to the Excel Workbook.
 #  String
 #          sheetNameString
 #                          The parameter is name of the Worksheet in the the Excel 
 #                          Workbook.
 #  Integer
 #          headerRowInteger
 #                          This parameter is the Worksheet's row index for the column 
 #                          headers.
 #  Integer
 #          indexColumnInteger
 #                          This parameter is the Worksheet's column index for the indices.
 #  Dictionary
 #          dataTypeDictionary
 #                          This parameter is the Dictionary of the Worksheet's column data 
 #                          types.
 #  Dictionary
 #          converterTypeDictionary
 #                          This parameter is the Dictionary of functions for converting
 #                          worksheet values.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/21/2023          Initial Development                         N. James George
 #  09/25/2023          Added Converter Dictionary parameter        N. James George
 #
 #******************************************************************************************/

def ReturnExcelFileAsDataFrame \
        (filePathString,
         sheetNameString \
            = None,
         headerRowInteger \
            = None,
         indexColumnInteger \
            = None,
         dataTypeDictionary \
            = None,
         converterTypeDictionary \
            = None):
    
    try:

        return \
            pd \
                .read_excel \
                    (open \
                        (filePathString, 'rb'),
                     sheet_name \
                        = sheetNameString,
                     header \
                        = headerRowInteger,
                     index_col \
                        = indexColumnInteger,
                     dtype \
                        = dataTypeDictionary,
                     converters \
                        = converterTypeDictionary) 
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnExcelFileAsDataFrame, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return an Excel file as a DataFrame, '
                 + f'{filePathString}.')
    
        return \
            None


# In[32]:


#*******************************************************************************************
 #
 #  Function Name:  DisplayDataFrameDescription
 #
 #  Function Description:
 #      This function takes a DataFrame and returns the formatted description.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrame
 #                          The parameter is input DataFrame.
 #  String
 #          captionString
 #                          The parameter is the text for the caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/21/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayDataFrameDescription \
        (inputDataFrame,
         captionString):
    
    try:
        
        descriptionDataFrame \
            = inputDataFrame \
                .describe()
    
    
        formattersDictionary \
            = {'count': lambda x: f'{x:,.0f}',
               'mean': lambda x: f'{x:,.2f}',
               'std': lambda x: f'{x:,.2f}',
               'min': lambda x: f'{x:,.0f}',
               '25%': lambda x: f'{x:,.2f}',
               '50%': lambda x: f'{x:,.2f}',
               '75%': lambda x: f'{x:,.2f}',
               'max': lambda x: f'{x:,.0f}'}

        descriptionStylerObject \
            = ReturnFormattedRowsAsStylerObject \
                (descriptionDataFrame \
                     .style, 
                 formattersDictionary)
        
        descriptionStylerObject \
            .set_caption \
                (captionString) \
            .set_table_styles \
                ([{'selector': 
                        'caption', 
                   'props':
                        [('color', 
                              'black'), 
                         ('font-size', 
                              '16px'),
                         ('font-style', 
                              'bold'),
                         ('text-align', 
                              'center')]}]) \
            .set_properties \
                (**{'text-align':
                        'center',
                    'border':
                        '1.3px solid red',
                    'color':
                        'blue'})
            
            
        return \
            descriptionStylerObject
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, DisplayDataFrameDescription, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f"cannot display the DataFrame's description.")
        
        return \
            None 


# In[33]:


#*******************************************************************************************
 #
 #  Function Name:  DisplayDataFrameMemoryUsage
 #
 #  Function Description:
 #      This function takes a DataFrame and returns the formatted memory usage.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrame
 #                          The parameter is input DataFrame.
 #  String
 #          captionString
 #                          The parameter is the text for the caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/21/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayDataFrameMemoryUsage \
        (inputDataFrame,
         captionString):
    
    try:
        
        memoryUsageDataFrame \
            = inputDataFrame \
                .memory_usage() \
                .to_frame()

        memoryUsageDataFrame \
            .columns \
                = memoryUsageDataFrame \
                    .iloc[0]

        memoryUsageDataFrame \
            .drop \
                (index \
                     = memoryUsageDataFrame \
                         .index[0], 
                 axis \
                     = 0, 
                 inplace \
                     = True)

        memoryUsageDataFrame \
            .rename \
                (columns \
                     = {memoryUsageDataFrame.keys()[0]: 
                            'Memory (bytes)'},
                 inplace \
                    = True)

        return \
            ReturnStylerObjectStandardFormat \
                (memoryUsageDataFrame,
                 captionString,
                 hideFlagBooleanParameter = False)
        
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, DisplayDataFrameMemoryUsage, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f"cannot display the DataFrame's memory usage.")
        
        return \
            None


# In[34]:


#*******************************************************************************************
 #
 #  Function Name:  DisplayDataFrameDataTypes
 #
 #  Function Description:
 #      This function takes a DataFrame and returns the formatted column data types.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrame
 #                          The parameter is input DataFrame.
 #  String
 #          captionString
 #                          The parameter is the text for the caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/21/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayDataFrameDataTypes \
        (inputDataFrame,
         captionString):
    
    try:
        
        dataTypesDataFrame \
            = inputDataFrame \
                .dtypes \
                .to_frame()

        dataTypesDataFrame \
            .rename \
                (columns \
                     = {dataTypesDataFrame.keys()[0]: 
                            'Data Type'},
                 inplace \
                    = True)
        
        dataTypesDataFrame \
            .index.name \
                = 'Columns'


        return \
            ReturnStylerObjectStandardFormat \
                (dataTypesDataFrame,
                 captionString,
                 hideFlagBooleanParameter = False)
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, DisplayDataFrameDataTypes, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f"cannot display the DataFrame's column data types.")
        
        return \
            None


# In[35]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnFormattedStatisticsDataFrameFromDataFrameList
 #
 #  Function Description:
 #      This function receives a Series, calculates its statistical values, places them
 #      in a DataFrame, and returns the formatted DataFrame to the caller.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          The parameter is the input DataFrame.
 #  String
 #          keyStringParameter
 #                          The parameter is the text for the caption.
 #  String
 #          captionStringParameter
 #                          The parameter is the text for the caption.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/29/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnFormattedStatisticsDataFrameFromDataFrameList \
        (inputDataFrameList,
         keyStringList,
         captionString \
             = ''):
    
    try:

        indexStringList \
            = ['Mean', 
               'Median', 
               'Mode', 
               'Variance', 
               'Std Dev', 
               'SEM', 
               'Minimum', 
               '25%', 
               '50%', 
               '75%', 
               'Maximum', 
               'Count']

        for index, value in enumerate(keyStringList): 

            inputSeries = inputDataFrameList[index][value]
   
            valueList \
                = [inputSeries.mean(),
                   inputSeries.median(),
                   inputSeries.mode()[0],
                   inputSeries.var(),
                   inputSeries.std(),
                   inputSeries.sem(),
                   inputSeries.min(),
                   inputSeries.describe().loc['25%'],
                   inputSeries.describe().loc['50%'],
                   inputSeries.describe().loc['75%'],
                   inputSeries.max(),
                   inputSeries.count()]
    
           
            tempDataFrame \
                = pd \
                    .DataFrame \
                        (valueList, 
                         columns \
                             = [value], 
                         index \
                             = indexStringList)

            if index == 0:
            
                statisticsDataFrame \
                    = tempDataFrame.copy()
            
            else:
            
                statisticsDataFrame \
                    = pd \
                        .concat \
                            ([statisticsDataFrame, 
                              tempDataFrame], 
                             axis = 1)

        formattersDictionary \
            = {'Mean': lambda x: f'{x:.4f}',
               'Median': lambda x: f'{x:.4f}',
               'Mode': lambda x: f'{x:.4f}',
               'Variance': lambda x: f'{x:.4f}',
               'Std Dev': lambda x: f'{x:.4f}',
               'SEM': lambda x: f'{x:.4f}',
               'Minimum': lambda x: f'{x:.2f}',
               '25%': lambda x: f'{x:.2f}',
               '50%': lambda x: f'{x:.2f}',
               '75%': lambda x: f'{x:.2f}',
               'Maximum': lambda x: f'{x:.2f}',
               'Count': lambda x: f'{x:.0f}'}

        statisticsStylerObject \
            = ReturnFormattedRowsAsStylerObject \
                (statisticsDataFrame.style, 
                 formattersDictionary)
        
        
        return \
            statisticsStylerObject \
                .set_caption \
                    (captionString) \
                .set_table_styles \
                    ([{'selector': 'caption', 
                       'props': [('color', 'black'), 
                                 ('font-size', '16px'),
                                 ('font-style', 'bold'),
                                 ('text-align', 'center')]}]) \
                .set_properties \
                    (**{'text-align': 'center',
                        'border': '1.3px solid red',
                        'color': 'blue'})
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnFormattedStatisticsDataFrameFromDataFrameList, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return a formatted statistics DataFrame.')
        
        return \
            None


# In[36]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnMinimumMaximumValuesXAxisHistogram
 #
 #  Function Description:
 #      This function returns the minimum and maximum x-axis values 
 #      from a list of DataFrames.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame List
 #          inputDataFrameList
 #                          The parameter is the input DataFrame List.
 #  String List
 #          columnNameStringList
 #                          This parameter is a List of the columns for display.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/30/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnMinimumMaximumValuesXAxisHistogram \
        (inputDataFrameList,
         columnNameStringList):

    try:
        
        minimumXValueFloat \
            = inputDataFrameList[0] \
                [columnNameStringList[0]] \
                    .min()
            
        maximumXValueFloat \
            = inputDataFrameList[0] \
                [columnNameStringList[0]] \
                    .max()
            
        for index in range(len(inputDataFrameList)):
                
            currentMinimumXValueFloat \
                = inputDataFrameList[index] \
                    [columnNameStringList[index]] \
                        .min()
                
            currentMaximumXValueFloat \
                = inputDataFrameList[index] \
                    [columnNameStringList[index]] \
                        .max()
                
            if currentMinimumXValueFloat <= minimumXValueFloat:
                    
                minimumXValueFloat = currentMinimumXValueFloat
                    
            if currentMaximumXValueFloat >= maximumXValueFloat:
                    
                maximumXValueFloat = currentMaximumXValueFloat 
                
        return \
            [minimumXValueFloat,
             maximumXValueFloat]
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnMinimumMaximumValuesXAxisHistogram, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return minimum and maximum x-axis values.')
        
        return \
            None        


# In[37]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnMinimumMaximumValuesYAxisHistogram
 #
 #  Function Description:
 #      This function returns the minimum and maximum y-axis values 
 #      from a list of DataFrames.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame List
 #          inputDataFrameList
 #                          The parameter is the input DataFrame List.
 #  String List
 #          columnNameStringList
 #                          This parameter is a List of the columns for display.
 #  Boolean
 #          normalizeYAxisHighestValueCountBoolean
 #                          This parameter indicates whether the highest value count alone 
 #                          is the maximum y-axis value.
 #  Integer
 #          binsInteger
 #                          This parameter is the number of bins in the histograms.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/30/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnMinimumMaximumValuesYAxisHistogram \
        (inputDataFrameList,
         columnNameStringList,
         normalizeYAxisHighestValueCountBoolean,
         binsInteger):
    
    try:
        
        minimumYValueFloat = 0.0
            
        maximumYValueFloat = 0.0
            
        if normalizeYAxisHighestValueCountBoolean == True:
            
            for index in range(len(inputDataFrameList)):
                
                currentMinimumYValueFloat \
                    = inputDataFrameList[index] \
                        [columnNameStringList[index]] \
                            .min()
                
                currentMaximumYValueFloat \
                    = inputDataFrameList[index] \
                        [columnNameStringList[index]] \
                            .max()
                
                if currentMinimumYValueFloat <= minimumYValueFloat:
                    
                    minimumYValueFloat = currentMinimumYValueFloat
                    
                if currentMaximumYValueFloat >= maximumYValueFloat:
                    
                    maximumYValueFloat = currentMaximumYValueFloat
                        
        else:
            
            for index in range(len(inputDataFrameList)):
                    
                upperIndexLimitFloat \
                    = inputDataFrameList[index] \
                        [columnNameStringList[index]].max() \
                      / float(binsInteger)

                sumOfFrequencyCountsInteger = 0
                
                for rowIndex, row \
                    in enumerate \
                        (inputDataFrameList[index] \
                             [columnNameStringList[index]] \
                                .value_counts().index):
                    
                    if row <= upperIndexLimitFloat:
    
                        sumOfFrequencyCountsInteger \
                            += inputDataFrameList[index] \
                                [columnNameStringList[index]] \
                                    .value_counts()[row]


                if sumOfFrequencyCountsInteger >= maximumYValueFloat:
                    
                    maximumYValueFloat = sumOfFrequencyCountsInteger
        
        
        return \
            [minimumYValueFloat, 
             maximumYValueFloat]
    
    except:
        
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ReturnMinimumMaximumValuesYAxisHistogram, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to return minimum and maximum y-axis values.')
        
        return \
            None        


# In[38]:


#*******************************************************************************************
 #
 #  Function Name:  ConvertDateStringListToMonthDayStringSeries
 #
 #  Function Description:
 #      This function converts a String with the format, yyyy-mm-dd, and returns
 #      the String, mm-dd.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  String
 #          inputDateStringList
 #                          This parameter is a input date String.
 #  Integer
 #          removeNumberOfFirstCharactersInteger
 #                          This parameter indicates how many characters to remove
 #                          from the beginning of the input String.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/30/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ConvertDateStringListToMonthDayStringSeries \
        (inputDateStringList,
         removeNumberOfFirstCharactersInteger):
    
    try:
        
        tempSeries \
            = pd.Series \
                (inputDateStringList)
    
        monthDaySeries \
            = tempSeries \
                .apply \
                    (lambda x: x[removeNumberOfFirstCharactersInteger:])

        return \
            monthDaySeries
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, ConvertDateStringListToMonthDayStringSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to convert a date to a month and day.')
        
        return \
            None         


# In[39]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnNormalizedMonthDayIndexSeries
 #
 #  Function Description:
 #      This function returns a normalized index Series from a DataFrame List.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame List
 #          inputDataFrameList
 #                          This parameter is a input DataFrame List
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/30/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnNormalizedMonthDayIndexSeries \
        (inputDataFrameList):
    
    try:
        
        sortedDataFrameList \
            = sorted(inputDataFrameList, key=len)

        for index, dataFrameObject in enumerate(sortedDataFrameList):
    
            if 'newIndex' not in dataFrameObject.index.name:
            
                seriesObject \
                    = ConvertDateStringListToMonthDayStringSeries \
                        (dataFrameObject.index.tolist(), 5)
    
                dataFrameObject['newIndex'] \
                    = seriesObject.values
    
                dataFrameObject \
                    .set_index \
                        ('newIndex',  
                         drop = True, 
                         append = False,
                         inplace = True,
                         verify_integrity = False)
        
    
            if index > 1:

                currentDataFrameIndexSeries \
                    = dataFrameObject.index
        
        
                lastDataFrameIndexLengthInteger \
                    = len(tempIndexSeries)
        
                currentDataFrameIndexLengthInteger \
                    = len(currentDataFrameIndexSeries)
        
        
                tempIndexSeries \
                    = currentDataFrameIndexSeries \
                        [currentDataFrameIndexSeries.isin(tempIndexSeries)]
        
            else:

                tempIndexSeries \
                    = dataFrameObject.index    
        
        
        return \
            tempIndexSeries
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ReturnNormalizedMonthDayIndexSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to normalize the index series from ' 
                 + 'a DataFrame List.')
        
        return \
            None


# In[40]:


#*******************************************************************************************
 #
 #  Function Name:  ReturnNormalizedDataFrameFromIndex
 #
 #  Function Description:
 #      This function returns a normalized DataFrame from a normalized index Series
 #      and a DataFrame List.
 #
 #
 #  Function Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame List
 #          inputDataFrameList
 #                          This parameter is a input DataFrame List
 #  String
 #          omitColumnNameString
 #                          This parameter is the name of an omitted DataFrame column.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/30/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def ReturnNormalizedDataFrameFromIndex \
        (inputDataFrameList,
         omitColumnNameString):
    
    try:
        normalizedIndexSeries \
            = ReturnNormalizedMonthDayIndexSeries \
                (inputDataFrameList)

        normalizedDataFrameList \
            = []

        for index, dataFrameObject in enumerate(inputDataFrameList):

            tempDataFrame \
                = dataFrameObject \
                    .apply \
                        (lambda row: row[dataFrameObject.index.isin(normalizedIndexSeries)])
    
            if omitColumnNameString not in dataFrameObject.columns:
        
                normalizedDataFrameList \
                    .append \
                        (tempDataFrame)
        
        return \
            pd.concat \
                (normalizedDataFrameList, 
                 axis = 1)
    
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The function, ReturnNormalizedDataFrameFromIndex, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + 'was unable to return a normalized DataFrame from a ' 
                 + 'normalized index.')
        
        return \
            None


# In[ ]:




