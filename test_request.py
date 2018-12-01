import requests

BASE_URL = 'https://smartmark01.herokuapp.com'
# BASE_URL = 'http://localhost:8000'

def main():
    # WRITE DATA
    response = requests.post(BASE_URL + '/store', data={'V': 22220, 'A': 3, 'W': 4, "socket_id": 1})
    print(response.content)
    
    # READ DATA from Server
    response = requests.get(BASE_URL + '/info')
    print(response.content)

if __name__ == "__main__":
    main()