# Pick one of two API endpoints at runtime and send the right headers.

import requests

PJ_URL = "https://official-joke-api.appspot.com/random_joke"
DAD_JOKE_URL = "https://icanhazdadjoke.com/"


def get_joke(url, mood):
    headers = {"Accept": "application/json"}
    data = requests.get(url, headers=headers, timeout=10).json()

    if mood == "dad":
        return data["joke"]
    return f'{data["setup"]} ... {data["punchline"]}'


def main():
    while True:
        try:
            mood = input("Which joke? (dad / pj): ").strip().lower()    #strip() removes whitespace from the beginning and end of the string, lower() converts to lowercase
            if mood not in ["dad", "pj"]:
                raise ValueError("Invalid input. Please enter 'dad' or 'pj'.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    url = PJ_URL if mood == "pj" else DAD_JOKE_URL
    mood = "pj" if mood == "pj" else "dad"
    print("\n" + get_joke(url, mood))


if __name__ == "__main__":
    main()
