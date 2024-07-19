import requests

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = 'alskdjlasjd'
USERNAME = 'lim1122'

user_params= {
    'token': TOKEN
    'username': USERNAME
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graph"