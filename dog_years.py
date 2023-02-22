def dog_years(years):
    years = int(years)
    if years < 0:
        return("This is not an real age")
    return years*7
#this is where u put the dog years and it times 7 years

human_years = input('Enter your dog year')
print(dog_years(human_years))