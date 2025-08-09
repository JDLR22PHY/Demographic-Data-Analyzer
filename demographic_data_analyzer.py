# @title Default title text
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df["sex"] == "Male", "age"].mean()
    average_age_men = round(average_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = len(df.loc[df["education"] == "Bachelors", "education"]) * 100 / len(df)
    percentage_bachelors = round(percentage_bachelors, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    educate_people = df.loc[(df["education"] == "Bachelors") | (df['education'] == "Masters") | (df['education'] == "Doctorate")]
    educate_people_50k = educate_people.loc[educate_people["salary"] == ">50K"]
    higher_education_rich = round(len(educate_people_50k) * 100 / len(educate_people), 1)


    # What percentage of people without advanced education make more than 50K?
    not_educate_people = df.loc[(df["education"] != "Bachelors") & (df['education'] != "Masters") & (df['education'] != "Doctorate")]
    not_educate_people_50k = not_educate_people.loc[not_educate_people["salary"] == ">50K"]
    lower_education_rich =  round(len(not_educate_people_50k) * 100 / len(not_educate_people), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    work_hour = df["hours-per-week"]
    min_work_hours = work_hour.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mask_minhour = df["hours-per-week"] <= min_work_hours
    work_minhour = df[mask_minhour]
    work_minhour_50k = work_minhour.loc[work_minhour["salary"] == ">50K"]
    rich_percentage = len(work_minhour_50k) * 100 // len(work_minhour)

    # What country has the highest percentage of people that earn >50K?
    people_50k = df.loc[df["salary"] == ">50K"]
    people_50k_country = people_50k["native-country"]
    people_50k_country = people_50k_country.value_counts()
    people_country = df["native-country"]
    people_country = people_country.value_counts()
    highest_earning_country = (people_50k_country / people_country).idxmax()
    highest_earning_country_percentage = round((people_50k_country / people_country).max() * 100, 1)
    

    # Identify the most popular occupation for those who earn >50K in India.
    people_india_50k = df.loc[(df["salary"] == ">50K") & (df["native-country"] == "India")]
    people_india_50k_occupation = people_india_50k["occupation"]
    people_india_50k_occupation = people_india_50k_occupation.value_counts()
    top_IN_occupation = people_india_50k_occupation.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
