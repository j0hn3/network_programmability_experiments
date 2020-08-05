import ipaddress
import sys 
import read_write_as_json

if __name__ == "__main__":
    address_scheme = read_write_as_json.open_address_scheme(input("Enter the file name of the address scheme to open or leave blank for ip_address_scheme.json: ") or "ip_address_scheme.json")
    print(type(address_scheme))
    print(address_scheme)
    