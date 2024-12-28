import os
import sys
from modules import (
    social_recon,
    domain_recon,
    email_recon,
    phone_recon,
    ip_recon,
    web_crawler,
)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_menu():
    print("""
    ======================================
                OSINT Framework
    ======================================
    1. Social Media Reconnaissance
    2. Domain Reconnaissance
    3. Email Reconnaissance
    4. Phone Number Reconnaissance
    5. IP Address Reconnaissance
    6. Web Crawler
    0. Exit
    ======================================
    """)

def main():
    while True:
        clear_screen()
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            social_recon.run()
        elif choice == "2":
            domain_recon.run()
        elif choice == "3":
            email_recon.run()
        elif choice == "4":
            phone_recon.run()
        elif choice == "5":
            ip_recon.run()
        elif choice == "6":
            web_crawler.run()
        elif choice == "0":
            print("Exiting the OSINT Framework. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice! Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
