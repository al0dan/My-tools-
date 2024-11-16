import dns.resolver

def enumerate_dns(domain):
    records = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA', 'PTR']
    print(f"Enumerating DNS records for: {domain}")
    for record in records:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"\n{record} Records:")
            for answer in answers:
                print(f"  {answer}")
        except dns.resolver.NoAnswer:
            print(f"No {record} record found.")
        except Exception as e:
            print(f"Error querying {record} record: {e}")

def fuzz_dns(domain):
    subdomains = ['www', 'mail', 'ftp', 'admin', 'test', 'api', 'dev']
    print(f"\nFuzzing subdomains for: {domain}")
    for sub in subdomains:
        subdomain = f"{sub}.{domain}"
        try:
            answers = dns.resolver.resolve(subdomain, 'A')
            print(f"Found: {subdomain}")
            for answer in answers:
                print(f"  IP: {answer}")
        except dns.resolver.NXDOMAIN:
            pass
        except Exception as e:
            print(f"Error querying {subdomain}: {e}")

# Example Usage
domain = input("Enter domain: ")
enumerate_dns(domain)
fuzz_dns(domain)
