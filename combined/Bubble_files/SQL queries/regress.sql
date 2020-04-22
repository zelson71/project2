CREATE TABLE regression(category VARCHAR(30), slope FLOAT, intercept FLOAT);

SELECT * FROM all_wines;

INSERT INTO regression(category) 
SELECT DISTINCT category FROM all_wines

INSERT INTO regression(category,slope,intercept)
VALUES ('Red',0.0253725687731849,87.3763926061008)

INSERT INTO regression(category,slope,intercept)
VALUES ('White',0.0511808841416066,86.498984695771);

INSERT INTO regression(category,slope,intercept)
VALUES ('Rose',0.0670108293913071,85.3963110484119);

INSERT INTO regression(category,slope,intercept)
VALUES ('Sparkling',0.0273393923435366,87.1374226086509)

INSERT INTO regression(category,slope,intercept)
VALUES ('Dessert',0.0224989005750288,88.34607735694)

INSERT INTO regression(category,slope,intercept)
VALUES ('Fortified',)

INSERT INTO regression(category,slope,intercept)
VALUES ('Port/Sherry',)


SELECT * FROM regression;

DROP TABLE regression

SELECT regr_slope(rating, price) slope FROM all_wines;
SELECT regr_intercept(rating, price) intercept FROM all_wines;

SELECT regr_slope(rating, price) slope FROM all_wines WHERE category='Red';
SELECT regr_intercept(rating, price) intercept FROM all_wines WHERE category='Red';

SELECT regr_slope(rating, price) slope FROM all_wines WHERE category='White';
SELECT regr_intercept(rating, price) intercept FROM all_wines WHERE category='White';

SELECT regr_slope(rating, price) slope FROM all_wines WHERE category='Sparkling';
SELECT regr_intercept(rating, price) intercept FROM all_wines WHERE category='Sparkling';

SELECT regr_slope(rating, price) slope FROM all_wines WHERE category='Rose';
SELECT regr_intercept(rating, price) intercept FROM all_wines WHERE category='Rose';

SELECT regr_slope(rating, price) slope FROM all_wines WHERE category='Dessert';
SELECT regr_intercept(rating, price) intercept FROM all_wines WHERE category='Dessert';

SELECT regr_slope(rating, price) slope FROM all_wines WHERE category='Fortified';
SELECT regr_intercept(rating, price) intercept FROM all_wines WHERE category='Fortified';

SELECT regr_slope(rating, price) slope FROM all_wines WHERE category='Port/Sherry';
SELECT regr_intercept(rating, price) intercept FROM all_wines WHERE category='Port/Sherry';