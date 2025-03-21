
import os
import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)
DATABASE = os.path.join(os.path.dirname(__file__), 'jokes.db')

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row   
    return conn

# API endpoint to get all jokes
@app.route('/jokes', methods=['GET'])
def get_all_jokes():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, joke_text FROM jokes')
        jokes = cursor.fetchall()
        conn.close()
        
        if not jokes:
            return "<h1>No jokes found in database</h1>", 404
            
        return render_template('joke.html', jokes=jokes)
        
    except sqlite3.Error as e:
        return f"<h2>Database Error:</h2><p>{e}</p>", 500
# Start the Flask development server
if __name__ == '__main__':
    app.run(debug=True)