def check_blood_pressure(systolic, diastolic):
    if systolic < 90 and diastolic < 60:
        result = "Low"
    elif systolic < 120 and diastolic < 80:
        result = "Ideal"
    elif systolic < 140 and diastolic < 90:
        result = "Pre-high"
    else: 
        result = "High"
    return result

test_systolic = 110
test_diastolic = 85

print(check_blood_pressure(test_systolic, test_diastolic))