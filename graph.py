import matplotlib.pyplot as plt 
from datetime import datetime
import numpy as np 
from read_data import read_earthquakes, read_cities
import math
from statistics import strong_per_month

def barplot_earthquake(time_start, time_end, list_of_regions, show):
	"""
	draws a barplot for the earthquakes that happened between time_start and time_end in one the regions of list_of_regions.
	If the boolean variable show is True, the function will plot the graph, otherwise it will save it into the folder ../graphs with a unique identifier. 
	This function takes the following arguments: time_start, time_end, list_of_regions, show. 
	time_start and time_end are objects such as datetime(2018, 04, 19) and datetime(2019, 02, 24) for instance.
	list_of_regions is a list of the regions of your choice such as central_south_america, polynesia, etc.
	"""
	magnitude = np.array(['4.0-4.9', '5.0-5.9', '6.0-6.9', '7.0-7.9', '8.0'])
	list_earthquakes_1 = []
	list_earthquakes_2 = []
	list_earthquakes_3 = []
	list_earthquakes_4 = []
	list_earthquakes_5 = []
	for region in list_of_regions:
		np_data_earth = read_earthquakes(region)
		time_filter_start = np_data_earth[:, 0] >= time_start
		time_filter_end = np_data_earth[:, 0] <= time_end
		np_data_earth_timefilter = np_data_earth[np.logical_and(time_filter_start, time_filter_end)]
		for cell in np_data_earth[:, 1]:
			if float(cell) <= 4.9 and float(cell) >= 4.0:
				list_earthquakes_1.append(cell)
			if float(cell) <= 5.9 and float(cell) >= 5.0:
				list_earthquakes_2.append(cell)
			if float(cell) <= 6.9 and float(cell) >= 6.0:
				list_earthquakes_3.append(cell)
			if float(cell) <= 7.9 and float(cell) >= 7.0:
				list_earthquakes_4.append(cell)
			if float(cell) >= 8.0:
				list_earthquakes_5.append(cell)
			list_all = [len(list_earthquakes_1), len(list_earthquakes_2), len(list_earthquakes_3), len(list_earthquakes_4), len(list_earthquakes_5)]
		plt.title('Earthquakes that happened between %s and %s in %s' %(time_start, time_end, region)) 
		x_pos = np.arange(len(magnitude))
		bc = plt.bar(x_pos, list_all, color='g')
		plt.xticks(x_pos, magnitude)
		plt.ylabel('Number of earthquakes')
		plt.xlabel('Order of magnitude')
		if show == True:
			plt.show()
		else:
			plt.savefig('graphs/earthquake_%s_%s.png' %(region, repr(datetime.now())))

def piechart_strong_earthquake(time_start, time_end, show):
	"""
	draws a piechart of the proportion of strong earthquakes in each region between time_start and time_end. 
	If the boolean variable show is True, the function will plot the graph, otherwise it will save it into the folder ../graphs with a unique identifier. 
	This function takes the following arguments: time_start, time_end, show. 
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
	list_earthquake = []
	for region in list_of_regions:
		np_data_earth = read_earthquakes(region) 
		time_filter_start = np_data_earth[:, 0] >= time_start
		time_filter_end = np_data_earth[:, 0] <= time_end
		magn_filter = np_data_earth[:, 1] > 5
		depth_filter = np_data_earth[:, 4] < 70
		np_data_earth_filter = np_data_earth[np.all([magn_filter, depth_filter, time_filter_start, time_filter_end], axis=0)]
		list_earthquake.append(len(np_data_earth_filter))
	plt.figure(1, figsize=(6,6))
	fracs = np.array(list_earthquake)
	plt.pie(fracs, labels=list_of_regions, autopct='%1.2f%%',shadow=False) 
	plt.title('Percentage of strong earthquakes between %s and %s in each region' %(time_start, time_end))
	if show: 
		plt.show()
	else:
		plt.savefig('graphs/number_earthquakes_piechart_%s.png' %repr(datetime.now()))

def map_earthquake(k, time_start, time_end, show):
	"""
	draws a 2D map of the k strongest earthquakes between time_start and time_end. 
	This function takes the following arguments: k, time_start, time_end, show.
	k is an integer of your choice that stands for the number of strong eartquakes you are interest in e.g. k = 1000.
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
	colors_dict = {
		"polynesia" : 'red',
		"fiji_tonga" : 'navy',
		"cascadia": 'cyan',
		"aleutian_isles" : 'g',
		"japan" : 'darkorange',
		"south_east_asia" : 'orchid',
		"central_america" : 'fuchsia',
		"central_south_america" : 'deepskyblue',
		"mediterranean" : 'olive',
		"east_africa" : 'yellow',
		"horn_of_africa" : 'tomato'
	}
	list_earthquakes = []
	np_earthquakes_total_region = np.empty([0, 7], dtype=float)
	for region in list_of_regions:
		np_data_earth_region = read_earthquakes(region)
		np_name_region = np.full([len(np_data_earth_region), 1], colors_dict[region])
		np_data_earth = np.concatenate((np_data_earth_region, np_name_region), axis=1)
		np_earthquakes_total_region = np.concatenate((np_data_earth, np_earthquakes_total_region), axis=0)
	time_filter_start = np_earthquakes_total_region[:, 0] >= time_start
	time_filter_end = np_earthquakes_total_region[:, 0] <= time_end
	np_data_earth_filter = np_earthquakes_total_region[np.all([time_filter_start, time_filter_end], axis=0)]
	sorted_list_earth = sorted(np_data_earth_filter, key=lambda earthquake_row: earthquake_row[1], reverse=True)
	k_sorted_earthquakes = sorted_list_earth[:k]
	np_list_earthquakes = np.array(k_sorted_earthquakes)
	MAP_WIDTH = 100.0
	MAP_HEIGHT = 100.0
	list_points_x = []
	list_points_y = []
	for row in np_list_earthquakes:
		latitude = row[2]
		longitude = row[3]
		x = (MAP_WIDTH / 360.0) * (180 + longitude)
		y = (MAP_HEIGHT / 180.0) * (latitude - 90)
		list_points_x.append(x)
		list_points_y.append(y)
	np_points_x = np.array(list_points_x)
	np_points_y = np.array(list_points_y)
	colors = np_list_earthquakes[:, 6]
	plt.scatter(np_points_x, np_points_y, c=colors, alpha=0.5)
	plt.title('2D map of the %d earthquakes between %s and %s' %(k, time_start, time_end))
	plt.show()

def graph_strong_earthquakes_month(region, show):
	"""
	takes a region and a boolean variable show as arguments, and returns a barchart with the number of strong earthquakes that happened in this region per month. 
	If the boolean variable show is True, the function will plot the graph, otherwise it will save it into the folder ../graphs with a unique identifier. 
	"""
	np_strong_earthquakes_region = strong_per_month(region)
	x_pos = np.arange(len(np_strong_earthquakes_region))
	bc = plt.bar(x_pos, np_strong_earthquakes_region[:, 1], color='b')
	x_pos_2 = np.arange(0, len(np_strong_earthquakes_region), 4)
	plt.xticks(x_pos_2, np_strong_earthquakes_region[:, 0], rotation=40)
	plt.ylabel('Number of strong earthquakes')
	plt.xlabel('Month')
	plt.title('Number of strong earthquakes in %s per month' %region)
	if show == True:
		plt.show()
	else:
		plt.savefig('graphs/strong_earthquake_in_%s_permonth_%s.png' %(region, repr(datetime.now())))

if __name__ == "__main__":
	time_start = datetime(2018, 0o4, 19)
	time_end = datetime(2019, 0o2, 24)
	list_of_regions = ['polynesia', 'central_south_america']
	show = True
	k = 10000

	#barplot = barplot_earthquake(time_start, time_end, list_of_regions, show)	
	piechart = piechart_strong_earthquake(time_start, time_end, show)	
	map_e = map_earthquake(k, time_start, time_end, show)

	region = 'central_south_america'
	#graph_bar = graph_strong_earthquakes_month(region, show)
	#print graph_bar
