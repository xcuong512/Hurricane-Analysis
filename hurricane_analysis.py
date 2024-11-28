# 1
# Update Recorded Damages
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 
           'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', 
           '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', 
           '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', 
           '91.6B', '25.1B']

def update_damage(damages):
    conversion = {
        'M': 1000000,
        'B': 1000000000
    }
    updated_damages = []
    for damage in damages:
        if damage == 'Damages not recorded':
            updated_damages.append(damage)
        if damage.find('M') != - 1:
            updated_damages.append(float(damage[0:damage.find('M')]) * conversion['M'])
        if damage.find('B') != - 1:
            updated_damages.append(float(damage[0:damage.find('B')]) * conversion['B'])
    return updated_damages

updated_damages = update_damage(damages)
# print(updated_damages)

# 2 
# Create and view the hurricanes dictionary
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 
         'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 
         'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 
         'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']
# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 
          'September', 'September', 'September', 'September', 'October', 'September', 'August', 
          'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 
          'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 
          'October', 'September', 'September', 'October']
# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 
         1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 
         2016, 2017, 2017, 2018]
# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 
                       175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 
                       175, 160]
# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], 
                  ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], 
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], 
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], 
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], 
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], 
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], 
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], 
                  ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], 
                  ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], 
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], 
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], 
                  ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], 
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], 
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], 
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]
# print(areas_affected)
# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,
          51,124,17,1836,125,87,45,133,603,138,3057,74]

def create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricane_dictionary = {}
    for i in range(len(names)):
        hurricane_dictionary[names[i]] = {
            'Name': names[i],
            'Month': months[i],
            'Year': years[i],
            'Max Sustained Wind': max_sustained_winds[i],
            'Areas Affected': areas_affected[i],
            'Damage': updated_damages[i],
            'Death': deaths[i]
        }
    return hurricane_dictionary

hurricane_dictionary = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
# print(hurricane_dictionary)
        
# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key
def year_key(hurricane_dictionary):
    dict_by_year = {}
    for cane in hurricane_dictionary:
        current_year = hurricane_dictionary[cane]['Year']
        current_cane = [cane]
        if current_year not in dict_by_year:
            dict_by_year[current_year] = current_cane
        else:
            dict_by_year[current_year].append(current_cane)
    return dict_by_year

dictionary_by_year = year_key(hurricane_dictionary)
# print(dictionary_by_year)

# 4
# Counting Damaged Areas
def damage_by_area(hurricane_dictionary):
    area_count = {}
    for cane in hurricane_dictionary:
        for area in hurricane_dictionary[cane]['Areas Affected']:
            if area in area_count:
                area_count[area] += 1
            else:
                area_count[area] = 1
    return area_count

counting_damaged_areas = damage_by_area(hurricane_dictionary)
# print(counting_damaged_areas)

# 5 
# Calculating Maximum Hurricane Count
def max_hurricane_count(counting_damaged_areas):
    max_areas = 'Mexico'
    max_count = 0
    for area in counting_damaged_areas:
        if counting_damaged_areas[area] > max_count:
            max_areas = area
            max_count = counting_damaged_areas[area]
    return max_areas, max_count

maximum_hurricane_count = max_hurricane_count(counting_damaged_areas)
# print(maximum_hurricane_count)

# 6
# Calculating the Deadliest Hurricane
def max_death(hurricane_dictionary):
    max_death_cane = 'Michael'
    max_death_count = 0
    for cane in hurricane_dictionary:
        if hurricane_dictionary[cane]['Death'] > max_death_count:
            max_death_cane = cane
            max_death_count = hurricane_dictionary[cane]['Death']
    return max_death_cane, max_death_count

deadliest_hurricane = max_death(hurricane_dictionary)
# print(deadliest_hurricane)

# 7
# Rating Hurricanes by Mortality
def rating_hurricane(hurricane_dictionary):
    mortality_scale = {
        0: 0,
        1: 100,
        2: 500,
        3: 1000,
        4: 10000
    }
    hurricane_by_mortality = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: []
    }
    for cane in hurricane_dictionary:
        if hurricane_dictionary[cane]['Death'] == mortality_scale[0]:
            hurricane_by_mortality[0].append(hurricane_dictionary[cane])
        elif hurricane_dictionary[cane]['Death'] > mortality_scale[0] and hurricane_dictionary[cane]['Death'] <= mortality_scale[1]:
            hurricane_by_mortality[1].append(hurricane_dictionary[cane])
        elif hurricane_dictionary[cane]['Death'] > mortality_scale[1] and hurricane_dictionary[cane]['Death'] <= mortality_scale[2]:
            hurricane_by_mortality[2].append(hurricane_dictionary[cane])
        elif hurricane_dictionary[cane]['Death'] > mortality_scale[2] and hurricane_dictionary[cane]['Death'] <= mortality_scale[3]:
            hurricane_by_mortality[3].append(hurricane_dictionary[cane])
        elif hurricane_dictionary[cane]['Death'] > mortality_scale[3] and hurricane_dictionary[cane]['Death'] <= mortality_scale[4]:
            hurricane_by_mortality[4].append(hurricane_dictionary[cane])
        else:
            hurricane_by_mortality[5].append(hurricane_dictionary[cane])
    return hurricane_by_mortality

rating_hurricane_mortality = rating_hurricane(hurricane_dictionary)
# print(rating_hurricane_mortality)

# 8 Calculating Hurricane Maximum Damage
def maximum_damage(hurricane_dictionary):
    max_cane = 'Michael'
    max_damage = 0
    for cane in hurricane_dictionary:
        if hurricane_dictionary[cane]['Damage'] == 'Damages not recorded':
            pass
        elif hurricane_dictionary[cane]['Damage'] > max_damage:
            max_cane = cane
            max_damage = hurricane_dictionary[cane]['Damage']
    return max_cane, max_damage

hurricane_max_damage = maximum_damage(hurricane_dictionary)
# print(hurricane_max_damage)

# 9
# Rating Hurricanes by Damage
def rating_by_damage(hurricane_dictionary):
    damage_scale = {
        0: 0,
        1: 100000000,
        2: 1000000000,
        3: 10000000000,
        4: 50000000000
    }
    rating_damages = {
        0: [], 
        1: [], 
        2: [], 
        3: [], 
        4: [], 
        5: []
    }
    for cane in hurricane_dictionary:
        if hurricane_dictionary[cane]['Damage'] == damage_scale[0] or hurricane_dictionary[cane]['Damage'] == 'Damages not recorded':
            rating_damages[0].append(hurricane_dictionary[cane])
        elif hurricane_dictionary[cane]['Damage'] > damage_scale[0] and hurricane_dictionary[cane]['Damage'] <= damage_scale[1]:
            rating_damages[1].append(hurricane_dictionary[cane])
        elif hurricane_dictionary[cane]['Damage'] > damage_scale[1] and hurricane_dictionary[cane]['Damage'] <= damage_scale[2]:
            rating_damages[2].append(hurricane_dictionary[cane])
        elif hurricane_dictionary[cane]['Damage'] > damage_scale[2] and hurricane_dictionary[cane]['Damage'] <= damage_scale[3]:
            rating_damages[3].append(hurricane_dictionary[cane])
        elif hurricane_dictionary[cane]['Damage'] > damage_scale[3] and hurricane_dictionary[cane]['Damage'] <= damage_scale[4]:
            rating_damages[4].append(hurricane_dictionary[cane])
        elif hurricane_dictionary[cane]['Damage'] > damage_scale[4]:
            rating_damages[5].append(hurricane_dictionary[cane])
    return rating_damages

rating_hurricane_damages = rating_by_damage(hurricane_dictionary)
print(rating_hurricane_damages)
            
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    