/****************************************************************************
 *
 *  File Name:  aviationAccidentsDashboard.js
 *
 *  File Description:
 *      This Javascript file contains the function calls for the html file,
 *      indexAccidentsDashboard.html. Here is a list of the functions
 *      and subroutines:
 *  
 *      FetchJsonDataFromURLFunction
 *      ReturnStartYearStringFunction
 *      ReturnEndYearStringFunction
 *      ReturnSortedCategoryStringListFunction
 *      ReturnFatalitiesIntegerListFunction
 * 
 *      PopulateYearDropdownMenuSubroutine
 *      PopulateAccidentIDDropdownMenuSubroutine
 *      PopulateThresholdDropdownMenuSubroutine
 *      PopulateDropdownMenuSubroutine
 * 
 *      RetrieveAccidentDataFromAPISubroutine
 *      AddOptionToDropdownMenuSubroutine
 *      ChangeDropdownMenuSelectedOptionSubroutine
 *      
 *      ChangeStartYearSubroutine
 *      ChangeEndYearSubroutine
 *      ChangeThresholdSubroutine
 *      ChangeAccidentIDSubroutine
 * 
 *      SetCurrentCategoryDictionarySubroutine
 *      SetCurrentBubbleChartDictionarySubroutine
 *      SetCurrentPieChartDictionarySubroutine
 * 
 *      GenerateBarChartSubroutine
 *      GenerateBubbleChartSubroutine
 *      GeneratePieChartSubroutine
 *      GenerateChartsSubroutine
 * 
 *      InitializeWebPageSubroutine
 * 
 *
 *  Date        Description                             Programmer
 *  ----------  ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/26/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

// This global variable contains the Aviation Accidents data set as
// a List of JSON Dictionaries.
let accidentsGeoJSONDictionaryList = null;


// This Dictionary contains the current values for various dropdown menus.
let selectedDropdownMenuOptionsDictionary
        = {
            startYear: 'Start Year',
            endYear: 'End Year',
            types: 'Aircraft Type',
            operators: 'Aircraft Operator',
            damage: 'Aircraft Damage',
            phase: 'Flight Phase',
            nature: 'Nature of Flight',
            country: 'Location (Country)'
          };

// This Dictionary contains the default values for the various dropdown menus.
const defaultSelectedDropdownMenuOptionsDictionary
        = {
            startYear: 'Start Year',
            endYear: 'End Year',
            types: 'Aircraft Type',
            operators: 'Aircraft Operator',
            damage: 'Aircraft Damage',
            phase: 'Flight Phase',
            nature: 'Nature of Flight',
            country: 'Location (Country)'
          };


// This Dictinary holds all the data for the bar char functionality.
let currentCategoryDictionary
          = {
                type: {trace: {x: [[]],
                               y: [[]]},
                       layout: {title: {font: {size: 28},
                                        text: '<b>Fatalities vs. Aircraft Type</b>'},
                                xaxis: {title: '<b>Types</b>',
                                        titlefont: {size: 20}}}},
                operator: {trace: {x: [[]],
                                   y: [[]]},
                           layout: {title: {font: {size: 28},
                                            text: '<b>Fatalities vs. Aircraft Operator</b>'},
                                    xaxis: {title: '<b>Operators</b>',
                                            titlefont: {size: 20}}}},
                phase: {trace: {x: [[]],
                                y: [[]]},
                        layout: {title: {font: {size: 28},
                                         text: '<b>Fatalities vs. Flight Phase</b>'},
                                 xaxis: {title: '<b>Operators</b>',
                                         titlefont: {size: 20}}}},
                nature: {trace: {x: [[]],
                                 y: [[]]},
                         layout: {title: {font: {size: 28},
                                          text: '<b>Fatalities vs. Nature of Flight</b>'},
                                  xaxis: {title: '<b>Nature</b>',
                                          titlefont: {size: 20}}}},
                departure: {trace: {x: [[]],
                                    y: [[]]},
                            layout: {title: {font: {size: 28},
                                             text: '<b>Fatalities vs. Departure Airport</b>'},
                                     xaxis: {title: '<b>Airport</b>',
                                             titlefont: {size: 20}}}},
                destination: {trace: {x: [[]],
                                      y: [[]]},
                              layout: {title: {font: {size: 28},
                                               text: '<b>Fatalities vs. Destination Airport</b>'},
                              xaxis: {title: '<b>Airport</b>',
                                      titlefont: {size: 20}}}},
                year: {trace: {x: [[]],
                               y: [[]]},
                       layout: {title: {font: {size: 28},
                                        text: '<b>Fatalities vs. Year</b>'},
                                xaxis: {title: '<b>Year</b>',
                                        titlefont: {size: 20}}}}
            };


// These Dictionaries hold the necessary values to plot the bubble and pie charts.
let currentBubbleChartDictionary
        = {
                latidude: [],
                longitude: [],
                fatalities: [],
                accident_ids: [],
                labels: []
          };

let currentPieChartDictionary
        = {
                phase: [],
                fatalities: []
          };


// This variable holds the current active category for the Bar Chart's
// pulldown menu.
let currentCategoryString = 'type';


// This variable contains the current fatalities threshold value.
let currentThresholdInteger = 1;


/****************************************************************************
 *
 *  Function Name:  FetchJsonDataFromURLFunction
 *
 *  Function Description:  
 *      This function is the first stage for retrieving the aviation 
 *      accidents data set from the specified URL.
 *
 *
 *  Function Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  String
 *          urlString
 *                          This parameter is the URL for the source data.
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/26/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

async function FetchJsonDataFromURLFunction 
                (urlString) 
{
    let dataD3JsonObject 
            = null;
  
    try 
    {
        dataD3JsonObject 
            = await 
                d3.json
                    (urlString);
    }
    catch (error) 
    {
        console.error
            (error);
    }
 
    return dataD3JsonObject;
} // This right brace ends the block for the function, 
// FetchJsonDataFromURLFunction.


/****************************************************************************
 *
 *  Function Name:  ReturnStartYearStringFunction
 *
 *  Function Description:  
 *      This function returns the start year for the visualization.
 *
 *
 *  Function Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  n/a     n/a             n/a
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ReturnStartYearStringFunction() 
{
    var startYearString;

    if (selectedDropdownMenuOptionsDictionary['startYear'] == 'Start Year')
    {
        selectedDropdownMenuOptionsDictionary['startYear'] = '1970';

        startYearString = '1970';
    }
    else
    {
        startYearString = selectedDropdownMenuOptionsDictionary['startYear'];
    }

    return startYearString;
} // This right brace ends the block for the function, 
// ReturnStartYearStringFunction.


/****************************************************************************
 *
 *  Function Name:  ReturnEndYearStringFunction
 *
 *  Function Description:  
 *      This function returns the end year for the visualization.
 *
 *
 *  Function Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  n/a     n/a             n/a
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ReturnEndYearStringFunction() 
{
    var endYearString;

    if (selectedDropdownMenuOptionsDictionary['endYear'] == 'End Year')
    {
        selectedDropdownMenuOptionsDictionary['endYear'] = '2022';

        endYearString = '2022';
    }
    else
    {
        endYearString = selectedDropdownMenuOptionsDictionary['endYear'];
    }

    return endYearString;
} // This right brace ends the block for the function, 
// ReturnEndYearStringFunction.


/****************************************************************************
 *
 *  Function Name:  ReturnSortedCategoryStringListFunction
 *
 *  Function Description:  
 *      This function returns the unique sorted values of the specified 
 *      category from the aviation accidents data set.
 *
 *
 *  Function Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  Dictionary
 *          accidentsDictionaryList
 *                          This parameter is the list of accident data
 *                          Dictionaries.
 *  Integer
 *          startYearInteger
 *                          This parameter is the specified start year
 *                          for the requested data.
 *  Integer
 *          endYearInteger
 *                          This parameter is the specified end year
 *                          for the requested data.
 *  String
 *          categoryString
 *                          This parameter is the specified category.
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ReturnSortedCategoryStringListFunction
            (accidentsDictionaryList,
             startYearInteger,
             endYearInteger,
             categoryString)
{
    var categoryStringList
            = [];
    
    for (var i = 0; i < accidentsDictionaryList.length; i++)
    {   
        if (accidentsDictionaryList[i].properties.year >= startYearInteger
            && accidentsDictionaryList[i].properties.year <= endYearInteger)
        {
            categoryStringList.push(accidentsDictionaryList[i].properties[categoryString]);
        }
    }

    let uniqueCategoryStringList = [...new Set(categoryStringList)];
    
    return uniqueCategoryStringList.sort();
} // This right brace ends the block for the function, 
// ReturnSortedCategoryStringListFunction.


/****************************************************************************
 *
 *  Function Name:  ReturnFatalitiesIntegerListFunction
 *
 *  Function Description:  
 *      This function returns the total fatalities for each category
 *      in the provided array.
 *
 *
 *  Function Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  Dictionary
 *          accidentsDictionaryList
 *                          This parameter is the list of accident data
 *                          Dictionaries.
 *  Integer
 *          startYearInteger
 *                          This parameter is the specified start year
 *                          for the requested data.
 *  Integer
 *          endYearInteger
 *                          This parameter is the specified end year
 *                          for the requested data.
 *  String
 *          categoryString
 *                          This parameter is the specified category.
 *  List
 *          sortedCategoryStringList
 *                          This parameter is the sorted list of unique 
 *                          values from the specified category.
 *          
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ReturnFatalitiesIntegerListFunction
            (accidentsDictionaryList,
             startYearInteger,
             endYearInteger,
             categoryString,
             sortedCategoryStringList,
             pieChartBooleanFlag = false)
{
    var fatalitiesIntegerList
            = new Array(sortedCategoryStringList.length).fill(0);

    for (var i = 0; i < sortedCategoryStringList.length; i++)
    {
        for (var j = 0; j < accidentsDictionaryList.length; j++)
        {
            if (accidentsDictionaryList[j].properties[categoryString] == sortedCategoryStringList[i]
                && accidentsDictionaryList[j].properties.year >= startYearInteger
                && accidentsDictionaryList[j].properties.year <= endYearInteger)
            {
                if (accidentsDictionaryList[j].properties.fatalities > currentThresholdInteger)
                {
                    fatalitiesIntegerList[i] += accidentsDictionaryList[j].properties.fatalities;
                }
            }
        }
     }

    return fatalitiesIntegerList;
} // This right brace ends the block for the function, 
// ReturnFatalitiesIntegerListFunction.



/****************************************************************************
 *
 *  Subroutine Name:  PopulateYearDropdownMenuSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine populates a year dropdown menu with the full range 
 *      of years from the aviation accident data set.
 *
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  String
 *          dropdownIDString
 *                          This parameter is the identification for the 
 *                          dropdown menu.
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/26/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function PopulateYearDropdownMenuSubroutine
            (dropdownIDString) 
{
    PopulateDropdownMenuSubroutine
        ('http://127.0.0.1:5000/api/v1.0/years',
         dropdownIDString);

    PopulateAccidentIDDropdownMenuSubroutine();
} // This right brace ends the block for the subroutine, 
// PopulateYearDropdownMenuSubroutine.


/****************************************************************************
 *
 *  Subroutine:  PopulateAccidentIDDropdownMenuSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine populates the Accident ID dropdown menu.
 *
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  n/a     n/a             n/a
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function PopulateAccidentIDDropdownMenuSubroutine()
{
    var startYearString
            = ReturnStartYearStringFunction();

    var endYearString
            = ReturnEndYearStringFunction();

    routeURLString
        = 'http://127.0.0.1:5000/api/v1.0/accident_id_list/'
            + startYearString
            + '/'
            + endYearString;

    PopulateDropdownMenuSubroutine
        (routeURLString,
         'selectAccidentID');
} // This right brace ends the block for the subroutine, 
// PopulateAccidentIDDropdownMenuSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  PopulateThresholdDropdownMenuSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine populates the fatalities threshold dropdown menu.
 *
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  n/a     n/a             n/a
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function PopulateThresholdDropdownMenuSubroutine()
{
    let thresholdIntegerArray
            = Array.from({length: 100}, (_, i) => i + 1);

    var selectElementObject 
            = document
                .getElementById
                    ('selectThreshold');

    for (var i = 0; i < thresholdIntegerArray.length; i++) 
    {
        AddOptionToDropdownMenuSubroutine
            (selectElementObject,
             thresholdIntegerArray[i].toString());
    }

    currentThresholdInteger = 1;
} // This right brace ends the block for the subroutine, 
// PopulateThresholdDropdownMenuSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  PopulateDropdownMenuSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine populates the specified dropdown menu with the
 *      provided URL.
 *
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  String
 *          routeURLString
 *                          This parameter is the specified URL for the
 *                          requested data.
 *  String
 *          dropdownIDString
 *                          This parameter is the identification for the 
 *                          dropdown menu.
 *
 *
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function PopulateDropdownMenuSubroutine
            (routeURLString,
             dropdownIDString)
{
    FetchJsonDataFromURLFunction 
        (routeURLString)
            .then
            (
                (currentStringArray => 
                    {
                        var selectElementObject 
                                = document
                                    .getElementById
                                        (dropdownIDString);
                       
                        if (dropdownIDString == 'selectAccidentID')
                        {
                            var lastElementIndexInteger
                                    = selectElementObject.options.length - 1;

                            for (var i = lastElementIndexInteger; i >= 0; i--) 
                            {
                                selectElementObject.remove(i);
                            }

                            ChangeAccidentIDSubroutine(currentStringArray[0]);
                        }

                        for (var i = 0; i < currentStringArray.length; i++) 
                        {
                            AddOptionToDropdownMenuSubroutine
                                (selectElementObject,
                                 currentStringArray[i]);
                        }
                    }
                )
            );
} // This right brace ends the block for the subroutine, 
// PopulateDropdownMenuSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  RetrieveAccidentDataFromAPISubroutine
 *
 *  Subroutine Description:  
 *      This subroutine retrieves the entire aviation accident data set
 *      from the database.
 *
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  n/a     n/a             n/a
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function RetrieveAccidentDataFromAPISubroutine()
{
    var routeURLString
        = 'http://127.0.0.1:5000/api/v1.0/accidents/'
            + '1970'
            + '/'
            + '2022'
            + '/'
            + defaultSelectedDropdownMenuOptionsDictionary['types']
            + '/'
            + defaultSelectedDropdownMenuOptionsDictionary['operators']
            + '/'
            + defaultSelectedDropdownMenuOptionsDictionary['damage']
            + '/'
            + defaultSelectedDropdownMenuOptionsDictionary['phase']
            + '/'
            + defaultSelectedDropdownMenuOptionsDictionary['nature']
            + '/'
            + defaultSelectedDropdownMenuOptionsDictionary['country'];

    FetchJsonDataFromURLFunction
        (routeURLString)
            .then
            (
                (accidentsGeoJSONDictionaryCollection => 
                 {
                    accidentsGeoJSONDictionaryList
                        = accidentsGeoJSONDictionaryCollection.features;

                    GenerateChartsSubroutine();
                 }
                )
            );
} // This right brace ends the block for the subroutine, 
// RetrieveAccidentDataFromAPISubroutine.



/****************************************************************************
 *
 *  Subroutine Name:  AddOptionToDropdownMenuSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine adds one option to a dropdown menu.
 *
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  String
 *          selectElementObject
 *                          This parameter is the dropdown menu object.
 *  String
 *          optionString
 *                          This parameter is the new option for the
 *                          dropdownn menu.
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/26/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function AddOptionToDropdownMenuSubroutine
            (selectElementObject,
             optionString)
{
    var documentElementObject
        = document
            .createElement
                ('option');

    documentElementObject.textContent 
        = optionString;

    documentElementObject.value 
        = optionString;

    selectElementObject
        .appendChild
            (documentElementObject);
} // This right brace ends the block for the subroutine, 
// AddOptionToDropdownMenuSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  ChangeDropdownMenuSelectedOptionSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine changes the selected element in a dropdown menu.
 *
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  String
 *          dropdownIDString
 *                          This parameter is the identification for the 
 *                          dropdown menu.
 *  String
 *          selectedIDString
 *                          This parameter is the selected option from
 *                          the dropdown menu.
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/26/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ChangeDropdownMenuSelectedOptionSubroutine
            (dropdownIDString,
             selectedIDString)
{
    var selectElementObject 
            = document
                .getElementById
                    (dropdownIDString);

    for (var i = 0; i < selectElementObject.options.length; i++)
    {
        if (selectElementObject.options[i].value == selectedIDString)
        {
            selectElementObject.options[i].selected = true;
            
            break;
        }
    }
} // This right brace ends the block for the subroutine, 
// ChangeDropdownMenuSelectedOptionSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  ChangeStartYearSubroutine 
 *
 *  Subroutine Description:  
 *      This subroutine sets the start year values and populates all the 
 *      category dropdown menus when the user changes the start year
 *      dropdown menu.
 *
 *
 *  Subroutines Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  String
 *          selectedIDString
 *                          This parameter is the selected option from
 *                          the dropdown menu.
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/26/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ChangeStartYearSubroutine 
            (selectedIDString)
{
    if (selectedDropdownMenuOptionsDictionary['endYear'] == 'End Year'
         || selectedDropdownMenuOptionsDictionary['endYear'] == '2022')
    {
        selectedDropdownMenuOptionsDictionary['endYear'] = '2022';

        ChangeDropdownMenuSelectedOptionSubroutine
            ('selectEndYear',
             '2022');
    }

    if (selectedIDString == 'Start Year')
    {
        selectedDropdownMenuOptionsDictionary['startYear'] = '1970';
    }
    else if (parseInt(selectedIDString) 
                > parseInt(selectedDropdownMenuOptionsDictionary['endYear']))
    {
        selectedDropdownMenuOptionsDictionary['startYear'] = selectedIDString;

        selectedDropdownMenuOptionsDictionary['endYear'] = selectedIDString;

        ChangeDropdownMenuSelectedOptionSubroutine
            ('selectStartYear',
             selectedIDString);

        ChangeDropdownMenuSelectedOptionSubroutine
            ('selectEndYear',
             selectedIDString);
    }
    else 
    {
        selectedDropdownMenuOptionsDictionary['startYear'] = selectedIDString;

        ChangeDropdownMenuSelectedOptionSubroutine
            ('selectStartYear',
             selectedIDString);
    }

    PopulateAccidentIDDropdownMenuSubroutine();

    GenerateChartsSubroutine();
} // This right brace ends the block for the subroutine, 
// ChangeStartYearSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  ChangeEndYearSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine sets the end year values and populates all the 
 *      category dropdown menus when the user changes the end year
 *      dropdown menu.
 *
 *
 *  Subroutines Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  String
 *          selectedIDString
 *                          This parameter is the selected option from
 *                          the dropdown menu.
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/26/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ChangeEndYearSubroutine
            (selectedIDString)
{
    if (selectedDropdownMenuOptionsDictionary['startYear'] == 'Start Year' 
        || selectedDropdownMenuOptionsDictionary['startYear'] == '1970')
    {
        selectedDropdownMenuOptionsDictionary['startYear'] = '1970';

        ChangeDropdownMenuSelectedOptionSubroutine
            ('selectStartYear',
             '1970');
    }

    if (selectedIDString == 'End Year')
    {
        selectedDropdownMenuOptionsDictionary['endYear'] = '2022';
    }
    else if (parseInt(selectedIDString) 
                < parseInt(selectedDropdownMenuOptionsDictionary['startYear']))
    {
        selectedDropdownMenuOptionsDictionary['startYear'] = selectedIDString;

        selectedDropdownMenuOptionsDictionary['endYear'] = selectedIDString;

        ChangeDropdownMenuSelectedOptionSubroutine
            ('selectStartYear',
             selectedIDString);

        ChangeDropdownMenuSelectedOptionSubroutine
            ('selectEndYear',
             selectedIDString);
    }
    else 
    {
        selectedDropdownMenuOptionsDictionary['endYear'] = selectedIDString;

        ChangeDropdownMenuSelectedOptionSubroutine
            ('selectEndYear',
             selectedIDString);
    }

    PopulateAccidentIDDropdownMenuSubroutine();

    GenerateChartsSubroutine();
} // This right brace ends the block for the subroutine, 
// ChangeEndYearSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  ChangeThresholdSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine changes the fatalities threshold to the provided 
 *      value.
 *  
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  String
 *          thresholdString
 *                          This parameter is new value for the fatalities
 *                          threshold.
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ChangeThresholdSubroutine
            (thresholdString)
{
    if (thresholdString == 'Threshold')
    {
        currentThresholdInteger = 1;
    }
    else
    {
        currentThresholdInteger
            = parseInt(thresholdString);
    }

    GenerateChartsSubroutine();
} // This right brace ends the block for the subroutine, 
// ChangeThresholdSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  ChangeAccidentIDSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine is the call back for the accident ID dropdoown 
 *      menu.
 *
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  String
 *          dropdownIDString
 *                          This parameter is the identification for the 
 *                          dropdown menu.
 *
 *
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ChangeAccidentIDSubroutine
            (dropdownIDString = 'ACC102')
{
    routeURLString
        = 'http://127.0.0.1:5000/api/v1.0/accident_by_id/'
            + dropdownIDString;

    FetchJsonDataFromURLFunction 
        (routeURLString)
            .then
            (
                (currentAccidentDictionary => 
                    {
                        d3.select
                            ('#metadata-accidents')
                          .html
                            ('');

                        d3.select
                            ('#metadata-accidents')
                          .append
                            ('p')
                          .text
                            ('Accident ID: ' + `${currentAccidentDictionary.properties.accident_id}`);

                        d3.select
                            ('#metadata-accidents')
                          .append
                            ('p')
                          .attr
                            ("dy", "1em")
                          .text
                            ('Date: ' + `${currentAccidentDictionary.properties.date}`);

                        d3.select
                            ('#metadata-accidents')
                          .append
                            ('p')
                          .text
                            ('Aircraft Type: ' + `${currentAccidentDictionary.properties.type}` );

                        d3.select
                            ('#metadata-accidents')
                          .append
                            ('p')
                          .text
                            ('Aircraft Operator: ' + `${currentAccidentDictionary.properties.operator}` );

                        d3.select
                            ('#metadata-accidents')
                          .append
                            ('p')
                          .text
                            ('Fatalities: ' + `${currentAccidentDictionary.properties.fatalities}` );

                        d3.select
                            ('#metadata-accidents')
                          .append
                            ('p')
                          .text
                            ('Occupants: ' + `${currentAccidentDictionary.properties.occupants}` );

                        d3.select
                            ('#metadata-accidents')
                          .append
                            ('p')
                          .text
                            ('Damage: ' + `${currentAccidentDictionary.properties.damage}` );

                        d3.select
                            ('#metadata-accidents')
                          .append
                            ('p')
                          .text
                            ('Phase: ' + `${currentAccidentDictionary.properties.phase}` );

                        d3.select
                            ('#metadata-accidents')
                          .append
                            ('p')
                          .text
                            ('Nature: ' + `${currentAccidentDictionary.properties.nature}` );

                        d3.select
                            ('#metadata-accidents')
                          .append
                            ('p')
                          .text
                            ('Departure Airport: ' + `${currentAccidentDictionary.properties.departure}` );

                        d3.select
                            ('#metadata-accidents')
                          .append
                            ('p')
                          .text
                            ('Destination Airport: ' + `${currentAccidentDictionary.properties.destination}` );

                        d3.select
                            ('#metadata-accidents')
                          .append
                            ('p')
                          .text
                            ('Location: ' + `${currentAccidentDictionary.properties.location}` );
                    }
                )
            );
} // This right brace ends the block for the subroutine, 
// ChangeAccidentIDSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  SetCurrentCategoryDictionarySubroutine
 *
 *  Subroutine Description:  
 *      This subroutine sets the values for the category dictionary for
 *      the purposes of generating a chart.
 *
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  List
 *          accidentsDictionaryList
 *                          This parameter is the list of accident 
 *                          Dictionaries.
 *  Dictionary
 *          categoryDictionary
 *                          This parameter is the dictionary for a 
 *                          particular category.
 *
 *
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function SetCurrentCategoryDictionarySubroutine
            (accidentsDictionaryList,
             categoryDictionary)
{
    var startYearInteger
            = parseInt(ReturnStartYearStringFunction());

    var endYearInteger
            = parseInt(ReturnEndYearStringFunction());

    var sortedCategoryStringList;

    var fatalitiesIntegerList;

    for (const keyString in categoryDictionary)
    {   
        sortedCategoryStringList
            = ReturnSortedCategoryStringListFunction
                (accidentsDictionaryList,
                 startYearInteger,
                 endYearInteger,
                 keyString);
        
        fatalitiesIntegerList
            = ReturnFatalitiesIntegerListFunction
                (accidentsDictionaryList,
                 startYearInteger,
                 endYearInteger,
                 keyString,
                 sortedCategoryStringList);

        for (i = 0; i < fatalitiesIntegerList.length; i++)
        {
            if (fatalitiesIntegerList[i] < currentThresholdInteger)
            {
                delete sortedCategoryStringList[i];

                delete fatalitiesIntegerList[i];
            }
        }

        categoryDictionary[keyString].trace.x = [sortedCategoryStringList];

        categoryDictionary[keyString].trace.y = [fatalitiesIntegerList];
    }

    return categoryDictionary;
} // This right brace ends the block for the subroutine, 
// SetCurrentCategoryDictionarySubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  SetCurrentBubbleChartDictionarySubroutine
 *
 *  Subroutine Description:  
 *      This subroutine sets the values for the bubble chart dictionary
 *      for the purpose of generating a bubble chart.
 *
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  List
 *          accidentsDictionaryList
 *                          This parameter is the list of accident 
 *                          Dictionaries.
 *  Dictionary
 *          bubbleChartDictionary
 *                          This parameter is the dictionary for a 
 *                          bubble chart.
 *
 *
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function SetCurrentBubbleChartDictionarySubroutine
            (accidentsDictionaryList,
             bubbleChartDictionary)
{
    var startYearInteger
            = parseInt(ReturnStartYearStringFunction());

    var endYearInteger
            = parseInt(ReturnEndYearStringFunction());

    var labelsStringList
            = [];

    var accidentIDStringList
            = [];

    var latitudeFloatList
            = [];

    var longitudeFloatList
            = [];

    var fatalitiesIntegerList
            = [];

    var tempString;

    for (var i = 0; i < accidentsDictionaryList.length; i++)
    {   

        if (accidentsDictionaryList[i].properties.year >= startYearInteger
            && accidentsDictionaryList[i].properties.year <= endYearInteger)
        {
            tempString
                = accidentsDictionaryList[i].properties.accident_id
                    + ';'
                    + accidentsDictionaryList[i].properties.date
                    + ';'
                    + accidentsDictionaryList[i].properties.type
                    + ';'
                    + accidentsDictionaryList[i].properties.operator
                    + ';'
                    + accidentsDictionaryList[i].properties.fatalities.toString()
                    + ';'
                    + accidentsDictionaryList[i].properties.occupants.toString()
                    + ';'
                    + accidentsDictionaryList[i].properties.damage
                    + ';'
                    + accidentsDictionaryList[i].properties.phase
                    + ';'
                    + accidentsDictionaryList[i].properties.nature
                    + ';'
                    + accidentsDictionaryList[i].properties.location;

            labelsStringList
                .push
                    (tempString);

            accidentIDStringList
                .push
                    (accidentsDictionaryList[i].properties.accident_id.slice(3));

            latitudeFloatList
                .push
                    (accidentsDictionaryList[i].geometry.coordinates[0]);

            longitudeFloatList
                .push
                    (accidentsDictionaryList[i].geometry.coordinates[1]);

            fatalitiesIntegerList
                .push
                    (accidentsDictionaryList[i].properties.fatalities);
        }
    }

    for (i = 0; i < fatalitiesIntegerList.length; i++)
    {
        if (fatalitiesIntegerList[i] < currentThresholdInteger)
        {
            delete labelsStringList[i];

            delete accidentIDStringList[i];

            delete latitudeFloatList[i];

            delete longitudeFloatList[i];

            delete fatalitiesIntegerList[i];
        }
    }


    bubbleChartDictionary.latidude = latitudeFloatList;

    bubbleChartDictionary.longitude = longitudeFloatList;

    bubbleChartDictionary.accident_ids = accidentIDStringList;

    bubbleChartDictionary.fatalities = fatalitiesIntegerList;

    bubbleChartDictionary.labels = labelsStringList;


    return bubbleChartDictionary;
} // This right brace ends the block for the subroutine, 
// SetCurrentBubbleChartDictionarySubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  SetCurrentPieChartDictionarySubroutine
 *
 *  Subroutine Description:  
 *      This subroutine is the call back for the accident ID dropdoown 
 *      menu.
 *
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  List
 *          accidentsDictionaryList
 *                          This parameter is the list of accident 
 *                          Dictionaries.
 *  Dictionary
 *          bubbleChartDictionary
 *                          This parameter is the dictionary for a 
 *                          pie chart.
 *
 *
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function SetCurrentPieChartDictionarySubroutine
            (accidentsDictionaryList,
             pieChartDictionary)
{
    var startYearInteger
            = parseInt(ReturnStartYearStringFunction());

    var endYearInteger
            = parseInt(ReturnEndYearStringFunction());

    var sortedCategoryStringList
            = ReturnSortedCategoryStringListFunction
                (accidentsDictionaryList,
                 startYearInteger,
                 endYearInteger,
                 'phase');

    var fatalitiesIntegerList
            = ReturnFatalitiesIntegerListFunction
                (accidentsDictionaryList,
                 startYearInteger,
                 endYearInteger,
                 'phase',
                 sortedCategoryStringList,
                 true);

    for (var i = 0; i < fatalitiesIntegerList.length; i++)
    {
        if (fatalitiesIntegerList[i] < currentThresholdInteger)
        {
            delete sortedCategoryStringList[i];

            delete fatalitiesIntegerList[i];
        }
    }

    pieChartDictionary.phase = sortedCategoryStringList;

    pieChartDictionary.fatalities = fatalitiesIntegerList;

    return pieChartDictionary;
} // This right brace ends the block for the subroutine, 
// SetCurrentPieChartDictionarySubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  GenerateBarChartSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine generates the bar chart.
 *  
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  n/a     n/a             n/a
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/24/2023  Initial Development                     N. James George
 *
 ****************************************************************************/

function GenerateBarChartSubroutine() 
{
    currentCategoryString
        = 'type';

    currentCategoryDictionary
        = SetCurrentCategoryDictionarySubroutine
            (accidentsGeoJSONDictionaryList,
             currentCategoryDictionary);

    let barChartTraceDictionaryList
        = [
            {
                type: 'bar',
                x: currentCategoryDictionary[currentCategoryString].trace.x[0],
                y: currentCategoryDictionary[currentCategoryString].trace.y[0],
                marker: 
                    {color: 'firebrick',
                     line: {color: 'black',
                            width: 1.0}}
            }
          ];

    let barChartLayoutDictionary 
            = {
                    title: {font: {size: 28},
                            text: currentCategoryDictionary[currentCategoryString].layout.title.text},
                    margin: {l:100, r:100, t:100, b:300},
                    width: 2500, 
                    height: 700, 
                    font: {color: 'black'},
                    paper_bgcolor: '#E1F3FB',
                    plot_bgcolor: '#fff',
                    showlegend: false,
                    xaxis: {title: currentCategoryDictionary[currentCategoryString].layout.xaxis.title, 
                            titlefont: {size: 20}},
                    yaxis: {title: '<b>Fatalities</b>', 
                            titlefont: {size: 20}},
                    annotations: [{
                                  x: -0.14,
                                  y: 1.12,
                                  xref: 'paper',
                                  yref: 'paper',
                                  align: 'left',
                                  text: '<b>Category:<b>',
                                  showarrow: false,
                                  font: {size: 20}}],
                    updatemenus: [{
                        active: 0,
                        bgcolor: '#FAF3E0',
                        bordercolor: 'black',
                        buttons: [
                            {
                            args:   [currentCategoryDictionary['type'].trace, currentCategoryDictionary['type'].layout, [0]],
                            execute: 'true',
                            method: 'update',
                            label: 'Aircraft Type'
                          },
                          {
                            args:   [currentCategoryDictionary['operator'].trace, currentCategoryDictionary['operator'].layout, [0]],
                            execute: 'true',
                            method: 'update',
                            label: 'Aircraft Operator'
                          },
                          {
                            args:   [currentCategoryDictionary['phase'].trace, currentCategoryDictionary['phase'].layout, [0]],
                            execute: 'true',
                            method: 'update',
                            label: 'Flight Phase'
                          },
                          {
                            args:   [currentCategoryDictionary['nature'].trace, currentCategoryDictionary['nature'].layout, [0]],
                            execute: 'true',
                            method: 'update',
                            label: 'Nature of Flight'
                          },
                          {
                            args:   [currentCategoryDictionary['departure'].trace, currentCategoryDictionary['departure'].layout, [0]],
                            execute: 'true',
                            method: 'update',
                            label: 'Departure Airport'
                          },
                          {
                            args:   [currentCategoryDictionary['destination'].trace, currentCategoryDictionary['destination'].layout, [0]],
                            execute: 'true',
                            method: 'update',
                            label: 'Destination Airport'
                          },
                          {
                            args:   [currentCategoryDictionary['year'].trace, currentCategoryDictionary['year'].layout, [0]],
                            execute: 'true',
                            method: 'update',
                            label: 'Year'
                          }
                        ],
                        font: {size: 16},
                        y: 1
                      }]
              };

    Plotly.newPlot
        ('barChart', 
         barChartTraceDictionaryList,
         barChartLayoutDictionary);
}; // This right brace ends the block for the subroutine, 
// GenerateBarChartSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  GenerateBubbleChartSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine generates the bubble chart.
 *  
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  n/a     n/a             n/a
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function GenerateBubbleChartSubroutine()
{
    currentBubbleChartDictionary
        = SetCurrentBubbleChartDictionarySubroutine
            (accidentsGeoJSONDictionaryList,
             currentBubbleChartDictionary);
    
    let bubbleChartTraceDictionaryList
             = [{
                     text: currentBubbleChartDictionary.labels,
                     x: currentBubbleChartDictionary.longitude,
                     y: currentBubbleChartDictionary.latidude,
                     mode: 'markers',
                     marker: 
                         {size: currentBubbleChartDictionary.fatalities,
                          color: currentBubbleChartDictionary.accident_ids,
                          colorscale: 'Jet'}
                 }];
 
    let bubbleChartLayoutDictionary 
        = {
            title: '<b>Aviation Accidents Geographical Composition</b>',
                 margin: {l: 100, 
                          r: 100, 
                          t: 100, 
                          b: 100},
                 titlefont: {size: 28},
                 font: {color: 'black'},
                 width: 1250, 
                 height: 650, 
                 font: {color: 'black'},
                 paper_bgcolor: '#E1F3FB',
                 plot_bgcolor: '#fff',
                 showlegend: false,
                 xaxis: {title: '<b>Longitude</b>', 
                         titlefont: {size: 20}},
                 yaxis: {title: '<b>Latitude</b>', 
                         titlefont: {size: 20}},
                 hovermode: 'closest',
           };
 
     Plotly.newPlot
         ('bubbleChart', 
          bubbleChartTraceDictionaryList, 
          bubbleChartLayoutDictionary);
} // This right brace ends the block for the subroutine, 
// GenerateBubbleChartSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  GeneratePieChartSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine generates the pie chart.
 *  
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  n/a     n/a             n/a
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function GeneratePieChartSubroutine()
{
    currentPieChartDictionary
        = SetCurrentPieChartDictionarySubroutine
            (accidentsGeoJSONDictionaryList,
             currentPieChartDictionary);

    let pieChartTraceDictionaryList
             = [{
                     values: currentPieChartDictionary.fatalities,
                     labels: currentPieChartDictionary.phase,
                     domain: {column: 0},
                     name: 'Flight Phase vs. Fatalities',
                     hoverinfo: 'label+percent+name',
                     hole: .4,
                     type: 'pie'
                 }];
                 
    let pieChartLayoutDictionary 
        = {
            title: '<b>Flight Phase vs. Fatalities</b>',
                 margin: {l: 100, 
                          r: 100, 
                          t: 100, 
                          b: 100},
                 titlefont: {size: 28},
                 font: {color: 'black'},
                 width: 800, 
                 height: 650, 
                 font: {color: 'black',
                        size: '20'},
                 paper_bgcolor: '#E1F3FB',
                 plot_bgcolor: '#fff',
                 showlegend: true
           };
 
     Plotly.newPlot
         ('pieChart', 
          pieChartTraceDictionaryList, 
          pieChartLayoutDictionary);
} // This right brace ends the block for the subroutine, 
// GeneratePieChartSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  GenerateChartsSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine generates the charts for the dashboard.
 *  
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  n/a     n/a             n/a
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function GenerateChartsSubroutine()
{
    GenerateBarChartSubroutine();

    GenerateBubbleChartSubroutine();

    GeneratePieChartSubroutine();
} // This right brace ends the block for the subroutine, 
// GenerateChartsSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  InitializeWebPageSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine initializes the Aviation Accidents Dashboard
 *      by populating the drop down menus and charts.
 *
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  n/a     n/a             n/a
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     N. James George
 *  10/26/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function InitializeWebPageSubroutine() 
{
    PopulateYearDropdownMenuSubroutine
        ('selectStartYear');

    PopulateYearDropdownMenuSubroutine
        ('selectEndYear');

    PopulateThresholdDropdownMenuSubroutine()

    RetrieveAccidentDataFromAPISubroutine();    

} // This right brace ends the block for the subroutine, 
// InitializeWebPageSubroutine.


InitializeWebPageSubroutine();