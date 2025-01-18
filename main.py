import requests
import os
from bs4 import BeautifulSoup

ROLIMONS_API_URL = "https://www.rolimons.com/itemapi/itemdetails"
ROLIMONS_ITEM_URL = "https://www.rolimons.com/item/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_item_details_from_api():
    response = requests.get(ROLIMONS_API_URL, headers=headers)
    response.raise_for_status()
    return response.json()["items"]

def get_item_id(query, items):
    query_lower = query.lower()
    for item_id, details in items.items():
        name = details[0].lower()
        acronym = details[1].lower()
        if query_lower in [item_id, name, acronym]:
            return item_id
    return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def search_menu(items):
    while True:
        query = input("Enter item name, acronym, or ID to search (or 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        item_id = get_item_id(query, items)
        if item_id:
            print(f"Item found: {item_id}")
            item_details = items[item_id]
            print(f"Name: {item_details[0]}")
            print(f"Acronym: {item_details[1]}")
            print(f"Best Price: {item_details[2]}")
        else:
            print("Item not found.")

def main():
    items = fetch_item_details_from_api()
    while True:
        clear_screen()
        print("Main Menu:")
        print("1. Fetch item details")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            search_menu(items)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter 1, 2.")
main()
