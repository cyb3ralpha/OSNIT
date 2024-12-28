import requests
from bs4 import BeautifulSoup
import json

# Global API keys (replace with real ones)
API_KEYS = {
    "twitter": "your_twitter_api_key",
    "github": "your_github_api_key",
    # Add other APIs here
}

def run():
    print("\n[Social Media OSINT Tool]")
    username = input("Enter the username to search: ")
    print(f"\n[Gathering OSINT for Username: {username}]\n")
    
    # Perform OSINT tasks
    gather_profile_info(username)
    gather_social_footprint(username)
    scrape_twitter(username)  # Scraper logic for Twitter example
    search_leaked_credentials(username)
    
    input("\nPress Enter to return to the menu...")

# 1. Gather Profile Information using APIs
def gather_profile_info(username):
    print("[+] Gathering Profile Information...")
    try:
        twitter_data = get_twitter_info(username)
        github_data = get_github_info(username)
        gender_data = predict_gender(username)  # Genderize API Integration
        
        if twitter_data:
            print("\n--- Twitter API Data ---")
            print(json.dumps(twitter_data, indent=2))
        
        if github_data:
            print("\n--- GitHub API Data ---")
            print(json.dumps(github_data, indent=2))
        
        if gender_data:
            print("\n--- Gender Prediction ---")
            print(f"Name: {gender_data['name']}")
            print(f"Predicted Gender: {gender_data['gender']}")
            print(f"Probability: {gender_data['probability'] * 100:.2f}%")
    
    except Exception as e:
        print(f"[!] Error gathering profile info: {e}")

# 2. Cross-Platform Social Footprint
def gather_social_footprint(username):
    print("\n[+] Gathering Social Footprint Across Platforms...")
    platforms = [
        f"https://twitter.com/{username}",
        f"https://www.instagram.com/{username}/",
        f"https://github.com/{username}",
        f"https://www.reddit.com/user/{username}",
    ]
    for platform in platforms:
        response = requests.get(platform)
        if response.status_code == 200:
            print(f"[*] Found profile: {platform}")
        else:
            print(f"[!] Profile not found: {platform}")

# 3. Search Leaked Credentials
def search_leaked_credentials(username_or_email):
    print("\n[+] Searching for Leaked Credentials...")
    try:
        # Example API integration for breached emails (like "Have I Been Pwned?")
        url = f"https://api.hibp.com/breachedaccount/{username_or_email}"
        api_key = "your_hibp_api_key"  # Replace with actual key
        headers = {"Authorization": f"Bearer {api_key}"}
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            breaches = response.json()
            print("[*] Leaked credentials found:")
            for breach in breaches:
                print(f"- {breach['Title']}: {breach['BreachDate']}")
        else:
            print("[!] No leaks found.")
    except Exception as e:
        print(f"[!] Error searching for leaks: {e}")

# 4. Scraper Logic for Twitter (Example)
def scrape_twitter(username):
    print("\n[+] Scraping Twitter Profile...")
    try:
        url = f"https://twitter.com/{username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Example: Scrape profile name
            name_tag = soup.find('div', {'data-testid': 'UserName'})
            if name_tag:
                print(f"Profile Name: {name_tag.text}")
            else:
                print("Profile Name: Not found.")
            
            # Example: Scrape bio
            bio_tag = soup.find('div', {'data-testid': 'UserDescription'})
            if bio_tag:
                print(f"Bio: {bio_tag.text}")
            else:
                print("Bio: Not found.")
        else:
            print(f"[!] Failed to scrape Twitter. Status code: {response.status_code}")
    except Exception as e:
        print(f"[!] Error scraping Twitter: {e}")

# 5. Twitter API Example
def get_twitter_info(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {
        "Authorization": f"Bearer {API_KEYS['twitter']}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

# 6. GitHub API Example
def get_github_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# 7. Genderize API Example
def predict_gender(name):
    print("[+] Predicting Gender...")
    try:
        url = f"https://api.genderize.io?name={name}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("[!] Gender prediction failed.")
    except Exception as e:
        print(f"[!] Error predicting gender: {e}")
    return None

# Run the program
if __name__ == "__main__":
    run()