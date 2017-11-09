#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2, sys


def connect(database_name):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print "Unable to connect to database"   
        sys.exit(1)
        # OR perhaps throw an error
        #raise e (If you choose to raise an exception, it will need to be caught by the whoever called this function)
    #return psycopg2.connect("dbname=tournament")


def execute(query):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    db, c = connect("tournament")   
    c.execute(query)
    db.commit()
    db.close()




def deleteMatches():
    """Remove all the match records from the database."""
    query = "delete from matches;"
    execute(query)


def deletePlayers():
    """Remove all the player records from the database."""
    query = "delete from players; delete from matches;"
    execute(query)

def countPlayers():
    """Returns the number of players currently registered."""
    db, c = connect("tournament")
    c.execute("select count(*) from players ;")
    results = c.fetchone()
    db.close()
    return results[0]
    
    


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db, c = connect("tournament")
    c.execute("insert into players (name) values (%s);",(name,))
    db.commit()
    db.close()
    

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
    db, c = connect("tournament")
    c.execute("select players.id, players.name, wins.wins, matchtotal.matches from players join wins on players.id=wins.id join matchtotal on players.id=matchtotal.id order by wins.wins desc;")
    results = c.fetchall()
    db.close()
    return results
    

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, c = connect("tournament")
    c.execute("insert into matches (winner,loser) values (%s,%s)",(winner,loser))
    db.commit()
    db.close()
 
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
 

