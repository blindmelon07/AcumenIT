
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os


app = Flask(__name__)
# location ng database file
DATABASE = os.path.join(os.path.dirname(__file__), 'jokes.db')

# db connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)  # Buksan ang database connection
    conn.row_factory = sqlite3.Row   # Gawing dictionary ang mga resulta
    return conn

# Unang route (home page) - magre-redirect sa add joke page
@app.route('/')
def index():
    return redirect(url_for('add_joke'))  # Diretso sa add joke page

# Route para magdagdag ng joke
@app.route('/add-joke', methods=['GET', 'POST'])
def add_joke():
    if request.method == 'POST':
        joke_text = request.form['joke_text']  # Kunin ang joke mula sa form
        
        # Siguraduhing hindi blanko ang joke
        if not joke_text.strip():
            return render_template('add_joke.html', error="Joke cannot be empty!")
            
        try:
            conn = get_db_connection()
            # I-save ang joke sa database
            conn.execute('INSERT INTO jokes (joke_text) VALUES (?)', (joke_text,))
            conn.commit()  # I-save ang changes
            conn.close()
            return redirect(url_for('view_jokes'))  # Pumunta sa jokes list
        except sqlite3.Error as e:
            return render_template('add_joke.html', error=str(e))  # Magpakita ng error
    
    return render_template('add_joke.html')  # Ipakita ang add joke form

# Route para makita ang lahat ng jokes
@app.route('/jokes')
def view_jokes():
    conn = get_db_connection()
    jokes = conn.execute('SELECT id, joke_text FROM jokes').fetchall()  # Kunin lahat ng jokes
    conn.close()
    return render_template('jokes.html', jokes=jokes)  # Ipakita sa template

# Patakbuhin ang app
if __name__ == '__main__':
    app.run(debug=True)  # Simulan ang development server