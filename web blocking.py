import os

def block_website(website_name):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    website_url = website_name
    website_ip = "127.0.0.1"

    # Check if website is already blocked
    with open(hosts_path, 'r') as file:
        content = file.readlines()
        for line in content:
            if website_url in line:
                print("Website is already blocked.")
                return

    # Block website
    with open(hosts_path, 'a') as file:
        file.write(f"{website_ip} {website_url}\n")
    print(f"{website_name} has been blocked.")

def unblock_website(website_name):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    website_url = website_name
    website_ip = "127.0.0.1"
    updated_content = []

    # Check if website is already unblocked
    with open(hosts_path, 'r') as file:
        content = file.readlines()
        website_blocked = False
        for line in content:
            if website_url in line:
                website_blocked = True
            else:
                updated_content.append(line)
        if not website_blocked:
            print("Website is already unblocked.")
            return

    # Unblock website
    with open(hosts_path, 'w') as file:
        for line in updated_content:
            file.write(line)
    print(f"{website_name} has been unblocked.")

def main():
    choice = None
    while choice != "q":
        print("Enter 'b' to block a website.")
        print("Enter 'u' to unblock a website.")
        print("Enter 'q' to quit.")
        choice = input("Enter your choice: ")
        if choice == 'b':
            website_name = input("Enter website name (e.g. www.example.com): ")
            block_website(website_name)
        elif choice == 'u':
            website_name = input("Enter website name (e.g. www.example.com): ")
            unblock_website(website_name)

if __name__ == "__main__":
    main()
