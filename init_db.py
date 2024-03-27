import sqlite3


connection = sqlite3.connect("database.db")


with open("schema.sql", "r+") as file:
    connection.executescript(file.read())


cur = connection.cursor()

cur.execute(
    "INSERT INTO posts (title, content) VALUES (?, ?)",
    ("Fist Post", "Content for the first post."),
)

cur.execute(
    "INSERT INTO posts (title, content) VALUES (?, ?)",
    ("Second post", "Content for the second post."),
)

# commit the changes to the database
connection.commit()
connection.close()
