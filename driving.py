country=input("Which country were you from:")
age=int(input("How old are you:"))
if country == "Taiwan":
	if age >= 18:
		print("you are able to apply a license")
	else:
		print("you are not able to apply a license") 