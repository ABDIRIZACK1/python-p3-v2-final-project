import sqlite3

def connect():
    return sqlite3.connect('sports_management.db')

def create_tables():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            city TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            team_id INTEGER,
            position TEXT,
            FOREIGN KEY (team_id) REFERENCES teams (id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team1_id INTEGER,
            team2_id INTEGER,
            date TEXT,
            score TEXT,
            FOREIGN KEY (team1_id) REFERENCES teams (id),
            FOREIGN KEY (team2_id) REFERENCES teams (id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transfers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER,
            from_team_id INTEGER,
            to_team_id INTEGER,
            date TEXT,
            fee REAL,
            FOREIGN KEY (player_id) REFERENCES players (id),
            FOREIGN KEY (from_team_id) REFERENCES teams (id),
            FOREIGN KEY (to_team_id) REFERENCES teams (id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS loans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_id INTEGER,
            from_team_id INTEGER,
            to_team_id INTEGER,
            start_date TEXT,
            end_date TEXT,
            FOREIGN KEY (player_id) REFERENCES players (id),
            FOREIGN KEY (from_team_id) REFERENCES teams (id),
            FOREIGN KEY (to_team_id) REFERENCES teams (id)
        )
    ''')
    conn.commit()
    conn.close()

def add_team(name, city):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO teams (name, city) VALUES (?, ?)', (name, city))
    conn.commit()
    conn.close()

def get_teams():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM teams')
    teams = cursor.fetchall()
    conn.close()
    return teams

def add_player(name, team_id, position):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO players (name, team_id, position) VALUES (?, ?, ?)', (name, team_id, position))
    conn.commit()
    conn.close()

def get_players():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM players')
    players = cursor.fetchall()
    conn.close()
    return players

def add_match(team1_id, team2_id, date, score):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO matches (team1_id, team2_id, date, score) VALUES (?, ?, ?, ?)', (team1_id, team2_id, date, score))
    conn.commit()
    conn.close()

def get_matches():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM matches')
    matches = cursor.fetchall()
    conn.close()
    return matches

def add_transfer(player_id, from_team_id, to_team_id, date, fee):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO transfers (player_id, from_team_id, to_team_id, date, fee) VALUES (?, ?, ?, ?, ?)', (player_id, from_team_id, to_team_id, date, fee))
    conn.commit()
    conn.close()

def get_transfers():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transfers')
    transfers = cursor.fetchall()
    conn.close()
    return transfers

def add_loan(player_id, from_team_id, to_team_id, start_date, end_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO loans (player_id, from_team_id, to_team_id, start_date, end_date) VALUES (?, ?, ?, ?, ?)', (player_id, from_team_id, to_team_id, start_date, end_date))
    conn.commit()
    conn.close()

def get_loans():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM loans')
    loans = cursor.fetchall()
    conn.close()
    return loans
