from netscan.ping import ping_host

if __name__ == "__main__":
    host = input("Enter IP 🌐 or domain 🌍 to ping: ")
    result = ping_host(host)
    print(result)
    
    