import requests 
from bs4 import BeautifulSoup

links = [
	"http://ds.iris.edu/ieb/evtable.phtml?caller=IEB&st=1970-01-01&et=2025-01-01&ob=time-desc&li=25000&xla=-0.014&nla=-39.910&xlo=-57.656&nlo=-89.283&sbl=1&pbl=1&caller=self&name=Central%20South%20America&zm=4&mt=ter&rgn=Central%20South%20America&title=IEB%20export%3A%2025000%20earthquakes%20as%20a%20sortable%20table.&stitle=from%20the%20earliest%20to%20the%20latest%20available%2C%20all%20mags%2C%20all%20depths%2C%20with%20priority%20for%20most%20recent%2C%20and%20limited%20to%2025000.",
	"http://ds.iris.edu/ieb/evtable.phtml?caller=IEB&st=1970-01-01&et=2025-01-01&ob=time-desc&li=25000&xla=14.000&nla=-33.000&xlo=-155.000&nlo=93.000&sbl=1&pbl=1&caller=self&name=Polynesia&zm=3&mt=ter&rgn=Polynesia&title=IEB%20export%3A%2025000%20earthquakes%20as%20a%20sortable%20table.&stitle=from%20the%20earliest%20to%20the%20latest%20available%2C%20all%20mags%2C%20all%20depths%2C%20with%20priority%20for%20most%20recent%2C%20and%20limited%20to%2025000.",
	"http://ds.iris.edu/ieb/evtable.phtml?caller=IEB&st=1970-01-01&et=2025-01-01&ob=time-desc&li=25000&xla=-12.100&nla=-32.200&xlo=-164.800&nlo=170.500&sbl=1&pbl=1&caller=self&name=Fiji%20Tonga%20Region&zm=5&mt=ter&rgn=Fiji%20Tonga%20Region&title=IEB%20export%3A%2025000%20earthquakes%20as%20a%20sortable%20table.&stitle=from%20the%20earliest%20to%20the%20latest%20available%2C%20all%20mags%2C%20all%20depths%2C%20with%20priority%20for%20most%20recent%2C%20and%20limited%20to%2025000.",
	"http://ds.iris.edu/ieb/evtable.phtml?caller=IEB&st=1970-01-01&et=2025-01-01&ob=time-desc&li=25000&xla=51.000&nla=38.000&xlo=-118.000&nlo=-128.000&sbl=1&pbl=1&caller=self&name=Cascadia&zm=5&mt=ter&rgn=Cascadia&title=IEB%20export%3A%2025000%20earthquakes%20as%20a%20sortable%20table.&stitle=from%20the%20earliest%20to%20the%20latest%20available%2C%20all%20mags%2C%20all%20depths%2C%20with%20priority%20for%20most%20recent%2C%20and%20limited%20to%2025000.",
	"http://ds.iris.edu/ieb/evtable.phtml?caller=IEB&st=1970-01-01&et=2025-01-01&ob=time-desc&li=25000&xla=57.000&nla=48.000&xlo=-156.000&nlo=168.000&sbl=1&pbl=1&caller=self&name=Aleutian%20Islands&zm=5&mt=ter&rgn=Aleutian%20Islands&title=IEB%20export%3A%2025000%20earthquakes%20as%20a%20sortable%20table.&stitle=from%20the%20earliest%20to%20the%20latest%20available%2C%20all%20mags%2C%20all%20depths%2C%20with%20priority%20for%20most%20recent%2C%20and%20limited%20to%2025000.",
	"http://ds.iris.edu/ieb/evtable.phtml?caller=IEB&st=1970-01-01&et=2025-01-01&ob=time-desc&li=25000&xla=56.000&nla=22.000&xlo=159.000&nlo=127.000&sbl=1&pbl=1&caller=self&name=Japan%20Region&zm=4&mt=ter&rgn=Japan%20Region&title=IEB%20export%3A%2025000%20earthquakes%20as%20a%20sortable%20table.&stitle=from%20the%20earliest%20to%20the%20latest%20available%2C%20all%20mags%2C%20all%20depths%2C%20with%20priority%20for%20most%20recent%2C%20and%20limited%20to%2025000.",
	"http://ds.iris.edu/ieb/evtable.phtml?caller=IEB&st=1970-01-01&et=2025-01-01&ob=time-desc&li=25000&xla=37.720&nla=9.800&xlo=107.580&nlo=64.510&sbl=1&pbl=1&caller=self&name=S.E.%20Asia%20Region&zm=4&mt=ter&rgn=S.E.%20Asia%20Region&title=IEB%20export%3A%2025000%20earthquakes%20as%20a%20sortable%20table.&stitle=from%20the%20earliest%20to%20the%20latest%20available%2C%20all%20mags%2C%20all%20depths%2C%20with%20priority%20for%20most%20recent%2C%20and%20limited%20to%2025000.",
	"http://ds.iris.edu/ieb/evtable.phtml?caller=IEB&st=1970-01-01&et=2025-01-01&ob=time-desc&li=25000&xla=28.770&nla=4.920&xlo=-53.440&nlo=-118.480&sbl=1&pbl=1&caller=self&name=Central%20America&zm=4&mt=ter&rgn=Central%20America&title=IEB%20export%3A%2025000%20earthquakes%20as%20a%20sortable%20table.&stitle=from%20the%20earliest%20to%20the%20latest%20available%2C%20all%20mags%2C%20all%20depths%2C%20with%20priority%20for%20most%20recent%2C%20and%20limited%20to%2025000.",
	"http://ds.iris.edu/ieb/evtable.phtml?caller=IEB&st=1970-01-01&et=2025-01-01&ob=time-desc&li=25000&xla=48.220&nla=31.580&xlo=45.880&nlo=7.560&sbl=1&pbl=1&caller=self&name=E.%20Mediterranean&zm=5&mt=ter&rgn=E.%20Mediterranean&title=IEB%20export%3A%2025000%20earthquakes%20as%20a%20sortable%20table.&stitle=from%20the%20earliest%20to%20the%20latest%20available%2C%20all%20mags%2C%20all%20depths%2C%20with%20priority%20for%20most%20recent%2C%20and%20limited%20to%2025000.",
	"http://ds.iris.edu/ieb/evtable.phtml?caller=IEB&st=1970-01-01&et=2025-01-01&ob=time-desc&li=25000&xla=48.220&nla=31.580&xlo=45.880&nlo=7.560&sbl=1&pbl=1&caller=self&name=E.%20Mediterranean&zm=5&mt=ter&rgn=E.%20Mediterranean&title=IEB%20export%3A%2025000%20earthquakes%20as%20a%20sortable%20table.&stitle=from%20the%20earliest%20to%20the%20latest%20available%2C%20all%20mags%2C%20all%20depths%2C%20with%20priority%20for%20most%20recent%2C%20and%20limited%20to%2025000.",
	"http://ds.iris.edu/ieb/evtable.phtml?caller=IEB&st=1970-01-01&et=2025-01-01&ob=time-desc&li=25000&xla=21.170&nla=0.000&xlo=59.000&nlo=37.000&sbl=1&pbl=1&caller=self&name=Horn%20of%20Africa&zm=5&mt=ter&rgn=Horn%20of%20Africa&title=IEB%20export%3A%2012290%20earthquakes%20as%20a%20sortable%20table.&stitle=from%20the%20earliest%20to%20the%20latest%20available%2C%20all%20mags%2C%20all%20depths%2C%20with%20priority%20for%20most%20recent%2C%20and%20limited%20to%2025000.",
]

names_regions = [
	"central_south_america",
	"polynesia", 
	"fiji_tonga", 
	"cascadia", 
	"aleutian_isles", 
	"japan", 
	"south_east_asia", 
	"central_america", 
	"mediterranean", 
	"east_africa", 
	"horn_of_africa"
]
k = 0 
for link in links:
	page = requests.get(link)
	soup = BeautifulSoup(page.content, "html.parser")
	info = soup.select('td')
	data = []
	for tag in info :
		data.append(tag.get_text())
	data_eq = []
	for i in range(0, len(data), 11):
		data_eq.append(data[i:i+9])
	name = "data/dataearth_%s.csv" %names_regions[k]
	out_file = open(name, "w")
	out_file.write("year;month;day;time;magnitude;latitude;longitude;depth;region\n")
	for eq in data_eq: 
		for i in range(9):
			out_file.write(eq[i])
			if not i == 8:
				out_file.write(";")
		out_file.write('\n')
	out_file.close()
	k = k + 1 
