import requests
import json

api_url = "https://api.github.com/users/"

def github_user_info(username):
    try:
        response = requests.get(f"{api_url}{username}")
        if response.status_code == 200:
            return response.json()
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return None

def output_user_info(user_info):
    if user_info:
        for detail in info:
            print(f"{detail}: {user_info.get(detail)}")
    else:
        print("No user information available.")

def output_json(user_info):
    with open(f"github_{user_info.get('login')}.json", "w") as json_file:
        json.dump(user_info, json_file, indent=2)

if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    info = ["name", "public_repos", "followers", "location"]
    user_info = github_user_info(username)
    output_user_info(user_info)
    output_json(user_info)