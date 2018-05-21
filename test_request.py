import requests


def main():
    # WRITE DATA
    response = requests.post('http://localhost:8000/store', data={'V': 220, 'A': 2, 'W': 440, "socket_id": 1})
    print(response.content)
    
    # READ DATA from Server
    response = requests.get('http://localhost:8000/info')
    print(response.content)

    
main()