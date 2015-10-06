CREATE TABLE home_status (
	id	bigint NOT NULL,
	text	varchar(150) NOT NULL,
	author_id	bigint NOT NULL,
	retweet_count	integer,
	geo	varchar,
	created_at datetime,
	place	varchar
	in_reply_to_status_id varchar,
	in_reply_to_user_id varchar,
);

CREATE TABLE home_author (
	id	bigint NOT NULL,
	verified	boolean,
	followers_count integer,
	protected	boolean,
	location varchar, 
	statuses_count integer, 
	description varchar,
	friends_count integer, 
	geo_enabled boolean, 
	screen_name varchar, 
	lang varchar, 
	favourites_count integer, 
	name varchar, 
	created_at timestamp, 
	time_zone varchar, 
	listed_count integer
);
