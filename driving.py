country=input("Which country were you from(Taiwan or US):")
age=int(input("How old are you:"))
if country == "Taiwan":
	if age >= 18:
		print("you are able to apply a license")
	else:
		print("you are not able to apply a license") 
elif country == "US":
	if age >= 16:
		print("you are able to apply a license")
	else:
		print("you are not able to apply a license") 
else:
	print("you can only type in Taiwan or US")
