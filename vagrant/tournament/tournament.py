#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("update players set wins = 0, matches = 0;")
    c.execute("delete from matches;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("delete from players;")
    c.execute("delete from matches;")
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("select count(*) from players ;")
    count = c.fetchone()
    return count[0]
    conn.commit()
    conn.close()
    


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    c.execute("insert into players (name) values (%s);",(name,))
    #c.execute("insert into matches (id,wins,matches) values ((select id from players where name = (%s)),0,0)",(name,))
    conn.commit()
    conn.close()
    

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    c.execute("select id, name, wins, matches from players order by wins;")
    standings = c.fetchall()
    return standings
    conn.close()

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    c.execute("insert into matches (winner,loser) values (%s,%s)",(winner,loser))
    c.execute("update players set matches = matches +1, wins = wins + 1 where id = (%s);", (winner,))
    c.execute("update players set matches = matches +1 where id = (%s);", (loser,))
    conn.commit()
    conn.close() 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    info = list()
    for (a,b,c,d) in standings:
        info.append((a,b))
    pairings = list()
    pairn = len(info)
    n = 0
    while n < pairn:
        pairings.append(info[n]+info[n+1])
        n = n + 2
    return pairings
    #[(pid1, pname1),(pid2, pname2), (pid3, pname3),(pid4, pname4), (pid5, pname5),(pid6, pname6), (pid7, pname7),(pid8, pname8)] = info
    #return [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4), (pid5, pname5, pid6, pname6), (pid7, pname7, pid8, pname8)] 
 

