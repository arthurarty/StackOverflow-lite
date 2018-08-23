"""the User class reupresents a user of the system."""
import psycopg2
conn = psycopg2.connect("dbname=stack user=postgres")

class User:

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
        self.id = 0

    def add_user_to_db(self):
        cur = conn.cursor()
        cur.execute("INSERT INTO users (email, name, password)" + 
        "VALUES (%s, %s, %s)",(self.email, self.name, self.password))
        conn.commit()
        cur.execute("SELECT * FROM users WHERE email = %s", (self.email,))
        return cur.fetchone()

conn.close       

#new_user = User("foryou@tru.com", "metune", "me2g")
#print(new_user.add_user_to_db())