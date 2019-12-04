import numpy as np 
from datetime import datetime

def read_earthquakes(region_name):
	"""
	This function takes a region name as an argument and returns numpy arrays containing the data in the file
	"""
	filename = "data/dataearth_%s.csv" %region_name
	file = open(filename, 'r')
	lines = file.readlines()
	file.close()
	data_earth = []
	for line in lines[1:]:
		year, month, day, time, magnitude, latitude, longitude, depth, district = line.strip().split(";")
		hour, minute, second = time.split(':')
		d = datetime(int(year), int(month), int(day), int(hour), int(minute), int(float(second)))
		data_earth.append([d, float(magnitude), float(latitude), float(longitude), float(depth), district])
	np_data_earth = np.array(data_earth)
	return np_data_earth

def read_cities(filename):
	"""
	This function takes the name of a csv file as argument and returns numpy array containing the city, the latitude and the longitude
	"""
	file = open(filename, 'r')
	lines = file.readlines()
	file.close()
	data_cities = []
	for line in lines[1:]:
		country, city, accentcity, region, population, latitude, longitude = line.strip().split(",")
		data_cities.append([city, float(latitude), float(longitude)])
	np_data_cities = np.array(data_cities)
	return np_data_cities


if __name__ == "__main__":
	region_name = "japan"
	np_data_earth = read_earthquakes(region_name)
	print np_data_earth

	filename2 = "data/worldcitiespop.csv"
	np_data_cities = read_cities(filename2)
	print np_data_cities

