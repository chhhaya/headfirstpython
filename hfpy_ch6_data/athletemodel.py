import pickle
from athletelist import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as f:
            tmp = f.readline()
        data = tmp.strip().split(',')
        return AthleteList(data.pop(0), data.pop(0),  data)
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return None

def put_to_store(file_list):
    all_athletes = {}

    for e_file in file_list:
        ath = get_coach_data(e_file)
        all_athletes[ath.name] = ath

    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File Error(put_and_store):' + str(ioerr))

    return all_athletes



def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File Error(put_and_store):' + str(ioerr))

    return all_athletes
