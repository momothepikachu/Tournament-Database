-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
drop database if exists tournament;
create database tournament;
\c tournament

create table players (id serial primary key, name text);
Create table matches (id serial primary key, winner integer references players (id), loser integer references players(id));

create view wins as 
	select players.id, count(matches.winner) as wins 
	from players left join matches
	on players.id = matches.winner
	group by players.id
	order by wins desc;

create view matchtotal as
	select players.id, count(matches.*) as matches
	from players left join matches
	on players.id = matches.winner or players.id = matches.loser
	group by players.id
	order by matches desc;


