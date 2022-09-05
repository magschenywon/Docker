select count(*), db1.mytable.state, db3.mytable.state
from db1.mytable,db3.mytable
where db1.mytable.ID = db3.mytable.ID
group by db1.mytable.state, db3.mytable.state;

select count(*), db1.mytable.state, db2.mytable.state
from db1.mytable,db2.mytable
where db1.mytable.ID = db2.mytable.ID 
group by db1.mytable.state, db2.mytable.state;


select count(*), db3.mytable.state, db4.mytable.state
from db3.mytable,db4.mytable
where db3.mytable.ID = db4.mytable.ID 
group by db3.mytable.state, db4.mytable.state;

select count(*), db5.mytable.state, db6.mytable.state
from db5.mytable,db6.mytable
where db5.mytable.ID = db6.mytable.ID 
group by db5.mytable.state, db6.mytable.state;

select count(*), db7.mytable.state, db8.mytable.state
from db7.mytable,db8.mytable
where db7.mytable.ID = db8.mytable.ID 
group by db7.mytable.state, db8.mytable.state;

select count(*), db2.mytable.state, db4.mytable.state
from db2.mytable,db4.mytable
where db2.mytable.ID = db4.mytable.ID
group by db2.mytable.state, db4.mytable.state;

select count(*), db6.mytable.state, db8.mytable.state
from db6.mytable,db8.mytable
where db6.mytable.ID = db8.mytable.ID
group by db6.mytable.state, db8.mytable.state;


