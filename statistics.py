import numpy as np 
from datetime import datetime
from read_data import read_earthquakes, read_cities
import math 

def print_array(np_array, name):
	"""
	takes a two-dimensional numpy array and its name and prints the information contained in it.
	This function takes the following arguments: np_array and its name.
	"""
	print('The name of the two-dimensional array is %s' %name)
	print("Matrix[" + ("%d" %np_array.shape[1]) + "] [" + ("%d" %np_array.shape[0]) + "]")
	for row in np_array:
		list_row = []
		for element in row:
			new_element = str(element)
			list_row.append(new_element)
		print("\t|\t".join(list_row))

def earthquake_frequency(min_magnitude, max_magnitude, time_start, time_end, list_of_regions, show):
	"""
	returns a numpy array that contains, for each region in the given list of regions, the total number of 
	earthquakes of magnitude between the min and the max given that happened between the time_start and time_end. 
	If the boolean variable show is True, the function will print out the array. 
	This function takes the following arguments: min_magnitude, max_magnitude, time_start, time_end, list_of_regions, show.
	max_magnitude and min_magnitude are floats of your choice between 1 and 10. 
	time_start and time_end are objects such as datetime(2018, 04, 19) and datetime(2019, 02, 24) for instance. 
	list_of_regions is a list of the regions of your choice such as central_south_america, polynesia, etc. 
	"""
	list_earthquakes = []
	for region in list_of_regions:
		np_data_earth = read_earthquakes(region)
		magn_filter_max = np_data_earth[:, 1] <= max_magnitude
		magn_filter_min = np_data_earth[:, 1] >= min_magnitude
		time_filter_start = np_data_earth[:, 0] >= time_start
		time_filter_end = np_data_earth[:, 0] <= time_end
		np_data_earth_filter = np_data_earth[np.all([magn_filter_max, magn_filter_min, time_filter_start, time_filter_end], axis=0)]
		list_earthquakes.append([len(np_data_earth_filter)])
	np_list_earthquakes = np.array(list_earthquakes)
	if show == True:
		print_array(np_list_earthquakes, 'Earthquake frequency')
	return np_list_earthquakes

def strongest_earthquakes(k, time_start, time_end, list_of_regions, show):
	"""
	returns a numpy array which, for each region in list_of_region, contains the information about k strongest 
	(by magnitude) earthquakes which happened between time_start and time_end. 
	If the boolean variable show is True, the function will print out the k strongest earthquakes for each region. 
	This function takes the following arguments: k, time_start, time_end, list_of_regions, show. 
	k is an integer of your choice.
	time_start and time_end are objects such as datetime(2018, 04, 19) and datetime(2019, 02, 24) for instance.
	list_of_regions is a list of the regions of your choice such as central_south_america, polynesia, etc. 
	"""
	list_earthquakes = []
	for region in list_of_regions:
		np_data_earth = read_earthquakes(region)
		time_filter_start = np_data_earth[:, 0] >= time_start
		time_filter_end = np_data_earth[:, 0] <= time_end
		np_data_earth_filter = np_data_earth[np.logical_and(time_filter_start, time_filter_end)] 
		sorted_list_earth = sorted(np_data_earth_filter, key=lambda earthquake_row: earthquake_row[1], reverse=True)
		k_sorted_earthquakes = sorted_list_earth[:k]
		list_earthquakes.append(k_sorted_earthquakes)
	np_list_earthquakes = np.array(list_earthquakes)
	if show == True:
		for element in np_list_earthquakes:
			print_array(element, 'strongest earthquakes')
	return np_list_earthquakes

def city_risk(name_city, R, time_start, time_end):
	"""
	returns the number of strong earthquakes (magnitude >5, depth < 70 km) that happened between time_start and time_end 
	at a distance at most R from the name_city. 
	This function takes the following arguments: name_city, R, time_start, time_end. 
	name_city is the name of the city og your choice e.g. 'andorra'
	R is an integer in km that stands for the maximum distance between the city you chose and the strongest earthquakes. 
	time_start and time_end are objects such as datetime(2018, 04, 19) and datetime(2019, 02, 24) for instance.
	"""
	list_of_regions = [
		"polynesia", 
		"fiji_tonga", 
		"cascadia", 
		"aleutian_isles", 
		"japan", 
		"south_east_asia", 
		"central_america", 
		"central_south_america", 
		"mediterranean", 
		"east_africa", 
		"horn_of_africa"
	]
	np_earthquakes_total_region = np.empty([0, 6], dtype=float)
	for region in list_of_regions:
		np_data_earth = read_earthquakes(region) 
		np_earthquakes_total_region = np.concatenate((np_data_earth, np_earthquakes_total_region), axis=0)
	time_filter_start = np_earthquakes_total_region[:, 0] >= time_start
	time_filter_end = np_earthquakes_total_region[:, 0] <= time_end
	magn_filter = np_earthquakes_total_region[:, 1] > 5
	depth_filter = np_earthquakes_total_region[:, 4] < 70
	np_data_earth_filter = np_earthquakes_total_region[np.all([magn_filter, depth_filter, time_filter_start, time_filter_end], axis=0)]
	np_cities = read_cities("data/worldcitiespop.csv")
	latitude_city = None
	longitude_city = None
	for city in np_cities:
		if city[0] == name_city: 
			latitude_city = float(city[1])
			longitude_city = float(city[2])
	if latitude_city == None:
		print("The city is not in our list")
		return 
	earth_radius = 6371
	list_distance_earthquake_city = []
	for row in np_data_earth_filter:
		latitude_earthquake = row[2]
		longitude_earthquake = row[3]
		a = math.sin((latitude_city - latitude_earthquake) / 2)**2 + math.cos(latitude_city) * math.cos(latitude_earthquake) * (math.sin((longitude_city - longitude_earthquake) / 2)**2)
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
		distance = earth_radius * c
		list_distance_earthquake_city.append(distance)
	np_distance_earthquake_city = np.array(list_distance_earthquake_city)
	comparison_filter = np_distance_earthquake_city <= R 
	return len(np_distance_earthquake_city[comparison_filter])

def strong_per_month(region):
	"""
	takes a region (e.g. 'central_south_america') and a boolean variable show as arguments, and returns an array with the number of strong earthquakes that happened in this region per month.
	"""
	np_data_region = read_earthquakes(region)
	magn_filter_7 = np_data_region[:, 1] >= 7
	np_data_region_filter = np_data_region[magn_filter_7]
	date_max = max(np_data_region[:, 0])
	date_min = min(np_data_region[:, 0])
	list_dates = []
	month = date_min.month
	year = date_min.year 
	while month <= date_max.month or year < date_max.year: 
		list_dates.append([str(month) + "/" + str(year), 0])
		month = month + 1 
		if month == 13:
			month = 1
			year = year + 1 
	np_list_dates = np.array(list_dates, dtype=object)
	for earthquake in np_data_region_filter:
		counter_index = (earthquake[0].year - date_min.year) * 12 + (earthquake[0].month - date_min.month) 
		np_list_dates[:, 1][counter_index] = np_list_dates[:, 1][counter_index] + 1
	return np_list_dates

def city_is_safe(name_city, length_stay_days):
	"""
	takes the name_city and length_stay_days as arguments and returns the probability not to have a strong earthquake in this peculiar city during your stay.
	length_stay_days is the duration of your stay in name_city expressed in days.
	"""
	list_of_regions = [
		"polynesia", 
		"fiji_tonga", 
		"cascadia", 
		"aleutian_isles", 
		"japan", 
		"south_east_asia", 
		"central_america", 
		"central_south_america", 
		"mediterranean", 
		"east_africa", 
		"horn_of_africa"
	]
	np_earthquakes_total_region = np.empty([0, 6], dtype=float)
	for region in list_of_regions:
		np_data_earth = read_earthquakes(region) 
		np_earthquakes_total_region = np.concatenate((np_data_earth, np_earthquakes_total_region), axis=0)
	magn_filter = np_earthquakes_total_region[:, 1] > 5
	depth_filter = np_earthquakes_total_region[:, 4] < 70
	np_data_earth_filter = np_earthquakes_total_region[np.all([magn_filter, depth_filter], axis=0)]
	np_cities = read_cities("data/worldcitiespop.csv")
	latitude_city = None
	longitude_city = None
	for city in np_cities:
		if city[0] == name_city: 
			latitude_city = float(city[1])
			longitude_city = float(city[2])
	if latitude_city == None:
		print("The city is not in our list")
		return 
	earth_radius = 6371
	list_distance_earthquake_city = []
	for row in np_data_earth_filter:
		latitude_earthquake = row[2]
		longitude_earthquake = row[3]
		a = math.sin((latitude_city - latitude_earthquake) / 2)**2 + math.cos(latitude_city) * math.cos(latitude_earthquake) * (math.sin((longitude_city - longitude_earthquake) / 2)**2)
		c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
		distance = earth_radius * c
		list_distance_earthquake_city.append(distance)
	np_distance_earthquake_city = np.array(list_distance_earthquake_city)
	comparison_filter = np_distance_earthquake_city <= 1000
	date_min = min(np_earthquakes_total_region[:, 0])
	date_max = max(np_earthquakes_total_region[:, 0])
	diff = date_max - date_min
	average = len(np_distance_earthquake_city[comparison_filter]) / float(diff.days) * length_stay_days
	return math.exp(-average)
	




