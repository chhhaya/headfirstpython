def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[:3]

def get_coach_data(filename):
    try:
        with open(filename) as f:
            tmp = f.readline()
        data = tmp.strip().split(',')
        return AthleteList(data.pop(0), data.pop(0),  data)
        #return {'name':data.pop(0),
#                                    'dob':data.pop(0),
#                                    'time':str(sorted(set([sanitize(t) for t in data]))[:3])}
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None

sarah = get_coach_data('sarah2.txt')
julie = get_coach_data('julie2.txt')
print(sarah.name + "'s fastest times are:" + str(sarah.top3()))
print(julie.name + "'s fastest times are:" + str(julie.top3()))

vera = AthleteList('vera vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22', '1-21', '2:23'])
print(vera.top3())
