-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

drop table if exists matches cascade;
Create table matches (id serial, winner integer references players (id), loser integer references players(id));

drop table if exists players cascade;
create table players (id serial primary key, name text, wins integer default 0, matches integer default 0);


