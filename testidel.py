import pickle
try:
    with open('mydata.pickle', 'wb') as mysavedata:
        pickle.dump([1, 2, 'three'], mysavedata)
except pickle.PickleError as perr:
    print('Pickling error:' + str(perr))

with open('mydata.pickle', 'rb') as myrestoredata:
    a_list = pickle.load(myrestoredata)

print(a_list)
