import requests

# Global API keys (replace with real ones)
API_KEYS = {
    "numverify": "your_numverify_api_key",  # Replace with your NumVerify API key
    "opencage": "your_opencage_api_key",   # Replace with your OpenCage Geocoder API key
}

def run():
    print("\n[Phone Number Reconnaissance]")
    phone = input("Enter the phone number (with country code): ")
    print(f"\n[Gathering information about phone number: {phone}]\n")
    
    # Perform phone number reconnaissance tasks
    validate_phone_number(phone)
    geolocate_phone_number(phone)
    
    input("\nPress Enter to return to the menu...")

# 1. Validate Phone Number using NumVerify API
def validate_phone_number(phone):
    print("[+] Validating Phone Number...")
    try:
        url = f"http://apilayer.net/api/validate?access_key={API_KEYS['numverify']}&number={phone}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data['valid']:
                print("\n--- Phone Number Details ---")
                print(f"Number: {data.get('number', 'N/A')}")
                print(f"Country: {data.get('country_name', 'N/A')} ({data.get('country_code', 'N/A')})")
                print(f"Location: {data.get('location', 'N/A')}")
                print(f"Carrier: {data.get('carrier', 'N/A')}")
                print(f"Line Type: {data.get('line_type', 'N/A')}")
            else:
                print("[!] Invalid phone number.")
        else:
            print(f"[!] Failed to validate phone number. Status code: {response.status_code}")
    except Exception as e:
        print(f"[!] Error validating phone number: {e}")

# 2. Geolocate Phone Number using OpenCage API
def geolocate_phone_number(phone):
    print("\n[+] Geolocating Phone Number...")
    try:
        # Extract location information from NumVerify (if available)
        numverify_url = f"http://apilayer.net/api/validate?access_key={API_KEYS['numverify']}&number={phone}"
        response = requests.get(numverify_url)
        if response.status_code == 200:
            numverify_data = response.json()
            location = numverify_data.get('location')
            country = numverify_data.get('country_name')

            # Use OpenCage Geocoder to get precise coordinates
            if location and country:
                opencage_url = f"https://api.opencagedata.com/geocode/v1/json?q={location},{country}&key={API_KEYS['opencage']}"
                geocode_response = requests.get(opencage_url)
                if geocode_response.status_code == 200:
                    geocode_data = geocode_response.json()
                    if geocode_data['results']:
                        coords = geocode_data['results'][0]['geometry']
                        print(f"Latitude: {coords['lat']}, Longitude: {coords['lng']}")
                    else:
                        print("[!] Could not geolocate the phone number.")
                else:
                    print(f"[!] Failed to fetch geolocation. Status code: {geocode_response.status_code}")
            else:
                print("[!] Location data not available for geolocation.")
        else:
            print("[!] Failed to validate phone number for geolocation.")
    except Exception as e:
        print(f"[!] Error geolocating phone number: {e}")

# Run the program
if __name__ == "__main__":
    run()
