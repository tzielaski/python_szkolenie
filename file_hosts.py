from pprint import pprint

filename = r'hosts.txt'

try:
    with open(filename,'r') as file:
        content = file.readlines()

except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("No permission to read from the file.")

hosts_list = []
for line in content:
    if line.startswith('#'):
        continue
    elif line[0].isspace():
        continue
    else:
        line_elements = line.split()
        ip = line_elements[0]
        hosts_list.append({
            'hostnames': line_elements[1:],
            'ip': ip,
            'protocol': 'ipv4' if '.' in ip else 'ipv6'
        })

pprint(hosts_list)