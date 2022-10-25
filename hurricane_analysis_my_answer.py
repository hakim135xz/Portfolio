# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def update_damage(damages_list):
    new_damages = []
    new_damages_float = []
    for string in damages:
        if "." in string and "M" in string:
            new_damages.append(string.replace(".", "").replace("M", "00000"))
        elif "." in string and "B" in string:
            new_damages.append(string.replace(".", "").replace("B", "00000000"))
        elif "M" in string:
            new_damages.append(string.replace("M", "000000"))
        elif "B" in string:
            new_damages.append(string.replace("B", "000000000"))
        else:
            new_damages.append(string)
    for string in new_damages:
        if "a" in string:
            new_damages_float.append(string)
        else:
            new_damages_float.append(float(string))
    return new_damages_float
    

# testing the update damage function

#print(update_damage(damages))

updated_damages = ['Damages not recorded', 100000000.0, 'Damages not recorded', 40000000.0, 27900000.0, 5000000.0, 'Damages not recorded', 306000000.0, 2000000.0, 65800000.0, 326000000.0, 60300000.0, 208000000.0, 14200000000.0, 25400000.0, 'Damages not recorded', 15400000000.0, 12400000000.0, 7100000000.0, 10000000000.0, 26500000000.0, 6200000000.0, 53700000000.0, 23300000000.0, 10100000000.0, 125000000000.0, 12000000000.0, 29400000000.0, 17600000000.0, 720000000.0, 15100000000.0, 64800000000.0, 91600000000.0, 25100000000.0]

# write your construct hurricane dictionary function here:

hurricane_data_dictionary = {}
def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    for i in range(len(names)):
        dictio = {"Name": names[i], "Month": months[i], "Year": years[i], "Max_sustained_winds": max_sustained_winds[i], "Areas_affected": areas_affected[i], "Damages": damages[i], "Deaths": deaths[i]}
        hurricane_data_dictionary[names[i]] = dictio
    return hurricane_data_dictionary


# testing dict function

hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)

#print(hurricane_data_dictionary)

# write your construct hurricane by year dictionary function here:


def hurrican_by_year(dictionary):
    year_dictionary = dict()
    for item in dictionary:
        list_key = dictionary[item]["Year"]
        list_value = dictionary[item]
        if list_key not in dictionary[item]:
            year_dictionary[list_key] = list_value
        else:
            year_dictionary[list_key].append(list_value)
    return year_dictionary

# testing function year

year_dictionary = hurrican_by_year(hurricane_data_dictionary)
#print(year_dictionary[1932])

# write your count affected areas function here:

area_count = dict()
area_affect = []
def count_affected_areas(dictionary):
    for item in dictionary:
        for area in dictionary[item]["Areas_affected"]:
            area_affect.append(area)
            for item in area_affect:
                area_count[area] = area_affect.count(area)
    return area_count

area_count = count_affected_areas(hurricane_data_dictionary)

#print(area_count)

# write your find most affected area function here:

def most_affected_areas(dictionary):
    max_area = 'Central America'
    max_area_count = 0
    for area in dictionary:
        if dictionary[area] > max_area_count:
            max_area = area
            max_area_count = dictionary[area]
    return (max_area, max_area_count)

max_area, max_area_count = most_affected_areas(area_count)

#print(max_area, max_area_count)
    

# write your greatest number of deaths function here:

cane_by_deaths = dict()
def hurricane_by_deaths(dictionary):
    for cane in dictionary:
        cane_by_deaths[cane] = dictionary[cane]['Deaths']
    return cane_by_deaths

cane_by_deaths = hurricane_by_deaths(hurricane_data_dictionary)
#print(cane_by_deaths)

def hurricane_highest_kill_count(dictionary):
    highest_kill = 'Mitch'
    highest_count = 0
    for cane in dictionary:
        if dictionary[cane] > highest_count:
            highest_kill = cane
            highest_count = dictionary[cane]
    return highest_kill, highest_count
        
highest_kill, highest_count = hurricane_highest_kill_count(cane_by_deaths)
#print(highest_kill, highest_count)

# write your catgeorize by mortality function here:

def hurricane_mortality(dictionary):
    mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for cane in dictionary:
        num_deaths = dictionary[cane]['Deaths']
        if num_deaths == mortality_scale[0]:
            hurricanes_by_mortality[0].append(dictionary[cane])
        elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
            hurricanes_by_mortality[1].append(dictionary[cane])
        elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
            hurricanes_by_mortality[2].append(dictionary[cane])
        elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
            hurricanes_by_mortality[3].append(dictionary[cane])
        elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
            hurricanes_by_mortality[4].append(dictionary[cane])
        elif num_deaths > mortality_scale[4]:
            hurricanes_by_mortality[5].append(dictionary[cane])
    return hurricanes_by_mortality

hurricanes_by_mortality = hurricane_mortality(hurricane_data_dictionary)
#print(hurricanes_by_mortality[5])

# write your greatest damage function here:

cane_by_damage = dict()
def hurricane_by_damage(dictionary):
    for cane in dictionary:
        cane_by_damage[cane] = dictionary[cane]['Damages']
    return cane_by_damage

cane_by_damage = hurricane_by_damage(hurricane_data_dictionary)
#print(cane_by_damage)

def hurricane_highest_damage(dictionary):
    highest_name = 'Mitch'
    highest_damage = 0
    for cane in dictionary:
        if dictionary[cane] == 'Damages not recorded':
            pass
        elif dictionary[cane] > highest_damage:
            highest_name = cane
            highest_damage = dictionary[cane]
    return highest_name, highest_damage

highest_name, highest_damage = hurricane_highest_damage(cane_by_damage)
#print(highest_name, highest_damage)

# write your catgeorize by damage function here:

def hurricane_damages(dictionary):
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    hurricanes_by_damages = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for cane in dictionary:
        num_damage = dictionary[cane]['Damages']
        if num_damage == damage_scale[0]:
            hurricanes_by_damages[0].append(dictionary[cane])
        elif num_damage > damage_scale[0] and num_damage <= damage_scale[1]:
            hurricanes_by_damages[1].append(dictionary[cane])
        elif num_damage > damage_scale[1] and num_damage <= damage_scale[2]:
            hurricanes_by_damages[2].append(dictionary[cane])
        elif num_damage > damage_scale[2] and num_damage <= damage_scale[3]:
            hurricanes_by_damages[3].append(dictionary[cane])
        elif num_damage > damage_scale[3] and num_damage <= damage_scale[4]:
            hurricanes_by_damages[4].append(dictionary[cane])
        elif num_damage > damage_scale[4]:
            hurricanes_by_damages[5].append(dictionary[cane])
    return hurricanes_by_damages

hurricanes_by_damages = hurricane_mortality(hurricane_data_dictionary)
print(hurricanes_by_damages[3])


