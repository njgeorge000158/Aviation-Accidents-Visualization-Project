/****************************************************************************
 *
 *  File Name:  aviationAccidentsVisualization.js
 *
 *  File Description:
 *      This Javascript file contains the function calls for the html file,
 *      indexAccidentVisualization.html. Here is a list of the functions
 *      and subroutines:
 *  
 *      FetchJsonDataFromURLFunction
 *      ChooseColorFromFatalitiesFunction
 *      SetMarkerSizeFromFatalitiesFunction
 *      ReturnStartYearFunction
 *      ReturnEndYearFunction
 * 
 *      CreateLegendSubroutine
 * 
 *      InsertDefaultAsFirstInDropdownMenuSubroutine
 *      AddOptionToDropdownMenuSubroutine
 *      ChangeDropdownMenuSelectedOptionSubroutine
 *      PopulateYearDropdownMenuSubroutine
 *      PopulateCategoryDropdownMenuSubroutine
 *      PopulateCategoryDropdownMenusSubroutine
 *      
 *      ChangeStartYearSubroutine
 *      ChangeEndYearSubroutine
 *      ChangeTypeSubroutine
 *      ChangeOperatorSubroutine
 *      ChangeDamageSubroutine
 *      ChangePhaseSubroutine
 *      ChangeNatureSubroutine
 *      ChangeCountrySubroutine
 *      
 *      UpdateAllMapMarkersSubroutine
 *      UpdateAirportMapMarkersSubroutine
 * 
 *      InitializeWebPageSubroutine
 *      
 *
 *  Date        Description                             Programmer
 *  ----------  ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

// These objects are the three overlay layers: aviation accidents, 
// departure airports, and destination airports.
let accidentsOverlayLayerGroup
      = L.layerGroup();

let departuresOverlayLayerGroup
      = L.layerGroup();

let destinationsOverlayLayerGroup
      = L.layerGroup();


// These lines of code declare the four map tile layers.
let outdoorsMapTileLayer 
      = L.tileLayer
        (
            'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', 
            {
                attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
                tileSize: 512,
                maxZoom: 18,
                zoomOffset: -1,
                id: 'mapbox/outdoors-v11',
                accessToken: API_KEY
            }
        );

let grayscaleMapTileLayer 
      = L.tileLayer
        (
            'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', 
            {
                attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
                tileSize: 512,
                maxZoom: 18,
                zoomOffset: -1,
                id: 'mapbox/light-v10',
                accessToken: API_KEY
            }
        );

let satelliteMapTileLayer 
      = L.tileLayer
        (
            'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}',
            {
                attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
                maxZoom: 18,
                id: 'mapbox.satellite',
                accessToken: API_KEY
            }
        );

let darkMapTileLayer 
      = L.tileLayer 
        (
            'https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', 
            {
                attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
                maxZoom: 18,
                id: 'dark-v10',
                accessToken: API_KEY
            }
        );


// This Dictionary contains the base map tile layers.
let baseMapTileLayerDictionary
        = {
              'Dark Map': darkMapTileLayer,
              'Satellite Map': satelliteMapTileLayer,
              'Outdoors Map': outdoorsMapTileLayer,
              'Grayscale Map': grayscaleMapTileLayer
          };

// This Dictionary contains three map overlay layers for aviation accidents, 
// departure airports, destination airports.
let overlayLayerGroupDictionary 
        = {
              'Accidents': accidentsOverlayLayerGroup,
              'Departure Airports': departuresOverlayLayerGroup,
              'Destination Airports': destinationsOverlayLayerGroup
          };

// This map object is the current map and displays the dark map 
// with the three overlay layers.
let currentMapObject 
        = L.map
            ('mapid', 
             {
                center: [30, -28.6731],
                zoom: 2.5,
                layers: [darkMapTileLayer,
                         accidentsOverlayLayerGroup,
                         departuresOverlayLayerGroup,
                         destinationsOverlayLayerGroup]
             }
            );

// This control object is the map legend.
let legendControlObject 
      = L.control
        (
            {position: 'bottomright'}
        );


// This Array includes the levels of fatalaties for color assignment.
let fatalitiesRangeIntegerArray
        = [1, 40, 80, 120, 160, 200];

// This Array holds current accident IDs
let currentAccidentIDStringArray
        = []


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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/26/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

async function FetchJsonDataFromURLFunction 
                (urlString) 
{
    var dataD3JsonObject 
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
 *  Function Name:  ChooseColorFromFatalitiesFunction
 *
 *  Function Description:  
 *      This function chooses a color based on the number of fatalities
 *      in an aviation accident.
 *
 *
 *  Function Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  Integer
 *          fatalitiesInteger
 *                          This parameter is the number of fatalities
 *                          from an aviation accident.
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ChooseColorFromFatalitiesFunction
            (fatalitiesInteger) 
{
    if (fatalitiesInteger > fatalitiesRangeIntegerArray[5])
    {
        return 'red';
    }
    else if (fatalitiesInteger > fatalitiesRangeIntegerArray[4])
    {
        return 'orangered';
    }
    else if (fatalitiesInteger > fatalitiesRangeIntegerArray[3])
    {
        return 'orange';
    }
    else if (fatalitiesInteger > fatalitiesRangeIntegerArray[2])
    {
        return 'gold';
    }
    else if (fatalitiesInteger > fatalitiesRangeIntegerArray[1])
    {
        return 'yellow';
    }
    else
    {
        return 'lightgreen';
    }
} // This right brace ends the block for the function, 
// ChooseColorFromFatalitiesFunction.


/****************************************************************************
 *
 *  Function Name:  SetMarkerSizeFromFatalitiesFunction
 *
 *  Function Description:  
 *      This function chooses a color based on the number of fatalities
 *      in an aviation accident.
 *
 *
 *  Function Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  Integer
 *          fatalitiesInteger
 *                          This parameter is the number of fatalities
 *                          from an aviation accident.
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function SetMarkerSizeFromFatalitiesFunction
            (fatalitiesInteger) 
{
    return Math.sqrt(fatalitiesInteger) * 20000;
} // This right brace ends the block for the function, 
// SetMarkerSizeFromFatalitiesFunction.


/****************************************************************************
 *
 *  Function Name:  ReturnStartYearFunction
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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ReturnStartYearFunction() 
{
    var startYearString;

    if (selectedDropdownMenuOptionsDictionary['startYear'] == 'Start Year')
    {
        startYearString = '1970';
    }
    else
    {
        startYearString = selectedDropdownMenuOptionsDictionary['startYear'];
    }

    return startYearString;
} // This right brace ends the block for the function, 
// ReturnStartYearFunction.


/****************************************************************************
 *
 *  Function Name:  ReturnEndYearFunction
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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ReturnEndYearFunction() 
{
    var endYearString;

    if (selectedDropdownMenuOptionsDictionary['endYear'] == 'End Year')
    {
        endYearString = '2022';
    }
    else
    {
        endYearString = selectedDropdownMenuOptionsDictionary['endYear'];
    }

    return endYearString;
} // This right brace ends the block for the function, 
// ReturnEndYearFunction.


/****************************************************************************
 *
 *  Subroutine Name:  CreateLegendSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine creates the legend for the base map.
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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function CreateLegendSubroutine() 
{
    legendControlObject
        .onAdd 
            = function() 
              {
                    var divDOMUtilityObject
                            = L.DomUtil
                               .create
                                    ('div', 
                                     'info legend');
   
                    divDOMUtilityObject.innerHTML 
                        += "<h4 style='text-align: center'>Fatalities</h3>";

                    for (var i = 0; 
                         i < fatalitiesRangeIntegerArray.length; 
                         i++)
                    {
                  
                        divDOMUtilityObject.innerHTML 
                            += '<i style = "background:' 
                                + ChooseColorFromFatalitiesFunction 
                                    (fatalitiesRangeIntegerArray[i] + 1) 
                                + '"></i> ' 
                                + fatalitiesRangeIntegerArray[i] 
                                + (fatalitiesRangeIntegerArray[i+ 1] ? '&ndash;' 
                                + fatalitiesRangeIntegerArray[i + 1] 
                                + '<br>' : '+')
                  
                    }
  
                    return divDOMUtilityObject;
              };

    legendControlObject
        .addTo
          (currentMapObject);

    L.control
     .layers
     (   
        baseMapTileLayerDictionary, 
        overlayLayerGroupDictionary, 
        {collapsed: true}
     )
     .addTo
        (currentMapObject);
} // This right brace ends the block for the subroutine, 
// CreateLegendSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  InsertDefaultAsFirstInDropdownMenuSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine inserts the dropdown menu's default value as its
 *      first value.
 *
 *
 *  Subroutine Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  String
 *          dropdownIDString
 *                          This parameter is the identification for a
 *                          particular dropdown menu.
 * String
 *          selectElementObject
 *                          This parameter is the dropdown menu object.
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function InsertDefaultAsFirstInDropdownMenuSubroutine
            (dropdownIDString,
             selectElementObject)
{
    var defaultOptionString;

    if (dropdownIDString == 'selectStartYear')
    {
        defaultOptionString 
            = defaultSelectedDropdownMenuOptionsDictionary['startYear'];

        selectedDropdownMenuOptionsDictionary['startYear'] 
            = '1970';
    }
    else if (dropdownIDString == 'selectEndYear')
    {
        defaultOptionString 
            = defaultSelectedDropdownMenuOptionsDictionary['endYear'];

        selectedDropdownMenuOptionsDictionary['startYear'] 
            = '2022';
    }
    else if (dropdownIDString == 'selectType')
    {
        defaultOptionString
            = defaultSelectedDropdownMenuOptionsDictionary['types'];

        selectedDropdownMenuOptionsDictionary['types'] 
            = defaultSelectedDropdownMenuOptionsDictionary['types'];
    }
    else if (dropdownIDString == 'selectOperator')
    {
        defaultOptionString 
            = defaultSelectedDropdownMenuOptionsDictionary['operators'];

        selectedDropdownMenuOptionsDictionary['operators']
            = defaultSelectedDropdownMenuOptionsDictionary['operators'];
    }
    else if (dropdownIDString == 'selectDamage')
    {
        defaultOptionString 
            = defaultSelectedDropdownMenuOptionsDictionary['damage'];

        selectedDropdownMenuOptionsDictionary['damage']
            = defaultSelectedDropdownMenuOptionsDictionary['damage'];
    }
    else if (dropdownIDString == 'selectPhase')
    {
        defaultOptionString 
            = defaultSelectedDropdownMenuOptionsDictionary['phase'];

        selectedDropdownMenuOptionsDictionary['phase']
            = defaultSelectedDropdownMenuOptionsDictionary['phase'];
    }
    else if (dropdownIDString == 'selectNature')
    {
        defaultOptionString 
            = defaultSelectedDropdownMenuOptionsDictionary['nature'];

        selectedDropdownMenuOptionsDictionary['nature']
            = defaultSelectedDropdownMenuOptionsDictionary['nature'];
    }
    else
    {
        defaultOptionString 
            = defaultSelectedDropdownMenuOptionsDictionary['country'];

        selectedDropdownMenuOptionsDictionary['country']
            = defaultSelectedDropdownMenuOptionsDictionary['country'];
    }

    AddOptionToDropdownMenuSubroutine
        (selectElementObject,
         defaultOptionString);
} // This right brace ends the block for the subroutine, 
// InsertDefaultAsFirstInDropdownMenuSubroutine.


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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
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
 *      This subroutine adds one option to a dropdown menu.
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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
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

    for (var i = 0; i< selectElementObject.options.length; i++)
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
 *  Subroutine Name:  PopulateYearDropdownMenuSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine populates a year dropdown with the full range of years
 *      from the aviation accident data set.
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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function PopulateYearDropdownMenuSubroutine
            (dropdownIDString) 
{
    FetchJsonDataFromURLFunction 
        ('http://127.0.0.1:5000/api/v1.0/years')
            .then
            (
                (yearStringArray => 
                    {
                        var selectElementObject 
                                = document
                                    .getElementById
                                        (dropdownIDString);
         
                        for (var i = 0; i < yearStringArray.length; i++) 
                        {
                            AddOptionToDropdownMenuSubroutine
                                (selectElementObject,
                                 yearStringArray[i]);
                        }
                    }
                )
            );
} // This right brace ends the block for the subroutine, 
// PopulateYearDropdownMenuSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  PopulateCategoryDropdownMenuSubroutine 
 *
 *  Subroutine Description:  
 *      This subroutine populates a category dropdown menu with the full
 *      range of years from the aviation accident data set.
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
 * String
 *          categoryString
 *                          This parameter is the category identification
 *                          for the Flask API.
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function PopulateCategoryDropdownMenuSubroutine 
            (dropdownIDString,
             categoryString) 
{
    var routeURLString
            = 'http://127.0.0.1:5000/api/v1.0/categories/'
                + categoryString
                + '/'
                + selectedDropdownMenuOptionsDictionary['startYear']
                + '/'
                + selectedDropdownMenuOptionsDictionary['endYear'];
                
    FetchJsonDataFromURLFunction 
        (routeURLString)
            .then
            (
                (categoryStringArray => 
                    {
                        var selectElementObject 
                                = document
                                    .getElementById
                                        (dropdownIDString);

                        var lastElementIndexInteger
                                = selectElementObject.options.length - 1;

                        for (var i = lastElementIndexInteger; i >= 0; i--) 
                        {
                            selectElementObject.remove(i);
                        }
             
                        InsertDefaultAsFirstInDropdownMenuSubroutine
                            (dropdownIDString,
                             selectElementObject);

                        for (var i = 0; i < categoryStringArray.length; i++) 
                        {       
                            AddOptionToDropdownMenuSubroutine
                                (selectElementObject,
                                 categoryStringArray[i]);
                        }          
                    }
                )
            );
} // This right brace ends the block for the subroutine, 
// PopulateCategoryDropdownMenuSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  PopulateCategoryDropdownMenusSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine populates all the category dropdown menus when the
 *      user changes the start or end years.
 *
 *
 *  Subroutines Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  n/a     n/a             n/a
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function PopulateCategoryDropdownMenusSubroutine()
{
    PopulateCategoryDropdownMenuSubroutine 
        ('selectType',
         'type');

    PopulateCategoryDropdownMenuSubroutine 
        ('selectOperator',
         'operator');

    PopulateCategoryDropdownMenuSubroutine 
        ('selectDamage',
         'damage');

    PopulateCategoryDropdownMenuSubroutine 
        ('selectPhase',
         'phase');

    PopulateCategoryDropdownMenuSubroutine 
        ('selectNature',
         'nature');

    PopulateCategoryDropdownMenuSubroutine 
        ('selectCountry',
         'country');


    selectedDropdownMenuOptionsDictionary['types'] 
        = defaultSelectedDropdownMenuOptionsDictionary['types'];

    selectedDropdownMenuOptionsDictionary['operators'] 
        = defaultSelectedDropdownMenuOptionsDictionary['operators'];

    selectedDropdownMenuOptionsDictionary['damage'] 
        = defaultSelectedDropdownMenuOptionsDictionary['damage'];

    selectedDropdownMenuOptionsDictionary['phase'] 
        = defaultSelectedDropdownMenuOptionsDictionary['phase'];

    selectedDropdownMenuOptionsDictionary['nature'] 
        = defaultSelectedDropdownMenuOptionsDictionary['nature'];

    selectedDropdownMenuOptionsDictionary['country'] 
        = defaultSelectedDropdownMenuOptionsDictionary['country'];
} // This right brace ends the block for the subroutine, 
// PopulateCategoryDropdownMenusSubroutine.


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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
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

    PopulateCategoryDropdownMenusSubroutine();

    UpdateAllMapMarkersSubroutine();
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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
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

    PopulateCategoryDropdownMenusSubroutine();

    UpdateAllMapMarkersSubroutine();
} // This right brace ends the block for the subroutine, 
// ChangeEndYearSubroutine.


/****************************************************************************
 *
 *  Subroutine Name: ChangeTypeSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine sets the aircraft type value when the user changes 
 *      the aircraft type dropdown meny.
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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ChangeTypeSubroutine
            (selectedIDString)
{
    selectedDropdownMenuOptionsDictionary['types']
        = selectedIDString;

    UpdateAllMapMarkersSubroutine();
} // This right brace ends the block for the subroutine, 
// ChangeTypeSubroutine.


/****************************************************************************
 *
 *  Subroutine Name: ChangeOperatorSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine sets the aircraft operator value when the user changes 
 *      the aircraft operator dropdown menu.
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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ChangeOperatorSubroutine
            (selectedIDString)
{
    selectedDropdownMenuOptionsDictionary['operators']
        = selectedIDString;

    UpdateAllMapMarkersSubroutine();
} // This right brace ends the block for the subroutine, 
// ChangeOperatorSubroutine.


/****************************************************************************
 *
 *  Subroutine Name: ChangeDamageSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine sets the aircraft damage value when the user changes 
 *      the aircraft damage dropdown menu.
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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ChangeDamageSubroutine
            (selectedIDString)
{
    selectedDropdownMenuOptionsDictionary['damage']
        = selectedIDString;

    UpdateAllMapMarkersSubroutine();
} // This right brace ends the block for the subroutine, 
// ChangeDamageSubroutine.


/****************************************************************************
 *
 *  Subroutine Name: ChangePhaseSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine sets the flight phase value when the user changes 
 *      the flight phase dropdown menu.
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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ChangePhaseSubroutine
            (selectedIDString)
{
    selectedDropdownMenuOptionsDictionary['phase']
        = selectedIDString;

    UpdateAllMapMarkersSubroutine();
} // This right brace ends the block for the subroutine, 
// ChangePhaseSubroutine.


/****************************************************************************
 *
 *  Subroutine Name: ChangeNatureSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine sets the nature of flight value when the user changes 
 *      the nature of flight dropdown menu.
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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ChangeNatureSubroutine
            (selectedIDString)
{
    selectedDropdownMenuOptionsDictionary['nature']
        = selectedIDString;

    UpdateAllMapMarkersSubroutine();
} // This right brace ends the block for the subroutine, 
// ChangeNatureSubroutine.


/****************************************************************************
 *
 *  Subroutine Name: ChangeCountrySubroutine
 *
 *  Subroutine Description:  
 *      This subroutine sets the aviation accident's country location 
 *      when the user changes the country dropdown menu.
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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function ChangeCountrySubroutine
            (selectedIDString)
{
    selectedDropdownMenuOptionsDictionary['country']
        = selectedIDString;

    UpdateAllMapMarkersSubroutine();
} // This right brace ends the block for the subroutine, 
// ChangeCountrySubroutine.


/****************************************************************************
 *
 *  Subroutine Name: UpdateAllMapMarkersSubroutine 
 *
 *  Subroutine Description:  
 *      This subroutine creates and displays aviation all the markers 
 *      on the map.
 *
 *
 *  Subroutines Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
 *  n/a     n/a             n/a
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function UpdateAllMapMarkersSubroutine()
{
    var layerExistsBoolean
            = true;

    if (currentMapObject.hasLayer(accidentsOverlayLayerGroup) == false)
    {
        layerExistsBoolean = false;
    }

    var startYearString
            = ReturnStartYearFunction();

    var endYearString
            = ReturnEndYearFunction();
    
    var routeURLString
            = 'http://127.0.0.1:5000/api/v1.0/accidents/'
                + startYearString
                + '/'
                + endYearString
                + '/'
                + selectedDropdownMenuOptionsDictionary['types']
                + '/'
                + selectedDropdownMenuOptionsDictionary['operators']
                + '/'
                + selectedDropdownMenuOptionsDictionary['damage']
                + '/'
                + selectedDropdownMenuOptionsDictionary['phase']
                + '/'
                + selectedDropdownMenuOptionsDictionary['nature']
                + '/'
                + selectedDropdownMenuOptionsDictionary['country'];

    accidentsOverlayLayerGroup.clearLayers();

    accidentsOverlayLayerGroup.addTo(currentMapObject);

    FetchJsonDataFromURLFunction 
        (routeURLString)
            .then
            (
                (accidentsGeoJSONDictionary => 
                    {
                        for (var i = 0; 
                             i < accidentsGeoJSONDictionary.features.length; 
                             i++)
                        {
                            L.circle
                            (
                                ([accidentsGeoJSONDictionary.features[i].geometry.coordinates[0],
                                  accidentsGeoJSONDictionary.features[i].geometry.coordinates[1]]), 
                                 {
                                    radius: SetMarkerSizeFromFatalitiesFunction
                                                (accidentsGeoJSONDictionary.features[i].properties.fatalities),
                                    fillColor: ChooseColorFromFatalitiesFunction
                                                (accidentsGeoJSONDictionary.features[i].properties.fatalities),
                                    fillOpacity: 0.7,
                                    color: 'black',
                                    stroke: true,
                                    weight: 0.5
                                 }
                            )
                            .bindPopup
                            (
                                '<p> Date: ' + accidentsGeoJSONDictionary.features[i].properties.date + '</p>'
                                + '<p> Type: ' + accidentsGeoJSONDictionary.features[i].properties.type + '</p>'
                                + '<p> Operator: ' + accidentsGeoJSONDictionary.features[i].properties.operator + '</p>'
                                + '<p> Fatalities: ' + accidentsGeoJSONDictionary.features[i].properties.fatalities + '</p>'
                                + '<p> Occupants: ' + accidentsGeoJSONDictionary.features[i].properties.occupants + '</p>'
                                + '<p> Damage: ' + accidentsGeoJSONDictionary.features[i].properties.damage + '</p>'
                                + '<p> Phase: ' + accidentsGeoJSONDictionary.features[i].properties.phase + '</p>'
                                + '<p> Nature: ' + accidentsGeoJSONDictionary.features[i].properties.nature + '</p>'
                                + '<p> Departure: ' + accidentsGeoJSONDictionary.features[i].properties.departure + '</p>'
                                + '<p> Destination: ' + accidentsGeoJSONDictionary.features[i].properties.destination + '</p>'
                                + '<p> Location: ' + accidentsGeoJSONDictionary.features[i].properties.location + '</p>'
                                + '<p> Country: ' + accidentsGeoJSONDictionary.features[i].properties.country + '</p>'
                            )
                            .addTo(accidentsOverlayLayerGroup);
                             
                            if (layerExistsBoolean == false)
                            {
                                currentMapObject.removeLayer(accidentsOverlayLayerGroup);
                            }
                            else
                            {
                                accidentsOverlayLayerGroup.addTo(currentMapObject); 
                            }
                        }
                    }
                )
            );

    UpdateAirportMapMarkersSubroutine
        (startYearString,
         endYearString,
         selectedDropdownMenuOptionsDictionary['types'],
         selectedDropdownMenuOptionsDictionary['operators'],
         selectedDropdownMenuOptionsDictionary['damage'],
         selectedDropdownMenuOptionsDictionary['phase'],
         selectedDropdownMenuOptionsDictionary['nature'],
         selectedDropdownMenuOptionsDictionary['country'],
         'departure');
   
    UpdateAirportMapMarkersSubroutine
        (startYearString,
         endYearString,
         selectedDropdownMenuOptionsDictionary['types'],
         selectedDropdownMenuOptionsDictionary['operators'],
         selectedDropdownMenuOptionsDictionary['damage'],
         selectedDropdownMenuOptionsDictionary['phase'],
         selectedDropdownMenuOptionsDictionary['nature'],
         selectedDropdownMenuOptionsDictionary['country'],
         'destination');
} // This right brace ends the block for the subroutine, 
// UpdateAllMapMarkersSubroutine.


/****************************************************************************
 *
 *  Subroutine Name: UpdateAirportMapMarkersSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine creates and displays the current airport markers 
 *      on the map.
 *
 *
 *  Subroutines Parameters:
 *
 *  Type    Name            Description
 *  -----   -------------   ----------------------------------------------
  *  String
 *          startYearString
 *                          This parameter is the start year for the 
 *                          aviation accidents.
 *  String
 *          endYearString
 *                          This parameter is the end year for the 
 *                          aviation accidents.
 *  String
 *          typesString
 *                          This parameter is the aircraft type.
 *  String
 *          operatorssString
 *                          This parameter is the aircraft operator.
 *  String
 *          damageString
 *                          This parameter is the aircraft damage.
 *  String
 *          phaseString
 *                          This parameter is the flight phase.
 *  String
 *          natureString
 *                          This parameter is the nature of the flight.
 *  String
 *          countryString
 *                          This parameter is the country of the accident.
 *  String
 *          airportTypeString
 *                          This parameter is the type of airport 
 *                          (departure/destination).
 *
 * 
 *  Date        Description                             Programmer
 *  --------    ------------------------------------    ------------------
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function UpdateAirportMapMarkersSubroutine
            (startYearString,
             endYearString,
             typesString,
             operatorsString,
             damageString,
             phaseString,
             natureString,
             countryString,
             airportTypeString)
{

    var routeURLString
            = 'http://127.0.0.1:5000/api/v1.0/airports/'
                + startYearString
                + '/'
                + endYearString
                + '/'
                + typesString
                + '/'
                + operatorsString
                + '/'
                + damageString
                + '/'
                + phaseString
                + '/'
                + natureString
                + '/'
                + countryString
                + '/'
                + airportTypeString;

    if (airportTypeString == 'departure')
    {
        var currentOverlayLayerGroup
                = departuresOverlayLayerGroup;

        var markerIconObject
                = new 
                    L.Icon
                    (
                        {
                            iconUrl: './img/marker-icon-2x-blue.png',
                            shadowUrl: './img/marker-shadow.png',
                            iconSize: [22, 34],
                            iconAnchor: [12, 41],
                            popupAnchor: [1, -34],
                            shadowSize: [41, 41]
                        }
                    );
    }
    else if (airportTypeString == 'destination')
    {
        var currentOverlayLayerGroup
                = destinationsOverlayLayerGroup;

        var markerIconObject
                = new 
                    L.Icon
                    (
                        {
                            iconUrl: 'img/marker-icon-2x-orange.png',
                            shadowUrl: 'img/marker-shadow.png',
                            iconSize: [18, 30],
                            iconAnchor: [12, 41],
                            popupAnchor: [1, -34],
                            shadowSize: [41, 41]
                        }
                    );
    }
    else
    {
        return;
    }

    var layerExistsBoolean
            = true;

    if (currentMapObject.hasLayer(currentOverlayLayerGroup) == false)
    {
        layerExistsBoolean = false;
    }
        
    currentOverlayLayerGroup.clearLayers();

    currentOverlayLayerGroup.addTo(currentMapObject);

    FetchJsonDataFromURLFunction 
        (routeURLString)
            .then
            (
                (airportsGeoJSONDictionary => 
                    {
                        for (var i = 0; i < airportsGeoJSONDictionary.features.length; i++)
                        {
                            L.marker
                            (
                                [airportsGeoJSONDictionary.features[i].geometry.coordinates[0],
                                 airportsGeoJSONDictionary.features[i].geometry.coordinates[1]], 
                                {icon: markerIconObject}
                            )
                            .bindPopup
                            (
                                '<h3> Name: ' + airportsGeoJSONDictionary.features[i].properties.name + '</h3><hr>'
                                + '<p> Country: ' + airportsGeoJSONDictionary.features[i].properties.country + '</p>'
                                + '<p> ICAO: ' + airportsGeoJSONDictionary.features[i].properties.icao + '</p>'
                                + '<p> IATA: ' + airportsGeoJSONDictionary.features[i].properties.iata + '</p>'
                            )
                            .addTo(currentOverlayLayerGroup);

                            if (layerExistsBoolean == false)
                            {
                                currentMapObject.removeLayer(currentOverlayLayerGroup);
                            }
                            else
                            {
                                currentOverlayLayerGroup.addTo(currentMapObject); 
                            }
                        }
                    }
                )
            );
} // This right brace ends the block for the subroutine, 
// UpdateAirportMapMarkersSubroutine.


/****************************************************************************
 *
 *  Subroutine Name:  InitializeWebPageSubroutine
 *
 *  Subroutine Description:  
 *      This subroutine initializes the Aviation Accidents Visualization
 *      Toolkit by populating the drop down menus and setting up the
 *      legend, dropdown menus, and map layers.
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
 *  10/18/2023  Initial Development                     Theresa Bravo
 *  10/24/2023  Integrated code with new data set       N. James George
 *
 ****************************************************************************/

function InitializeWebPageSubroutine () 
{
    PopulateYearDropdownMenuSubroutine
        ('selectStartYear');

    PopulateYearDropdownMenuSubroutine
        ('selectEndYear');

    selectedDropdownMenuOptionsDictionary['startYear'] 
        = '1970';

    selectedDropdownMenuOptionsDictionary['endYear'] 
        = '2022';

    PopulateCategoryDropdownMenusSubroutine();

    CreateLegendSubroutine();

    UpdateAllMapMarkersSubroutine();
} // This right brace ends the block for the subroutine, 
// InitializeWebPageSubroutine.


InitializeWebPageSubroutine();