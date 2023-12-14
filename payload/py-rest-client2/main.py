import requests, urllib3, os, string, random, time
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient


urllib3.disable_warnings()


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CREDS_FILE = os.path.join(BASE_DIR, 'creds.txt')
TOKEN_URL = "https://wso2.keys4.local:9443/oauth2/token"
BASE_URL = "https://wso2.keys4.local:8243/"


def get_creds():
    creds = []
    with open(CREDS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            creds.append([el for el in line.split(':')])
    # client_id, client_secret, api_appender
    return creds

def get_random_string(num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(num))

def enrich_with_tokens(creds: list):
    res = []
    for line in creds:
        client = BackendApplicationClient(client_id=line[0])
        oauth = OAuth2Session(client=client)
        full_access_token = oauth.fetch_token(token_url=TOKEN_URL, client_id=line[0], client_secret=line[1],verify=False)
        access_token = full_access_token['access_token']
        # print(line[0], line[1], access_token, sep="==")
        res.append([line[0], line[1], line[2], access_token])
    return res

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

# print(f"ACCESS_TOKEN: {access_token} \n")

def make_request(data: list):
    inner_data = random.choice(data)
    resourse_appender = random.choice(["small", "middle", "big", get_random_string(6), "hello"])
    url = BASE_URL + inner_data[2] + "/" + resourse_appender
    print(url)
    if resourse_appender == "hello":
        payload = get_random_string(1024)
        response = requests.post(url, data={'key': payload}, auth=BearerAuth(inner_data[3]), verify=False)
    else:
        response = requests.get(url, auth=BearerAuth(inner_data[3]),verify=False)
    # print(f"RESPONSE CODE: {response.status_code}  RESPONSE MESSAGE: {response.content} \n")
    print(f"RESPONSE CODE: {response.status_code}\n")


creds = enrich_with_tokens(get_creds())
# print(creds)
for i in range(10):
    make_request(creds)
    time.sleep(random.randint(1, 4))