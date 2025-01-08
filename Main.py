from dotenv import load_dotenv
from atproto import Client, client_utils

import os
import requests

def get_last_show_watched(user_id):
    url = "https://graphql.anilist.co"
    
    body = """ 
    query ($userId: Int) {
    MediaListCollection(userId: $userId, type: ANIME, status: COMPLETED, sort: UPDATED_TIME_DESC) {
        lists {
        entries {
            media {
            title {
                romaji
                english
                native
            }
            id
            episodes
            status
            }
            completedAt {
            year
            month
            day
            }
        }
        }
    }
    }
    """
    
    response = requests.post(url=url, json={"query": body}) 
    print("response status code: ", response.status_code) 
    if response.status_code == 200: 
        print("response : ", response.content) 
    return response

def main():
    client = Client()
    username = os.getenv('BLUESKY_USERNAME')
    password = os.getenv('BLUESKY_PASSWORD')
    client.login(username, password)

    # Example usage
    user_id = os.getenv('ANILIST_USER_ID')
    last_show = get_last_show_watched(user_id)
    if last_show:
        print(f"Last show watched: {last_show['title']['romaji']}")
    else:
        print("No completed shows found for this user.")
        
    # while True:
    #     user_input = input('Enter your post (or type "exit" to quit): ')
    #     if user_input.lower() == 'exit':
    #         break
    #     post = client.send_post(user_input)

    
if __name__ == '__main__':
    load_dotenv()
    main()