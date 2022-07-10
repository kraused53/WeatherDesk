import geocoder

'''
	get_location():
		Use teh geocoder API to estimate user's
		current location using their computer's
		IP address.

		Returns a list containing location information
			['City, State', [lat, long]]
'''
def get_location():
	g = geocoder.ip('me')
	data = []
	data.append(str(g.city+', '+g.state))
	data.append(g.latlng)
	return data

# If location.py is run as main, print location to terminal
if __name__ == '__main__':
	print(get_location())