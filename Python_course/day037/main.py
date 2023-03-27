import requests
from datetime import datetime

USERNAME = "toksy"
TOKEN = "hgg54ffdg67hg8jt5"

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "study_hour",
    "unit": "hour",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now().strftime("%Y%m%d")

new_pixel_endpoint = f"{graph_endpoint}/graph1"

new_pixel_config = {
    "date": today,
    "quantity": "8",
}


# response = requests.post(url=new_pixel_endpoint, json=new_pixel_config, headers=headers)
# print(response.text)


update_graph_endpoint = f"{graph_endpoint}/graph1/20230324"

update_config = {
    "quantity": "15",
}

# response = requests.put(url=update_graph_endpoint, json=update_config, headers=headers)
# print(response.text)

delete_graph_endpoint = f"{graph_endpoint}/graph1/20230324"

response = requests.delete(url=delete_graph_endpoint, headers=headers)
print(response.text)
