import requests
import json

# Global API keys (replace with real ones)
API_KEYS = {
    "ipinfo": "your_ipinfo_api_key",  # Replace with your ipinfo.io API key
    "shodan": "your_shodan_api_key",  # Replace with your Shodan API key
}

def run():
    print("\n[IP Address Reconnaissance]")
    ip = input("Enter the IP address to search: ")
    print(f"\n[Gathering information about IP: {ip}]\n")
    
    # Perform IP reconnaissance tasks
    get_ip_info(ip)
    check_ip_reputation(ip)
    analyze_ip_with_shodan(ip)
    
    input("\nPress Enter to return to the menu...")

# 1. Get IP Information (Basic Details and Geolocation)
def get_ip_info(ip):
    print("[+] Fetching IP Information...")
    try:
        url = f"https://ipinfo.io/{ip}?token={API_KEYS['ipinfo']}"
        response = requests.get(url)
        
        if response.status_code == 200:
            ip_data = response.json()
            print("\n--- IP Information ---")
            print(f"IP: {ip_data.get('ip', 'N/A')}")
            print(f"City: {ip_data.get('city', 'N/A')}")
            print(f"Region: {ip_data.get('region', 'N/A')}")
            print(f"Country: {ip_data.get('country', 'N/A')}")
            print(f"Organization: {ip_data.get('org', 'N/A')}")
            print(f"Location: {ip_data.get('loc', 'N/A')}")
        else:
            print(f"[!] Failed to fetch IP information. Status code: {response.status_code}")
    except Exception as e:
        print(f"[!] Error fetching IP information: {e}")

# 2. Check IP Reputation (Threat Analysis)
def check_ip_reputation(ip):
    print("\n[+] Checking IP Reputation...")
    try:
        # Example free API for IP reputation (replace with an actual service)
        url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}"
        headers = {
            "Key": "your_abuseipdb_api_key",  # Replace with AbuseIPDB API key
            "Accept": "application/json",
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            reputation_data = response.json()
            print("\n--- IP Reputation Results ---")
            print(f"Abuse Confidence Score: {reputation_data['data']['abuseConfidenceScore']}")
            print(f"Total Reports: {reputation_data['data']['totalReports']}")
        else:
            print(f"[!] Failed to fetch IP reputation. Status code: {response.status_code}")
    except Exception as e:
        print(f"[!] Error checking IP reputation: {e}")

# 3. Analyze IP with Shodan (Port Scanning and Services)
def analyze_ip_with_shodan(ip):
    print("\n[+] Analyzing IP with Shodan...")
    try:
        url = f"https://api.shodan.io/shodan/host/{ip}?key={API_KEYS['shodan']}"
        response = requests.get(url)
        
        if response.status_code == 200:
            shodan_data = response.json()
            print("\n--- Shodan Analysis ---")
            print(f"IP: {shodan_data.get('ip_str', 'N/A')}")
            print(f"Organization: {shodan_data.get('org', 'N/A')}")
            print(f"ISP: {shodan_data.get('isp', 'N/A')}")
            print("Open Ports:")
            for port in shodan_data.get('ports', []):
                print(f" - {port}")
        else:
            print(f"[!] Failed to analyze IP with Shodan. Status code: {response.status_code}")
    except Exception as e:
        print(f"[!] Error analyzing IP with Shodan: {e}")

# Run the program
if __name__ == "__main__":
    run()
