-- preventing table conflicts
drop table if exists vic_elec

-- creating the table
Create table vic_elec (
Ind varchar(50),
Time varchar(50),
Demand float,
Temperature float,
Date date,
Holiday varchar(50))

-- inserting the table from csv
bulk insert vic_elec from 'C:\Users\Kim\Documents\Data607\vic_elec.csv' with (firstrow = 2, fieldterminator = ',', rowterminator = '\n')

-- Delete index column as it is not needed; neither is holiday but it's less annoying to look at
IF EXISTS (SELECT 1
               FROM   INFORMATION_SCHEMA.COLUMNS
               WHERE  TABLE_NAME = 'vic_elec'
                      AND COLUMN_NAME = 'ind'
                      AND TABLE_SCHEMA='DBO')
  BEGIN
      Alter Table vic_elec
		Drop column ind;
  END

-- Simplifying dataset to day averages (temp) and day sum (demand)

drop table if exists vic_elec_simplified;

select left(date,4) as year, date, left(avg(temperature),4) as dayTemp, sum(demand) as DayDemand 
  into vic_elec_simplified from vic_elec
  group by date, holiday
  order by date;

-- For 6 day average, use lag window function.  For beginning of dataset (i.e. when there are no previous rows), insert null instead as it is not applicable
with sixday as (
select *, lag(dayDemand,1,0) over (order by date) as previous1, lag(dayDemand,2,0) over (order by date) as previous2, lag(dayDemand,3,0) over (order by date) as previous3, lag(dayDemand,4,0) over (order by date) as previous4, lag(dayDemand,5,0) over (order by date) as previous5
from vic_elec_simplified)
select year, date, dayTemp, dayDemand, case when previous5 <> 0 then (dayDemand+previous1+previous2+previous3+previous4+previous5)/6 else null end as Six_Day_Running_Average_Demand 
from sixday order by date;

-- For YTD averages, use avg window function with partition/order by 
select *, avg(daydemand) over (partition by year order by date) as Year_to_Date_Average_Demand from vic_elec_simplified
order by date

