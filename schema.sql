
drop table if exists transactions
create table transactions (
    id integer primary key autoincrement,
    txn_id integer not null,
    type text not null,
    user text not null,
    comment text not null,
    paths text not null
);
