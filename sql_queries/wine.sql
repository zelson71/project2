-- get a full list of the database
select * from all_wines
-- just testing
select DISTINCT region from all_wines where region IS NOT NULL and subregion IS NOT NULL

select DISTINCT varietal from all_wines

-- ran to see how many there were wher both conditions were true

select * from all_wines where region IS NULL and subregion IS NULL


-- this gives a short list of wines
select * from all_wines where region != subregion


-- ran this to get a distinct list

select DISTINCT region from all_wines

-- ran this to populate the regions that were null
update all_wines
set region = subregion
where region IS NULL

select * from all_wines
select ID  from all_wines


copy (select * from all_wines) to 'd:\test\all_wines.csv' csv header