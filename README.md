![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/1ca02e8d-bd3c-4e10-8361-819ab8cec8b0)

# Aviation Accidents Visualization Project
----
Air travel stands as an undeniable revolution in the transportation sector, delivering a multitude of invaluable advantages: unprecedented speed, unparalleled global connectivity, and a continuous drive for innovation. Nevertheless, the aviation industry encounters its fair share of challenges, especially concerning the issue of safety. In this project, we delve into the intricate tapestry of aviation safety, exploring how it varies among different countries, aircraft types, and operators in a comprehensive analysis of over 50 years of aviation accident data (1970-2022). 

Questions we considered:
* Where are aviation accidents likely to occur?
* In recent years, are there certain airlines that have more crashes than others?
* Are there outside factors affecting these trends?

To find the answers to our many questions, we obtained the requisite information by means of a customized Extract-Transform-Load process. The procurement of aviation accident information began with web scraping information sources on the Internet.  Subsequently, an initial review of the information showed important details mixed together with irrelenant ones in various and inconsistent forms.  To compensate for this obstacle, we implemented algorithms to parse text for important specifics, verify or augment information using APIs and other sources, and standardize the data.  After placing the cleaned information in an SQLite database, a Flask API provided the information to front-end applications in an efficent and effective manner. To accomplish our goal of interactive visualization, we employed certain technologies -- D3, JSON, JS, Plotly, Bootstrap, among others -- and aimed to create an informative representation of historical aviation accident data, which could allow stakeholders to uncover patterns, trends, and insight.

## Aviation Accidents Worldwide Visualization Toolkit:

![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/811b062a-d574-4d0e-807e-388ffe3443f0)

![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/e670cc73-e09b-4263-8583-b3ba341f5175)

![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/d91573cd-9001-4250-b707-5c59084e43d4)

## Aviation Accidents Worldwide Heatmap Toolkit:

![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/5acddd9f-f938-4ff6-9072-7a10d97685a9)

![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/cb121ea0-def8-4656-b24b-40da1dda95f1)

![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/a7aa13af-9682-4d26-ae4f-0cfe29c80977)

## Aviation Accidents Worldwide Dashboard:

<img width="1679" alt="Screenshot 2023-11-05 at 12 31 54 PM" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/b7e7b9e4-fe96-4542-8ad0-e0901e00a27c">

<img width="1679" alt="Screenshot 2023-11-05 at 12 33 55 PM" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/e2d62e39-c49e-4403-a3b1-b50512384ae4">

To best convey our findings, we summarized them in a series of visual aids. First, our analysis revealed a downward trend in fatalities from aviation accidents over the last fifty years. 

<img width="617" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/177588e2-cf44-4a1d-8b06-e48e3e4234dc">

This downward trend also manifested itself in a lower average casualty rate per flight and lower and narrower casualty rate distributions.

<img width="741" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/c52b3b28-3b31-412e-9f4a-1a236af69550">

<img width="741" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/8df7472d-6f0c-4cd7-9632-ea08fb3c48b9">

Overall and most recently, accidents occur when the aircraft is en route or approaching its destination.

<img width="623" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/c304e4ad-a0b3-4dad-b50d-1521ff48f053">

In the last fifty years, Aeroflot has been the airline with the highest fatalities although these accidents primarily occurred in the 1970s and 1980s during the Soviet era. In the last two years, China Eastern Airlines has had a troubling number of fatalities in a time of safer aircraft and practices.

<img width="404" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/61ab3880-a4fb-448b-80f6-fc201ac90587"><img width="404" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/40821864-b1c8-4af3-ba87-73dc3aed0e54">

The aircraft most prone to fatalities from aviation accidents is the Tupolev TU-154, a Soviet era aircraft, followed by the Lockheed L-1011 and Boeing 727.  In the last twenty years or so the Boeing 737 has been the leader in this infamous category.

<img width="404" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/23a05db8-b849-430a-a957-604f2b61aa64">

<img width="506" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/a99ffbe9-7e5e-4052-9b90-c22ca7ac582c">

<img width="404" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/09da2831-5195-486e-a471-1efbd0d942d3">

In any period, domestic scheduled passenger flights are most likely to have fatalities from aviation accidents followed by international scheduled passenger flights.

<img width="720" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/9d4720a7-4462-48b0-a4e8-32fc00491566">

In the last decade or so, certain Chinese airports have had the largest proportion of accidents.

<img width="404" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/68cd9132-4722-4b22-82f0-64780efb5a87"><img width="404" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/e7f957f4-c01c-4e06-ade3-e789a17c3a08">

Also, Russia has consistently been the a location for high numbers of fatalities even though China has lately taken on that mantle.

<img width="432" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/c4949211-48c4-4547-b81b-040a596b9078">

<img width="432" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/d1812e69-2394-4c4b-b528-629522cc16b8">

Ultimately, we could not accurately predict the locations of aircraft accidents only the likelihood based on past events, but we did observe some trends.  During the last ten years, China Eastern Airlines has experienced the largest fatalities. Although the reasons for and concentrations of aviation accidents varied from decade to decade, currently, possible outside factors include terrorism, poor maintenance, and employee malfeasance, misfeasance, or nonfeasance. The next flight on China Eastern Airlines' domestic passenger flight from Kunming Changshui International Airport to Guangzhou Baiyun International Airport on a Boeing 737 should likely be avoided!In the future, these numbers should be compared with total flight data to render percentages as the metric.

----
## **Authors and Acknowledgment:**

## Group 3 members:
Arame Diasse, Jackie Ochuida, Nicholas George, Rajib Maji, Stephen Grantham, Theresa Bravo, Vishnu Pillai

## Copyright

N. James George © 2023. All Rights Reserved.
