import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='12345',
    host='localhost',  # or wherever your DB is hosted
    port=5432
)

cur = conn.cursor()

# Insert an ability
cur.execute("""
    INSERT INTO abilities (name, description)
    VALUES (%s, %s)
    RETURNING id;
""", ('Piano', 'Learn how to play piano'))

# Get the new ability's ID
ability_id = cur.fetchone()[0]

# Insert subskills for that ability
subskills = [
    ('Chords', 'Practice major and minor chords'),
    ('Finger Dexterity', 'Hanon finger exercises'),
]

for name, description in subskills:
    cur.execute("""
        INSERT INTO subskills (ability_id, name, description)
        VALUES (%s, %s, %s);
    """, (ability_id, name, description))

# Commit the transaction and close
conn.commit()
cur.close()
conn.close()