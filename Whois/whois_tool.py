import whois

try:
    light_green = "\033[1;32m"
    domain = str(input("Enter your domain name : "))
    w = whois.whois(domain)
    print()
    print(light_green, end="")
    print(w)
except:
    print("ENVALID DOMAIN!")
