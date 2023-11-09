#!/usr/bin/env python
# coding: utf-8

# In[1]:


#*******************************************************************************************
 #
 #  File Name:  PySubroutines.py
 #
 #  File Description:
 #      This Python script, PySubroutines.py, contains generic Python subroutines
 #      for completing common tasks.  Here is the list:
 #
 #      DisplayPandasBarChartFromSeries
 #      DisplayMatplotlibBarChartFromSeries
 #      DisplayPandasPieChartFromSeries
 #      DisplayMatplotlibPieChartFromSeries
 #      DisplayMatplotlibBoxPlotFromSeriesList
 #      DisplayMatplotlibLineChartFromXYSeries
 #      DisplayRegressionLine
 #      DisplayMatplotlibScatterPlotFromXYSeries
 #      DisplaySummaryStatisticsBoxPlot
 #      DisplayOneLineGraphFromSeries
 #      DisplaySeriesCountAndRedundancies
 #      DisplayTwoByTwoHistograms
 #      DisplayLinearRegressionLine
 #      DisplayTwoPieChartsSideBySide
 #      DisplayStackedBarChartFromDataFrame
 #      DisplayHistogramFromSeries
 #      DisplayPlotFromXYSeries
 #      DisplayPieChartFromXYLists
 #      DisplayHorizontalBarChartFromXYLists
 #      DisplayTwoScatterPlotsSideBySide
 #      DisplayPlotFromDataFrame
 #      DisplayMultiLineGraphFromDataFrame
 #      DisplayTwoByFourHistogramsFromDataFrameList
 #      InsertJSONFileIntoMongoDBCollection
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  08/22/2023      Initial Development                     N. James George
 #  09/03/2023      Added DisplayStackedBarChartFromDataFrame
 #                                                          N. James George
 #  09/06/2023      Added DisplayHistogramFromSeries        N. James George
 #  09/11/2023      Set figure size to (9.708, 6) for all plots
 #                                                          N. James George
 #  09/12/2023      Set font sizes to 20, 16, 16, 14, 14    N. James George
 #  09/13/2023      Added ReturnPlotFromXYSeries            N. James George
 #  09/15/2023      Added DisplayPieChartFromXYLists        N. James George
 #                  and DisplayHorizontalBarChartFromXYLists      
 #  09/16/2023      Added DisplayTwoScatterPlotsSideBySide  N. James George
 #  09/17/2023      Added DisplayPlotFromDataFrame          N. James George
 #  09/22/2023      Added parameter, labelYOffsetFloat,     N. James George
 #                  to ReturnPlotFromXYSeries
 #  09/23/2023      Renamed ReturnPlotFromXYSeries to DisplayPlotFromXYSeries
 #                                                          N. James George
 #  09/28/2023      Added parameters to DisplayHistogramFromSeries
 #                                                          N. James George
 #  09/29/2023      Added DisplayMultiLineGraphFromDataFrame,
 #                        DisplayTwoByFourHistogramsFromDataFrameList
 #                                                          N. James George
 #  09/29/2023      Added DisplayTwoByFourPlotsFromDataFrameList
 #                                                          N. James George
 #  10/18/2023      Transferred InsertJSONFileIntoMongoDBCollection
 #                                                          N. James George
 #
 #******************************************************************************************/

import PyFunctions as function
import PyLogSubRoutines as log_subroutine

import math

import matplotlib.pyplot as plt
import pandas as pd

from scipy import stats
from pathlib import Path


# In[2]:


CONSTANT_LOCAL_FILE_NAME \
    = 'PySubroutines.py'


# In[3]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayPandasBarChartFromSeries
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters 
 #      and plots a bar chart using the Pandas DataFrame.plot() 
 #      method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the Series used as input.
 #  List
 #          barColorsListParameter
 #                          This parameter is the list of bar colors.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  String
 #          yLabelStringParameter
 #                          This parameter is the y-axis label.
 #  String
 #          edgeColorStringParameter
 #                          This parameter is the bar edge color.
 #  Float
 #          lineWidthFloatParameter
 #                          This parameter is the bar edge line width.
 #  Float
 #          alphaFloatParameter
 #                          This parameter is the transparency value
 #                          for the bars (0.0-1.0).
 #  Float
 #          widthFloatParameter
 #                          This parameter is the width of a bar.
 #  Float
 #          axisTickLabelRotationFloatParameter
 #                          This parameter is the rotation of the x-axis 
 #                          tick labels.
 #  String
 #          xLabelStringParameter
 #                          This parameter is the x-axis label.
 #  Float List
 #          figureSizeFloatList
 #                          This parameter is the dimensions of the figure.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #  9/06/2023           Added xLabelStringParameter                 N. James George
 #
 #******************************************************************************************/

def DisplayPandasBarChartFromSeries \
        (inputSeriesParameter,
         barColorsListParameter,
         captionStringParameter, 
         yLabelStringParameter,
         edgeColorStringParameter \
            = 'black',
         lineWidthFloatParameter \
            = 1.5,
         alphaFloatParameter \
            = 1.0,
         widthFloatParameter \
            = 0.5,
         axisTickLabelRotationFloatParameter \
            = 80.0,
         xLabelStringParameter \
            = None,
         figureSizeFloatList \
            = [9.708, 6.0]):
    
    try:
        
        inputSeries \
            = inputSeriesParameter.copy()
        
        inputSeries \
            .plot \
            .bar \
                (stacked \
                     = False,
                 align \
                     = 'center',
                 color \
                     = barColorsListParameter,
                 edgecolor \
                     = edgeColorStringParameter,
                 linewidth \
                     = lineWidthFloatParameter,
                 alpha \
                     = alphaFloatParameter,
                 width \
                     = widthFloatParameter, 
                 rot \
                     = axisTickLabelRotationFloatParameter,
                 legend \
                     = False,
                 figsize \
                     = (figureSizeFloatList[0], 
                        figureSizeFloatList[1]))
        
        plt \
            .title \
                (captionStringParameter,
                 fontdict \
                     = {'fontsize': 
                            20, 
                        'fontstyle': 
                            'normal'},
                 pad \
                     = 20)

        if xLabelStringParameter == None:
            
            xLabelStringParameter \
                = inputSeries \
                    .name
        
        plt \
            .xlabel \
                (xLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            16,
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 10)

        plt \
            .ylabel \
                (yLabelStringParameter,
                 fontdict \
                    = {'fontsize': 
                            16,
                       'fontstyle': 
                            'normal'},
                 labelpad \
                     = 10)
        
        plt \
            .xticks \
                (fontsize \
                     = 14)
       
        plt \
            .yticks \
                (fontsize \
                     = 14)
    
        plt \
            .grid \
                (axis \
                    = "y")
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
      
        plt \
            .show()
     
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayPandasBarChartFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a bar chart using Pandas.')


# In[4]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayMatplotlibBarChartFromSeries
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters 
 #      and plots a bar chart using the Matplotlib pyplot method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the Series used as input.
 #  List
 #          barColorsListParameter
 #                          This parameter is the list of bar colors.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  String
 #          yLabelStringParameter
 #                          This parameter is the y-axis label.
 #  String
 #          edgeColorStringParameter
 #                          This parameter is the bar edge color.
 #  Float
 #          lineWidthFloatParameter
 #                          This parameter is the bar edge line width.
 #  Float
 #          alphaFloatParameter
 #                          This parameter is the transparency value
 #                          for the bars (0.0-1.0).
 #  Float
 #          widthFloatParameter
 #                          This parameter is the width of a bar.
 #  Float
 #          axisTickLabelRotationFloatParameter
 #                          This parameter is the rotation of the x-axis 
 #                          tick labels.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayMatplotlibBarChartFromSeries \
        (inputSeriesParameter,
         barColorsListParameter,
         captionStringParameter, 
         yLabelStringParameter,
         edgeColorStringParameter \
            = 'black',
         lineWidthFloatParameter \
            = 1.5,
         alphaFloatParameter \
            = 1.0,
         widthFloatParameter \
            = 0.5,
         axisTickLabelRotationFloatParameter \
            = 80.0):
    
    
    try:
        
        inputSeries \
            = inputSeriesParameter.copy()
        
        plt \
            .figure \
                (figsize \
                     = (9.708, 6))
        
        plt \
            .bar \
                (inputSeries.keys(),
                 inputSeries,
                 align \
                     = 'center',
                 color \
                     = barColorsListParameter,
                 edgecolor \
                     = edgeColorStringParameter,
                 linewidth \
                     = lineWidthFloatParameter,
                 alpha \
                     = alphaFloatParameter,
                 width \
                     = widthFloatParameter)
        
        plt \
            .title \
                (captionStringParameter,
                 fontdict \
                     = {'fontsize': 
                            20, 
                        'fontstyle': 
                            'normal'},
                 pad \
                    = 20)

        plt \
            .xlabel \
                (inputSeries \
                     .name,
                 fontdict \
                     = {'fontsize': 
                            16, 
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 10)
        
        plt \
            .ylabel \
                (yLabelStringParameter,
                 fontdict \
                    = {'fontsize': 
                            16, 
                       'fontstyle': 
                            'normal'},
                 labelpad \
                    = 10)
        
        plt \
            .xticks \
                (rotation \
                     = axisTickLabelRotationFloatParameter,
                 fontsize \
                     = 14)
        
        plt \
            .yticks \
                (fontsize \
                     = 14)

        plt \
            .grid \
                (axis \
                    = "y")
        
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show()

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayMatplotlibBarChartFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a bar chart using Matplotlib.')


# In[5]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayPandasPieChartFromSeries
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters 
 #      and plots a pie chart using the Pandas DataFrame.plot() 
 #      method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the Series used as input.
 #  List
 #          colorsListParameter
 #                          This parameter is the list of bar colors.
 #  List
 #          explodeTupleParameter
 #                          This parameter specifies the fraction of the 
 #                          radius with which to offset each wedge.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  Float
 #          startAngleFloatParameter
 #                          This parameter is the angle by which the start 
 #                          of the pie is rotated, counterclockwise from 
 #                          the x-axis.
 #  Float
 #          autoPercentStringParameter
 #                          This parameter is the format of the wedge label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
    
def DisplayPandasPieChartFromSeries \
        (inputSeriesParameter, 
         colorsListParameter,
         explodeTupleParameter,
         captionStringParameter,
         startAngleFloatParameter \
            = 45.0,
         autoPercentStringParameter \
            = '%1.1f%%'):
    
    try:

        inputSeries \
            = inputSeriesParameter.copy()
        
        inputSeries \
            .rename \
                (None, 
                 inplace \
                     = True)
        
        inputSeries \
            .plot \
            .pie \
                (colors \
                     = colorsListParameter, 
                 explode \
                     = explodeTupleParameter, 
                 shadow \
                     = True, 
                 startangle \
                     = startAngleFloatParameter, 
                 autopct \
                     = autoPercentStringParameter,
                 pctdistance \
                     = 0.75,
                 legend \
                     = False,
                 figsize \
                    = (9.708, 6),
                 textprops \
                     = {'fontsize':
                           14})

        plt \
            .title \
                (captionStringParameter,
                 fontdict \
                     = {'fontsize': 
                            20, 
                        'fontstyle': 
                            'normal'},
                 pad \
                    = 5)

        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayPandasPieChartFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a pie chart using Pandas.')


# In[6]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayMatplotlibPieChartFromSeries
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters 
 #      and plots a pie chart using the Matplotlib pyplot method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the Series used as input.
 #  List
 #          colorsListParameter
 #                          This parameter is the list of bar colors.
 #  List
 #          explodeTupleParameter
 #                          This parameter specifies the fraction of the 
 #                          radius with which to offset each wedge.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  Float
 #          startAngleFloatParameter
 #                          This parameter is the angle by which the start 
 #                          of the pie is rotated, counterclockwise from 
 #                          the x-axis.
 #  Float
 #          autoPercentStringParameter
 #                          This parameter is the format of the wedge label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayMatplotlibPieChartFromSeries \
        (inputSeriesParameter, 
         colorsListParameter,
         explodeTupleParameter,
         captionStringParameter,
         startAngleFloatParameter \
            = 45.0,
         autoPercentStringParameter \
            = '%1.1f%%'):
    
    try:

        inputSeries \
            = inputSeriesParameter.copy()
        
        inputSeries \
            .rename \
                (None, 
                 inplace \
                     = True)
        
        plt \
            .figure \
                (figsize \
                     = (9.708, 6))
        
        plt \
            .pie \
                (inputSeries,
                 labels \
                     = inputSeries.index, 
                 colors \
                     = colorsListParameter,        
                 explode \
                     = explodeTupleParameter, 
                 shadow \
                     = True,
                 pctdistance \
                     = 0.75,
                 startangle \
                     = startAngleFloatParameter,
                 autopct \
                     = autoPercentStringParameter,
                 textprops \
                     = {'fontsize':
                           14})
        
        plt \
            .title \
                (captionStringParameter,
                 fontdict \
                     = {'fontsize': 
                            20, 
                        'fontstyle': 
                            'normal'},
                 pad \
                    = 5)   
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayMatplotlibPieChartFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a pie chart using Matplotlib.')


# In[7]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayMatplotlibBoxPlotFromSeriesList
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters and plots 
 #      a box plot using the Matplotlib pyplot method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List of Series
 #          inputSeriesListParameter
 #                          This parameter holds a list of series where 
 #                          each series is the data for one box plot.
 #  List
 #          xTicksLabelListParameter
 #                          This parameter is the list of x-axis tick 
 #                          labels.
 #  String
 #          xLabelParameter
 #                          This parameter is the x-axis label. 
 #  String
 #          xLabelParameter
 #                          This parameter is the y-axis label.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  Boolean
 #          verticalFlagBooleanParameter
 #                          This parameter indicates whether the box
 #                          plots are vertical or horizontal.
 #  Float
 #          xTicksRotationFloat
 #                          This parameter sets the rotation angle for the x-ticks labels.
 #
 #  Float List
 #          figureSizeFloatList
 #                          This parameter sets the figure size.
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/19/2023           Initial Development                         N. James George
 #  9/15/2023           Added parameter,  xTicksRotationFloat       N. James George
 #
 #******************************************************************************************/
        
def DisplayMatplotlibBoxPlotFromSeriesList \
        (inputSeriesListParameter,
         xTicksLabelListParameter,
         xLabelStringParameter,
         yLabelStringParameter,
         captionStringParameter,
         verticalFlagBooleanParameter \
             = True,
         xTicksRotationFloat \
            = 0.0,
         figureSizeFloatList \
            = [9.708, 6.0]):
    
    try:
        
        inputSeriesList \
            = inputSeriesListParameter.copy()
        
        fig1, ax \
            = plt \
                .subplots \
                    (figsize \
                         = (figureSizeFloatList[0], 
                            figureSizeFloatList[1]))

        ax \
            .boxplot \
                (inputSeriesList,
                 vert \
                     = verticalFlagBooleanParameter,
                 widths \
                     = 0.45,
                 meanline \
                     = True, 
                 showmeans \
                     = True)
        
        ax \
            .set_title \
                (captionStringParameter,
                 fontdict \
                     = {'fontsize': 
                            20, 
                        'fontstyle': 
                            'normal'},
                 pad \
                     = 20)
        
        ax \
            .set_xlabel \
                (xLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            16, 
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 10)

        ax \
            .set_ylabel \
                (yLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            16, 
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 10)
          
        ticksIndexList \
            = []
        
        for index, regimen in enumerate(xTicksLabelListParameter):
            
                ticksIndexList \
                    .append \
                        ( index + 1 )
        
        ax \
            .set_xticks \
                (ticksIndexList, 
                 xTicksLabelListParameter,
                 fontsize \
                    = 14,
                 rotation \
                    = xTicksRotationFloat)
        
        if verticalFlagBooleanParameter == True:
        
            plt \
                .grid \
                    (axis \
                        = 'y')
        
        else:
            
            plt \
                .grid \
                    (axis \
                        = 'x')
        
        
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show() 
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayMatplotlibBoxPlotFromSeriesList, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a box plot using Matplotlib.')


# In[8]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayMatplotlibLineChartFromXYSeries
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters 
 #      and plots a line chart using the Matplotlib pyplot method.
 #
 #
 #  Subroutine Parameters:
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
 #  String
 #          lineColorStringParameter
 #                          This parameter is the line color.
 #  String
 #          lineTypeStringParameter
 #                          This parameter is the line style ('solid', 
 #                          'dotted', 'dashed', or 'dashdot'.
 #  String
 #          xLabelStringParameter
 #                          This parameter is the labe for the x-axis.
 #  String
 #          yLabelStringParameter
 #                          This parameter is the labe for the y-axis.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/18/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/
        
def DisplayMatplotlibLineChartFromXYSeries \
        (xSeriesParameter,
         ySeriesParameter,
         lineColorStringParameter,
         lineTypeStringParameter,
         xLabelStringParameter,
         yLabelStringParameter,
         captionStringParameter):
    
    try:

        xSeries \
            = xSeriesParameter.copy()
       
        ySeries \
            = ySeriesParameter.copy()
            
        plt \
            .figure \
                (figsize \
                     = (9.708, 6))
    
        plt \
            .plot \
                (xSeries,
                 ySeries,
                 alpha \
                    = 1.0,
                 color \
                     = lineColorStringParameter,
                 fillstyle \
                     = 'full',
                 linewidth \
                     = 3.0,
                 marker \
                     = 'o',
                 markerfacecolor \
                     = 'red',
                 markeredgecolor \
                     = 'black',
                 markersize \
                     = 10,
                 markeredgewidth \
                     = 1.0,
                 linestyle \
                     = lineTypeStringParameter)

        plt \
            .title \
                (captionStringParameter,
                 fontdict \
                     = {'fontsize': 
                            20, 
                        'fontstyle': 
                            'normal'},
                 pad \
                    = 20)

        plt \
            .xlabel \
                (xLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            16,
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 10)

        plt \
            .ylabel \
                (yLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            16,
                        'fontstyle': 
                            'normal'},
                 labelpad \
                     = 10)
        
        plt \
            .xticks \
                (fontsize \
                     = 14)
       
        plt \
            .yticks \
                (fontsize \
                     = 14)

        plt \
            .grid()
        
    
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)

        plt \
            .show()

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayMatplotlibLineChartFromXYSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a line chart using Matplotlib.')


# In[9]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayRegressionLine 
 #
 #  Subroutine Description:
 #      This subroutine receives two Series and the polynomial degree, calculates 
 #      the parameters of the regression line, and displays the results on the 
 #      scatter plot and above it.
 #
 #
 #  Subroutine Parameters:
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
 #  Float
 #          xCoordinateFloatParameter
 #                          This parameter is the x-coordinate of the text 
 #                          in the chart.
 #  Float
 #          yCoordinateFloatParameter
 #                          This parameter is the y-coordinate of the text 
 #                          in the chart.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/  
        
def DisplayRegressionLine \
                (xSeriesParameter,
                 ySeriesParameter,
                 degreeIntegerParameter,
                 xCoordinateFloatParameter,
                 yCoordinateFloatParameter):

    try:
        
        modelEquationList \
            = function \
                .ReturnRegressionModelEquationList \
                    (xSeriesParameter,
                     ySeriesParameter,
                     degreeIntegerParameter)
 
        polynomialLineSeries \
            = function \
                .ReturnPolynomialLineSeries \
                    (xSeriesParameter, 
                     ySeriesParameter)
 
        plt \
            .plot \
                (polynomialLineSeries, 
                 modelEquationList \
                    (polynomialLineSeries),
                 color \
                     = 'red',
                 linewidth \
                     = 3.0,
                 alpha \
                     = 1.0)

        equationLabelStringVariable \
            = function \
                .ReturnEquationAsString \
                    (modelEquationList)
    
        plt.annotate \
            (equationLabelStringVariable,
             (xCoordinateFloatParameter,
              yCoordinateFloatParameter),
             fontsize \
                 = 16,
             fontweight \
                 = 'bold',
             color \
                 = 'blue')
    
        rSquaredFloatVariable \
            = function \
                .ReturnRSquaredValue \
                    (xSeriesParameter,
                     ySeriesParameter,
                     degreeIntegerParameter)
    
        rValueFloatVariable \
            = math.sqrt(rSquaredFloatVariable)

        log_subroutine \
            .PrintAndLogWriteText \
                ('r-value:     {:.4f}'.format(rValueFloatVariable))
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('r-squared:   {:.4f}'.format(rSquaredFloatVariable))
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayRegressionLine, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'was unable to calculate and display a regression line.')


# In[10]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayMatplotlibScatterPlotFromXYSeries
 #
 #  Subroutine Description:
 #      This subroutine receives two Series and formatting parameters 
 #      and plots a scatter plot using the Matplotlib pyplot method.
 #      If the polynomial degree parameter is greater than zero, it 
 #      also plots the regression line and displays the results of 
 #      the regression.
 #
 #
 #  Subroutine Parameters:
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
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  Integer
 #          optionalDegreeIntegerParameter
 #                          This parameter is degree of the polynomial 
 #                          regression.
 #  Integer
 #          optionalTextXCoordinateIntegerParameter
 #                          This parameter is the x-coordinate of the text 
 #                          in the chart.
 #  Integer
 #          optionalTextYCoordinateIntegerParameter
 #                          This parameter is the y-coordinate of the text 
 #                          in the chart.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/  
    
def DisplayMatplotlibScatterPlotFromXYSeries \
        (xSeriesParameter, 
         ySeriesParameter, 
         captionStringParameter,
         optionalDegreeIntegerParameter \
             = 0,
         optionalTextXCoordinateFloatParameter \
             = 0,
         optionalTextYCoordinateFloatParameter \
             = 0):
    
    try:
        
        xSeries \
            = xSeriesParameter.copy()
    
        ySeries \
            = ySeriesParameter.copy()
    
        plt \
            .figure \
                (figsize \
                     = (9.708, 6))
        
        plt \
            .scatter \
                (xSeries, 
                 ySeries, 
                 marker \
                     = 'o',
                 s \
                     = 80,
                 color 
                     = 'lime', 
                 linewidth \
                     = 1.5,
                 edgecolors \
                     = 'black',
                 alpha \
                     = 0.8)

        plt \
            .title \
                (captionStringParameter, 
                 fontdict \
                     = {'fontsize': 
                            20, 
                        'fontstyle': 
                            'normal'},
                 pad \
                     = 20)
    
        plt \
            .xlabel \
                (xSeries \
                     .name,
                 fontdict \
                     = {'fontsize': 
                            16, 
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 10)

        plt \
            .ylabel \
                (ySeries \
                     .name,
                 fontdict \
                     = {'fontsize': 
                            16, 
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 10)
        
        plt \
            .xticks \
                (fontsize \
                     = 14)
       
        plt \
            .yticks \
                (fontsize \
                     = 14)
        
        plt \
            .grid()
        
        if optionalDegreeIntegerParameter == 1:
            
            DisplayLinearRegressionLine \
                (xSeries,
                 ySeries,
                 optionalTextXCoordinateFloatParameter,
                 optionalTextYCoordinateFloatParameter)
            
        elif optionalDegreeIntegerParameter > 1:
                
            DisplayRegressionLine \
                (xSeries,
                 ySeries,
                 optionalDegreeIntegerParameter,
                 optionalTextXCoordinateFloatParameter,
                 optionalTextYCoordinateFloatParameter)
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayMatplotlibScatterPlotFromXYSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a scatter plot using Matplotlib.')


# In[11]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayStackedSubplots
 #
 #  Subroutine Description:
 #      This subroutine receives a DataFrame, and formatting parameters, and creates
 #      stacked subplots.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary
 #          frameDictionaryParameter
 #                          This parameter is the input Dictionary for conversion 
 #                          to a DataFrame.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  List of Strings
 #          colorListParameter
 #                          This parameter is the list of colors for the subplots.
 #  String
 #          figureXLabelStringParameter
 #                          This parameter is the title for the figure's x-axis.
 #  String
 #          figureYLabelStringParameter
 #                          This parameter is the title for the figure's y-axis.
 #  String
 #          xLabelStringParameter
 #                          This parameter is the title for the plot's x-axis.
 #  String
 #          yLabelStringParameter
 #                          This parameter is the title for the plot's y-axis.
 #  Float
 #          figureXLabelYPositionFloatParameter
 #                          This parameter is the y-axis offset for the figure's 
 #                          x-label.
 #  Float
 #          figureYLabelYPositionFloatParameter
 #                          This parameter is the x-axis offset for the figure's 
 #                          y-label.
 #  Boolean
 #          legendFlagBooleanParameter 
 #                          This parameter indicates whether there will be a 
 #                          legend or not.
 #  Float
 #          legendXOffsetFloatParameter
 #                          This parameter is the x-axis offset for the figure's 
 #                          legend.
 #  Float
 #          legendYOffsetFloatParameter
 #                          This parameter is the y-axis offset for the figure's 
 #                          legend.
 #  Boolean
 #          firstYLabelOffsetBooleanParameter
 #                          This parameter indicates whether there will be a 
 #                          offset for the first subplot y-axis label.
 #  Float
 #          firstYLabelOffsetFloatParameter
 #                          This parameter is the y-axis offset for the first
 #                          subplot's y-axis label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/  
        
def DisplayStackedSubplots \
        (frameDictionaryParameter,
         captionStringParameter,
         colorListParameter,
         figureXLabelStringParameter \
            = None,
         figureYLabelStringParameter \
            = None,
         xLabelStringParameter \
            = None,
         yLabelStringParameter \
            = None,
         figureXLabelYPositionFloatParameter \
            = 0.0,
         figureYLabelXPositionFloatParameter \
            = 0.0,
         legendFlagBooleanParameter \
            = False,
         legendXOffsetFloatParameter \
            = 0.0,
         legendYOffsetFloatParameter \
            = 0.0,
         firstYLabelOffsetBooleanParameter \
            = False,
         firstYLabelOffsetFloatParameter \
            = 0.0):
    
    try:

        inputDataFrame \
            = pd \
                .DataFrame \
                    (frameDictionaryParameter)
        
        numberOfSubPlotsIntegerVariable \
            = len \
                (inputDataFrame \
                     .keys())
    
        fig, axs \
            = plt \
                .subplots \
                    (numberOfSubPlotsIntegerVariable,
                     figsize \
                        = (9.708, 6))
   
        fig \
            .suptitle \
                (captionStringParameter, 
                 fontsize \
                     = 20)
      
        if figureXLabelStringParameter != None:
            
            fig \
                .supxlabel \
                    (figureXLabelStringParameter,
                     fontsize \
                         = 16,
                     y \
                         = figureXLabelYPositionFloatParameter)
       
        if figureYLabelStringParameter != None:
            
            fig \
                .supylabel \
                    (figureYLabelStringParameter,
                     fontsize \
                         = 16,
                     x \
                         = figureYLabelXPositionFloatParameter)
    
        legendLinePlotList \
             = []
        
        legendLineNamesList \
            = []
    
        for index, subPlot in enumerate(axs):
        
            lineSubPlot, \
                = subPlot \
                    .plot \
                        (inputDataFrame.iloc[:,index], 
                         color \
                             = colorListParameter[index])
            
            legendLinePlotList \
                .append \
                    (lineSubPlot)
            
            legendLineNamesList \
                .append \
                    (inputDataFrame.iloc[:,index].name)
            
            subPlot \
                .grid()
            
            if index != (numberOfSubPlotsIntegerVariable - 1):

                subPlot \
                    .set_xticklabels \
                        (labels = [])

            else:

                if xLabelStringParameter == None:

                    subPlot \
                        .set_xlabel \
                            ('',
                             fontsize \
                                = 16)
                else:
                    
                    subPlot \
                        .set_xlabel \
                            (xLabelStringParameter,
                                fontsize \
                                = 16)


            if yLabelStringParameter == None:
               
                if firstYLabelOffsetBooleanParameter == True \
                    and index == 0:
                    
                    subPlot \
                        .set_ylabel \
                            (inputDataFrame \
                                 .iloc \
                                     [:,index] \
                                         .name,
                             fontsize \
                                = 16,
                             labelpad \
                                = firstYLabelOffsetFloatParameter)
                    
                else:
                    
                    subPlot \
                        .set_ylabel \
                            (inputDataFrame \
                                 .iloc \
                                     [:,index] \
                                         .name,
                             fontsize \
                                = 16,
                             labelpad \
                                = 10)

            else:

                subPlot \
                    .set_ylabel \
                        (yLabelStringParameter,
                         fontsize \
                            = 16,
                         labelpad \
                            = 0)
                
            subPlot \
                .tick_params \
                    (axis \
                        = 'x', 
                     rotation \
                        = 90.0,
                     labelsize \
                        = 14)
            
            subPlot \
                .tick_params \
                    (axis \
                        = 'y', 
                     rotation \
                        = 0.0,
                     labelsize \
                        = 14)
                        
        if legendFlagBooleanParameter == True:

            fig \
                .legend \
                    (legendLinePlotList, 
                     legendLineNamesList, 
                     loc \
                         = 'center right',
                     fontsize \
                         = '14',
                     bbox_to_anchor \
                         = (legendXOffsetFloatParameter, 
                            legendYOffsetFloatParameter))

        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
        
        plt \
            .show()
            
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayStackedSubplots, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to create stacked subplots.')


# In[12]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplaySummaryStatisticsBoxPlot
 #
 #  Subroutine Description:
 #      This subroutine receives a DataFrame and column name and plots a horizontal
 #      box plot based on the information.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          boxPlotDataFrameParameter
 #                          This parameter is the input DataFrame
 #  Series
 #          columnNameStringParameter
 #                          This parameter is the input Series used as y-axis 
 #                          values.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/  
            
def DisplaySummaryStatisticsBoxPlot \
        (boxPlotDataFrameParameter, \
         columnNameStringParameter, \
         captionStringParameter):
    
    try:
        
        boxPlotDataFrame \
            = boxPlotDataFrameParameter.copy()
        
        boxPlotAxes \
            = boxPlotDataFrame \
                .boxplot \
                    (by \
                         ='Industry', \
                     column \
                         = [columnNameStringParameter], 
                     fontsize \
                         = 14,
                     rot \
                         = 0.0,
                     grid \
                         = True,
                     figsize \
                         = (9.708, 6),
                     vert \
                         = False,
                     widths \
                         = 0.7,
                     meanline \
                         = True,
                     showmeans \
                         = True)
        
        plt \
            .suptitle \
                (captionStringParameter, 
                 fontsize \
                     = 20, 
                 y \
                    = 1.01)
        
        plt \
            .title \
                (columnNameStringParameter, 
                 fontsize \
                     = 16)
    
        plt \
            .xlabel \
                ('',
                 fontsize \
                    = 16)
    
        plt \
            .ylabel \
                ('',
                 fontsize \
                    = 16)
    
        boxPlotAxes \
            .get_figure() \
            .gca() \
            .set_xlabel \
                ('',
                 fontsize \
                    = 16)
        
        plt \
            .xticks \
                (fontsize \
                     = 14)
       
        plt \
            .yticks \
                (fontsize \
                     = 14)
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
    
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplaySummaryStatisticsBoxPlot, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to create a horizontal box plot.')


# In[13]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayOneLineGraphFromSeries
 #
 #  Subroutine Description:
 #      This subroutine displays a one line graph based on an input Series 
 #      and formatting parameters.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the input Series
 #  String
 #          colorStringParameter
 #                          This parameter specifies the color of the line.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  String
 #          xLabelStringParameter
 #                          This parameter is the x-axis label.
 #  String
 #          yLabelStringParameter
 #                          This parameter is the y-axis label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/22/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 

def DisplayOneLineGraphFromSeries \
    (inputSeriesParameter,
     colorStringParameter,
     captionStringParameter,
     xLabelStringParameter,
     yLabelStringParameter):
    
    try:
    
        inputSeries \
            = inputSeriesParameter.copy()
    
        inputSeries \
            .plot \
                (kind \
                     = 'line', 
                 color \
                     = colorStringParameter, 
                 grid \
                     = True, 
                 legend \
                     = False, 
                 fontsize \
                     = 12,
                 rot \
                    = 90.0,
                 figsize \
                    = (9.708, 6))

        plt \
            .suptitle \
                (captionStringParameter, 
                 fontsize \
                    = 20, 
                 y \
                    = 1.0)
    
        plt \
            .xlabel \
                (xLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            16, 
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 10)
    
        plt \
            .ylabel \
                (yLabelStringParameter, \
                 fontdict \
                     = {'fontsize': 
                            16, 
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 0)
        
        plt \
            .xticks \
                (fontsize \
                     = 14)
       
        plt \
            .yticks \
                (fontsize \
                     = 14)
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
    
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayOneLineGraphFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to create a one line graph.')


# In[14]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayLinesGraph
 #
 #  Subroutine Description:
 #      This subroutine displays a multiple line graph based on an input Dictionary
 #      and formatting parameters.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary
 #          frameDictionaryParameter
 #                          This parameter is the input Series as a Dictionary.
 #  List of Strings
 #          colorListParameter
 #                          This parameter is a List of colors for the lines.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  String
 #          xLabelStringParameter
 #                          This optional parameter is the x-axis label.
 #  String
 #          yLabelStringParameter
 #                          This optional parameter is the y-axis label.
 #  Integer
 #          rotationIntegerParameter
 #                          This optional parameter is the angle of rotation
 #                          for the x-axis tick labels.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  08/22/2023          Initial Development                         N. James George
 #  09/30/2023          Fixed misspelled parameter causing problem  N. James George
 #
 #******************************************************************************************/ 

def DisplayLinesGraph \
        (frameDictionaryParameter,
         colorListParameter,
         captionStringParameter,
         xLabelStringParameter = '',
         yLabelStringParameter = '',
         rotationIntegerParameter = 0.0):
        
    try:

        lineDataFrame \
            = pd \
                .DataFrame \
                    (frameDictionaryParameter)
    
        lineDataFrame \
            .plot \
                (kind \
                     = 'line',
                 grid \
                     = True, 
                 legend \
                     = True, 
                 fontsize \
                     = 14,
                 rot \
                     = 90.0,
                 color \
                     = colorListParameter,
                 figsize \
                    = (9.708, 6))

        plt \
            .suptitle \
                (captionStringParameter, 
                 fontsize \
                    = 20, 
                 y \
                    = 0.99)

        plt.xlabel \
            (xLabelStringParameter,
             fontdict = {'fontsize': 16, 
                         'fontstyle': 'normal'},
             labelpad = 10)

        plt \
            .ylabel \
                (yLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            16, 
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 0)

        plt \
            .xticks \
                (fontsize \
                     = 14)

        plt \
            .yticks \
                (fontsize \
                     = 14)

        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)

        plt \
            .show()

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayLinesGraph, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to create a line graph.')


# In[15]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplaySeriesCountAndRedundancies
 #
 #  Subroutine Description:
 #      This subroutine displays a multiple line graph based on an input Dictionary
 #      and formatting parameters.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the input Series.
 #  String
 #          whatIsItStringParameter
 #                          This parameter is the what the Series holds.
 #  String
 #          whereIsItStringParameter
 #                          This parameter is where the values came from.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/23/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 

def DisplaySeriesCountAndRedundancies \
        (inputSeriesParameter,
         whatIsItStringParameter,
         whereIsItStringParameter):
    
    numberOfTickersIntegerVariable \
        = inputSeriesParameter.count()

    numberOfRedundanciesIntegerVariable \
        = function \
            .ReturnNumberOfRedundanciesInSeries \
                (inputSeriesParameter)

    log_subroutine \
        .PrintAndLogWriteText \
            (f'There are now {numberOfTickersIntegerVariable} '
             + f'{whatIsItStringParameter} '
             + f'with {numberOfRedundanciesIntegerVariable} '
             + f'redundancies in {whereIsItStringParameter}.')


# In[16]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayLinesGraph
 #
 #  Subroutine Description:
 #      This subroutine displays a multi-line graph.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary
 #          frameDictionaryParameter
 #                          This parameter is the input Series as a Dictionary.
 #  String
 #          figureTitleStringParameter
 #                          This parameter is the figure title.
 #  String
 #          figureXLabelStringParameter
 #                          This parameter is the figure x-axis label.
 #  String
 #          figureYLabelStringParameter
 #                          This parameter is the figure y-axis label.
 #  Integer
 #          numberOfBinsIntegerParameter
 #                          This optional parameter is the number of bins
 #                          for the histogram.
 #  Float
 #          alphaFloatParameter
 #                          This parameter is the alpha value (transparency level)
 #                          of the histogram bars.
 #  List of Strings
 #          colorListParameter
 #                          This parameter is a List of colors for the four histograms.
 #  Tuple of Integers
 #          figSizeTupleOfIntegersParamete
 #                          This parameter is the length and width of the figure.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/24/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 

def DisplayTwoByTwoHistograms \
        (frameDictionaryParameter,
         figureTitleStringParameter \
             = '',
         figureXLabelStringParameter \
             = '',
         figureYLabelStringParameter \
             = '',
         numberOfBinsIntegerParameter \
             = 10,
         alphaFloatParameter \
             = 0.8,
         colorListOfStringsParameter \
             = ['darkgreen', 
                'darkorange', 
                'darkblue', 
                'firebrick'],
         figSizeTupleOfIntegersParameter \
             = (9.708, 6)):

    try:

        inputDataFrame \
            = pd \
                .DataFrame \
                    (frameDictionaryParameter)

        fig, axs \
            = plt \
                .subplots \
                    (2, 2,
                     figsize \
                        = figSizeTupleOfIntegersParameter,
                     sharey \
                         = True, 
                     tight_layout \
                         = True)

        index \
            = 0

        for row in range(2):
            
            for column in range(2):
    
                inputDataFrame \
                    .hist \
                        (column \
                             = inputDataFrame.keys()[index], 
                         ax \
                             = axs \
                                 [row, column], 
                         bins \
                             = numberOfBinsIntegerParameter, 
                         alpha \
                             = alphaFloatParameter, 
                         color \
                             = colorListOfStringsParameter \
                                 [index])
                
                axs[row, column] \
                    .set_title \
                        (inputDataFrame.keys() \
                             [index],
                         fontsize \
                            = 14)
                
                axs[row, column] \
                    .tick_params \
                        (axis \
                             = 'x', 
                         labelsize \
                             = 12)
                
                axs[row, column] \
                    .tick_params \
                        (axis \
                             = 'y', 
                         labelsize \
                             = 12)
                
                index \
                    += 1

        fig \
            .suptitle \
                (figureTitleStringParameter,
                 fontsize \
                     = 20)

        fig \
            .supxlabel \
                (figureXLabelStringParameter,
                 fontsize \
                     = 16)

        fig \
            .supylabel \
                (figureYLabelStringParameter,
                 fontsize \
                     = 16)

        log_subroutine \
            .SavePlotImage \
                (figureTitleStringParameter)
        
        plt.show()

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayTwoByTwoHistograms, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {figureTitleStringParameter},\n'
                 + f'was unable to create a two-by-two set of four histograms.')


# In[17]:


#*******************************************************************************************
 #
 #  Subroutine Name:  WriteDataFrameToCSVFile
 #
 #  Subroutine Description:
 #      This subroutine receives a file path to a csv file as a parameter, 
 #      and write the DataFrame to the file.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrameParameter
 #                          This parameter is the input DataFrame.
 #  String or IOString
 #          filePathStringOrIOStringParameter
 #                          The parameter is name of the path to the csv file.
 #                          (i.e., './Resources/input.csv') or an IOString Object.
 #  String
 #          indexNameStringParameter
 #                          This parameter is the name of the index column.
 #  Boolean
 #          stringFlagBooleanParameter
 #                          This parameter indicates whether the first parameter
 #                          is a String variable or an IOString object.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/26/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def WriteDataFrameToCSVFile \
        (inputDataFrameParameter,
         filePathStringOrIOStringParameter,
         indexNameStringParameter
              = '',
         stringFlagBooleanParameter \
            = True):
    
    try:
        
        if stringFlagBooleanParameter == True:
            
            pathObject \
                = Path \
                    (filePathStringOrIOStringParameter)
            
        else:
            
            pathObject \
                = filePathStringOrIOStringParameter
        
        
        inputDataFrameParameter \
            .to_csv \
                (pathObject,
                    index_label \
                        = indexNameStringParameter)
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, WriteDataFrameToCSVFile, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to write a DataFrame to file path, '
                 + f'{filePathStringParameter}.')


# In[18]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayLinearRegressionLine
 #
 #  Subroutine Description:
 #      This subroutine receives two Series and the polynomial degree, calculates 
 #      the parameters of the linear regression line, and displays the results on
 #      the scatter plot and above it.
 #
 #
 #  Subroutine Parameters:
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
 #  Float
 #          xCoordinateFloatParameter
 #                          This parameter is the x-coordinate of the text 
 #                          in the chart.
 #  Float
 #          yCoordinateFloatParameter
 #                          This parameter is the y-coordinate of the text 
 #                          in the chart.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/20/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayLinearRegressionLine \
        (xSeriesParameter,
         ySeriesParameter,
         xCoordinateFloatParameter,
         yCoordinateFloatParameter):
    
    try:
        
        xSeries \
            = xSeriesParameter.copy()
        
        ySeries \
            = ySeriesParameter.copy()
        
        (slope, 
         intercept, 
         rvalue, 
         pvalue, 
         stderr) \
            = stats \
                .linregress \
                    (xSeries, 
                     ySeries)

        linearRegressionSeries \
            = (xSeries * slope) + intercept
        
        plt \
            .plot \
                (xSeries,
                 linearRegressionSeries,
                 color \
                     = 'red',
                 linewidth \
                     = 3.0,
                 alpha \
                     = 1.0)
        
        linearEquationStringVariable \
            = 'y = ' + str( round( slope, 4 ) ) + 'x + ' + str( round( intercept, 4 ) )
        
        plt \
            .annotate \
                (linearEquationStringVariable,
                 (xCoordinateFloatParameter, yCoordinateFloatParameter),
                  fontsize \
                     = 16,
                  fontweight \
                     = 'bold',
                  color \
                     = 'blue')   
        
        rSquaredFloatVariable \
            = rvalue*rvalue
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('r-value:     {:.4f}'.format(rvalue))
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('r-squared:   {:.4f}\n'.format(rSquaredFloatVariable))
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayLinearRegressionLine, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'was unable to calculate and display a linear regression line.')


# In[19]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayTwoPieChartsSideBySide
 #
 #  Subroutine Description:
 #      This subroutine receives a Frame Dictionary with two Series and formatting 
 #      parameters and plots a pie chart using the Pandas DataFrame.plot() method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary
 #          frameDictionaryParameter
 #                          This parameter is the Dictionary used as input.
 #  List
 #          colorsListParameter
 #                          This parameter is the list of bar colors.
 #  List
 #          explodeTupleParameter
 #                          This parameter specifies the fraction of the 
 #                          radius with which to offset each wedge.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  Float
 #          startAngleFloatParameter
 #                          This parameter is the angle by which the start 
 #                          of the pie is rotated, counterclockwise from 
 #                          the x-axis.
 #  Float
 #          autoPercentStringParameter
 #                          This parameter is the format of the wedge label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/28/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayTwoPieChartsSideBySide \
        (frameDictionaryParameter, 
         colorsListParameter,
         explodeTupleParameter,
         captionStringParameter,
         startAngleFloatParameter \
            = 45.0,
         autoPercentStringParameter \
            = '%1.1f%%',
         supTitleYOffsetFloatParameter \
            = 0.82):

    try:
        
        inputDataFrame \
            = pd \
                .DataFrame \
                    (frameDictionaryParameter)

        fig, axs \
            = plt \
                .subplots \
                    (1, 2,
                     figsize \
                        = (9.708, 6))
        
        
        fig \
            .suptitle \
                (captionStringParameter, 
                 y \
                     = supTitleYOffsetFloatParameter, 
                 fontsize \
                     = 20)

        for columnIndex in range(2):
    
            inputDataFrame \
                .iloc[:,columnIndex]  \
                .plot \
                .pie \
                    (ax \
                        = axs \
                            [columnIndex], 
                     colors \
                        = colorsListParameter, 
                     explode \
                        = explodeTupleParameter, 
                     shadow \
                        = True, 
                     startangle \
                        = startAngleFloatParameter, 
                     autopct \
                        = autoPercentStringParameter,
                     legend \
                        = False,
                     labeldistance \
                        = 1.2,
                     pctdistance \
                        = 0.75,
                     ylabel \
                        = '')
        
            axs \
                [columnIndex] \
                    .set_title \
                        (inputDataFrame \
                             .iloc \
                                 [:, columnIndex].name, 
                         fontsize \
                             = 16)

        plt \
            .subplots_adjust \
                (wspace \
                     = 1.1, 
                 hspace \
                     = None)
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)

        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayTwoPieChartsSideBySide, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'was unable to calculate and display two pie charts side-by-side\n'
                 + f'for the caption, {captionStringParameter}.')


# In[20]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayStackedBarChartFromDataFrame
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters 
 #      and plots a bar chart using the Pandas DataFrame.plot() 
 #      method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputSeriesParameter
 #                          This parameter is the Series used as input.
 #  List
 #          barColorsListParameter
 #                          This parameter is the list of bar colors.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  String
 #          yLabelStringParameter
 #                          This parameter is the y-axis label.
 #  String
 #          edgeColorStringParameter
 #                          This parameter is the bar edge color.
 #  Float
 #          lineWidthFloatParameter
 #                          This parameter is the bar edge line width.
 #  Float
 #          alphaFloatParameter
 #                          This parameter is the transparency value
 #                          for the bars (0.0-1.0).
 #  Float
 #          widthFloatParameter
 #                          This parameter is the width of a bar.
 #  Float
 #          axisTickLabelRotationFloatParameter
 #                          This parameter is the rotation of the x-axis 
 #                          tick labels.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/03/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayStackedBarChartFromDataFrame \
        (inputDataFrameParameter,
         captionStringParameter, 
         xLabelStringParameter \
             = '',
         yLabelStringParameter \
             = '',
         barColorsListParameter \
             = ['darkgreen', 
                'steelblue',
                'purple',
                'firebrick'],
         edgeColorStringParameter \
            = 'black',
         lineWidthFloatParameter \
            = 1.5,
         alphaFloatParameter \
            = 1.0,
         widthFloatParameter \
            = 0.5,
         axisTickLabelRotationFloatParameter \
            = 90.0):
    
    try:
        
        inputDataFrame \
            = inputDataFrameParameter.copy()
        
        inputDataFrame \
            .plot \
            .bar \
                (stacked \
                     = True,
                 align \
                     = 'center',
                 color \
                     = barColorsListParameter,
                 edgecolor \
                     = edgeColorStringParameter,
                 linewidth \
                     = lineWidthFloatParameter,
                 alpha \
                     = alphaFloatParameter,
                 width \
                     = widthFloatParameter, 
                 rot \
                     = axisTickLabelRotationFloatParameter,
                 legend \
                     = True,
                 figsize \
                    = (9.708, 6))
        
        plt \
            .legend \
                (bbox_to_anchor \
                     = (1.1, 
                        1.05))

        plt \
            .title \
                (captionStringParameter,
                 fontdict \
                     = {'fontsize': 
                            20, 
                        'fontstyle': 
                            'normal'},
                 pad \
                     = 20)

        plt \
            .xlabel \
                (xLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            16,
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 10)

        plt \
            .ylabel \
                (yLabelStringParameter,
                 fontdict \
                    = {'fontsize': 
                            16,
                       'fontstyle': 
                            'normal'},
                 labelpad \
                     = 10)
        
        plt \
            .xticks \
                (fontsize \
                     = 14)
       
        plt \
            .yticks \
                (fontsize \
                     = 14)
       
        plt \
            .grid \
                (axis \
                    = "y")
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
      
        plt \
            .show()
     
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayPandasBarChartFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a bar chart using Pandas.')


# In[21]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayHistogramFromSeries
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters and displays
 #      a histogram.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List of Series
 #          inputSeriesListParameter
 #                          This parameter holds the input Series.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  String
 #          xLabelStringParameter
 #                          This parameter is the x-axis label. 
 #  String
 #          yLabelStringParameter
 #                          This parameter is the y-axis label.
 #  Integer
 #          binsIntegerParameter
 #                          This parameter is the number of bins
 #                          for the histogram.
 #  Float
 #          alphaFloatParameter
 #                          This parameter is the transparency value
 #                          for the bars (0.0-1.0).
 #  String
 #          colorStringParameter
 #                          This parameter specifies the color of the histogram bars.
 #  Float
 #          lineWidthFloatParameter
 #                          This parameter is the bar edge line width.
 #  String
 #          edgeColorStringParameter
 #                          This parameter is the bar edge color.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/06/2023          Initial Development                         N. James George
 #  09/28/2023          Added parameters, figureWidthFloat and figureHeightFloat
 #                                                                  N. James George
 #
 #******************************************************************************************/

def DisplayHistogramFromSeries \
        (inputSeriesParameter,
         captionStringParameter,
         xLabelStringParameter,
         yLabelStringParameter,
         binsIntegerParameter \
             = 20,
         alphaFloatParameter \
             = 1.0,
         colorStringParameter \
             = 'red',
         lineWidthFloatParameter \
            = 1.5,
         edgeColorStringParameter \
            = 'black',
         figureWidthFloat \
             = 9.708,
         figureHeightFloat \
             = 6.0):
    
    try:
        
        inputSeries \
            = inputSeriesParameter.copy()
    
        inputSeries \
            .plot \
            .hist \
                (bins \
                     = binsIntegerParameter, 
                 alpha \
                     = alphaFloatParameter, 
                 color \
                     = colorStringParameter, 
                 linewidth \
                     = lineWidthFloatParameter, 
                 edgecolor \
                     = edgeColorStringParameter, 
                 legend \
                     = False,
                 figsize \
                    = (figureWidthFloat, 
                       figureHeightFloat))

        plt \
            .title \
                (captionStringParameter,
                 fontdict \
                     = {'fontsize': 
                            20, 
                        'fontstyle': 
                            'normal'},
                 pad \
                     = 20)
        
        plt \
            .xlabel \
                (xLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            16,
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 10)

        plt \
            .ylabel \
                (yLabelStringParameter,
                 fontdict \
                    = {'fontsize': 
                            16,
                       'fontstyle': 
                            'normal'},
                 labelpad \
                     = 10)
        
        plt \
            .xticks \
                (fontsize \
                     = 14)
       
        plt \
            .yticks \
                (fontsize \
                     = 14)
       
        plt \
            .grid \
                (axis \
                    = 'x')
        
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)
      
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayHistogramFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionStringParameter},\n'
                 + f'was unable to plot a histogram from a Series.')


# In[22]:


#*******************************************************************************************
 #
 #  Subroutine Name:  ReturnPlotFromXYSeries
 #
 #  Subroutine Description:
 #      This subroutine plot two series and any peaks that are passed to it.
 #
 #
 #  Subroutine Parameters:
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
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  String
 #          xLabelStringParameter
 #                          This parameter is the label for the x-axis.
 #  String
 #          yLabelStringParameter
 #                          This parameter is the label for the y-axis.
 #  String
 #          colorStringListParameter
 #                          This parameter is the list of colors for the line 
 #                          and peak markers, and peak labels.
 #  Numpy Array
 #          peaksNumpyArrayParameter
 #                          This parameter is the array of peak indexes for the plot.
 #  Float
 #          labelYOffsetFloat
 #                          This parameter is y coordinate offset for the peak label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/13/2023          Initial Development                         N. James George
 #  09/23/2023          Added parameter, labelYOffsetFloat          N. James George
 #                      and renamed subroutine
 #
 #******************************************************************************************/

def DisplayPlotFromXYSeries \
    (xSeriesParameter,
     ySeriesParameter,
     captionStringParameter,
     xLabelStringParameter,
     yLabelStringParameter,
     colorStringListParameter,
     peaksNumpyArrayParameter \
        = [],
     labelYOffsetFloat \
        = 0.0):
    
    try:
        
        xSeries \
            = xSeriesParameter.copy()
       
        ySeries \
            = ySeriesParameter.copy()

        plt \
            .figure \
                (figsize \
                    = (9.708, 6))
        
        plt \
            .plot \
                (xSeries,
                 ySeries,
                 alpha \
                    = 1.0,
                 color \
                    = colorStringListParameter[0])

        if len(peaksNumpyArrayParameter) > 0:

            plt \
                .plot \
                    (xSeries[peaksNumpyArrayParameter], 
                     ySeries[peaksNumpyArrayParameter], 
                     'x', 
                      markersize \
                         = 15, 
                      color \
                         = colorStringListParameter[1])

            for i, j in zip(xSeries[peaksNumpyArrayParameter], ySeries[peaksNumpyArrayParameter]):
                
                yCoordinateFloat \
                    = j+labelYOffsetFloat
                
                plt \
                    .annotate \
                        (i, 
                         xy \
                             = (i, 
                                yCoordinateFloat), 
                         size \
                             = 12, 
                         color \
                             = colorStringListParameter[2])

        plt \
            .title \
                (captionStringParameter,
                 fontdict \
                     = {'fontsize': 
                            20, 
                        'fontstyle': 
                            'normal'},
                 pad \
                    = 20)

        plt \
            .xlabel \
                (xLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            16,
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 10)

        plt \
            .ylabel \
                (yLabelStringParameter,
                 fontdict \
                     = {'fontsize': 
                            16,
                        'fontstyle': 
                            'normal'},
                 labelpad \
                     = 10)
        
        plt \
            .xticks \
                (fontsize \
                     = 14)
       
        plt \
            .yticks \
                (fontsize \
                     = 14)

        plt \
            .grid()
        
    
        log_subroutine \
            .SavePlotImage \
                (captionStringParameter)

        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The function, DisplayPlotFromXYSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, '
                 + f'was unable to display a plot from XY Series.')


# In[23]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayPieChartFromXYLists
 #
 #  Subroutine Description:
 #      This subroutine takes a list for values and a list for labels 
 #      with formatting parameters and plots a pie chart.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List
 #          valueList
 #                          This parameter is the list of values for the pie chart.
 #  List
 #          labelList
 #                          This parameter is the list of labels for the pie chart.
 #  List
 #          colorsList
 #                          This parameter is the list of pie wedge colors.
 #  Tuple or Float
 #          explodeTuple
 #                          This parameter specifies the fraction of the radius
 #                          with which to offset each wedge.
 #  String
 #          captionString
 #                          This parameter is the chart title.
 #  String
 #          xLabelString
 #                          This parameter is the x-axis title.
 #  String
 #          yLabelString
 #                          This parameter is the y-axis title.
 #  Float
 #          startAngleFloat
 #                          This parameter is the angle by which the start 
 #                          of the pie is rotated, counterclockwise from 
 #                          the x-axis.
 #  String
 #          autoPercentString
 #                          This parameter is the format of the wedge label.
 #  Float
 #          percentDistanceFloat
 #                          This parameter is the percent distance from the center 
 #                          for wedge value labels.
 #  Float
 #          labelDistanceFloat
 #                          This parameter is the percent distance from the center 
 #                          for wedge labels.
 #  Float
 #          chartFontSize
 #                          This parameter is the chart font size.
 #  Float
 #          titleFontSize
 #                          This parameter is the chart title font size.
 #  Float
 #          labelFontSize
 #                          This parameter is the chart axis font size.
 #  Float
 #          titlePad
 #                          This parameter is the title padding from the chart.
 #  Float
 #          labelPad
 #                          This parameter is the axis label padding from the chart.
 #  
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/15/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayPieChartFromXYLists \
        (valueList,
         labelList,
         colorsList,
         explodeTuple,
         captionString \
             = '',
         xLabelString \
             = '',
         yLabelString \
             = '',
         startAngleFloat \
            = 0.0,
         autoPercentString \
            = '%1.1f%%',
         percentDistanceFloat \
            = 2.0/3.0,
         labelDistanceFloat \
            = 1.1,
         chartFontSizeFloat \
             = 14,
         titleFontSizeFloat \
            = 20,
         labelFontSizeFloat \
            = 16,
         titlePadFloat \
            = 5,
         labelPadFloat \
            = 10):
    
    try:

        inputSeries \
            = pd \
                .Series \
                    (valueList,
                     index \
                         = labelList)
        
        plt \
            .figure \
                (figsize \
                     = (9.708, 6))
        
        plt \
            .pie \
                (inputSeries,
                 labels \
                     = inputSeries.index, 
                 colors \
                     = colorsList,        
                 explode \
                     = explodeTuple, 
                 shadow \
                     = True,
                 pctdistance \
                     = percentDistanceFloat,
                 labeldistance \
                     = labelDistanceFloat,
                 startangle \
                     = startAngleFloat,
                 autopct \
                     = autoPercentString,
                 textprops \
                     = {'fontsize':
                           chartFontSizeFloat})
        
        plt \
            .title \
                (captionString,
                 fontdict \
                     = {'fontsize': 
                            titleFontSizeFloat, 
                        'fontstyle': 
                            'normal'},
                 pad \
                    = titlePadFloat)
        
        plt \
            .xlabel \
                (xLabelString,
                 fontdict \
                     = {'fontsize': 
                            labelFontSizeFloat,
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = labelPadFloat)

        plt \
            .ylabel \
                (yLabelString,
                 fontdict \
                     = {'fontsize': 
                            labelFontSizeFloat,
                        'fontstyle': 
                            'normal'},
                 labelpad \
                     = labelPadFloat)
        
        log_subroutine \
            .SavePlotImage \
                (captionString)
        
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayMatplotlibPieChartFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionString},\n'
                 + f'was unable to plot a pie chart using Matplotlib.')


# In[24]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayHorizontalBarChartFromXYLists
 #
 #  Subroutine Description:
 #      This subroutine receives a Series and formatting parameters 
 #      and plots a bar chart using the Matplotlib pyplot method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  List
 #          valueList
 #                          This parameter is the list of values for the horizontal 
 #                          bar chart.
 #  List
 #          labelList
 #                          This parameter is the list of labels for the horizontal 
 #                          bar chart.
 #  List
 #          barColorsList
 #                          This parameter is the list of bar colors.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  String
 #          xLabelString
 #                          This parameter is the x-axis title.
 #  String
 #          yLabelString
 #                          This parameter is the y-axis title.
 #  String
 #          edgeColorString
 #                          This parameter is the bar edge color.
 #  Float
 #          edgeLineWidthFloat
 #                          This parameter is the bar edge line width.
 #  Float
 #          barHeightFloat
 #                          This parameter is the width of a bar.
 #  Float
 #          alphaFloat
 #                          This parameter is the transparency value
 #                          for the bars (0.0-1.0).
 #  Float
 #          xAxisTickLabelRotationFloatParameter
 #                          This parameter is the rotation of the x-axis 
 #                          tick labels.
 #  Float
 #          yAxisTickLabelRotationFloatParameter
 #                          This parameter is the rotation of the y-axis 
 #                          tick labels.
 #  Float
 #          chartFontSize
 #                          This parameter is the chart font size.
 #  Float
 #          titleFontSize
 #                          This parameter is the chart title font size.
 #  Float
 #          labelFontSize
 #                          This parameter is the chart axis font size.
 #  Float
 #          titlePad
 #                          This parameter is the title padding from the chart.
 #  Float
 #          labelPad
 #                          This parameter is the axis label padding from the chart.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/15/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayHorizontalBarChartFromXYLists \
        (valueList,
         labelList,
         barColorsList \
             = 'steelblue',
         captionString \
             = '',
         xLabelString \
             = '',
         yLabelString \
             = '',
         edgeColorString \
            = 'black',
         edgeLineWidthFloat \
            = 1.75,
         barHeightFloat \
            = 0.5,
         alphaFloat \
            = 1.0,
         xAxisTickLabelRotationFloat \
            = 0.0,
         yAxisTickLabelRotationFloat \
            = 0.0,
         chartFontSizeFloat \
             = 14,
         titleFontSizeFloat \
            = 20,
         labelFontSizeFloat \
            = 16,
         titlePadFloat \
            = 20,
         labelPadFloat \
            = 10):         
    
    try:
             
        plt \
            .figure \
                (figsize \
                     = (9.708, 6))

        plt \
            .barh \
                (labelList,
                 valueList,
                 height \
                     = barHeightFloat,
                 align \
                     = 'center',
                 color \
                     = barColorsList,
                 edgecolor \
                     = edgeColorString,
                 linewidth \
                     = edgeLineWidthFloat,
                 alpha \
                     = alphaFloat)
       
        plt \
            .title \
                (captionString,
                 fontdict \
                     = {'fontsize': 
                            titleFontSizeFloat, 
                        'fontstyle': 
                            'normal'},
                 pad \
                    = titlePadFloat)

        plt \
            .xlabel \
                (xLabelString,
                 fontdict \
                     = {'fontsize': 
                            labelFontSizeFloat, 
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = labelPadFloat)
        
        plt \
            .ylabel \
                (yLabelString,
                 fontdict \
                    = {'fontsize': 
                            labelFontSizeFloat, 
                       'fontstyle': 
                            'normal'},
                 labelpad \
                    = labelPadFloat)
        
        plt \
            .xticks \
                (rotation \
                     = xAxisTickLabelRotationFloat,
                 fontsize \
                     = chartFontSizeFloat)
        
        plt \
            .yticks \
                (rotation \
                     = yAxisTickLabelRotationFloat,
                 fontsize \
                     = chartFontSizeFloat)

        plt \
            .grid \
                (axis \
                    = 'x')
        
        
        log_subroutine \
            .SavePlotImage \
                (captionString)
        
        plt \
            .show()

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayHorizontalBarChartFromXYLists, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionString},\n'
                 + f'was unable to plot a horizontal bar chart using Matplotlib.')


# In[25]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayTwoScatterPlotsSideBySide
 #
 #  Subroutine Description:
 #      This subroutine receives a Frame Dictionary with two Series and formatting 
 #      parameters and plots a pie chart using the Pandas DataFrame.plot() method.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Dictionary
 #          frameDictionaryParameter
 #                          This parameter is the Dictionary used as input.
 #  List
 #          colorsListParameter
 #                          This parameter is the list of bar colors.
 #  List
 #          explodeTupleParameter
 #                          This parameter specifies the fraction of the 
 #                          radius with which to offset each wedge.
 #  String
 #          captionStringParameter
 #                          This parameter is the chart title.
 #  Float
 #          startAngleFloatParameter
 #                          This parameter is the angle by which the start 
 #                          of the pie is rotated, counterclockwise from 
 #                          the x-axis.
 #  Float
 #          autoPercentStringParameter
 #                          This parameter is the format of the wedge label.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  8/28/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayTwoScatterPlotsSideBySide \
        (xSeriesList,
         ySeriesList,
         titleStringList,
         captionString \
             = '',
         xLabelString \
             = '',
         yLabelString \
             = '',
         polynomialDegreeInteger \
             = 0,
         equationXCoordinateFloatList \
            = [],
         equationYCoordinateFloatList \
            = []):

    try:
        
        plt \
            .subplots \
                (figsize \
                     = (15, 5.5181))

        plt \
            .clf()

        for index in range(2):
    
            plt \
                .subplot \
                    (1, 2, index+1)
    
            plt \
                .scatter \
                    (xSeriesList \
                         [index], 
                     ySeriesList \
                         [index], 
                     marker \
                        = 'o',
                     s \
                        = 80,
                     color 
                        = 'lime', 
                     linewidth \
                        = 1.5,
                     edgecolors \
                        = 'black',
                     alpha \
                        = 0.8)
    
            plt \
                .title \
                    (titleStringList \
                         [index], 
                     fontdict \
                        = {'fontsize': 
                                20, 
                           'fontstyle': 
                                'normal'},
                     pad \
                        = 10)
    
            plt \
                .xlabel \
                    (xLabelString,
                     fontdict \
                        = {'fontsize': 
                                16, 
                           'fontstyle': 
                                'normal'},
                     labelpad \
                        = 10)

            plt \
                .ylabel \
                    (yLabelString,
                     fontdict \
                        = {'fontsize': 
                                16, 
                           'fontstyle': 
                                'normal'},
                     labelpad \
                        = 10)
    
            plt \
                .xticks \
                    (fontsize \
                        = 14)
       
            plt \
                .yticks \
                    (fontsize \
                        = 14)
    
            plt \
                .grid()
    
            if polynomialDegreeInteger == 1:
                
                DisplayLinearRegressionLine \
                    (xSeriesList \
                         [index],
                     ySeriesList \
                         [index],
                     equationXCoordinateFloatList \
                         [index],
                     equationYCoordinateFloatList \
                         [index])
            
            elif polynomialDegreeInteger > 1:
        
                DisplayRegressionLine \
                    (xSeries,
                     ySeries,
                     polynomialDegreeInteger,
                     equationXCoordinateFloatList[index],
                     equationYCoordinateFloatList[index])

            plt \
                .tight_layout \
                    (pad \
                         = 3.0)
    
        plt \
            .suptitle \
                (captionString, 
                 fontsize \
                    = 20.0, 
                 y \
                    = 1.0)

        log_subroutine \
            .SavePlotImage \
                (captionString)

        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayTwoScatterPlotsSideBySide, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'was unable to display two scatter charts side-by-side\n'
                 + f'for the caption, {captionString}.')


# In[26]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayPlotFromDataFrame
 #
 #  Subroutine Description:
 #      This subroutine receives a DataFrame and formatting parameters 
 #      and plots it.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame
 #          inputDataFrame
 #                          This parameter is the input DataFrame for the subroutine.
 #                          bar chart.
 #  String
 #          colorString
 #                          This parameter is the color of the plot.
 #  String
 #          captionString
 #                          This parameter is the chart title.
 #  String
 #          xLabelString
 #                          This parameter is the x-axis title.
 #  String
 #          yLabelString
 #                          This parameter is the y-axis title.
 #  Float
 #          alphaFloat
 #                          This parameter is the transparency value
 #                          for the bars (0.0-1.0).
 #  Float
 #          xAxisTickLabelRotationFloat
 #                          This parameter is the rotation of the x-axis 
 #                          tick labels.
 #  Float
 #          yAxisTickLabelRotationFloat
 #                          This parameter is the rotation of the y-axis 
 #                          tick labels.
 #  Float
 #          titleFontSizeFloat
 #                          This parameter is the chart title font size.
 #  Float
 #          labelFontSizeFloat
 #                          This parameter is the chart axis font size.
 #  Float
 #          tickFontSizeFloat
 #                          This parameter is the font size for x and y axis ticks.
 #  Float
 #          titlePadFloat
 #                          This parameter is the title padding from the chart.
 #  Float
 #          labelPadFloat
 #                          This parameter is the axis label padding from the chart.
 #  Float
 #          figureWidthFloat
 #                          This parameter is the figure width.
 #  Float
 #          figureHeightFloat
 #                          This parameter is the figure height.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/17/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/

def DisplayPlotFromDataFrame \
        (inputDataFrame,
         colorString \
            = 'steelblue',
         captionString \
            = '',
         xLabelString \
            = '',
         yLabelString \
            = '',
         alphaFloat \
            = 1.0,
         xAxisTickLabelRotationFloat \
            = 90.0,
         yAxisTickLabelRotationFloat \
            = 0.0,
         titleFontSizeFloat \
            = 20.0,
         labelFontSizeFloat \
            = 16.0,
         tickFontSize \
            = 14.0,
         titlePadFloat \
            = 20.0,
         labelPadFloat \
            = 10.0,
         figureWidthFloat \
             = 9.708132,
         figureHeightFloat \
             = 6.0):
    
    try:
        
        plt \
            .figure \
                (figsize \
                    = (9.708132, 6.0))

        plt \
            .clf()

        inputDataFrame \
            .plot \
                (color \
                     = colorString,
                 alpha \
                     = alphaFloat,
                 legend \
                     = False)

        plt \
            .title \
                (captionString,
                 fontdict \
                    = {'fontsize': 
                            titleFontSizeFloat, 
                       'fontstyle': 
                            'normal'},
                 pad \
                    = titlePadFloat)
        
        plt \
            .xlabel \
                (xLabelString,
                 fontdict \
                    = {'fontsize': 
                            labelFontSizeFloat,
                       'fontstyle': 
                            'normal'},
                 labelpad \
                    = labelPadFloat)

        plt \
            .ylabel \
                (yLabelString,
                 fontdict \
                    = {'fontsize': 
                            labelFontSizeFloat,
                       'fontstyle': 
                            'normal'},
                 labelpad \
                    = labelPadFloat)
        
        plt \
            .xticks \
                (fontsize \
                    = tickFontSize,
                 rotation \
                    = xAxisTickLabelRotationFloat)
       
        plt \
            .yticks \
                (fontsize \
                    = tickFontSize,
                 rotation \
                    = yAxisTickLabelRotationFloat)
    
        plt \
            .grid \
                (axis \
                    = 'x')

        log_subroutine \
            .SavePlotImage \
                (captionString)

        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayPlotFromDataFrame, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'was unable to display a plot from a DataFrame\n'
                 + f'for the caption, {captionString}.')


# In[27]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayMultiLineGraphFromDataFrame
 #
 #  Subroutine Description:
 #      This subroutine displays a multi-line graph based on an input DataFrame
 #      and formatting parameters.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  Series
 #          inputDataFrame
 #                          This parameter is the input DataFrame
 #  String
 #          colorStringObject
 #                          This parameter specifies the colors of the lines.
 #  String
 #          captionString
 #                          This parameter is the chart title.
 #  Boolean
 #          legendFlagBoolean
 #                          This parameter indicates whether there is a legennd or not.
 #  Integer
 #          markerSizeInteger
 #                          This parameter is the line marker size.
 #  Float
 #          legendXCoordinateFloat
 #                          This parameter is the legend's x-coordinate from the
 #                          lower left corner of the chart.
 #  Float
 #          legendYCoordinateFloat
 #                          This parameter is the legend's y-coordinate from the
 #                          lower left corner of the chart.
 #  Integer List
 #          yLimitIntegerList
 #                          This parameter is the plot's y-axis limits.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/29/2023           Initial Development                         N. James George
 #
 #******************************************************************************************/ 

def DisplayMultiLineGraphFromDataFrame \
    (inputDataFrame,
     colorStringObject,
     captionString,
     xLabelString,
     yLabelString,
     legendFlagBoolean \
        = False,
     markerSizeInteger \
        = 40,
     legendXCoordinateFloat \
        = 0.0,
     legendYCoordinateFloat \
        = 0.0,
     yLimitIntegerList \
        = []):
    
    try:
    
        inputDataFrame \
            .plot \
                (kind \
                     = 'line', 
                 color \
                     = colorStringObject, 
                 grid \
                     = True, 
                 legend \
                     = legendFlagBoolean,
                 marker \
                     = 'o',
                 markerfacecolor \
                     = 'red',
                 markeredgecolor \
                     = 'black',
                 markersize \
                     = markerSizeInteger,
                 fontsize \
                     = 12,
                 rot \
                    = 90.0,
                 figsize \
                    = (9.708, 6))
        
        if legendFlagBoolean == True:
        
            plt \
                .legend \
                    (loc \
                         = 'center right', 
                     bbox_to_anchor \
                         = (legendXCoordinateFloat,
                            legendYCoordinateFloat))

        plt \
            .suptitle \
                (captionString, 
                 fontsize \
                    = 20, 
                 y \
                    = 1.0)
    
        plt \
            .xlabel \
                (xLabelString,
                 fontdict \
                     = {'fontsize': 
                            16, 
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 10)
    
        plt \
            .ylabel \
                (yLabelString, \
                 fontdict \
                     = {'fontsize': 
                            16, 
                        'fontstyle': 
                            'normal'},
                 labelpad \
                    = 0)
        
        plt \
            .xticks \
                (fontsize \
                     = 14)
       
        plt \
            .yticks \
                (fontsize \
                     = 14)
        
        if len(yLimitIntegerList) > 0:
            
            plt \
                .ylim \
                    (yLimitIntegerList[0], 
                     yLimitIntegerList[1])
        
        log_subroutine \
            .SavePlotImage \
                (captionString)
    
        plt \
            .show()
        
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayOneLineGraphFromSeries, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {captionString},\n'
                 + f'was unable to create a one line graph.')


# In[28]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayLinesGraph
 #
 #  Subroutine Description:
 #      This subroutine displays eight histograms in a four-by-eight grid.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame List
 #          inputDataFrameList
 #                          This parameter is the input List of DataFrames
 #  String List
 #          columnNameStringList
 #                          This parameter is a List of the columns for display.
 #  String
 #          figureTitleString
 #                          This parameter is the title of the figure.
 #  Float
 #          figureTitleFontSizeFloat
 #                          This parameter is the figure title's font size.
 #  Float
 #          figureTitleYPadFloat
 #                          This parameter is the figure title's space padding.
 #  String
 #          figureXLabelString
 #                          This parameter is the figure's x-axis label.
 #  Float
 #          figureXLabelFontSizeFloat
 #                          This parameter is the figure's x-axis label's font size.
 #  Float
 #          figureXLabelPadFloat
 #                          This parameter is the figure's x-axis label's padding.
 #  String
 #          figureYLabelString
 #                          This parameter is the figure's y-axis label.
 #  Float
 #          figureYLabelFontSizeFloat
 #                          This parameter is the figure's y-axis label's font size.
 #  Float
 #          figureYLabelPadFloat
 #                          This parameter is the figure's y-axis label's padding.
 #  Integer
 #          binsInteger
 #                          This parameter is the number of bins in the histograms.
 #  Float
 #          alphaFloat
 #                          This parameter is the transparency level of the histogram bars.
 #  String List
 #          colorStringList
 #                          This parameter is the colors for the different histograms.
 #  Float
 #          barLineWidthFloat
 #                          This parameter is the width of the lines outlining the histogram 
 #                          bars.
 #  String
 #          barEdgeColorString
 #                          This parameter is the color of the lines outlining the histogram
 #                          bars.
 #  String List
 #          plotTitleStringList
 #                          This parameter is the List of histogram titles.
 #  Float
 #          plotTitleFontSizeFloat
 #                          This parameter is the histogram title font size.
 #  Float
 #          plotTitleLabelPadFloat
 #                          This parameter is the histogram title space padding.
 #  String
 #          plotXLabelString
 #                          This parameter is the histogram x-axis label.
 #  Float
 #          plotXLabelFontSizeFloat
 #                          This parameter is the histogram x-axis label's font size.
 #  Float
 #          plotXLabelPadFloat
 #                          This parameter is the histogram x-axis label's space padding.
 #  String
 #          plotYLabelString
 #                          This parameter is the histogram y-axis label.
 #  Float
 #          plotYLabelFontSizeFloat
 #                          This parameter is the histogram y-axis label's font size.
 #  Float
 #          plotYLabelPadFloat
 #                          This parameter is the histogram y-axis label's space padding.
 #  Boolean
 #          normalizeYAxisBoolean
 #                          This parameter normalizes the y-axes for the various plots.
 #  Boolean
 #          normalizeYAxisHighestValueCountBoolean
 #                          This parameter indicates whether the highest value count alone 
 #                          is the maximum y-axis value.
 #  Float Tuple
 #          figSizeFloatTuple
 #                          This parameter is the figure length and height.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/29/2023          Initial Development                         N. James George
 #  09/30/2023          Added x-axis and y-axis limits parameters   N. James George
 #
 #******************************************************************************************/ 

def DisplayTwoByFourHistogramsFromDataFrameList \
        (inputDataFrameList,
         columnNameStringList,
         figureTitleString \
             = '',
         figureTitleFontSizeFloat \
             = 24.0,
         figureTitleYPadFloat \
             = 0.9,
         figureXLabelString \
             = '',
         figureXLabelFontSizeFloat \
             = 22.0,
         figureXLabelPadFloat \
             = 0.1,
         figureYLabelString \
             = '',
         figureYLabelFontSizeFloat \
             = 22.0,
         figureYLabelPadFloat \
             = 0.06,
         binsInteger \
             = 20,
         alphaFloat \
             = 0.8,
         colorStringList \
             = ['firebrick'],
         barLineWidthFloat \
             = 1.5,
         barEdgeColorString \
             = 'black',
         plotTitleStringList \
             = None,
         plotTitleFontSizeFloat \
             = 20.0,
         plotTitleLabelPadFloat \
             = 10.0,
         plotXLabelString \
             = '',
         plotXLabelFontSizeFloat \
             = 16.0,
         plotXLabelPadFloat \
             = 10.0,
         plotYLabelString \
             = '',
         plotYLabelFontSizeFloat \
             = 16.0,
         plotYLabelPadFloat \
             = 10.0,
         normalizeXAxisBoolean \
             = False,
         normalizeYAxisBoolean \
             = False,
         normalizeYAxisHighestValueCountBoolean \
             = False,
         figSizeFloatTuple \
             = (15, 9.2705)):

    try:

        fig, axs \
            = plt \
                .subplots \
                    (2, 4,
                     figsize \
                        = figSizeFloatTuple,
                     sharey \
                         = True, 
                     tight_layout \
                         = True)

        plt \
            .clf()
        
        
        if normalizeXAxisBoolean == True:

            xAxisRangeFloatList \
                = function \
                    .ReturnMinimumMaximumValuesXAxisHistogram \
                        (inputDataFrameList,
                         columnNameStringList)

        
        if normalizeYAxisBoolean == True:

            yAxisRangeFloatList \
                = function \
                    .ReturnMinimumMaximumValuesYAxisHistogram \
                        (inputDataFrameList,
                         columnNameStringList,
                         normalizeYAxisHighestValueCountBoolean,
                         binsInteger)


        print(yAxisRangeFloatList)
        for index in range(len(inputDataFrameList)):

            plt \
                .subplot \
                    (2, 4, index + 1)

            inputDataFrameList[index] \
                [columnNameStringList[index]] \
                    .plot \
                    .hist \
                        (bins \
                             = binsInteger, 
                         alpha \
                             = alphaFloat, 
                         color \
                             = colorStringList, 
                         linewidth \
                             = barLineWidthFloat, 
                         edgecolor \
                             = barEdgeColorString, 
                         legend \
                             = False)

            plt \
                .title \
                    (plotTitleStringList[index], 
                     fontdict \
                        = {'fontsize': plotTitleFontSizeFloat, 
                           'fontstyle': 'normal'},
                     pad = plotTitleLabelPadFloat)
  
            plt \
                .xlabel \
                    (plotXLabelString,
                     fontdict \
                        = {'fontsize': plotXLabelFontSizeFloat, 
                           'fontstyle': 'normal'},
                     labelpad = plotXLabelPadFloat)

            plt \
                .ylabel \
                    (plotYLabelString,
                     fontdict \
                        = {'fontsize': plotYLabelFontSizeFloat, 
                           'fontstyle': 'normal'},
                           labelpad = plotYLabelPadFloat)
        
            if normalizeXAxisBoolean == True:
                
                plt.xlim \
                    (xAxisRangeFloatList[0], 
                     xAxisRangeFloatList[1])

            if normalizeYAxisBoolean == True:

                plt.ylim \
                    (yAxisRangeFloatList[0], 
                     yAxisRangeFloatList[1])
            

        plt \
            .tight_layout \
                (pad = 3.0)
    
  
        fig \
            .suptitle \
                (figureTitleString, 
                 fontsize = figureTitleFontSizeFloat, 
                 y = figureTitleYPadFloat)
 
        fig \
            .supxlabel \
                (figureXLabelString,
                 fontsize = figureXLabelFontSizeFloat,
                 y = figureXLabelPadFloat)

        fig \
            .supylabel \
                (figureYLabelString,
                 fontsize = figureYLabelFontSizeFloat,
                 x = figureYLabelPadFloat)


        log_subroutine \
            .SavePlotImage \
                (figureTitleString)

  
        plt.show()

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayTwoByFourHistogramsFromDataFrameList, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {figureTitleString},\n'
                 + f'was unable to create a two-by-four set of eight histograms.')


# In[29]:


#*******************************************************************************************
 #
 #  Subroutine Name:  DisplayTwoByFourPlotsFromDataFrameList
 #
 #  Subroutine Description:
 #      This subroutine displays eight plots in a four-by-eight grid.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  DataFrame List
 #          inputDataFrameList
 #                          This parameter is the input List of DataFrames
 #  String List
 #          columnNameStringList
 #                          This parameter is a List of the columns for display.
 #  String
 #          figureTitleString
 #                          This parameter is the title of the figure.
 #  Float
 #          figureTitleFontSizeFloat
 #                          This parameter is the figure title's font size.
 #  Float
 #          figureTitleYPadFloat
 #                          This parameter is the figure title's space padding.
 #  String
 #          figureXLabelString
 #                          This parameter is the figure's x-axis label.
 #  Float
 #          figureXLabelFontSizeFloat
 #                          This parameter is the figure's x-axis label's font size.
 #  Float
 #          figureXLabelPadFloat
 #                          This parameter is the figure's x-axis label's padding.
 #  String
 #          figureYLabelString
 #                          This parameter is the figure's y-axis label.
 #  Float
 #          figureYLabelFontSizeFloat
 #                          This parameter is the figure's y-axis label's font size.
 #  Float
 #          figureYLabelPadFloat
 #                          This parameter is the figure's y-axis label's padding.
 #  Float
 #          alphaFloat
 #                          This parameter is the transparency level of the histogram bars.
 #  String List
 #          colorStringList
 #                          This parameter is the colors for the different histograms.
 #  String List
 #          plotTitleStringList
 #                          This parameter is the List of histogram titles.
 #  Float
 #          plotTitleFontSizeFloat
 #                          This parameter is the histogram title font size.
 #  Float
 #          plotTitleLabelPadFloat
 #                          This parameter is the histogram title space padding.
 #  String
 #          plotXLabelString
 #                          This parameter is the histogram x-axis label.
 #  Float
 #          plotXLabelFontSizeFloat
 #                          This parameter is the histogram x-axis label's font size.
 #  Float
 #          plotXLabelPadFloat
 #                          This parameter is the histogram x-axis label's space padding.
 #  String
 #          plotYLabelString
 #                          This parameter is the histogram y-axis label.
 #  Float
 #          plotYLabelFontSizeFloat
 #                          This parameter is the histogram y-axis label's font size.
 #  Float
 #          plotYLabelPadFloat
 #                          This parameter is the histogram y-axis label's space padding.
 #  Boolean
 #          normalizeYAxisBoolean
 #                          This parameter normalizes the y-axes for the various plots.
 #  Float Tuple
 #          figSizeFloatTuple
 #                          This parameter is the figure length and height.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  09/29/2023          Initial Development                         N. James George
 #
 #******************************************************************************************/ 

def DisplayTwoByFourPlotsFromDataFrameList \
        (inputDataFrameList,
         columnNameStringList,
         figureTitleString \
             = '',
         figureTitleFontSizeFloat \
             = 24.0,
         figureTitleYPadFloat \
             = 1.0,
         figureXLabelString \
             = '',
         figureXLabelFontSizeFloat \
             = 22.0,
         figureXLabelPadFloat \
             = 0.1,
         figureYLabelString \
             = '',
         figureYLabelFontSizeFloat \
             = 22.0,
         figureYLabelPadFloat \
             = 0.0,
         alphaFloat \
             = 0.8,
         colorStringList \
             = ['firebrick'],
         plotTitleStringList \
             = None,
         plotTitleFontSizeFloat \
             = 20.0,
         plotTitleLabelPadFloat \
             = 10.0,
         plotXLabelString \
             = '',
         plotXLabelFontSizeFloat \
             = 16.0,
         plotXLabelPadFloat \
             = 10.0,
         plotYLabelString \
             = '',
         plotYLabelFontSizeFloat \
             = 16.0,
         plotYLabelPadFloat \
             = 10.0,
         normalizeYAxisBoolean \
             = False,
         figSizeFloatTuple \
             = (15, 7.5)):

    try:

        fig, axs \
            = plt \
                .subplots \
                    (2, 4,
                     figsize \
                        = figSizeFloatTuple,
                     sharey \
                         = True, 
                     tight_layout \
                         = True)

        plt \
            .clf()
        
        if normalizeYAxisBoolean == True:
            
            minimumYValueFloat \
                = inputDataFrameList[0] \
                    [columnNameStringList[0]] \
                        .min()
            
            maximumYValueFloat \
                = inputDataFrameList[0] \
                    [columnNameStringList[0]] \
                        .max()
            
            for index in range(8):
                
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


        for index in range(8):

            plt \
                .subplot \
                    (2, 4, index + 1)

            inputDataFrameList[index] \
                [columnNameStringList[index]] \
                    .plot \
                        (color \
                            = colorStringList,
                         alpha \
                            = alphaFloat,
                         legend \
                            = False)

            plt \
                .title \
                    (plotTitleStringList[index], 
                     fontdict \
                        = {'fontsize': plotTitleFontSizeFloat, 
                           'fontstyle': 'normal'},
                     pad = plotTitleLabelPadFloat)
  
            plt \
                .xlabel \
                    (plotXLabelString,
                     fontdict \
                        = {'fontsize': plotXLabelFontSizeFloat, 
                           'fontstyle': 'normal'},
                     labelpad = plotXLabelPadFloat)
            
            plt \
                .tick_params \
                    (bottom = False,
                     labelbottom = False)

            plt \
                .ylabel \
                    (plotYLabelString,
                     fontdict \
                        = {'fontsize': plotYLabelFontSizeFloat, 
                           'fontstyle': 'normal'},
                           labelpad = plotYLabelPadFloat)
            
            if normalizeYAxisBoolean == True:
                
                plt.ylim \
                    (minimumYValueFloat, 
                     maximumYValueFloat)
            

        plt \
            .tight_layout \
                (pad = 3.0)
    
  
        fig \
            .suptitle \
                (figureTitleString, 
                 fontsize = figureTitleFontSizeFloat, 
                 y = figureTitleYPadFloat)
 
        fig \
            .supxlabel \
                (figureXLabelString,
                 fontsize = figureXLabelFontSizeFloat,
                 y = figureXLabelPadFloat)

        fig \
            .supylabel \
                (figureYLabelString,
                 fontsize = figureYLabelFontSizeFloat,
                 x = figureYLabelPadFloat)


        log_subroutine \
            .SavePlotImage \
                (figureTitleString)

  
        plt.show()

    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                (f'The subroutine, DisplayTwoByFourPlotsFromDataFrameList, '
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME},\n'
                 + f'with the caption, {figureTitleString},\n'
                 + f'was unable to create a two-by-four set of eight plots.')


# In[30]:


#*******************************************************************************************
 #
 #  Subroutine Name:  InsertJSONFileIntoMongoDBCollection
 #
 #  Subroutine Description:
 #      This subroutine reads the data from a JSON file and populates a MongoDB 
 #      collection with the information.  It also converts the date and time text
 #      string in the 'RatingDate' fields to a date text string.
 #
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  PyMongoCollectionObject
 #          pyMongoCollectionObject
 #                          This parameter is the PyMongoCollectionObject
 #                          for the current collection.
 #  String
 #          filePathString
 #                          This parameter is the file path for the JSON data file.
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  9/18/2023           Initial Development                         N. James George
 #  9/20/2023           Added conversion of 'RatingDate' to date String
 #                                                                  N. James George
 #
 #******************************************************************************************/

def InsertJSONFileIntoMongoDBCollection \
        (pyMongoCollectionObject,
         filePathString):
        
    try:

        with open(filePathString) as jsonFile:
    
            jsonDataObject \
                = json \
                    .load \
                        (jsonFile)

        
            for jsonDictionary in jsonDataObject:
                
                jsonDictionary \
                    ['RatingDate'] \
                        = jsonDictionary \
                            ['RatingDate'] \
                            [0:10]
            
        
        if isinstance(jsonDataObject, list):
            
            pyMongoCollectionObject \
                .insert_many \
                    (jsonDataObject)
            
        else:
            
            pyMongoCollectionObject \
                .insert_one \
                    (jsonDataObject)
            
    except:
        
        log_subroutine \
            .PrintAndLogWriteText \
                ('The subroutine, InsertJSONFileIntoMongoDBCollection, ' 
                 + f'in source file, {CONSTANT_LOCAL_FILE_NAME}, ' 
                 + 'cannot insert a JSON file into a Mongo DB database ' 
                 + 'as a Collection.')


# In[ ]:




