from pandas import *


db = read_csv("Database.csv", encoding='cp1251')
unsubs = read_csv("Unsubscribed.csv", header=None, encoding='cp1251')
unsubs = unsubs.drop_duplicates()

db[["Not by email", "Not by phone", "Unsubscribed"]] = "No"

col_project = "Project"
project = "B"
filtered_rows = db[db[col_project].str.contains(project)]


unsubs.columns = ['Unsubscribed']

for index, row in unsubs.iterrows():
    unsubscribed = row["Unsubscribed"]
    for i, r in filtered_rows.iterrows():
        phone = r["Phone"]
        phone = "+" + str(phone)
        email = r["Email"]

        if unsubscribed == phone:
            filtered_rows.loc[i, 'Not by phone'] = "Yes"
            filtered_rows.loc[i, "Unsubscribed"] = "Yes"
            break
        if unsubscribed == email:
            filtered_rows.loc[i, 'Not by email'] = "Yes"
            filtered_rows.loc[i, "Unsubscribed"] = "Yes"
            break

filtered_rows.to_csv("WhatsApp_Leads_Project_B")

