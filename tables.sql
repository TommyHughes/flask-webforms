create table posts (
	id integer primary key autoincrement,
	author text not null,
	submit_date date not null,
	post text not null
)