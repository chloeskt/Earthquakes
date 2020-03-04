# Earthquakes

This was my first project in Python, done in May 2019 for the course 'Introduction to programming' at École Normale Supérieure de Paris (Ulm). 

## Step 1: Gather the data

Using BeautifulSoup we select the 25 000 newest earthquakes from http://ds.iris.edu/ieb/index.html, and for each earthquake we store the following fields: year, month, day, time, magnitude, latitude, longitude, depth, region.
To these features, we add a world cities databased (obtained from https://www.kaggle.com/max-mind/world-cities-database). 

The goal was then two create functions to read more easily the csv. files and print results in a nice way which allows the user to get a better glance at the data. 

## Step 2: Statistics on the data 

We implemented the following functions: 

- earthquake_frequency: this function returns a numpy array that for each region in list_of_regions contains the total number of earthquakes of magnitude between min_magnitude and max_magnitude that happened between time_start and time_end.If the variable show is True, the function should additionally print out the array using the function print_array.

- strongest_earthquakes: the function returns a numpy array that for each region in list_of_regions contains the informations about k strongest (by magnitude) earthquakes that happened between time_start and time_end. If the variable show is True, the function additionally prints out the k strongest earthquakes for each region in the list using the function print_array.

- city_risk: returns the number of strong earthquakes (magnitude > 5, depth < 70 km) that happened between time_start and time_end at distance at most R from the city. To compute the distance d between two points given their longitude and latitude, use the harvesine formula:

![a = \sin^2(\Delta \phi / 2) + \cos (\phi_1) \times \cos(\phi_2) \times \sin^2 (\Delta \lambda /2) ](https://render.githubusercontent.com/render/math?math=a%20%3D%20%5Csin%5E2(%5CDelta%20%5Cphi%20%2F%202)%20%2B%20%5Ccos%20(%5Cphi_1)%20%5Ctimes%20%5Ccos(%5Cphi_2)%20%5Ctimes%20%5Csin%5E2%20(%5CDelta%20%5Clambda%20%2F2)%20)

![c = 2 \times \arctan( \sqrt(a), \sqrt(1-a))](https://render.githubusercontent.com/render/math?math=c%20%3D%202%20%5Ctimes%20%5Carctan(%20%5Csqrt(a)%2C%20%5Csqrt(1-a)))

![d = R \times c](https://render.githubusercontent.com/render/math?math=d%20%3D%20R%20%5Ctimes%20c)


$ a = \sin^2(\Delta \phi / 2) + \cos (\phi_1) \times \cos(\phi_2) \times \sin^2 (\Delta \lambda /2) \\
c = 2 \times \arctan( \sqrt(a), \sqrt(1-a) \\
d = R \times c $

where phi_1 and phi_2 are the latitudes, $\Delta \lambda$ is the difference between longitutdes and $R$ is the earth's radius. 
