import pandas as pd

data = pd.read_csv("data/CRDC2013_14.csv", encoding="Latin-1")

data["total_enrollment"] = data["TOT_ENR_M"] + data["TOT_ENR_F"]

all_enrollments = data["total_enrollment"].sum()

school_enrollment = [
    'SCH_ENR_HI_M',
    'SCH_ENR_HI_F',
    'SCH_ENR_AM_M',
    'SCH_ENR_AM_F',
    'SCH_ENR_AS_M',
    'SCH_ENR_AS_F',
    'SCH_ENR_HP_M',
    'SCH_ENR_HP_F',
    'SCH_ENR_BL_M',
    'SCH_ENR_BL_F',
    'SCH_ENR_WH_M',
    'SCH_ENR_WH_F',
    'SCH_ENR_TR_M',
    'SCH_ENR_TR_F']


enrollment_perc = {}

for i in school_enrollment:
	enrollment_perc[i] = ((data[i].sum()/all_enrollments)*100).round(2)

female_perc = (data["TOT_ENR_F"].sum()/all_enrollments).round(2)
male_perc = (data["TOT_ENR_M"].sum()/all_enrollments).round(2)

print("Enrollment percentages:", "\n", enrollment_perc)
print("Total Female Percentage:", female_perc)
print("Total Male Percentage:", male_perc)
