"""This file sets up the database"""
import psycopg2

conn = psycopg2.connect("dbname=stack user=postgres")

cur = conn.cursor()

#create users table
cur.execute("CREATE TABLE users(user_id SERIAL PRIMARY KEY,email text,name text,password text);")

#create questions table
cur.execute("CREATE TABLE questions(question_id SERIAL PRIMARY KEY," + 
"user_id int REFERENCES users(user_id), title text, created_at date);")

#create the answers table.
cur.execute("CREATE TABLE answers(answer_id SERIAL PRIMARY KEY, " + 
"question_id int REFERENCES questions(question_id), user_id int " + 
"REFERENCES users(user_id), title text, created_at date );")

conn.commit()
conn.close

