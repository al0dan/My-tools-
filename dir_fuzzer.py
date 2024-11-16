import requests

def fuzz_directories(base_url, wordlist, depth=1):
    def recursive_fuzz(url, current_depth):
        if current_depth > depth:
            return
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"Found: {url} ({response.status_code})")
                for word in wordlist:
                    recursive_fuzz(f"{url}/{word}", current_depth + 1)
        except Exception as e:
            print(f"Error accessing {url}: {e}")

    for word in wordlist:
        recursive_fuzz(f"{base_url}/{word}", 1)

# Example Usage
base_url = input("Enter base URL (e.g., https://example.com): ")
wordlist = ['admin', 'test', 'login', 'backup', 'dev']  # Replace with your own wordlist
fuzz_directories(base_url, wordlist, depth=2)
