from pandas import *

db = read_csv("Database.csv", encoding='UTF-8', dtype={"Phone": str})

unsubs = read_csv("Unsubscribed.csv", header=None, encoding='UTF-8')
unsubs = unsubs.drop_duplicates()

db["Unsubscribed"] = "No"

col_project = "Project"
project = "B"
filtered_rows = db[db[col_project].str.contains(project)].copy()

unsubs.columns = ["Unsubscribed"]

for index, row in unsubs.iterrows():
    unsubscribed = row["Unsubscribed"]
    for i, r in filtered_rows.iterrows():
        phone = r["Phone"]
        if unsubscribed == phone:
            filtered_rows.loc[i, "Unsubscribed"] = "Yes"
            break

filtered_rows.to_csv("WhatsApp_Leads_Project_B", encoding='UTF-8', index=False)
