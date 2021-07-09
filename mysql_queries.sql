#Select all rows from table
SELECT * FROM Proj.mytable;


#Select a row from table
SELECT * FROM Proj.mytable limit 1;


#select limited rows from table
SELECT * FROM ytable limit 9;


#Delete command
DELETE from mytable
where mea_id = 2515;
SELECT*FROM mytable;


#Update command
UPDATE mytable
SET category = "Rice Bowl" where meal_id=1109;
SELECT*FROM mytable;


#insert command
INSERT intomyable value (1109,"Snacks","Italian");
SELECT*FROM mytable;


#Drop a table
drop table mytable;
SELECT*FROM mytable;


#sort in an order
SELECT * FROM mytable;
ORDER BY cuisine DES