import requests
import datetime as dt
from dotenv import dotenv_values

cred = dotenv_values(".env")


TOKEN = cred["TOKEN"]
USERNAME = cred["USERNAME"]
GRAPHID = "pyb001"

PIXELAR_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELAR_ENDPOINT}/{USERNAME}/graphs"
POSTING_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPHID}"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

graph_config = {
    "id":GRAPHID,
    "name":"bibleGraph",
    "unit":"pages",
    "type":"int",
    "color":"momiji"
}

today = dt.datetime.now()
pixel_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"2"
}
# response = requests.post(url=pixelar_endpoint, json=user_params)
# print(response.text)


# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

response = requests.post(url=POSTING_ENDPOINT, json=pixel_config, headers=headers)
print(response.text)