from dotenv import load_dotenv
from atproto import Client, client_utils


import os

def main():
    client = Client()
    username = os.getenv('BLUESKY_USERNAME')
    password = os.getenv('BLUESKY_PASSWORD')
    profile = client.login(username, password)
    print('Welcome,', profile.display_name)

    while True:
        user_input = input('Enter your post (or type "exit" to quit): ')
        if user_input.lower() == 'exit':
            break
        post = client.send_post(user_input)
    
    
if __name__ == '__main__':
    load_dotenv()
    main()