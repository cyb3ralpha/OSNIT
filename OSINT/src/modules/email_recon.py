import requests
import json

# Global API keys (replace with real ones)
API_KEYS = {
    "hibp": "your_haveibeenpwned_api_key",  # Replace with your Have I Been Pwned API key
    "hunter": "your_hunter_api_key",        # Replace with your Hunter.io API key
}

def run():
    print("\n[Email Reconnaissance]")
    email = input("Enter the email address to search: ")
    print(f"\n[Gathering information about: {email}]\n")
    
    # Perform email reconnaissance
    check_email_breaches(email)
    verify_email_address(email)
    analyze_email_domain(email)
    
    input("\nPress Enter to return to the menu...")

# 1. Check Email Breaches
def check_email_breaches(email):
    print("[+] Checking for Breaches...")
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        headers = {"hibp-api-key": API_KEYS['hibp']}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            breaches = response.json()
            print("\n--- Breaches Found ---")
            for breach in breaches:
                print(f"- {breach['Name']} (Date: {breach['BreachDate']})")
        elif response.status_code == 404:
            print("[!] No breaches found for this email.")
        else:
            print(f"[!] Error checking breaches. Status code: {response.status_code}")
    except Exception as e:
        print(f"[!] Error checking breaches: {e}")

# 2. Verify Email Address
def verify_email_address(email):
    print("\n[+] Verifying Email Address...")
    try:
        url = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={API_KEYS['hunter']}"
        response = requests.get(url)
        
        if response.status_code == 200:
            verification = response.json()
            print("\n--- Email Verification Results ---")
            print(f"Email: {verification['data']['email']}")
            print(f"Valid: {verification['data']['result']}")
            print(f"Score: {verification['data']['score']}")
        else:
            print(f"[!] Failed to verify email. Status code: {response.status_code}")
    except Exception as e:
        print(f"[!] Error verifying email: {e}")

# 3. Analyze Email Domain
def analyze_email_domain(email):
    print("\n[+] Analyzing Email Domain...")
    try:
        domain = email.split('@')[-1]
        url = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={API_KEYS['hunter']}"
        response = requests.get(url)
        
        if response.status_code == 200:
            domain_info = response.json()
            print("\n--- Domain Analysis Results ---")
            print(f"Domain: {domain}")
            print(f"Organization: {domain_info['data']['organization']}")
            print(f"Emails Found: {len(domain_info['data']['emails'])}")
            for email_entry in domain_info['data']['emails']:
                print(f" - Email: {email_entry['value']}, Confidence: {email_entry['confidence']}")
        else:
            print(f"[!] Failed to analyze domain. Status code: {response.status_code}")
    except Exception as e:
        print(f"[!] Error analyzing domain: {e}")

# Run the program
if __name__ == "__main__":
    run()
