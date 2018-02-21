
def bookstore(book_ID, *arg, **keyval):
	print(book_ID)
	for reff_num in arg:
		print(reff_num)
	for key in keyval:
		print(key,keyval[key])
bookstore("23234.5545","2435399.09324",4374861.46576, book1="OS", book2="IS", book3="Automat")

def population(country, state="TX", population_number="20453612"):
	print("The",state,"state is having", population_number," population in ",country)

p={ "country": "United States","state" : "TX","population_number" : "20453612"}
population(**p)


