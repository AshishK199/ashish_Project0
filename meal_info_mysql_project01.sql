#meal_information project in mysql

#using the database which have created
use my_db;
#creating a table in to a databse
 CREATE TABLE  meal_information (
    meal_id INT,
    category VARCHAR(12), 
    cuisine VARCHAR(11)); 
    #inserting the information or data into table
  INSERT INTO meal_information VALUES
    (1885,'Beverages','Thai'),
    (1993,'Beverages','Thai'),
    (2539,'Beverages','Thai'),
    (1248,'Beverages','Indian'),
    (2631,'Beverages','Indian'),
    (1311,'Extras','Thai'),
    (1062,'Beverages','Italian'),
    (1778,'Beverages','Italian'),
    (1803,'Extras','Thai'),
    (1198,'Extras','Thai'),
    (2707,'Beverages','Italian'),
    (1847,'Soup','Thai'),
    (1438,'Soup','Thai'),
    (2494,'Soup','Thai'),
    (2760,'Other Snacks','Thai'),
    (2490,'Salad','Italian'),
    (1109,'Rice Bowl','Indian'),
    (2290,'Rice Bowl','Indian'),
    (1525,'Other Snacks','Thai'),
    (2704,'Other Snacks','Thai'),
    (1878,'Starters','Thai'),
    (2640,'Starters','Thai'),
    (2577,'Starters','Thai'),
    (1754,'Sandwich','Italian'),
    (1971,'Sandwich','Italian'),
    (2306,'Pasta','Italian'),
    (2139,'Beverages','Indian'),
    (2826,'Sandwich','Italian'),
    (2664,'Salad','Italian'),
    (2569,'Salad','Italian'),
    (1230,'Beverages','Continental'),
    (1207,'Beverages','Continental'),
    (2322,'Beverages','Continental'),
    (2492,'Desert','Indian'),
    (1216,'Pasta','Italian'),
    (1727,'Rice Bowl','Indian'),
    (1902,'Biryani','Indian'),
    (1247,'Biryani','Indian'),
    (2304,'Desert','Indian'),
    (1543,'Desert','Indian'),
    (1770,'Biryani','Indian'),
    (2126,'Pasta','Italian'),
    (1558,'Pizza','Continental'),
    (2581,'Pizza','Continental'),
    (1962,'Pizza','Continental'),
    (1571,'Fish','Continental'),
    (2956,'Fish','Continental'),
    (2104,'Fish','Continental'),
    (2444,'Seafood','Continental'),
    (2867,'Seafood','Continental'),
    (1445,'Seafood','Continental');
    
    # filtering the data where cuisine= "Italian" WHERE CLAUSE
select meal_id,category from meal_information where cuisine="Italian";

    # And Or condition by using where clause
    select meal_id,category,cuisine from meal_information where cuisine="continential" and category="beverage";
    #or operator
    select meal_id,category,cuisine from meal_information where cuisine="continential" or category="beverage";
#order by ascending order
select * from meal_information order by meal_id,cuisine;
#ORDER BY INTO DSECIND ORDER
select * from meal_information order by meal_id desc;
#group by
select meal_id, cuisine from meal_information group by meal_id;
