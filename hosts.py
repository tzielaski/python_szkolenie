from pprint import pprint

hosts = dict()


def is_dirty(line):
    return line.isspace() or line.startswith('#')


def is_clean(line):
    return not is_dirty(line)


with open('hosts.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        if is_clean(line):
            ip, *host_names = line.split()
            existing_host = hosts.get(ip)
            if not existing_host:
                hosts[ip] = host_names
            else:
                hosts[ip].append(host_names)

pprint(hosts)
