import requests
import whois
import json

# Global API keys (replace with real ones)
API_KEYS = {
    "shodan": "your_shodan_api_key",  # Replace with your Shodan API key
}

def run():
    print("\n[Domain Reconnaissance]")
    domain = input("Enter the domain to search: ")
    print(f"\n[Gathering data for domain: {domain}]\n")
    
    # Perform domain reconnaissance
    perform_whois_lookup(domain)
    perform_shodan_search(domain)
    
    input("\nPress Enter to return to the menu...")

# 1. Perform WHOIS Lookup
def perform_whois_lookup(domain):
    print("[+] Performing WHOIS Lookup...")
    try:
        domain_info = whois.whois(domain)
        print("\n--- WHOIS Data ---")
        for key, value in domain_info.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"[!] Error performing WHOIS lookup: {e}")

# 2. Perform Shodan Search
def perform_shodan_search(domain):
    print("\n[+] Performing Shodan Search...")
    try:
        url = f"https://api.shodan.io/dns/resolve?hostnames={domain}&key={API_KEYS['shodan']}"
        response = requests.get(url)
        if response.status_code == 200:
            ip_data = response.json()
            domain_ip = ip_data.get(domain, None)
            
            if domain_ip:
                print(f"[*] Resolved IP Address: {domain_ip}")
                # Fetch Shodan information for the IP
                fetch_shodan_ip_info(domain_ip)
            else:
                print("[!] Could not resolve IP address for the domain.")
        else:
            print(f"[!] Shodan API request failed. Status code: {response.status_code}")
    except Exception as e:
        print(f"[!] Error performing Shodan search: {e}")

# 3. Fetch Shodan IP Information
def fetch_shodan_ip_info(ip_address):
    print("\n[+] Fetching Shodan Data for IP...")
    try:
        url = f"https://api.shodan.io/shodan/host/{ip_address}?key={API_KEYS['shodan']}"
        response = requests.get(url)
        if response.status_code == 200:
            shodan_data = response.json()
            print("\n--- Shodan Data ---")
            print(f"IP: {shodan_data.get('ip_str', 'N/A')}")
            print(f"Organization: {shodan_data.get('org', 'N/A')}")
            print(f"ISP: {shodan_data.get('isp', 'N/A')}")
            print(f"Country: {shodan_data.get('country_name', 'N/A')}")
            print("\nOpen Ports and Services:")
            for port in shodan_data.get('ports', []):
                print(f"  - Port {port}")
        else:
            print(f"[!] Failed to fetch Shodan data. Status code: {response.status_code}")
    except Exception as e:
        print(f"[!] Error fetching Shodan IP information: {e}")

# Run the program
if __name__ == "__main__":
    run()
