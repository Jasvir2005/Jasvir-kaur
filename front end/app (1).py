from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('database (2).db')  # Replace with your database file path
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def search_proverb():
    translation = None
    if request.method == 'POST':
        punjabi_idiom = request.form['punjabi_idiom'].strip()  # Clean the input (strip extra spaces)
        print(f"User Input (cleaned): {punjabi_idiom}")  # Debug print
        
        # Query the database for the proverb (case-insensitive search)
        conn = get_db_connection()
        cursor = conn.cursor()
        query = 'SELECT * FROM proverbs WHERE LOWER(Punjabi_Idiom) LIKE ?'
        
        # Use parameterized query for safety
        cursor.execute(query, ('%' + punjabi_idiom.lower() + '%',))  # Convert to lowercase for case-insensitive search
        
        # Fetch all matching proverbs
        proverbs = cursor.fetchall()
        print(f"Found {len(proverbs)} matching proverbs.")  # Debug print
        
        conn.close()
        
        # If we have a matching proverb, return the first one
        if proverbs:
            proverb = proverbs[0]  # Just return the first match
            translation = {
                'meaning': proverb['English_meaning'],  # Assuming these fields exist
                'english_equivalent': proverb['Equivalent_English_Idiom']
            }
        else:
            translation = {
                'meaning': 'No translation found.',
                'english_equivalent': 'No equivalent found.'
            }
    
    return render_template('punjabverse.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)
