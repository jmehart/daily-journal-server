import sqlite3
import json
from models import Entries, Moods



def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id,
            m.label mood_label
        FROM Entries e
        JOIN Moods m
            ON m.id = e.mood_id
        """)

        # Initialize an empty list to hold all animal representations
        journal_entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            journal_entry = Entries(row['id'], row['concept'], row['entry'], row['date'],
                            row['mood_id'])

            # Create a Location instance from the current row
            mood = Moods(row['id'], row['mood_label'])

            # Add the dictionary representation of the location to the animal
            journal_entry.mood = mood.__dict__

            # Add the dictionary representation of the animal to the list
            journal_entries.append(journal_entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(journal_entries)


# Function with a single parameter
def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id,
            m.label mood_label
        FROM Entries e
        JOIN Moods m
            ON m.id = e.mood_id
        WHERE e.id = ?    
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        journal_entry = Entries(data['id'], data['concept'], data['entry'], data['date'],
                            data['mood_id'])
        
        mood = Moods(data['id'], data['mood_label'])

        journal_entry.mood = mood.__dict__

    # Use `json` package to properly serialize list as JSON
    return json.dumps(journal_entry.__dict__)
    
    
    
def delete_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM ENTRIES
        WHERE id = ?
        """, (id, ))    
        
        

def search_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id,
            m.label mood_label
        FROM Entries e
        JOIN Moods m
            ON m.id = e.mood_id
        WHERE entry LIKE '%?%'    
        """)

        # Initialize an empty list to hold all animal representations
        journal_entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            journal_entry = Entries(row['id'], row['concept'], row['entry'], row['date'],
                            row['mood_id'])

            # Create a Location instance from the current row
            mood = Moods(row['id'], row['mood_label'])

            # Add the dictionary representation of the location to the animal
            journal_entry.mood = mood.__dict__

            # Add the dictionary representation of the animal to the list
            journal_entries.append(journal_entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(journal_entries)  



def create_journal_entry(new_entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Entries
            ( concept, entry, date, mood_id )
        VALUES
            ( ?, ?, ?, ? );
        """, (new_entry['concept'], new_entry['entry'],
              new_entry['date'], new_entry['moodId'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id


    return json.dumps(new_entry)       



def update_entry(id, new_entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Entries
            SET
                concept = ?,
                entry = ?,
                date = ?,
                mood_id = ?
        WHERE id = ?
        """, (new_entry['concept'], new_entry['entry'],
              new_entry['date'], new_entry['moodId'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True 