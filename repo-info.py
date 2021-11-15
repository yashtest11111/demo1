# importing  the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "http://115.115.91.60:5432/train"

# data to be sent to api
data = {
	"url": "https://github.com/priyankdemo/reg_demo_priyank_yash",
	"branch_name": "master",
	"user_name": "priy@gmail.com"
}

# sending post request and saving response as response object
r = requests.post(url = API_ENDPOINT, data = data)

# extracting response text
pastebin_url = r.text
print("The pastebin URL is :%s"%pastebin_url)