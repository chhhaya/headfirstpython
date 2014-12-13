def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

with open('james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')

clean_james = [float(sanitize(t)) for t in james]
clean_julie = [float(sanitize(t)) for t in julie]
clean_mikey = [float(sanitize(t)) for t in mikey]
clean_sarah = [float(sanitize(t)) for t in sarah]

print(sorted(set(clean_james))[:3])
print(sorted(set(clean_julie))[:3])
print(sorted(set(clean_mikey))[:3])
print(sorted(set(clean_sarah))[:3])
