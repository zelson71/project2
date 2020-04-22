Select * From all_wines;

Select "ID", category, country, description, price, rating, region, title, varietal, vintage,url
From all_wines;

SELECT country, COUNT(*)
FROM all_wines
GROUP BY country
HAVING COUNT(*) > 1000
ORDER BY count DESC

select "ID", category, country, description, price, rating, region, title, varietal, vintage,url 
from all_wines
WHERE category='Red'
AND rating>94
AND country in ('US', 'France', 'Italy', 'Spain', 'Portugal', 'Chile', 'Argentina');


Select "ID", category, country, description, price, rating, region, title, varietal, vintage
FROM all_wines
WHERE rating>94

Select "ID", category, country, description, price, rating, region, title, varietal, vintage
FROM all_wines
WHERE country in ('US', 'France', 'Italy', 'Spain', 'Portugal', 'Chile', 'Argentina', 'Austria', 'Germany', 'New Zealand', 'South Africe')
AND rating>90;

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

SELECT regr_slope(rating, price) slope FROM all_wines WHERE category='Fortified';
SELECT regr_intercept(rating, price) intercept FROM all_wines WHERE category='Fortified';

SELECT regr_slope(rating, price) slope FROM all_wines WHERE category='Port/Sherry';
SELECT regr_intercept(rating, price) intercept FROM all_wines WHERE category='Port/Sherry';