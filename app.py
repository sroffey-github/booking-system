from flask import Flask, render_template, request, flash
import sqlite3, uuid, datetime

DB_PATH = 'info.db'

app = Flask(__name__)

times = []
for hour in range(12, 23): # change min and max to change open times
    for minute in range(0, 60, 15):
        times.append('{:02d}:{:02d}'.format(hour, minute))

def init():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Bookings(id INTEGER PRIMARY KEY, name TEXT, email TEXT, mobile TEXT, guests, TEXT, date TEXT, time TEXT)')
    conn.commit()
    c.close()
    conn.close()

def getTimes(date):
    temp = times # copy of times

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('SELECT time FROM Bookings WHERE date = ?', (date, ))

    results = c.fetchall()
    if results:
        for i in results:
            temp.remove(i)
        return temp
    else:
        return times

def book(name, email, mobile, guests, date, time):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('INSERT INTO Bookings(name, email, mobile, guests, date, time) VALUES(?, ?, ?, ?, ?, ?)', (name, email, mobile, guests, date, time))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['submit_btn'] == "Check Times":
            name = request.form['name']
            email = request.form['email']
            mobile = request.form['mobile']
            guests = request.form.get('guestDropdown')
            date = str(datetime.datetime.strptime(request.form['date'], '%Y-%m-%d'))

            return render_template('index.html', times=getTimes(date))

        if request.form['submit_btn'] == "Book Table":
            name = request.form['name']
            email = request.form['email']
            mobile = request.form['mobile']
            guests = str(request.form.get('guestDropdown'))
            date = str(datetime.datetime.strptime(request.form['date'], '%Y-%m-%d'))
            time = str(request.form.get('timeDropdown'))
            if book(name, email, mobile, guests, date, time):
                flash('Booking Saved!')
                return render_template('index.html')
            else:
                flash('Invalid Booking Information!')
                return render_template('index.html')

    else:
        return render_template('index.html')

if __name__ == '__main__':
    init()
    app.run(debug=True)