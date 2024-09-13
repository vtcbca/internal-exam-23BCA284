# Create table cricketer(cid, cname, match, run) and insert 8 players records. Print player records with average. and write this data into player.csv file. Do all this task from python.
import sqlite3 as sq
con=sq.connect("D:/23BCA284/sqlite3/database/cricket.db")
c=con.cursor()
# create the cricketer table¶
c.execute("create table if not exists  cricketer(cid,cname,match,run)")
# Insert player records into the table
players = [
    (1, 'Player1', 10, 150),
    (2, 'Player2', 12, 180),
    (3, 'Player3', 8, 200),
    (4, 'Player4', 15, 130),
    (5, 'Player5', 11, 170),
    (6, 'Player6', 9, 160),
    (7, 'Player7', 14, 140),
    (8, 'Player8', 13, 190)
]
c.executemany('INSERT INTO cricketer (cid, cname, match, run) VALUES (?, ?, ?, ?)', players)
con.commit()
# fetch player data with average runs per match
c.execute("select cname, match, run, (run * 1.0 / match) as average from cricketer")
rec=c.fetchall()
print(rec)
# writing csv file
import csv
players = [
    ('cid','cname','match','run','average'),
    (1, 'Player1', 10, 150,15.0),
    (2, 'Player2', 12, 180,15.0),
    (3, 'Player3', 8, 200,25.0),
    (4, 'Player4', 15, 130,8.666),
    (5, 'Player5', 11, 170,15.45),
    (6, 'Player6', 9, 160,17.77),
    (7, 'Player7', 14, 140,10.0),
    (8, 'Player8', 13, 190, 14.615)]
# write
with open('D:/23BCA284/sqlite3/csv/player.csv','w') as f:
    w=csv.writer(f)
    w.writerows(players)  
# read
with open('D:/23BCA284/sqlite3/csv/player.csv','r') as f:
    r=csv.reader(f)
    for row in r:
        print(row)
