![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/1ca02e8d-bd3c-4e10-8361-819ab8cec8b0)

# Aviation Accidents Visualization Project
----
Air travel stands as an undeniable revolution in the transportation sector, delivering a multitude of invaluable advantages: unprecedented speed, unparalleled global connectivity, and a continuous drive for innovation. Nevertheless, the aviation industry encounters its fair share of challenges and predicaments, especially concerning the issue of safety. In this project, we delve into the intricate tapestry of aviation safety, exploring how it varies among different countries, aircraft types, and operators. This project is a comprehensive analysis of aviation accident data collected over 50 years from 1970 to 2022. To accomplish our goal, we employed certain technologies -- D3, JSON, JS, Plotly, Bootstrap, among others -- and aimed to create an informative representation of historical aviation accident data, which could allow stakeholders to uncover patterns, trends, and insight.

Questions to be considered:
* Can we accurately predict where plane crashes are likely to occur?
* Are there certain airlines that have more crashes than others?
* Are there possible outside factors affecting these trends?

To find the answers to our many questions, we obtained the requisite information by means of a customized Extract-Transform-Load process. The procurement of aviation accident information began with web scraping information sources on the Internet.  Subsequently, an initial review of the information showed important details mixed together with irrelenant ones in various and inconsistent forms.  To compensate for this obstacle, we implemented algorithms to parse text for important specifics, verify or augment information using APIs and other sources, and standardize the data.  After placing the cleaned information in an SQLite database, a Flask API provided the information to front-end applications in an efficent and effective manner.  To make the information easily available to users, we created a dashboard and interactive toolkits with the requisite visualization technologies.

## Aviation Accidents Visualization Toolkit:

![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/811b062a-d574-4d0e-807e-388ffe3443f0)

![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/e670cc73-e09b-4263-8583-b3ba341f5175)

![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/d91573cd-9001-4250-b707-5c59084e43d4)

## Aviation Accidents Heatmap Toolkit:

![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/5acddd9f-f938-4ff6-9072-7a10d97685a9)

![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/cb121ea0-def8-4656-b24b-40da1dda95f1)

![image](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/a7aa13af-9682-4d26-ae4f-0cfe29c80977)

## Aviation Accidents Dashboard:

<img width="1679" alt="Screenshot 2023-11-05 at 12 31 54 PM" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/b7e7b9e4-fe96-4542-8ad0-e0901e00a27c">

<img width="1679" alt="Screenshot 2023-11-05 at 12 33 55 PM" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/e2d62e39-c49e-4403-a3b1-b50512384ae4">

On a positive note, our analysis demonstarted reduced mortality from aviation accidents over the last fifty years. We summarized our findings in a series of visual aids.

![download](https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/96cc92b2-8200-4ea6-a651-58167b787678)

<img width="548" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/08c897da-ec90-4fb8-8113-1b634a1156f9"><img width="548" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/eacad6d0-3f4f-48fb-9adb-4548efc12072">

<img width="548" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/fe7c1ea0-ad64-4a09-946d-3f875f7eeb05">

<img width="548" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/80ce7a58-549e-4c3f-bf0b-0e57783a7342">

<img width="548" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/af2324ae-bb87-47ad-ab12-db951ee8805a">

<img width="549" alt="image" src="https://github.com/njgeorge000158/Aviation-Accidents-Visualization-Project/assets/137228821/570722e3-7b13-4998-b1b8-b6e9f35dbe56">

Although we could not accurately predict the locations of plane crashes only the likelihood based on past events, we did observe some trends.  During the last ten years, China Eastern Airlines has experienced the largest fatalities. Although the reasons for and concentrations of aviation accidents varied from decade to decade, currently, possible outside factors include terrorism, poor maintenance, and employee malfeasance, misfeasance, or nonfeasance. But, one thing for certain, the next flight on China Eastern Airlines' domestic passenger flight from Kunming Changshui International Airport to Guangzhou Baiyun International Airport on a Boeing 737 should likely be avoided!


----
## **Authors and Acknowledgment:**

## Group 3 members:
Arame Diasse, Jackie Ochuida, Nicholas George, Rajib Maji, Stephen Grantham, Theresa Bravo, Vishnu Pillai

## Copyright

N. James George © 2023. All Rights Reserved.
