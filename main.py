# IS code tables are given as functions

def findExposure():
    print('''Choose the exposure from the given options
    a. Mild
    b. Moderate
    c. Severe
    d. Very Severe
    e. Extreme''')
    exposure_opt = input('Enter your option (Example ; a or b or c etc.) : ')
    if exposure_opt == 'a' or exposure_opt == 'A':
        return 'mild'
    elif exposure_opt == 'b' or exposure_opt == 'B':
        return 'moderate'
    elif exposure_opt == 'c' or exposure_opt == 'C':
        return 'severe'
    elif exposure_opt == 'd' or exposure_opt == 'D':
        return 'v_severe'
    elif exposure_opt == 'e' or exposure_opt == 'E':
        return 'extreme'

def sigma(fck):
    if 10 <= fck <= 15:
        return 3.5
    elif 20 <= fck <= 25:
        return 4
    elif 30 <= fck <= 55:
        return 5

def waterCementRatio(exposure):
    if exposure == 'mild':
        return 0.55
    elif exposure == 'moderate':
        return 0.5
    elif exposure == 'severe' or exposure == 'v_severe':
        return 0.45
    elif exposure == 'extreme':
        return 0.4


def waterContent(size):
    if size == 10:
        return 208
    elif size == 20:
        return 186
    elif size == 40:
        return 165

def cementContent(exposure):
    if exposure == 'mild' or exposure == 'moderate':
        return 300
    elif exposure == 'severe':
        return 320
    elif exposure == 'v_severe':
        return 340
    elif exposure == 'extreme':
        return 360
def findZone():
    print('''Enter the zone of the coarse aggregate
    1. Zone I
    2. Zone II
    3. Zone III
    4. Zone IV''')
    zone_val = int(input('Enter the option number of the corresponding zone (Eg 1 or 2 etc.) : '))
    return zone_val

def coarseAggregate(zone,size):
    if size == 10:
        if zone == 1:
            return 0.5
        elif zone == 2:
            return 0.48
        elif zone == 3:
            return 0.46
        elif zone == 4:
            return 0.44
    elif size == 20:
        if zone == 1:
            return 0.66
        elif zone == 2:
            return 0.64
        elif zone == 3:
            return 0.62
        elif zone == 4:
            return 0.6
    elif size == 40:
        if zone == 1:
            return 0.75
        elif zone == 2:
            return 0.73
        elif zone == 3:
            return 0.71
        elif zone == 4:
            return 0.69


# Inputs required to calculate the mix design
# fck   exposure    size (size of CA in mm)   w_c (water cement ratio)     slump (in mm)   zone
# sp_cement  sp_ca  sp_fa      (sp = specific gravity)

fck = int(input('Enter compressive strength value or fck value (Example 20 or 30 etc.) :'))
size = int(input('Enter the size of coarse aggregate in mm (10 / 20 / 40)'))
slump = int(input('Enter maximum value of required slump value out of 100 in mm  (60 or 70 etc.) '))
w_c = float(input('Enter water content ratio (Example: 0.45 or 0.5):'))
sp_cement = 3.15
sp_CA = 2.9
sp_FA = 2.7
exposure = findExposure()
zone = findZone()


# Step 1 finding the target strength (fm value)

fm = fck + 1.65 * sigma(fck)

# Step 2 Determining water cement ratio

if w_c > waterCementRatio(exposure):
    w_c = waterCementRatio(exposure)

# Step 3 Selection of water content for mix

water_content = waterContent(size)
if 50 < slump > 75:
    water_content += water_content * 0.03
if  slump >= 75:
    water_content += water_content * 0.06

# Step 4 Selection of cement content for mix

cement_content = water_content / w_c
if cement_content < cementContent(exposure):
    cement_content = cementContent(exposure)

# Step 5 Estimation of Coarse Aggregate proportion for the mix
proportion_ca = coarseAggregate(zone,size)
proportion_fa = 1 - proportion_ca

# Step 6 Estimation of mix materials

vol_agg = 1 - ((cement_content/sp_cement)+water_content)*(1/1000)
vol_ca = vol_agg * proportion_ca
vol_fa = vol_agg * proportion_fa

wt_fa = sp_FA * proportion_fa * 1000
wt_ca = sp_CA * proportion_ca * 1000

# Step 7 Finding ratio of materials

C = cement_content / 1450 # Dividing with bulk density
FA = wt_fa / 1695
FA = round(FA / C,2)
CA = wt_ca / 1590
CA = round(CA / C,2)
C=1
w_c = water_content/cement_content

print('\nRequired design for the given specification is as follows')
print('Required water content ratio :', w_c)
print('Cement : Fine Aggregate : Coarse Aggregate =',C,':',FA,':',CA)

