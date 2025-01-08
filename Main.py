from dotenv import load_dotenv
from atproto import Client, client_utils


import os

def main():
    client = Client()
    username = os.getenv('BLUESKY_USERNAME')
    password = os.getenv('BLUESKY_PASSWORD')
    profile = client.login(username, password)
    print('Welcome,', profile.display_name)

    text = client_utils.TextBuilder().text('Hello World from ').link('Python SDK', 'https://atproto.blue')
    post = client.send_post(text)
    client.like(post.uri, post.cid)
    
    
if __name__ == '__main__':
    load_dotenv()
    main()