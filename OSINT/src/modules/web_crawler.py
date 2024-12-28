import requests
from bs4 import BeautifulSoup

def run():
    print("\n[Web Crawler]")
    url = input("Enter the website URL to crawl: ")
    try:
        # Fetch the website
        response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract and print the page title
            print(f"\nTitle: {soup.title.string if soup.title else 'N/A'}")

            # Extract meta tags
            print("\nMeta Tags:")
            meta_tags = soup.find_all('meta')
            for meta in meta_tags:
                if meta.get('name') or meta.get('property'):
                    print(f"- {meta.get('name') or meta.get('property')}: {meta.get('content')}")

            # Extract and validate all links
            print("\nLinks found on the page:")
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                if href.startswith("http"):
                    link_status = validate_link(href)
                    print(f"{href} - {link_status}")
                else:
                    print(f"{href} - Skipped (not a full URL)")
        else:
            print(f"Failed to fetch the website. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    input("Press Enter to return to the menu...")

def validate_link(link):
    """Validate the link by checking its HTTP status."""
    try:
        response = requests.head(link, timeout=5)
        if response.status_code < 400:
            return "Accessible"
        else:
            return f"Error (status code: {response.status_code})"
    except requests.RequestException:
        return "Invalid or Unreachable"

# Run the program
if __name__ == "__main__":
    run()
