import sqlite3

db_name = 'coachdata.sqlite'

def get_namesID_from_store():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    results = cursor.execute("""SELECT name,id FROM athletes""")
    #response = [row[0] for row in cursor.fetchall()]
    response = results.fetchall()
    conn.close()
    return response

def get_athlete_from_id(athlete_id):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    results = cur.execute("SELECT name, dob FROM athletes WHERE id=?", (athlete_id,))
    (name, dob) = results.fetchone()

    results = cur.execute("SELECT value FROM timing_data WHERE athlete_id = ?", (athlete_id, ))
    data = [row[0] for row in results.fetchall()]

    response = { 'Name': name,
                 'Dob': dob,
                 'data': data,
                 'top3': data[:3]}
    conn.close()
    return response

print(get_namesID_from_store())