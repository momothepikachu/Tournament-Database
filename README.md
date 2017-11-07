# Tournament-Database
    Project Overview
In this project, I'll be writing a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

I will develop a database schema to store the game matches between players. Use Python module to rank the players and pair them up in matches in a tournament.

    Why This Project?
Modern data-driven applications require developers that know how to store data and interact programmatically with that data. In this project, you’ll design a database based off of a provided specification and use case and then write code that makes use of that data.

    Using the Vagrant Virtual Machine
The Vagrant folder has PostgreSQL installed and configured, as well as the psql command line interface (CLI) , so that you don't have to install or configure them on your local machine.

    Purposes of Each File(in vagrant/tournament)
--tournament.sql - this file is used to set up your database schema (the table
representation of your data structure).

--tournament.py - this file is used to provide access to your database via a library of
functions which can add, delete or query data in your database to another python
program (a client program). Remember that when you define a function, it does not
execute, it simply means the function is defined to run a specific set of instructions when
called.

--tournament_test.py - this is a client program which will use your functions written in
the tournament.py module. We've written this client program to test your implementation
of functions in tournament.py
