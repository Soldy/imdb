import sqlite3
import base64

def create_title_akas():
    conn = sqlite3.connect()
    conn.execute('''CREATE TABLE title_akas (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            title_id TEXT,
            ordering INTEGER,
            title TEXT,
            region TEXT,
            language TEXT,
            original_title INTEGER
       );'''
    )
    conn.commit()
    conn.close()

def create_title_akas_types():
    conn = sqlite3.connect()
    conn.execute('''CREATE TABLE title_akas_type (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            title_id TEXT,
            type TEXT
       );'''
    )
    conn.commit()
    conn.close()

def create_title_akas_attributes():
    conn = sqlite3.connect()
    conn.execute('''CREATE TABLE title_akas_attributes (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            title_id TEXT,
            attribute TEXT
       );'''
    )
    conn.commit()
    conn.close()


def create_name_basics():
    conn = sqlite3.connect()
    conn.execute('''CREATE TABLE name_basics (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name_id TEXT,
            primary_name TEXT,
            birth_year INTEGER,
            death_year INTEGER
       );'''
    )
    conn.commit()
    conn.close()

def create_name_basics_profession():
    conn = sqlite3.connect()
    conn.execute('''CREATE TABLE name_basics_profession (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name_id TEXT,
            profession TEXT,
       );'''
    )
    conn.commit()
    conn.close()

def create_name_basics_title():
    conn = sqlite3.connect()
    conn.execute('''CREATE TABLE name_basics_title (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name_id TEXT,
            title TEXT,
       );'''
    )
    conn.commit()
    conn.close()
