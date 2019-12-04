from statistics import print_array, earthquake_frequency, strongest_earthquakes, city_risk, strong_per_month, city_is_safe
from graph import barplot_earthquake, piechart_strong_earthquake, map_earthquake, graph_strong_earthquakes_month
from datetime import datetime

def ask(question, type_var):
	var = None
	while type(var) != type_var:
		var = input(question)
	return var

def main_project():
	print "Hello! Earthquake project is there. What would you like to learn? Here are the available options: "
	print '1 -> statistics'
	print '2 -> graphs'
	print '3 -> prediction'
	print '4 -> terminate the program'
	var = ask('Select one of the previous numbers: ', int)
	if var == 1:
		print "You have chosen the option statistics!"
		dictionaty_functions = {
		"print_array" : print_array.__doc__,
		"earthquake_frequency" : earthquake_frequency.__doc__,
		"strongest_earthquakes" : strongest_earthquakes.__doc__, 
		"city_risk" : city_risk.__doc__,
		"strong_per_month" : strong_per_month.__doc__
		}
		print "You can use the following functions: \n"
		for function, docstring in dictionaty_functions.items(): 
			print "The function %s %s" %(function, docstring)
		rep = ask("Would you like to choose one of the previous functions or go back to menu ? Yes/No: ", str)
		if rep == 'Yes': 
			choice = ask("Good choice! Which function would you like to use? ", str)
			if choice == 'print_array':
				print "The 2 arguments you need to specify is a two-dimensional numpy array and its name."
				np_array = input("Enter your array: ")
				name = ask("Enter the name of your array: ", str)
				result = print_array(np_array, name)
			if choice == 'earthquake_frequency':
				print "The arguments you need to specify are the minimal and maximal magnitude you want, the starting and ending time (format DD/MM/YYYY), a list of regions and a boolean variable"
				min_magnitude = ask("What is the minimal magnitude? ", float)
				max_magnitude = ask("What is the maximal magnitude? ", float)
				year_start = ask("What is the year YYYY of the starting time? ", int)
				month_start = ask("What is the month MM of the starting time? ", int)
				day_start = ask("What is the day DD of the starting time? ", int)
				time_start = datetime(year_start, month_start, day_start)
				year_end = ask("What is the year YYYY of the ending time? ", int)
				month_end = ask("What is the month MM of the ending time? ", int)
				day_end = ask("What is the day DD of the ending time? ", int)
				time_end = datetime(year_end, month_end, day_end)
				list_of_regions = ask("Enter a list of regions: ", list)
				show = ask("Choose between True or False for show: ", bool)
				result = earthquake_frequency(min_magnitude, max_magnitude, time_start, time_end, list_of_regions, show)
			if choice == 'strongest_earthquakes':
				print "The arguments you need to specify are an integer of your choice, the starting and ending time (format DD/MM/YYYY), the list of regions you are interested in and a boolean variable"
				k = ask("Enter an integer: ", int)
				year_start = ask("What is the year YYYY of the starting time? ", int)
				month_start = ask("What is the month MM of the starting time? ", int)
				day_start = ask("What is the day DD of the starting time? ", int)
				time_start = datetime(year_start, month_start, day_start)
				year_end = ask("What is the year YYYY of the ending time? ", int)
				month_end = ask("What is the month MM of the ending time? ", int)
				day_end = ask("What is the day DD of the ending time? ", int)
				time_end = datetime(year_end, month_end, day_end)
				list_of_regions = ask("Enter a list of regions: ", list)
				show = ask("Choose between True or False for show: ", bool)
				result = strongest_earthquakes(k, time_start, time_end, list_of_regions, show)
			if choice == 'city_risk':
				print "The arguments you need to specify are the name of the city, the maximum distance between the city you chose and the strongest earthquakes, the starting and ending time (format DD/MM/YYYY)"
				name_city = ask("Enter the name of the city you are interested in: ", str)
				R = ask("Enter an integer: ", int)
				year_start = ask("What is the year YYYY of the starting time? ", int)
				month_start = ask("What is the month MM of the starting time? ", int)
				day_start = ask("What is the day DD of the starting time? ", int)
				time_start = datetime(year_start, month_start, day_start)
				year_end = ask("What is the year YYYY of the ending time? ", int)
				month_end = ask("What is the month MM of the ending time? ", int)
				day_end = ask("What is the day DD of the ending time? ", int)
				time_end = datetime(year_end, month_end, day_end)
				result = city_risk(name_city, R, time_start, time_end)
				print "The number of strong earthquakes (magnitude >5, depth < 70 km) that happened between %s and %s is %s" %(time_start, time_end, result)
			if choice == 'strong_per_month':
				print "The argument you need to specify is the name of the region you care about"
				region = ask("Enter the name of the region you'd like to know more about: ", str)
				result = strong_per_month(region)
				print "The number of strong earthquakes that happened in this %s per month is: \n%s" %(region, result)
	if var == 2: 
		print "You have chosen the option graphs!"
		dictionaty_functions = {
		"barplot_earthquake" : barplot_earthquake.__doc__, 
		"piechart_strong_earthquake" : piechart_strong_earthquake.__doc__, 
		"map_earthquake" : map_earthquake.__doc__, 
		"graph_strong_earthquakes_month" : graph_strong_earthquakes_month.__doc__
		}
		print "You can use the following functions: \n"
		for function, docstring in dictionaty_functions.items(): 
			print "The function %s %s" %(function, docstring)
		rep = ask("Would you like to choose one of the previous functions or go back to menu ? Yes/No: ", str)
		if rep == 'Yes': 
			choice = ask("Good choice! Which function would you like to use? ", str)
			if choice == "barplot_earthquake":
				print "The arguments you need to specify are the starting and ending time (format DD/MM/YYYY) you want to consider, the list of regions you are interested in and a boolean variable"
				year_start = ask("What is the year YYYY of the starting time? ", str)
				month_start = ask("What is the month MM of the starting time? ", int)
				day_start = ask("What is the day DD of the starting time? ", int)
				time_start = datetime(year_start, month_start, day_start)
				year_end = ask("What is the year YYYY of the ending time? ", int)
				month_end = ask("What is the month MM of the ending time? ", int)
				day_end = ask("What is the day DD of the ending time? ", int)
				time_end = datetime(year_end, month_end, day_end)
				list_of_regions = ask("Enter a list of regions: ", list)
				show = ask("Choose between True or False for show: ", bool)
				result = barplot_earthquake(time_start, time_end, list_of_regions, show)
			if choice == "piechart_strong_earthquake":
				print "The arguments you need to specify are the starting and ending time (format DD/MM/YYYY) you want to consider and a boolean variable"
				year_start = ask("What is the year YYYY of the starting time? ", int)
				month_start = ask("What is the month MM of the starting time? ", int)
				day_start = ask("What is the day DD of the starting time? ", int)
				time_start = datetime(year_start, month_start, day_start)
				year_end = ask("What is the year YYYY of the ending time? ", int)
				month_end = ask("What is the month MM of the ending time? ", int)
				day_end = ask("What is the day DD of the ending time? ", int)
				time_end = datetime(year_end, month_end, day_end)
				show = ask("Choose between True or False for show: ", bool)
				result = piechart_strong_earthquake(time_start, time_end, show)
			if choice == "map_earthquake":
				print "The arguments you need to specify are the number of strong eartquakes you are interest, the starting and ending time (format DD/MM/YYYY) and a boolean variable"
				k = ask("Enter an integer: ", int)
				year_start = ask("What is the year YYYY of the starting time? ", int)
				month_start = ask("What is the month MM of the starting time? ", int)
				day_start = ask("What is the day DD of the starting time? ", int)
				time_start = datetime(year_start, month_start, day_start)
				year_end = ask("What is the year YYYY of the ending time? ", int)
				month_end = ask("What is the month MM of the ending time? ", int)
				day_end = ask("What is the day DD of the ending time? ", int)
				time_end = datetime(year_end, month_end, day_end)
				show = ask("Choose between True or False for show: ", bool)
				result = map_earthquake(k, time_start, time_end, show)
			if choice == "graph_strong_earthquakes_month":
				print "The arguments you need to specify are the region you care about and a boolean variable"
				region = ask("What region do you want to know more about? ", str)
				show = ask("Choose between True or False for show: ", bool)
				result = graph_strong_earthquakes_month(region, show)
	if var == 3: 
		print "You have chosen the option prediction!"
		dictionaty_functions = {
		"city_is_safe": city_is_safe.__doc__
		}
		print "You can use the following function: \n"
		for function, docstring in dictionaty_functions.items(): 
			print "The function %s %s" %(function, docstring)
		print "To use this function you need to specify the name of the city you will be staying in and the length of your stay in days"
		name_city = ask("What is the name of the city? ", str)
		length_stay_days = ask("Please enter the duration of your stay in days: ", int)
		result = city_is_safe(name_city, length_stay_days)
		print "\n"
		print "The probability not to have a strong earthquake is: %.6f" %result
	if var == 4:
		return True
	else:
		print "\n"
		return False

main = main_project()
while main == False: 
	main = main_project()


