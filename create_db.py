"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""

import sqlite3
from faker import Faker
import random
from datetime import datetime
conn = sqlite3.connect('social_network.db')
import os
import inspect

fake = Faker()

conn = sqlite3.connect('social_network.db')
c = conn.cursor()

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # : Create function body
    
    c.execute('''CREATE TABLE people
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             email TEXT,
             age INTEGER,
             created_at TEXT,
             updated_at TEXT)''')

    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # : Create function body
    
    # Generate and insert fake data
    n = []
    em = []
    ag = []
    cd = []
    ud = []

    for i in range(200):
        name = fake.name()
        n.append(name)
        email = fake.email()
        em.append(email)
        age = random.randint(1, 100)
        ag.append(age)
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cd.append(created_at)
        updated_at = created_at
        ud.append(updated_at)
        c.execute("INSERT INTO people (name, email, age, created_at, updated_at) VALUES (?, ?, ?, ?, ?)", (name, email, age, created_at, updated_at))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    return 

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()