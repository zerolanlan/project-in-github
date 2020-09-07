def moon_weight(start_weight, increase_weight,year):
    weight_every_year = []
    for year in range(year):
        weight = start_weight*0.165+ increase_weight*year*0.165
        weight_every_year.append(weight)
    print(weight_every_year)
        
input1 = float(input('Please enter your current Earth weight>',))
input2 = float(input('Please ebter the amount your weight might increase each year>',))
input3 = int(input('Please enter the number of years',))
moon_weight(input1,input2,input3)

