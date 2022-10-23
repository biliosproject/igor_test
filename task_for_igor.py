import requests

data_for_post_request = {
    "first_parameter": "first_value",
    "second_parameter": "second_value"
}

url_for_request = "https://webhook.site/e4d4d845-50d2-481f-a6e5-1255cbf54136"

requests.post(url=url_for_request, data=data_for_post_request)