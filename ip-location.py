#!/usr/bin/env python3
import re
import ipaddress
import socket
from ip2geotools.databases.noncommercial import DbIpCity

def is_ip(ip):
    try:
        # Versuche, die IP-Adresse zu parsen
        ip_obj = ipaddress.ip_address(ip)
        return True
    except ValueError:
        # Wenn es nicht möglich ist, die IP-Adresse zu parsen, ist sie ungültig
        return False

def get_domain_name(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except socket.herror:
        return ""

def main():
  userinput = input("Insert a Domain or IP: ")

  ip = ""
  domain = ""

  if is_ip(userinput):
    ip = userinput
    domain = get_domain_name(ip)
  else:
    ip = socket.gethostbyname(userinput)
    domain = f"{userinput} | {get_domain_name(ip)}"

  response = DbIpCity.get(ip, api_key="free")

  print(f"\nDomain: {domain} ({ip})")
  print(f"City: {response.city}")
  print(f"Region: {response.region}")
  print(f"Country: {response.country}")

if __name__ == "__main__":
    main()
