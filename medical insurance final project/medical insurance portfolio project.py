import csv


def percent_ratio(par1=0, name1="", par2=0, name2="", par3=0, name3="", par4=0, name4=""):
    summation = par1 + par2 + par3 + par4
    par1_cent_ratio = (par1 / summation) * 100
    par2_cent_ratio = (par2 / summation) * 100
    par3_cent_ratio = (par3 / summation) * 100
    par4_cent_ratio = (par4 / summation) * 100
    return f'''
They are in the percentage ratio: 
{name1}: {round(par1_cent_ratio, 1)}%
{name2}: {round(par2_cent_ratio, 1)}%
{name3}: {round(par3_cent_ratio, 1)}%
{name4}: {round(par4_cent_ratio, 1)}%
    '''


# # DATA ON AGE GROUPS
ages = []
# # DATA ON GENDER
sex = []
# # BMI
bmi = []
# # DATA ON PARENTAL STATUSES
children = []
# # SMOKING STATUSES
smoking_status = []
# # REGIONAL CLASSIFICATIONS
regions = []
# # DATA ON CHARGES
charges = []

with open("insurance.csv", newline="") as insurance_csv:
    insurance_record = csv.DictReader(insurance_csv)
    for row in insurance_record:
        ages.append(row["age"])
        sex.append(row["sex"])
        bmi.append(row["bmi"])
        children.append(row["children"])
        smoking_status.append(row["smoker"])
        regions.append(row["region"])
        charges.append(row["charges"])

average_age = 0
teens = []
youth = []
adult = []
oldees = []
age = 0
for data in ages:
    if int(data) <= 14:
        teens.append(data)
    elif int(data) >= 15 and int(data) <= 24:
        youth.append(data[0])
    elif int(data) >= 25 and int(data) <= 64:
        adult.append(data)
    else:
        oldees.append(data)
    age += float(data)
    average_age = round(age / len(ages))
# population of patients based on age group
p_teens = len(teens)
p_youth = len(youth)
p_adult = len(adult)
p_oldees = len(oldees)
percent_ratio_of_agegroup = percent_ratio(p_teens, "teens", p_youth, "youth", p_adult, "adult", p_oldees, "oldees")
# print(percent_ratio_of_agegroup)

males = []
females = []
# MALE VS  FEMALE
for data in sex:
    if data == "male":
        males.append(data)
    else:
        females.append(data)

# population of patients based on age group
p_males = len(males)
p_females = len(females)
percent_ratio_of_gender = percent_ratio(p_males, "males", p_females, "females")
# print(percent_ratio_of_gender)

# CLASSIFICATION OF BMI
underweight = []
healthy = []
overweight = []
obese = []
for data in bmi:
    if float(data) <= 18.5:
        underweight.append(data)
    elif float(data) >= 18.5 and float(data) <= 24.9:
        healthy.append(data)
    elif float(data) >= 25 and float(data) <= 29.9:
        overweight.append(data)
    else:
        obese.append(data)

# population of patients with classified bmi
p_underweight = len(underweight)
p_healthy = len(healthy)
p_overweight = len(overweight)
p_obese = len(obese)
percent_ratio_of_classified_bmi = percent_ratio(p_underweight, "underweight", p_healthy, "healthy", p_overweight, "overweight", p_obese, "obese")
# print(percent_ratio_of_classified_bmi)

# BMI BASED ON GENDER
# DATA ON MALES WITH CLASSIFIED BMI
male_bmis = []
female_bmis = []
underweight_male = []
healthy_male = []
overweight_male = []
obese_male = []
# CLASSIFICATION  OF BMI BY GENDER
bmi_and_sex = list(zip(bmi, sex))
sorted_bmi_and_sex = sorted(bmi_and_sex)
for data in bmi_and_sex:
    if data[-1] == "male":
        male_bmis.append(data)
    else:
        female_bmis.append(data)

for data in male_bmis:
    if float(data[0]) <= 18.5:
        underweight_male.append(data)
    elif float(data[0]) > 18.5 and float(data[0]) <= 24.9:
        healthy_male.append(data)
    elif float(data[0]) >= 25 and float(data[0]) <= 29.9:
        overweight_male.append(data)
    else:
        obese_male.append(data)

# population of males with classified bmi
p_underweight_male = len(underweight_male)
p_healthy_male = len(healthy_male)
p_overweight_male = len(overweight_male)
p_obese_male = len(obese_male)

# DATA ON FEMALES WITH CLASSIFIED BMI
underweight_female = []
healthy_female = []
overweight_female = []
obese_female = []
for data in female_bmis:
    if float(data[0]) <= 18.5:
        underweight_female.append(data)
    elif float(data[0]) > 18.5 and float(data[0]) <= 24.9:
        healthy_female.append(data)
    elif float(data[0]) >= 25 and float(data[0]) <= 29.9:
        overweight_female.append(data)
    else:
        obese_female.append(data)
# population of females with classified bmi
p_underweight_female = len(underweight_female)
p_healthy_female = len(healthy_female)
p_overweight_female = len(overweight_female)
p_obese_female = len(obese_female)

percent_ratio_of_underweight_gender = percent_ratio(p_underweight_female, "underweight male", p_underweight_female,
                                                    "underweight female")
# print(percent_ratio_of_underweight_gender)

percent_ratio_of_healthy_gender = percent_ratio(p_healthy_male, "healthy male", p_healthy_female, "healthy female")
# print(percent_ratio_of_healthy_gender)

percent_ratio_of_overweight_gender = percent_ratio(p_overweight_male, "overweight male", p_overweight_female,
                                                   "overweight female")
# print(percent_ratio_of_overweight_gender)

percent_ratio_of_obese_gender = percent_ratio(p_obese_male, "obese male", p_obese_female, "obese female")
# print(percent_ratio_of_obese_gender)

# BMI BASED ON AGE GROUP
# DATA ON TEENS BMI
age_underweight = []
age_healthy = []
age_overweight = []
age_obese = []
# CLASSIFICATION OF BMI BY AGE
bmi_and_age = list(zip(bmi, ages))
sorted_bmi_and_age = sorted(bmi_and_age)
for data in sorted_bmi_and_age:
    if float(data[0]) <= 18.5:
        age_underweight.append(data)
    elif float(data[0]) > 18.5 and float(data[0]) <= 24.9:
        age_healthy.append(data)
    elif float(data[0]) >= 25 and float(data[0]) <= 29.9:
        age_overweight.append(data)
    else:
        age_obese.append(data)
# population of bmis per age group
p_age_underweight = len(age_underweight)
p_age_healthy = len(age_healthy)
p_age_overweight = len(age_overweight)
p_age_obese = len(age_obese)
percent_ratio_of_bmi_per_age_group = percent_ratio(p_age_underweight, "age underweight", p_age_healthy, "age healthy",
                                                   p_age_overweight,
                                                   "age overweight", p_age_obese, "age obese")
# print(percent_ratio_of_bmi_per_age_group)

# DATA ON TEENS WITH CLASSIFIED BMI
underweight_teens = []
underweight_youths = []
underweight_adults = []
underweight_oldees = []
for data in age_underweight:
    if int(data[-1]) <= 14:
        underweight_teens.append(data)
    elif int(data[-1]) >= 15 and int(data[-1]) <= 24:
        underweight_youths.append(data)
    elif int(data[-1]) >= 25 and int(data[-1]) <= 64:
        underweight_adults.append(data)
    else:
        underweight_oldees.append(data)

# population of teens with classified bmi
p_ages_underweight = len(age_underweight)
p_underweight_teens = len(underweight_teens)
p_underweight_youths = len(underweight_youths)
p_underweight_adults = len(underweight_adults)
p_underweight_oldees = len(underweight_oldees)
percent_ratio_of_underweight_per_age_group = percent_ratio(p_underweight_teens, "underweight teens",
                                                           p_underweight_youths, "underweight youths",
                                                           p_underweight_adults, "underweight adults",
                                                           p_underweight_oldees, "underweight oldees")
# print(percent_ratio_of_underweight_per_age_group)

# DATA ON HEALTHY AGE GROUP
healthy_teens = []
healthy_youths = []
healthy_adults = []
healthy_oldees = []

for data in age_underweight:
    if int(data[-1]) <= 14:
        healthy_teens.append(data)
    elif int(data[-1]) >= 15 and int(data[-1]) <= 24:
        healthy_youths.append(data)
    elif int(data[-1]) >= 25 and int(data[-1]) <= 64:
        healthy_adults.append(data)
    else:
        healthy_oldees.append(data)
# population of youths with classified bmi
p_healthy_teens = len(healthy_teens)
p_healthy_youths = len(healthy_youths)
p_healthy_adults = len(healthy_adults)
p_healthy_oldees = len(healthy_oldees)
percent_ratio_of_healthy_per_age_group = percent_ratio(p_healthy_teens, "healthy teens", p_healthy_youths,
                                                       "healthy youths", p_healthy_adults, "healthy adults",
                                                       p_healthy_oldees, "healthy oldees")
# print(percent_ratio_of_healthy_per_age_group)

# DATA OF OVERWEIGHT AGE GROUP
overweight_teens = []
overweight_youths = []
overweight_adults = []
overweight_oldees = []

for data in age_overweight:
    if int(data[-1]) <= 14:
        overweight_teens.append(data)
    elif int(data[-1]) >= 15 and int(data[-1]) <= 24:
        overweight_youths.append(data[0])
    elif int(data[-1]) >= 25 and int(data[-1]) <= 64:
        overweight_adults.append(data)
    else:
        overweight_oldees.append(data)
# population of OVERWEIGHT AGE GROUP
p_overweight_teens = len(overweight_teens)
p_overweight_youths = len(overweight_youths)
p_overweight_adults = len(overweight_adults)
p_overweight_oldees = len(overweight_oldees)
percent_ratio_of_overweight_per_age_group = percent_ratio(p_overweight_teens, "overweight teens", p_overweight_youths,
                                                          "overweight youths", p_overweight_adults, "overweight adults",
                                                          p_overweight_oldees, "overweight oldees")
# print(percent_ratio_of_overweight_per_age_group)

# DATA ON OBESE AGE GROUP
obese_teens = []
obese_youths = []
obese_adults = []
obese_oldees = []

for data in age_obese:
    if int(data[-1]) <= 14:
        obese_teens.append(data)
    elif int(data[-1]) >= 15 and int(data[-1]) <= 24:
        obese_youths.append(data)
    elif int(data[-1]) >= 25 and int(data[-1]) <= 64:
        obese_adults.append(data)
    else:
        obese_oldees.append(data)
# population of OBESE AGE GROUP
p_obese_teens = len(obese_teens)
p_obese_youths = len(obese_youths)
p_obese_adults = len(obese_adults)
p_obese_oldees = len(obese_oldees)
percent_ratio_of_obese_per_age_group = percent_ratio(p_obese_teens, "obese teens", p_obese_youths, "obese youths",
                                                     p_obese_adults, "obese adults", p_obese_oldees, "obese oldees")
# print(percent_ratio_of_obese_per_age_group)

# PARENT VS NON PARENT
parents = []
non_parents = []
for data in children:
    if int(data) > 0:
        parents.append(data)
    else:
        non_parents.append(data)

# population of non parents
p_non_parents = len(non_parents)
# population of parents
p_parents = len(parents)
percent_ratio_of_parental_status = percent_ratio(p_non_parents, "non parents", p_parents, "parents")
# print(percent_ratio_of_parental_status)

# DATA OF PARENTS PER AGE GROUP
teens_parents = []
youth_parents = []
adult_parents = []
oldees_parents = []
# PARENTS
# CLASSIFICATION OF PARENTS BY AGE GROUPS
parents_record_by_ages = []
ages_and_parents = list(zip(ages, children))
sorted_ages_and_parents = sorted(ages_and_parents)
for data in sorted_ages_and_parents:
    if int(data[-1]) > 0:
        parents_record_by_ages.append(data)
for data in parents_record_by_ages:
    if float(data[0]) <= 14:
        teens_parents.append(data[0])
    elif float(data[0]) >= 15 and float(data[0]) <= 24:
        youth_parents.append(data[0])
    elif float(data[0]) >= 25 and float(data[0]) <= 64:
        adult_parents.append(data[0])
    else:
        oldees_parents.append(data)

# population of parents based on age group
p_teens_parents = len(teens_parents)
p_youth_parents = len(youth_parents)
p_adult_parents = len(adult_parents)
p_oldees_parents = len(oldees_parents)
percent_ratio_of_parents_per_age_group = percent_ratio(p_teens_parents, "teens parents", p_youth_parents,
                                                       "youth parents", p_adult_parents, "adult parents",
                                                       p_oldees_parents, "oldees parents")
# print(percent_ratio_of_parents_per_age_group)

# PARENTAL STATUS BASED ON GENDER
male_parents = []
female_parents = []

# CLASSSIFICATION OF PARENTS BY GENDER
sex_and_parents = list(zip(sex, children))
sorted_sex_and_parents = sorted(sex_and_parents)

for data in sorted_sex_and_parents:
    if int(data[-1]) > 0 and data[0] == "male":
        male_parents.append(data)
    elif int(data[-1]) > 0 and data[0] == "female":
        female_parents.append(data)

# population of parents based on gender
p_male_parents = len(male_parents)
p_female_parents = len(female_parents)
percent_ratio_of_parents_per_gender = percent_ratio(p_male_parents, "male parents", p_female_parents, "female parents")
# print(percent_ratio_of_parents_per_gender)

# PARENTAL STATUS BASED ON BMI
underweight_parents = []
healthy_parents = []
overweight_parents = []
obese_parents = []

# CLASSIFICATION OF PARENTS BY BMI
bmi_and_parents = list(zip(bmi, children))
sorted_bmi_and_parents = sorted(bmi_and_parents)
for data in sorted_bmi_and_parents:
    if int(data[-1]) > 0 and float(data[0]) <= 18.5:
        underweight_parents.append(data)
    elif int(data[-1]) > 0 and float(data[0]) > 18.5 and float(data[0]) <= 24.9:
        healthy_parents.append(data)
    elif int(data[-1]) > 0 and float(data[0]) >= 25 and float(data[0]) <= 29.9:
        overweight_parents.append(data)
    elif int(data[-1]) > 0 and float(data[0]) > 30:
        obese_parents.append(data)

# population of parents based on bmi
p_underweight_parents = len(underweight_parents)
p_healthy_parents = len(healthy_parents)
p_overweight_parents = len(overweight_parents)
p_obese_parents = len(obese_parents)
percent_ratio_of_parents_per_classified_bmi = percent_ratio(p_underweight_parents, "underweight parents",
                                                            p_healthy_parents,
                                                            "healthy parents", p_overweight_parents,
                                                            "overweight parents",
                                                            p_obese_parents, "obese parents")
# print(percent_ratio_of_parents_per_classified_bmi)

# DATA OF NON PARENTS PER AGE GROUP
teens_non_parents = []
youth_non_parents = []
adult_non_parents = []
oldees_non_parents = []

# CLASSIFICATION OF PARENTS BY AGE GROUPS
non_parents_record_by_ages = []
ages_and_non_parents = list(zip(ages, children))
sorted_ages_and_non_parents = sorted(ages_and_non_parents)
for data in sorted_ages_and_non_parents:
    if int(data[-1]) == 0:
        non_parents_record_by_ages.append(data)
for data in non_parents_record_by_ages:
    if float(data[0]) <= 14:
        teens_non_parents.append(data[0])
    elif float(data[0]) >= 15 and float(data[0]) <= 24:
        youth_non_parents.append(data[0])
    elif float(data[0]) >= 25 and float(data[0]) <= 64:
        adult_non_parents.append(data[0])
    else:
        oldees_non_parents.append(data)

# population of parents based on age group
p_teens_non_parents = len(teens_non_parents)
p_youth_non_parents = len(youth_non_parents)
p_adult_non_parents = len(adult_non_parents)
p_oldees_non_parents = len(oldees_non_parents)
percent_ratio_of_non_parents_per_age_group = percent_ratio(p_teens_non_parents, "teens non parents",
                                                           p_youth_non_parents,
                                                           " youth non parents", p_adult_non_parents,
                                                           "adult non parents",
                                                           p_oldees_non_parents, "oldees non parents")
# print(percent_ratio_of_non_parents_per_age_group)

# PARENTAL STATUS BASED ON GENDER
male_non_parents = []
female_non_parents = []

# CLASSSIFICATION OF PARENTS BY GENDER
sex_and_non_parents = list(zip(sex, children))
sorted_sex_and_non_parents = sorted(sex_and_non_parents)

for data in sorted_sex_and_non_parents:
    if int(data[-1]) == 0 and data[0] == "male":
        male_non_parents.append(data)
    elif int(data[-1]) == 0 and data[0] == "female":
        female_non_parents.append(data)

# population of non parents based on gender
p_male_non_parents = len(male_non_parents)
p_female_non_parents = len(female_non_parents)
percent_ratio_of_non_parents_per_gender = percent_ratio(p_male_non_parents, "male non parents", p_female_non_parents,
                                                        "female non parents")
# print(percent_ratio_of_non_parents_per_gender)

# PARENTAL STATUS BASED ON BMI
bmi_and_non_parents = list(zip(bmi, children))
sorted_bmi_and_non_parents = sorted(bmi_and_parents)

underweight_non_parents = []
healthy_non_parents = []
overweight_non_parents = []
obese_non_parents = []
for data in sorted_bmi_and_non_parents:
    if int(data[-1]) == 0 and float(data[0]) <= 18.5:
        underweight_non_parents.append(data)
    elif int(data[-1]) == 0 and float(data[0]) > 18.5 and float(data[0]) <= 24.9:
        healthy_non_parents.append(data)
    elif int(data[-1]) == 0 and float(data[0]) >= 25 and float(data[0]) <= 29.9:
        overweight_non_parents.append(data)
    elif int(data[-1]) == 0 and float(data[0]) > 30:
        obese_non_parents.append(data)

# population of non parents based on bmi
p_underweight_non_parents = len(underweight_non_parents)
p_healthy_non_parents = len(healthy_non_parents)
p_overweight_non_parents = len(overweight_non_parents)
p_obese_non_parents = len(obese_non_parents)
percent_ratio_of_non_parents_per_classified_bmi = percent_ratio(p_underweight_non_parents, "underweight non parents",
                                                                p_healthy_non_parents, "healthy non parents",
                                                                p_overweight_non_parents, "overweight non parents",
                                                                p_obese_non_parents, "obese non parents")
# print(percent_ratio_of_non_parents_per_gender)

# SMOKER VS NON SMOKER
smoker = []
non_smoker = []
for person in smoking_status:
    if person == "yes":
        smoker.append(person)
    else:
        non_smoker.append(person)

# population of smokers
p_smokers = len(smoker)
# population of non smokers
p_non_smokers = len(non_smoker)
percent_ratio_of_patients_per_smoking_status = percent_ratio(p_smokers, "smokers", p_non_smokers, "non smokers")
# print(percent_ratio_of_patients_per_smoking_status)

# AGE GROUP SMOKERS
teen_smokers = []
youth_smokers = []
adult_smokers = []
oldees_smokers = []
# CLASSIFICATION OF SMOKERS BY AGES
smokers_record_by_ages = []
ages_and_smoking_status = list(zip(ages, smoking_status))
sorted_ages_and_smoking_status = sorted(ages_and_smoking_status)
for data in sorted_ages_and_smoking_status:
    if data[-1] == "yes":
        smokers_record_by_ages.append(data)
for data in smokers_record_by_ages:
    if float(data[0]) <= 14:
        teen_smokers.append(data[0])
    elif float(data[0]) >= 15 and float(data[0]) <= 24:
        youth_smokers.append(data[0])
    elif float(data[0]) >= 25 and float(data[0]) <= 64:
        adult_smokers.append(data[0])
    else:
        oldees_smokers.append(data)

# population of age group smokers
p_teen_smokers = len(teen_smokers)
p_youth_smokers = len(youth_smokers)
p_adult_smokers = len(adult_smokers)
p_oldees_smokers = len(oldees_smokers)
percent_ratio_of_smokers_per_age_group = percent_ratio(p_teen_smokers, "teen smokers", p_youth_smokers, "youth smokers",
                                                       p_adult_smokers, "adult smokers", p_oldees_smokers,
                                                       "old smokers")
# print(percent_ratio_of_smokers_per_age_group)

# DATA ON SMOKERS BASED ON BMI
underweight_smokers = []
healthy_smokers = []
overweight_smokers = []
obese_smokers = []
# CLASSIFICATION OF SMOKERS BY BMI
bmi_and_smoking_status = list(zip(bmi, smoking_status))
sorted_bmi_and_smoking_status = sorted(bmi_and_smoking_status)
for data in sorted_bmi_and_smoking_status:
    if data[-1] == "yes" and float(data[0]) <= 18.5:
        underweight_smokers.append(data)
    elif data[-1] == "yes" and float(data[0]) > 18.5 and float(data[0]) <= 24.9:
        healthy_smokers.append(data)
    elif data[-1] == "yes" and float(data[0]) >= 25 and float(data[0]) <= 29.9:
        overweight_smokers.append(data)
    else:
        obese_smokers.append(data)
# POPULATION OF SMOKERS BASED ON BMI
p_underweight_smokers = len(underweight_smokers)
p_healthy_smokers = len(healthy_smokers)
p_overweight_smokers = len(overweight_smokers)
p_obese_smokers = len(obese_smokers)
percent_ratio_of_smokers_per_bmi = percent_ratio(p_underweight_smokers, "underweight smokers", p_healthy_smokers,
                                                 "healthy smokers", p_overweight_smokers, "overweight smokers",
                                                 p_obese_smokers, "obese smokers")
# print(percent_ratio_of_smokers_per_bmi)

# DATA ON SMOKERS BASED ON PARENTAL STATUS
parent_smokers = []
non_parent_smokers = []
# PARENT VS NON PARENT SMOKERS
smokers_record_by_parents = []
parents_and_smoking_status = list(zip(children, smoking_status))
sorted_parents_and_smoking_status = sorted(parents_and_smoking_status)
for data in sorted_parents_and_smoking_status:
    if data[-1] == "yes":
        smokers_record_by_parents.append(data)
for data in smokers_record_by_parents:
    if float(data[0]) > 0:
        parent_smokers.append(data[0])
    else:
        non_parent_smokers.append(data[0])

# population of smokers based on parental status
p_parent_smokers = len(parent_smokers)
p_non_parent_smokers = len(non_parent_smokers)
percent_ratio_of_smokers_per_parental_status = percent_ratio(p_parent_smokers, "parent smokers", p_non_parent_smokers,
                                                             "non parent smokers")
# print(percent_ratio_of_smokers_per_parental_status)

# DATA OF SMOKERS BASED ON GENDER
male_smokers = []
female_smokers = []

# FEMALE VS MALE SMOKERS
smokers_record_by_sex = []
sex_and_smoking_status = list(zip(sex, smoking_status))
sorted_sex_and_smoking_status = sorted(sex_and_smoking_status)
for data in sorted_sex_and_smoking_status:
    if data[-1] == "yes":
        smokers_record_by_sex.append(data)
for data in smokers_record_by_sex:
    if data[0] == "male":
        male_smokers.append(data[0])
    else:
        female_smokers.append(data[0])

# population of male smokers
p_male_smokers = len(male_smokers)
# population of female smokers
p_female_smokers = len(female_smokers)
percent_ratio_of_smokers_per_gender = percent_ratio(p_male_smokers, "male smokers", p_female_smokers, "female smokers")
# print(percent_ratio_of_smokers_per_gender)

# DATA ON NON SMOKERS BASED ON BMI
underweight_non_smokers = []
healthy_non_smokers = []
overweight_non_smokers = []
obese_non_smokers = []
# CLASSIFICATION OF NON SMOKERS BY BMI
bmi_and_non_smoking_status = list(zip(bmi, smoking_status))
sorted_bmi_and_non_smoking_status = sorted(bmi_and_smoking_status)
for data in sorted_bmi_and_non_smoking_status:
    if data[-1] == "no" and float(data[0]) <= 18.5:
        underweight_non_smokers.append(data)
    elif data[-1] == "no" and float(data[0]) > 18.5 and float(data[0]) <= 24.9:
        healthy_non_smokers.append(data)
    elif data[-1] == "no" and float(data[0]) >= 25 and float(data[0]) <= 29.9:
        overweight_non_smokers.append(data)
    else:
        obese_non_smokers.append(data)
# POPULATION OF NON SMOKERS BASED ON BMI
p_underweight_non_smokers = len(underweight_non_smokers)
p_healthy_non_smokers = len(healthy_non_smokers)
p_overweight_non_smokers = len(overweight_non_smokers)
p_obese_non_smokers = len(obese_non_smokers)
percent_ratio_of_non_smokers_per_bmi = percent_ratio(p_underweight_non_smokers, "underweight non smokers",
                                                     p_healthy_non_smokers,
                                                     "healthy non smokers", p_overweight_non_smokers,
                                                     "overweight non smokers",
                                                     p_obese_non_smokers, "obese non smokers")
# print(percent_ratio_of_non_smokers_per_bmi)

# CLASSIFICATION OF REGIONS
northeast = []
northwest = []
southeast = []
southwest = []
for data in regions:
    if data == "northeast":
        northeast.append(data)
    elif data == "northwest":
        northwest.append(data)
    elif data == "southeast":
        southeast.append(data)
    else:
        southwest.append(data)
# POPULATION OF PATIENTS PER REGION
p_northeast = len(northeast)
p_northwest = len(northwest)
p_southeast = len(southeast)
p_southwest = len(southwest)
percent_ratio_of_patients_per_region = percent_ratio(p_northeast, "northeast", p_northwest, "northwest",
                                                     p_southeast, "southeast", p_southwest, "southwest")
# print(percent_ratio_of_patients_per_region)

# DATA ON BMI PER REGION
regional_underweight = []
regional_healthy = []
regional_overweight = []
regional_obese = []

# CLASSIFICATION OF BMI BY REGION
bmi_and_regions = list(zip(bmi, regions))
sorted_bmi_and_regions = sorted(bmi_and_regions)
for data in sorted_bmi_and_regions:
    if float(data[0]) <= 18.5:
        regional_underweight.append(data)
    elif float(data[0]) > 18.5 and float(data[0]) <= 24.9:
        regional_healthy.append(data)
    elif float(data[0]) >= 25 and float(data[0]) <= 29.9:
        regional_overweight.append(data)
    else:
        regional_obese.append(data)

# POPULATION OF BMI PER REGION
p_regional_underweight = len(regional_underweight)
p_regional_healthy = len(regional_healthy)
p_regional_overweight = len(regional_overweight)
p_regional_obese = len(regional_obese)
percent_ratio_of_bmi_per_region = percent_ratio(p_regional_underweight, "regional underweight", p_regional_healthy,
                                                "regional healthy", p_regional_overweight, "regional overweight",
                                                p_regional_obese, "regional obese")
# print(percent_ratio_of_bmi_per_region)

# DATA ON CLASSIFIED BMI PER REGION
northeast_underweight = []
northwest_underweight = []
southeast_underweight = []
southwest_underweight = []
for data in regional_underweight:
    if data[-1] == "northeast":
        northeast_underweight.append(data)
    elif data[-1] == "northwest":
        northwest_underweight.append(data)
    elif data[-1] == "southeast":
        southeast_underweight.append(data)
    else:
        southwest_underweight.append(data)
# POPULATION OF UNDERWEIGHT PER REGION
p_regional_underweight = len(regional_underweight)
p_northeast_underweight = len(northeast_underweight)
p_northwest_underweight = len(northwest_underweight)
p_southeast_underweight = len(southeast_underweight)
p_southwest_underweight = len(southwest_underweight)
percent_ratio_of_underweight_per_region = percent_ratio(p_northeast_underweight, "northeast underweight",
                                                        p_northwest_underweight, "northwest underweight",
                                                        p_southwest_underweight, "southwest underweight",
                                                        p_southeast_underweight, "southeast underweight")
# print(percent_ratio_of_underweight_per_region)

northwest_healthy = []
northeast_healthy = []
southwest_healthy = []
southeast_healthy = []

for data in regional_healthy:
    if data[-1] == "northeast":
        northeast_healthy.append(data)
    elif data[-1] == "northwest":
        northwest_healthy.append(data)
    elif data[-1] == "southeast":
        southeast_healthy.append(data)
    else:
        southwest_healthy.append(data)
# POPULATION OF HEALTHY PER REGION
p_regional_healthy = len(regional_healthy)
p_northeast_healthy = len(northeast_healthy)
p_northwest_healthy = len(northwest_healthy)
p_southeast_healthy = len(southeast_healthy)
p_southwest_healthy = len(southwest_healthy)
percent_ratio_of_healthy_per_region = percent_ratio(p_northeast_healthy, "northeast healthy", p_northwest_healthy,
                                                    "northwest healthy", p_southwest_healthy, "southwest healthy",
                                                    p_southeast_healthy, "southeast healthy")
# print(percent_ratio_of_healthy_per_region)

# DATA OF OVERWEIGHT BMI PER REGION
southeast_overweight = []
southwest_overweight = []
northeast_overweight = []
northwest_overweight = []
for data in regional_overweight:
    if data[-1] == "northeast":
        northeast_overweight.append(data)
    elif data[-1] == "northwest":
        northwest_overweight.append(data)
    elif data[-1] == "southeast":
        southeast_overweight.append(data)
    else:
        southwest_overweight.append(data)
# POPULATION OF OVERWEIGHT PER REGION
p_regional_overweight = len(regional_overweight)
p_northeast_overweight = len(northeast_overweight)
p_northwest_overweight = len(northwest_overweight)
p_southeast_overweight = len(southeast_overweight)
p_southwest_overweight = len(southwest_overweight)
percent_ratio_of_overweight_per_region = percent_ratio(p_northeast_overweight, "northeast overweight",
                                                       p_northwest_overweight, "northwest overweight",
                                                       p_southwest_overweight, "southwest overweight",
                                                       p_southeast_overweight, "southeast overweight")
# print(percent_ratio_of_overweight_per_region)

# DATA OF OBESE PER REGION
southwest_obese = []
southeast_obese = []
northwest_obese = []
northeast_obese = []
for data in regional_obese:
    if data[-1] == "northeast":
        northeast_obese.append(data)
    elif data[-1] == "northwest":
        northwest_obese.append(data)
    elif data[-1] == "southeast":
        southeast_obese.append(data)
    else:
        southwest_obese.append(data)

# POPULATION OF OBESE PER REGION
p_regional_obese = len(regional_obese)
p_northeast_obese = len(northeast_obese)
p_northwest_obese = len(northwest_obese)
p_southeast_obese = len(southeast_obese)
p_southwest_obese = len(southwest_obese)
percent_ratio_of_obese_per_region = percent_ratio(p_northeast_obese, "northeast obese", p_northwest_obese,
                                                  "northwest obese", p_southwest_obese, "southwest obese",
                                                  p_southeast_obese, "southeast obese")
# print(percent_ratio_of_obese_per_region)

# DATA ON SMOKERS PER REGION
northeast_smokers = []
northwest_smokers = []
southeast_smokers = []
southwest_smokers = []

# CLASSIFICATION OF SMOKERS BY REGION
smokers_record_by_region = []
regions_and_smoking_status = list(zip(regions, smoking_status))
sorted_regions_and_smoking_status = sorted(regions_and_smoking_status)
for data in sorted_regions_and_smoking_status:
    if data[-1] == "yes":
        smokers_record_by_region.append(data)
for data in smokers_record_by_region:
    if data[0] == "northeast":
        northeast_smokers.append(data)
    if data[0] == "northwest":
        northwest_smokers.append(data)
    if data[0] == "southeast":
        southeast_smokers.append(data)
    else:
        southwest_smokers.append(data)

# POPULATION OF SMOKERS PER REGION
p_northeast_smokers = len(northeast_smokers)
p_northwest_smokers = len(northwest_smokers)
p_southeast_smokers = len(southeast_smokers)
p_southwest_smokers = len(southwest_smokers)
percent_ratio_of_smokers_per_region = percent_ratio(p_northeast_smokers, "northeast smokers", p_northwest_smokers,
                                                    "northwest smokers", p_southwest_smokers, "southwest smokers",
                                                    p_southeast_smokers, "southeast smokers")
# print(percent_ratio_of_smokers_per_region)

# DATA ON REGIONAL PARENTS
regional_parents = []
regional_teens_parents = []
regional_youth_parents = []
regional_adult_parents = []
regional_oldees_parents = []
# CLASSIFICATION OF PARENTS BY AGE GROUP AND REGION
age_group_parents_and_regions = list(zip(children, ages, regions))
sorted_age_group_parents_and_regions = sorted(age_group_parents_and_regions)
for data in sorted_age_group_parents_and_regions:
    if int(data[0]) > 0:
        regional_parents.append(data)

for data in regional_parents:
    if float(data[1]) <= 14:
        regional_teens_parents.append(data)
    elif float(data[1]) >= 15 and float(data[1]) <= 24:
        regional_youth_parents.append(data)
    elif float(data[1]) >= 25 and float(data[1]) <= 64:
        regional_adult_parents.append(data)
    else:
        regional_oldees_parents.append(data)

# CLASSIFICATION OF PARENTS PER REGION
northeast_parents = []
northwest_parents = []
southeast_parents = []
southwest_parents = []

for data in regional_parents:
    if data[-1] == "northeast":
        northeast_parents.append(data)
    elif data[-1] == "northwest":
        northwest_parents.append(data)
    elif data[-1] == "southeast":
        southeast_parents.append(data)
    else:
        southwest_parents.append(data)

# BIRTH RATES PER REGION
# note: p --> population
regional_parents = []
p_northeast_parents = len(northeast_parents)
p_southeast_parents = len(southeast_parents)
p_northwest_parents = len(northwest_parents)
p_southwest_parents = len(southwest_parents)
percent_ratio_of_birth_rates_per_region = percent_ratio(p_northeast_parents, "northeast parents", p_northwest_parents,
                                                        "northwest parents", p_southwest_parents, "southwest parents",
                                                        p_southeast_parents, "southeast parents")
# print(percent_ratio_of_birth_rates_per_region)

# DATA ON PARENTS ACCORDING TO AGE GROUPS PER REGION
northwest_teens_parents = []
northeast_teens_parents = []
southeast_teens_parents = []
southwest_teens_parents = []
for data in regional_teens_parents:
    if data[-1] == "northeast":
        northeast_teens_parents.append(data)
    elif data[-1] == "northwest":
        northwest_teens_parents.append(data)
    elif data[-1] == "southeast":
        southeast_teens_parents.append(data)
    else:
        southwest_teens_parents.append(data)

northwest_youth_parents = []
northeast_youth_parents = []
southwest_youth_parents = []
southeast_youth_parents = []
for data in regional_youth_parents:
    if data[-1] == "northeast":
        northeast_youth_parents.append(data)
    elif data[-1] == "northwest":
        northwest_youth_parents.append(data)
    elif data[-1] == "southeast":
        southeast_youth_parents.append(data)
    else:
        southwest_youth_parents.append(data)

southwest_adult_parents = []
southeast_adult_parents = []
northeast_adult_parents = []
northwest_adult_parents = []
for data in regional_adult_parents:
    if data[-1] == "northeast":
        northeast_adult_parents.append(data)
    elif data[-1] == "northwest":
        northwest_adult_parents.append(data)
    elif data[-1] == "southeast":
        southeast_adult_parents.append(data)
    else:
        southwest_adult_parents.append(data)

southwest_oldees_parents = []
southeast_oldees_parents = []
northeast_oldees_parents = []
northwest_oldees_parents = []
for data in regional_oldees_parents:
    if data[-1] == "northeast":
        northeast_oldees_parents.append(data)
    elif data[-1] == "northwest":
        northwest_oldees_parents.append(data)
    elif data[-1] == "southeast":
        southeast_oldees_parents.append(data)
    else:
        southwest_oldees_parents.append(data)

# EARLY/LATE MARRIAGE/BIRTH PER REGION
# note: p --> population
p_regional_teens_parents = len(regional_teens_parents)
p_southwest_teens_parents = len(southwest_teens_parents)
p_southwest_adult_parents = len(southwest_adult_parents)
p_southwest_youth_parents = len(southwest_youth_parents)
p_southwest_oldees_parents = len(southwest_oldees_parents)

p_regional_youth_parents = len(regional_youth_parents)
p_southeast_teens_parents = len(southeast_teens_parents)
p_southeast_youth_parents = len(southeast_youth_parents)
p_southeast_adult_parents = len(southeast_adult_parents)
p_southeast_oldees_parents = len(southeast_oldees_parents)

p_regional_adult_parents = len(regional_adult_parents)
p_northeast_teens_parents = len(northeast_teens_parents)
p_northeast_youth_parents = len(northeast_youth_parents)
p_northeast_adult_parents = len(northeast_adult_parents)
p_northeast_oldees_parents = len(northeast_oldees_parents)

p_regional_oldees_parents = len(regional_oldees_parents)
p_northwest_teens_parents = len(northwest_teens_parents)
p_northwest_youth_parents = len(northwest_youth_parents)
p_northwest_adult_parents = len(northwest_adult_parents)
p_northwest_oldees_parents = len(northwest_oldees_parents)
# percent_ratio_of_extreme_early_birth_per_region = percent_ratio(p_northwest_teens_parents, "northwest teens parents",
#                                                              p_northwest_teens_parents, "northwest teens parents",
#                                                              p_northwest_teens_parents, "northwest teens parents",
#                                                              p_northwest_teens_parents, "northwest teens parents")
# print(percent_ratio_of_extreme_early_birth_per_region)

percent_ratio_of_early_birth_per_region = percent_ratio(p_northeast_youth_parents, "northeast youth parents",
                                                        p_southeast_youth_parents, "southeast youth parents",
                                                        p_southwest_youth_parents, "southwest youth parents",
                                                        p_northwest_youth_parents, "northwest youth parents")
# print(percent_ratio_of_early_birth_per_region)

# percent_ratio_of_regional_late_birth = percent_ratio(p_southeast_adult_parents, "southeast adult parents",
#                                                              p_northeast_adult_parents, "northeast adult parents",
#                                                              p_southwest_adult_parents, "southwest adult parents",
#                                                              p_northwest_adult_parents, "northwest adult parents")
# print(percent_ratio_of_regional_late_birth)

# percent_ratio_of_regional_extremely_late_birth = percent_ratio(p_southwest_oldees_parents, "southwest oldees parents",
#                                                              p_southeast_oldees_parents, "southwest oldees parents",
#                                                              p_northwest_oldees_parents, "southwest oldees parents",
#                                                              p_northeast_oldees_parents, "southwest oldees parents")
# print(percent_ratio_of_regional_extremely_late_birth)

# DATA ON REGIONAL NON PARENT
# DATA ON REGIONAL PARENTS
regional_non_parents = []
regional_teens_non_parents = []
regional_youth_non_parents = []
regional_adult_non_parents = []
regional_oldees_non_parents = []
# CLASSIFICATION OF PARENTS BY AGE GROUP AND REGION
age_group_non_parents_and_regions = list(zip(children, ages, regions))
sorted_age_group_non_parents_and_regions = sorted(age_group_parents_and_regions)
for data in sorted_age_group_non_parents_and_regions:
    if int(data[0]) == 0:
        regional_non_parents.append(data)

for data in regional_non_parents:
    if float(data[1]) <= 14:
        regional_teens_non_parents.append(data)
    elif float(data[1]) >= 15 and float(data[1]) <= 24:
        regional_youth_non_parents.append(data)
    elif float(data[1]) >= 25 and float(data[1]) <= 64:
        regional_adult_non_parents.append(data)
    else:
        regional_oldees_non_parents.append(data)

# CLASSIFICATION OF NON PARENTS PER REGION
northeast_non_parents = []
northwest_non_parents = []
southeast_non_parents = []
southwest_non_parents = []

for data in regional_non_parents:
    if data[-1] == "northeast":
        northeast_non_parents.append(data)
    elif data[-1] == "northwest":
        northwest_non_parents.append(data)
    elif data[-1] == "southeast":
        southeast_non_parents.append(data)
    else:
        southwest_non_parents.append(data)

# BIRTH RATES PER REGION
# note: p --> population
p_regional_non_parents = len(regional_non_parents)
p_northeast_non_parents = len(northeast_non_parents)
p_southeast_non_parents = len(southeast_non_parents)
p_northwest_non_parents = len(northwest_non_parents)
p_southwest_non_parents = len(southwest_non_parents)

# DATA ON PARENTS ACCORDING TO AGE GROUPS PER REGION
northwest_teens_non_parents = []
northeast_teens_non_parents = []
southeast_teens_non_parents = []
southwest_teens_non_parents = []
for data in regional_teens_non_parents:
    if data[-1] == "northeast":
        northeast_teens_non_parents.append(data)
    elif data[-1] == "northwest":
        northwest_teens_non_parents.append(data)
    elif data[-1] == "southeast":
        southeast_teens_non_parents.append(data)
    else:
        southwest_teens_non_parents.append(data)

northwest_youth_non_parents = []
northeast_youth_non_parents = []
southwest_youth_non_parents = []
southeast_youth_non_parents = []
for data in regional_youth_non_parents:
    if data[-1] == "northeast":
        northeast_youth_non_parents.append(data)
    elif data[-1] == "northwest":
        northwest_youth_non_parents.append(data)
    elif data[-1] == "southeast":
        southeast_youth_non_parents.append(data)
    else:
        southwest_youth_non_parents.append(data)

southwest_adult_non_parents = []
southeast_adult_non_parents = []
northeast_adult_non_parents = []
northwest_adult_non_parents = []
for data in regional_adult_non_parents:
    if data[-1] == "northeast":
        northeast_adult_non_parents.append(data)
    elif data[-1] == "northwest":
        northwest_adult_non_parents.append(data)
    elif data[-1] == "southeast":
        southeast_adult_non_parents.append(data)
    else:
        southwest_adult_non_parents.append(data)

southwest_oldees_non_parents = []
southeast_oldees_non_parents = []
northeast_oldees_non_parents = []
northwest_oldees_non_parents = []
for data in regional_oldees_parents:
    if data[-1] == "northeast":
        northeast_oldees_non_parents.append(data)
    elif data[-1] == "northwest":
        northwest_oldees_non_parents.append(data)
    elif data[-1] == "southeast":
        southeast_oldees_non_parents.append(data)
    else:
        southwest_oldees_non_parents.append(data)

# EARLY/LATE MARRIAGE/BIRTH PER REGION
# note: p --> population
p_regional_teens_non_parents = len(regional_teens_non_parents)
p_southwest_teens_non_parents = len(southwest_teens_non_parents)
p_southwest_adult_non_parents = len(southwest_adult_non_parents)
p_southwest_youth_non_parents = len(southwest_youth_non_parents)
p_southwest_oldees_non_parents = len(southwest_oldees_non_parents)

p_regional_youth_non_parents = len(regional_youth_non_parents)
p_southeast_teens_non_parents = len(southeast_teens_non_parents)
p_southeast_youth_non_parents = len(southeast_youth_non_parents)
p_southeast_adult_non_parents = len(southeast_adult_non_parents)
p_southeast_oldees_non_parents = len(southeast_oldees_non_parents)

p_regional_adult_non_parents = len(regional_adult_non_parents)
p_northeast_teens_non_parents = len(northeast_teens_non_parents)
p_northeast_youth_non_parents = len(northeast_youth_non_parents)
p_northeast_adult_non_parents = len(northeast_adult_non_parents)
p_northeast_oldees_non_parents = len(northeast_oldees_non_parents)

p_regional_oldees_non_parents = len(regional_oldees_non_parents)
p_northwest_teens_non_parents = len(northwest_teens_non_parents)
p_northwest_youth_non_parents = len(northwest_youth_non_parents)
p_northwest_adult_non_parents = len(northwest_adult_non_parents)
p_northwest_oldees_non_parents = len(northwest_oldees_non_parents)
percent_ratio_of_youth_non_parents_per_region = percent_ratio(p_northeast_youth_non_parents,
                                                              "northeast youth non parents",
                                                              p_northwest_youth_non_parents,
                                                              "northwest youth non parents",
                                                              p_southeast_youth_non_parents,
                                                              "southeast youth non parents",
                                                              p_southwest_youth_non_parents,
                                                              "southwest youth non parents")
print(percent_ratio_of_youth_non_parents_per_region)

percent_ratio_of_adult_non_parents_per_region = percent_ratio(p_southeast_adult_non_parents, "southeast adult non parents", p_northeast_adult_non_parents,"northeast adult non parents", p_southwest_adult_non_parents, "southwest adult non parents", p_northwest_adult_non_parents, "northwest adult non parents")
# print(percent_ratio_of_adult_non_parents_per_region)

# percent_ratio_of_old_non_parents_per_region = percent_ratio(p_southwest_oldees_non_parents, "southwest oldees non parents",
#                                                              p_southeast_oldees_non_parents, "southwest oldees non parents",
#                                                              p_northwest_oldees_non_parents, "southwest oldees non parents",
#                                                              p_northeast_oldees_non_parents, "southwest oldees non parents")
# print(percent_ratio_of_old_non_parents_per_region)

# DATA OF MALES AND THEIR REGIONS
regional_males = []
regional_females = []
# classifications of genders in each region
genders_and_region = list(zip(sex, regions))
sorted_genders_and_region = sorted(genders_and_region)

for data in sorted_genders_and_region:
    if data[0] == "male":
        regional_males.append(data)
    else:
        regional_females.append(data)

# DATA OF MALES PER REGION
northwest_males = []
northeast_males = []
southeast_males = []
southwest_males = []
for data in regional_males:
    if data[-1] == "northwest":
        northwest_males.append(data)
    if data[-1] == "northeast":
        northeast_males.append(data)
    if data[-1] == "southeast":
        southeast_males.append(data)
    else:
        southwest_males.append(data)

# POPULATION OF MALES
# note: p --> population
p_regional_males = len(regional_males)
p_northeast_males = len(northeast_males)
p_northwest_males = len(northwest_males)
p_southeast_males = len(southeast_males)
p_southwest_males = len(southwest_males)
percent_ratio_of_males_per_region = percent_ratio(p_northwest_males, "northwest males", p_northeast_males,
                                                  "northeast males", p_southwest_males, "southwest males",
                                                  p_southeast_males, "southeast males")
# print(percent_ratio_of_males_per_region)

# DATA OF FEMALES PER REGION
northwest_females = []
northeast_females = []
southeast_females = []
southwest_females = []
for data in regional_females:
    if data[-1] == "northwest":
        northwest_females.append(data)
    if data[-1] == "northeast":
        northeast_females.append(data)
    if data[-1] == "southeast":
        southeast_females.append(data)
    else:
        southwest_females.append(data)

# POPULATION OF FEMALES
# note: p --> population
p_regional_females = len(regional_females)
p_northeast_females = len(northeast_females)
p_northwest_females = len(northwest_females)
p_southeast_females = len(southeast_females)
p_southwest_females = len(southwest_females)
percent_ratio_of_females_per_region = percent_ratio(p_northwest_females, "northwest females",
                                                    p_northeast_females, "northeast females",
                                                    p_southwest_females, "southwest females",
                                                    p_southeast_females, "southeast females")
# print(percent_ratio_of_females_per_region)

# DATA OF AGE GROUPS AND THEIR REGIONS
regional_teens = []
regional_youths = []
regional_adults = []
regional_oldees = []
# classification of ages by regions
ages_and_region = list(zip(ages, regions))
sorted_ages_and_region = sorted(ages_and_region)
for data in sorted_ages_and_region:
    if float(data[0]) <= 14:
        regional_teens.append(data)
    elif float(data[0]) >= 15 and float(data[0]) <= 24:
        regional_youths.append(data)
    elif float(data[0]) >= 25 and float(data[0]) <= 64:
        regional_adults.append(data)
    else:
        regional_oldees.append(data)

# data on regional teens
northeast_teens = []
northwest_teens = []
southeast_teens = []
southwest_teens = []
for data in regional_teens:
    if data[-1] == "northwest":
        northwest_teens.append(data)
    elif data[-1] == "northeast":
        northeast_teens.append(data)
    elif data[-1] == "southeast":
        southeast_teens.append(data)
    else:
        southwest_teens.append(data)

# POPULATION OF TEENS
# note: p --> population
p_regional_teens = len(regional_teens)
p_northeast_teens = len(northeast_teens)
p_northwest_teens = len(northwest_teens)
p_southeast_teens = len(southeast_teens)
p_southwest_teens = len(southwest_teens)
# percent_ratio_of_teens_per_region = percent_ratio(p_northwest_teens, "northwest teens", p_northeast_teens,
#                                                                 "northeast teens", p_southwest_teens, "southwest teens",
#                                                                 p_southeast_teens, "southwest teens")
# print(percent_ratio_of_teens_per_region)

# DATA OF YOUTHS AND THEIR REGIONS
northeast_youths = []
northwest_youths = []
southeast_youths = []
southwest_youths = []
for data in regional_youths:
    if data[-1] == "northwest":
        northwest_youths.append(data)
    elif data[-1] == "northeast":
        northeast_youths.append(data)
    elif data[-1] == "southeast":
        southeast_youths.append(data)
    else:
        southwest_youths.append(data)

# POPULATION OF YOUTHS
p_regional_youths = len(regional_youths)
p_northeast_youths = len(northeast_youths)
p_northwest_youths = len(northwest_youths)
p_southeast_youths = len(southeast_youths)
p_southwest_youths = len(southwest_youths)
percent_ratio_of_youths_per_region = percent_ratio(p_northwest_youths, "northwest youths",
                                                   p_northeast_youths, "northeast youths",
                                                   p_southwest_youths, "southwest youths",
                                                   p_southeast_youths, "southeast youths")
# print(percent_ratio_of_youths_per_region)

# DATA OF ADULTS AND THEIR REGIONS
northeast_adults = []
northwest_adults = []
southeast_adults = []
southwest_adults = []
for data in regional_adults:
    if data[-1] == "northwest":
        northwest_adults.append(data)
    elif data[-1] == "northeast":
        northeast_adults.append(data)
    elif data[-1] == "southeast":
        southeast_adults.append(data)
    else:
        southwest_adults.append(data)

# POPULATION OF ADULTS
p_regional_adults = len(regional_adults)
p_northeast_adults = len(northeast_adults)
p_northwest_adults = len(northwest_adults)
p_southeast_adults = len(southeast_adults)
p_southwest_adults = len(southwest_adults)
percent_ratio_of_adults_per_region = percent_ratio(p_northwest_adults, "northwest adults",
                                                   p_northeast_adults, "northeast adults",
                                                   p_southwest_adults, "southwest adults",
                                                   p_southeast_adults, "southeast adults")
# print(percent_ratio_of_adults_per_region)

# DATA OF OLDEES AND THEIR REGIONS
northeast_oldees = []
northwest_oldees = []
southeast_oldees = []
southwest_oldees = []
for data in regional_oldees:
    if data[-1] == "northwest":
        northwest_oldees.append(data)
    elif data[-1] == "northeast":
        northeast_oldees.append(data)
    elif data[-1] == "southeast":
        southeast_oldees.append(data)
    else:
        southwest_oldees.append(data)

# POPULATION OF OLDEES
p_regional_oldees = len(regional_oldees)
p_northeast_oldees = len(northeast_oldees)
p_northwest_oldees = len(northwest_oldees)
p_southeast_oldees = len(southeast_oldees)
p_southwest_oldees = len(southwest_oldees)
# percent_ratio_of_oldees_per_region = percent_ratio(p_northwest_oldees, "northwest oldees",
#                                                                  p_northeast_oldees, "northeast oldees",
#                                                                  p_southwest_oldees, "southwest oldees",
#                                                                  p_southeast_oldees, "southeast oldees")
# print(percent_ratio_of_oldees_per_region)


report = f'''
So far, no patient less than age 14 or more than age 64 pay medical insurance charge

more adults are involved than youths with about 50% difference

slightly more males are involved than females

most of the patients are obese and overweight(obesity surpasses though), very few are underweight, while less than twenty percent are healthy

population of underweight males and females is the same
there are slightly more healthy females than males
there are slightly more overweight females than males
there are more obese males than females

there are more underweight adults than youths
there are more healthy adults than youths
there are more overweight adults than youths
there are more obese adults than youths

there are more parents than non parents

late birth is prominent according to the data

there are slightly more male parents than female parents, therefore, there are more female non parents than male non parents

most of the parents are obese and overweight(obesity surpasses though), very few are underweight, while less than twenty percent are healthy

there are more adults are with no children than youths

most of the non parents are obese and overweight(obesity surpasses though), very few are underweight, while less than eighteeen percent are healthy

population of smokers is very minute

there are more adult smokers than youth smokers

most of the smokers are obese with very few being overweight, healthy and obese
most of the non smokers are obese less are overweight, lesser are healthy and the least are underweight

there are more parent smokers than non parent smokers

there are more male smokers than female smokers

there are more patients from southeast with little to no difference in the population of patients in other regions

there are more underweight patients in northeast, less in northwest and lesser in southwest and non in southeast

there are more healthy patients in northeast, less in northwest and lesser in southwest and least in southeast

there are more overweight patients in northwest, less in southwest and lesser in northeast and least in southeast

there are more smokers in southwest, less in southeast, lesser in northeast and least in northwest

there are more parents in southeast, less in northwest, lesser in southwest and least in northeast

early birth is more prominent in northwest,\
 p;less prominent in southeast, lesser prominent in southwest and least prominent in northeast  

there are more unmarried adults in southeast, less in northeast, lesser with slight difference in south and northwest
there are more unmarried youths in southeast, less in northeast, lesser in southwest and least in northwest 

there are more males in southwest, less in southeast, lesser with almost no difference in northeast and northwest

there are more females in southwest, less in southeast, lesser with almost no difference in northeast and northwest

there are more youths in southeast, less in both southwest and northeast with no difference and least in northwest 

there are more adults in southeast, less in southwest, northeast and northwest  

The prominent factors like obesity, males, adults, e.t.c. shows how much people with those factors are more likely to be involved in medical insurance than other less prominent factors.
'''


data_record = {
    "Age groups": {"teens": teens, "youths": youth, "adult": adult, "oldees": oldees},
    "Gender": {"males": males, "females": females},
    "classified bmi": {"underweight": underweight, "healthy": healthy, "overweight": overweight,
                       "obese": obese},
    "males classified bmi": {
        "underweight male": underweight_male,
        "healthy male": healthy_male,
        "overweight male": overweight_male,
        "obese male": obese_male},
    "females classified bmi": {
        "underweight female": underweight_female,
        "healthy female": healthy_female,
        "overweight female": overweight_female,
        "obese female": obese_female,
    },
    "age group bmis": {
        "age group underweight": age_underweight,
        "age group healthy": age_healthy,
        "age group overweight": age_overweight,
        "age group obese": age_obese,
    },
    "underweight per age group": {
        "underweight teens": underweight_teens,
        "underweight youths": underweight_youths,
        "underweight adults": underweight_adults,
        "underweight oldees": underweight_oldees,
    },
    "healthy per age group": {
        "healthy teens": healthy_teens,
        "healthy youths": healthy_youths,
        "healthy adults": healthy_adults,
        "healthy oldees": healthy_oldees,
    },
    "overweight per age group": {
        "overweight teens": overweight_teens,
        "overweight youths": overweight_youths,
        "overweight adults": overweight_adults,
        "overweight oldees": overweight_oldees,
    },
    "obese per age group": {
        "obese teens": overweight_teens,
        "obese youths": overweight_youths,
        "obese adults": overweight_adults,
        "obese oldees": overweight_oldees,
    },
    "parental status": {
        "parents": parents,
        "non parents": non_parents,
    },
    "parents per age group": {
        "teens parents": teens_parents,
        "youth parents": youth_parents,
        "adult parents": adult_parents,
        "oldees parents": oldees_parents,
    },
    "parents per gender": {
        "male parents": male_parents,
        "female parents": female_parents,
    },
    "parents per classified bmi": {
        "underweight parents": underweight_parents,
        "healthy parents": healthy_parents,
        "overweight parents": overweight_parents,
        "obese parents": obese_parents,
    },
    "smoking status": {
        "smokers": smoker,
        "non smokers": non_smoker,
    },
    "smokers per age group": {
        "teen smokers": teen_smokers,
        "youth smokers": youth_smokers,
        "adult smokers": adult_smokers,
        "oldees smokers": oldees_smokers,
    },
    "smokers per bmi": {
        "underweight smokers": underweight_smokers,
        "healthy smokers": healthy_smokers,
        "overweight smokers": overweight_smokers,
        "obese smokers": obese_smokers,
    },
    "smokers per parental status": {
        "parent smokers": parent_smokers,
        "non parent smokers": non_parent_smokers
    },
    "smokers per gender": {
        "male smokers": male_smokers,
        "female smokers": female_smokers,
    },
    "non smokers per bmi": {
        "underweight non smokers": underweight_non_smokers,
        "healthy non smokers": healthy_non_smokers,
        "overweight non smokers": overweight_non_smokers,
        "obese non smokers": obese_non_smokers
    },
    "patients per regions": {
        "northwest": northwest,
        "northeast": northeast,
        "southwest": southwest,
        "southeast": southeast
    },
    "bmi per region": {
        "regional underweight": regional_underweight,
        "regional healthy": regional_healthy,
        "regional overweight": regional_overweight,
        "regional obese": regional_obese,
    },
    "underweight per region": {
        "northwest underweight": northwest_underweight,
        "northeast underweight": northeast_underweight,
        "southwest underweight": southwest_underweight,
        "southeast underweight": southeast_underweight,
    },
    "healthy per region": {
        "northwest healthy": northwest_healthy,
        "northeast healthy": northeast_healthy,
        "southwest healthy": southwest_healthy,
        "southeast healthy": southeast_healthy,
    },
    "overweight per region": {
        "northwest overweight": northwest_overweight,
        "northeast overweight": northeast_overweight,
        "southwest overweight": southwest_overweight,
        "southeast overweight": southeast_overweight,
    },
    "obese per region": {
        "northwest obese": northwest_obese,
        "northeast obese": northeast_obese,
        "southwest obese": southwest_obese,
        "southeast obese": southeast_obese,
    },
    "smokers per region": {
        "northeast smokers": northeast_smokers,
        "northwest smokers": northwest_smokers,
        "southeast smokers": southeast_smokers,
        "southwest smokers": southwest_smokers,
    },
    "parents per region": {
        "northeast parents": northeast_parents,
        "northwest parents": northwest_parents,
        "southeast parents": southeast_parents,
        "southwest parents": southwest_parents,
    },
    "teens parents per region": {
        "northwest teens parents": northwest_teens_parents,
        "northeast teens parents": northeast_teens_parents,
        "southwest teens parents": southwest_teens_parents,
        "southeast teens parents": southeast_teens_parents,
    },
    "youth parents per region": {
        "northwest youth parents": northwest_youth_parents,
        "northeast youth parents": northeast_youth_parents,
        "southwest youth parents": southwest_youth_parents,
        "southeast youth parents": southeast_youth_parents,
    },
    "adult parents per region": {
        "northwest adult parents": northwest_adult_parents,
        "northeast adult parents": northeast_adult_parents,
        "southwest adult parents": southwest_adult_parents,
        "southeast adult parents": southeast_adult_parents,
    },
    "oldees parents per region": {
        "northwest oldees parents": northwest_oldees_parents,
        "northeast oldees parents": northeast_oldees_parents,
        "southwest oldees parents": southwest_oldees_parents,
        "southeast oldees parents": southeast_oldees_parents,
    },
    "P of youth non parents per region": {
        "northwest youth non parents": northwest_youth_non_parents,
        "northeast youth non parents": northeast_youth_non_parents,
        "southwest youth non parents": southwest_youth_non_parents,
        "southeast youth non parents": southeast_youth_non_parents,
    },
    "P of adult non parents per region ": {
        "northwest adult non parents": northwest_adult_non_parents,
        "northeast adult non parents": northeast_adult_non_parents,
        "southwest adult non parents": southwest_adult_non_parents,
        "southeast adult non parents": southeast_adult_non_parents,
    },
    "oldees non parents per region": {
        "northwest oldees non parents": northwest_oldees_non_parents,
        "northeast oldees non parents": northeast_oldees_non_parents,
        "southwest oldees non parents": southwest_oldees_non_parents,
        "southeast oldees non parents": southeast_oldees_non_parents,
    },
    "males per region": {
        "northwest males": northwest_males,
        "northeast males": northeast_males,
        "southeast males": southwest_males,
        "southwest males": southwest_males,
    },
    "females per region": {
        "northwest females": northwest_females,
        "northeast females": northeast_females,
        "southeast females": southwest_females,
        "southwest females": southwest_females,
    },
    "teens per region": {
        "northeast teens": northeast_teens,
        "southeast teens": southeast_teens,
        "northwest teens": northwest_teens,
        "southwest teens": southwest_teens,
    },
    "youths per region": {
        "northeast youths": northeast_youths,
        "southeast youths": southeast_youths,
        "northwest youths": northwest_youths,
        "southwest youths": southwest_youths,
    },
    "adults per region": {
        "northeast adults": northeast_adults,
        "southeast adults": southeast_adults,
        "northwest adults": northwest_adults,
        "southwest adults": southwest_adults,
    },
    "oldees per region": {
        "northeast oldees": northeast_oldees,
        "southeast oldees": southeast_oldees,
        "northwest oldees": northwest_oldees,
        "southwest oldees": southwest_oldees,
    },
    "report": report
}
population_record = {
    "P of age groups": {"p of teens": p_teens, "p of youths": p_youth, "p of adults": p_adult, "p of oldees": p_oldees,
                        "percent ratio of age group": percent_ratio_of_gender},
    "P of gender": {"p of males": p_males, "p of females": p_females,
                    "percent ratio of gender": percent_ratio_of_gender},
    "P of classified bmi": {"p of underweight": p_underweight, "p of healthy": p_healthy,
                            "p of overweight": p_overweight, "p of obese": p_obese,
                            "percent ratio of classified bmi": percent_ratio_of_classified_bmi},
    "P of males classified bmi": {
        "p of underweight male": p_underweight_male,
        "p of healthy male": p_healthy_male,
        "p of overweight male": p_overweight_male,
        "p of obese male": p_obese_male,
        "percent ratio of underweight gender": percent_ratio_of_underweight_gender,
        "percent ratio of healthy gender": percent_ratio_of_healthy_gender,
        "percent ratio of overweight gender": percent_ratio_of_overweight_gender,
        "percent ratio of obese gender": percent_ratio_of_obese_gender
    },
    "P of age group bmis": {
        "p of age group underweight": p_age_underweight,
        "p of age group healthy": p_age_healthy,
        "p of age group overweight": p_age_overweight,
        "p of age group obese": p_age_obese,
        "percent ratio of bmi per age group": percent_ratio_of_bmi_per_age_group
    },
    "P of underweight per age group": {
        "p of underweight_teens": p_underweight_teens,
        "p of underweight_youths": p_underweight_youths,
        "p of underweight_adults": p_underweight_adults,
        "p of underweight_oldees": p_underweight_oldees,
        "percent_ratio_of_underweight_per_age_group": percent_ratio_of_underweight_per_age_group
    },
    "P of healthy per age group": {
        "p of healthy teens": p_healthy_teens,
        "p of healthy youths": p_healthy_youths,
        "p of healthy adults": p_healthy_adults,
        "p of healthy oldees": p_healthy_oldees,
        "percent ratio of healthy per age group": percent_ratio_of_healthy_per_age_group
    },
    "P of overweight per age group": {
        "p of overweight teens": p_overweight_teens,
        "p of overweight youths": p_overweight_youths,
        "p of overweight adults": p_overweight_adults,
        "p of overweight oldees": p_overweight_oldees,
        "percent ratio of overweight per age group": percent_ratio_of_overweight_per_age_group
    },
    "P of obese per age group": {
        "p of obese teens": p_obese_teens,
        "p of obese youths": p_obese_youths,
        "p of obese adults": p_obese_adults,
        "p of obese oldees": p_obese_oldees,
        "percent ratio of obese per age group": percent_ratio_of_obese_per_age_group
    },
    "P of parental status": {
        "p of parents": p_parents,
        "p of non parents": p_non_parents,
        "percent ratio of parental status": percent_ratio_of_parental_status
    },
    "P of parents per age group": {
        "p of teens parents": p_teens_parents,
        "p of youth parents": p_youth_parents,
        "p of adult parents": p_adult_parents,
        "p of oldees parents": p_oldees_parents,
        "percent ratio of parents per age group": percent_ratio_of_parents_per_age_group
    },
    "P of parents per gender": {
        "p of male parents": p_male_parents,
        "p of female parents": p_female_parents,
        "percent ratio of parents per gender": percent_ratio_of_parents_per_gender,
    },
    "P of parents per classified bmi": {
        "p underweight parents": p_underweight_parents,
        "p_healthy_parents": p_healthy_parents,
        "p_overweight_parents": p_overweight_parents,
        "p_obese_parents": obese_parents,
        "percent_ratio_of_parents_per_classified_bmi": percent_ratio_of_parents_per_classified_bmi
    },
    "P of non parents per age group": {
        "p of teens non parents": p_teens_non_parents,
        "p of youth non parents": p_youth_non_parents,
        "p of adult non parents": p_adult_non_parents,
        "p of oldees non parents": p_oldees_non_parents,
        "percent ratio of non parents per age group": percent_ratio_of_non_parents_per_age_group
    },
    "P of non parents per gender": {
        "p of male non parents": p_male_non_parents,
        "p of female non parents": p_female_non_parents,
        "percent ratio of non parents per gender": percent_ratio_of_non_parents_per_gender,
    },
    "P of non parents per classified bmi": {
        "p underweight non parents": p_underweight_non_parents,
        "p healthy non parents": p_healthy_non_parents,
        "p overweight non parents": p_overweight_non_parents,
        "p obese non parents": obese_non_parents,
        "percent ratio of non parents per classified bmi": percent_ratio_of_non_parents_per_classified_bmi
    },
    "P of smoking status": {
        "p of smokers": p_smokers,
        "p of non smokers": p_non_smokers,
        "percent ratio of patients per smoking status": percent_ratio_of_patients_per_smoking_status
    },
    "P of smokers per age group": {
        "p of teen smokers": p_teen_smokers,
        "p of youth smokers": p_youth_smokers,
        "p of adult smokers": p_adult_smokers,
        "p of oldees smokers": p_oldees_smokers,
        "percent ratio of smokers per age group": percent_ratio_of_smokers_per_age_group
    },
    "P of smokers per bmi": {
        "p of underweight smokers": p_underweight_smokers,
        "p of healthy smokers": p_healthy_smokers,
        "p of overweight smokers": p_overweight_smokers,
        "p of obese smokers": p_obese_smokers,
        "percent ratio of smokers per bmi": percent_ratio_of_smokers_per_bmi
    },
    "P of smokers per parental status": {
        "p of parent smokers": p_parent_smokers,
        "p of non parent smokers": p_non_parent_smokers,
        "percent ratio of smokers per parental status": percent_ratio_of_smokers_per_parental_status
    },
    "P of smokers per gender": {
        "p of male smokers": p_male_smokers,
        "p of female smokers": p_female_smokers,
        "percent ratio of smokers per gender": percent_ratio_of_smokers_per_gender
    },
    "P of non smokers per bmi": {
        "p of underweight non smokers": p_underweight_non_smokers,
        "p of healthy non smokers": p_healthy_non_smokers,
        "p of overweight non smokers": p_overweight_non_smokers,
        "p of obese non smokers": p_obese_non_smokers,
        "percent ratio of non smokers per bmi": percent_ratio_of_non_smokers_per_bmi,
    },
    "P of patients per regions": {
        "p of northwest": p_northwest,
        "p of northeast": p_northeast,
        "p of southwest": p_southwest,
        "p of southeast": p_southeast,
        "percent ratio of patients per region": percent_ratio_of_patients_per_region,
    },
    "P of bmi per region": {
        "p of regional underweight": p_regional_underweight,
        "p of regional healthy": p_regional_healthy,
        "p of regional overweight": p_regional_overweight,
        "p of regional obese": p_regional_obese,
        "percent ratio of bmi per region": percent_ratio_of_bmi_per_region
    },
    "P of underweight per region": {
        "p of northwest underweight": p_northwest_underweight,
        "p of northeast underweight": p_northeast_underweight,
        "p of southwest underweight": p_southwest_underweight,
        "p of southeast underweight": p_southeast_underweight,
        "percent ratio of underweight per region": percent_ratio_of_underweight_per_region
    },
    "P of healthy per region": {
        "p of northwest healthy": p_northwest_healthy,
        "p of northeast healthy": p_northeast_healthy,
        "p of southwest healthy": p_southwest_healthy,
        "p of southeast healthy": p_southeast_healthy,
        "percent ratio of healthy per region": percent_ratio_of_healthy_per_region
    },
    "P of overweight per region": {
        "p of northwest overweight": p_northwest_overweight,
        "p of northeast overweight": p_northeast_overweight,
        "p of southwest overweight": p_southwest_overweight,
        "p of southeast overweight": p_southeast_overweight,
        "percent ratio of overweight per region": percent_ratio_of_overweight_per_region
    },
    "P of obese per region": {
        "p of northwest obese": p_northwest_obese,
        "p of northeast obese": p_northeast_obese,
        "p of southwest obese": p_southwest_obese,
        "p of southeast obese": p_southeast_obese,
        "percent_ratio_of_obese_per_region": percent_ratio_of_obese_per_region
    },
    "P of smokers per region": {
        "p of northeast smokers": p_northeast_smokers,
        "p of northwest smokers": p_northwest_smokers,
        "p of southeast smokers": p_southeast_smokers,
        "p of southwest smokers": p_southwest_smokers,
        "percent ratio of smokers per region": percent_ratio_of_smokers_per_region
    },
    "birth rates per region": {
        "p of northeast parents": p_northeast_parents,
        "p of northwest parents": p_northwest_parents,
        "p of southwest parents": p_southwest_parents,
        "p of southeast parents": p_southeast_parents,
        "percent ratio of birth rates per region": percent_ratio_of_birth_rates_per_region
    },
    "Extreme early birth per region": {
        "p of northwest teens parents": p_northwest_teens_parents,
        "p of northeast teens parents": p_northeast_teens_parents,
        "p of southwest teens parents": p_southwest_teens_parents,
        "p of southeast teens parents": p_southeast_teens_parents,
        # "percent ratio of extreme early birth per region": percent_ratio_of_extreme_early_birth_per_region
    },
    "Early birth per region": {
        "p of northwest youth parents": p_northwest_youth_parents,
        "p of northeast youth parents": p_northeast_youth_parents,
        "p of southwest youth parents": p_southwest_youth_parents,
        "p of southeast youth parents": p_southeast_youth_parents,
        "percent ratio of early birth per region": percent_ratio_of_early_birth_per_region
    },
    "P of youth non parents": {
        "p of northwest youth non parents": p_northwest_youth_non_parents,
        "p of northeast youth non parents": p_northeast_youth_non_parents,
        "p of southwest youth non parents": p_southwest_youth_non_parents,
        "p of southeast youth non parents": p_southeast_youth_non_parents,
        "percent ratio of youth non parents per region": percent_ratio_of_youth_non_parents_per_region
    },
    "P of adult singles": {
        "p of northwest adult non parents": p_northwest_adult_non_parents,
        "p of northeast adult non parents": p_northeast_adult_non_parents,
        "p of southwest adult non parents": p_southwest_adult_non_parents,
        "p of southeast adult non parents": p_southeast_adult_non_parents,
        "percent ratio of adult non parents per region": percent_ratio_of_adult_non_parents_per_region
    },
    "P of oldees singles": {
        "p of northwest oldees non parents": p_northwest_oldees_non_parents,
        "p of northeast oldees non parents": p_northeast_oldees_non_parents,
        "p of southwest oldees non parents": p_southwest_oldees_non_parents,
        "p of southeast oldees non parents": p_southeast_oldees_non_parents,
        # "percent ratio of old non parents per region": percent_ratio_of_old_non_parents_per_region
    },
    "P of males per region": {
        "p of northwest males": p_northwest_males,
        "p of northeast males": p_northeast_males,
        "p of southeast males": p_southwest_males,
        "p of southwest males": p_southwest_males,
        "percent ratio of males per region": percent_ratio_of_males_per_region,
    },
    "P of females per region": {
        "p of northwest females": p_northwest_females,
        "p of northeast females": p_northeast_females,
        "p of southeast females": p_southwest_females,
        "p of southwest females": p_southwest_females,
        "percent ratio of females per region": percent_ratio_of_females_per_region,
    },
    "P of teens per region": {
        "p of northeast teens": p_northeast_teens,
        "p of southeast teens": p_southeast_teens,
        "p of northwest teens": p_northwest_teens,
        "p of southwest teens": p_southwest_teens,
        # "percent ratio of teens per region": percent_ratio_of_teens_per_region
    },
    "P of youths per region": {
        "p of northeast youths": p_northeast_youths,
        "p of southeast youths": p_southeast_youths,
        "p of northwest youths": p_northwest_youths,
        "p of southwest youths": p_southwest_youths,
        "percent ratio of youths per region": percent_ratio_of_youths_per_region
    },
    "P of adults per region": {
        "p of northeast adults": p_northeast_adults,
        "p of southeast adults": p_southeast_adults,
        "p of northwest adults": p_northwest_adults,
        "p of southwest adults": p_southwest_adults,
        "percent ratio of adults per region": percent_ratio_of_adults_per_region
    },
    "P of oldees per region": {
        "p of northeast oldees": p_northeast_oldees,
        "p of southeast oldees": p_southeast_oldees,
        "p of northwest oldees": p_northwest_oldees,
        "p of southwest oldees": p_southwest_oldees,
        # "percent ratio of oldees per region": percent_ratio_of_oldees_per_region
    },
}

data_keys = []
data_values = []
population_keys = []
population_values = []
for key in data_record.keys():
    data_keys.append(key)
for key in population_record.keys():
    population_keys.append(key)
for value in data_record.values():
    data_values.append(value)
for value in population_record.values():
    population_values.append(value)

data_key_and_values = {key: value for key, value in zip(data_keys, data_values)}
population_key_and_values = {key: value for key, value in zip(population_keys, population_values)}

print(f'''
Welcome to Medical Insurance Analysis.
As an intro, there are two types of information you can further analyse or examine: the data and the population 
of each data. 
Please note that any point you see P or p, it stands for population
    ''')



def navigation(report=report):
    try:
        count = 0
        while count == 0:

            keys_request = input(
                'Please type "data" or "population" for you to see the information contained in either '
                'of the two. ')
            if keys_request.upper() == "DATA":
                print(f'''
    {", ".join(data_keys)} 
                ''')
            elif keys_request.lower() == "population":
                print(f'''
    {", ".join(population_keys)} 
                        ''')
            else:
                pass


            value_request = input(f'''
    Above are the keys to each data.
    Please type the exact case and spelling of any of the keys listed above to get further information: ''')
            for data in data_keys:
                if value_request.lower().upper() == data:
                    print(f'''
        {data_key_and_values[value_request]}
            ''')
            for data in population_keys:
                if value_request.lower().upper() == data:
                    print(f'''
    {population_key_and_values[value_request]}
            ''')

            analyze = input(f'''
    Do you wish to add some report?, if yes, type the report: 
    if no, please type no: ''')
            if analyze.lower() != "no":
                report += analyze
                print(report)
            else:
                print("Good luck as you examine the data")


            permission = input("Do you wish to view another dataset? Enter yes or no ")
            while permission.lower() == "yes":
                navigation()
            count += 1

    except ValueError as error:
        print("please make sure you are typing the correct spelling of any of the keys listed")

print(navigation())


# problems with the code
# the try except is not functioning properly, don't know if anyone can help out
# value_request only allows for the exact case and spelling to be typed, don't know if anyone can help me fix it so that it can be more flexible with the case
