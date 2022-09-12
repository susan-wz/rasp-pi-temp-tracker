import re

with open('/proc/cpuinfo', 'r') as infile:
        cpuinfo = infile.read()

match = re.search('^Hardware\s+:\s+(\w+)$', cpuinfo, flags=re.MULTILINE | re.IGNORECASE)
print(match.group(1))
