# Data Cleaning and create a view
#### individual_airlines_scheduled_passenger_kilometers_flown table
```
create view individual_airlines_scheduled_passenger_kilometers_flown_view as 
with cte as (select Rank_, Airline, Country, 2022_ value, '2022' 2022_ 
from individual_airlines_scheduled_passenger_kilometers_flown
union all
select Rank_, Airline, Country, 2021_ value, '2021' 2021_
from individual_airlines_scheduled_passenger_kilometers_flown
union all
select Rank_, Airline, Country, 2020_ value, '2020' 2020_
from individual_airlines_scheduled_passenger_kilometers_flown
union all
select Rank_, Airline, Country, 2019_ value, '2019' 2019_
from individual_airlines_scheduled_passenger_kilometers_flown
union all
select Rank_, Airline, Country, 2018_ value, '2018' 2018_
from individual_airlines_scheduled_passenger_kilometers_flown
union all
select Rank_, Airline, Country, 2017_ value, '2017' 2017_
from individual_airlines_scheduled_passenger_kilometers_flown
union all
select Rank_, Airline, Country, 2016_ value, '2016' 2016_
from individual_airlines_scheduled_passenger_kilometers_flown
union all
select Rank_, Airline, Country, 2015_ value, '2015' 2015_
from individual_airlines_scheduled_passenger_kilometers_flown
union all
select Rank_, Airline, Country, 2014_ value, '2014' 2014_
from individual_airlines_scheduled_passenger_kilometers_flown
union all
select Rank_, Airline, Country, 2013_ value, '2013' 2013_
from individual_airlines_scheduled_passenger_kilometers_flown
union all
select Rank_, Airline, Country, 2012_ value, '2012' 2012_
from individual_airlines_scheduled_passenger_kilometers_flown
union all
select Rank_, Airline, Country, 2011_ value, '2011' 2011_
from individual_airlines_scheduled_passenger_kilometers_flown)
select Rank_, Airline, Country, value as scheduled_passenger_kilometers_flown_in_millions, 2022_ as years from cte
;
```
#### Output
![Screen Shot 2024-06-14 at 10 23 33 PM](https://github.com/quocduyenanhnguyen/Airlines_Web_Scrapping/assets/92205707/fe861977-bbc3-4cf4-9442-a2b81086d34a)

-> After cleaning the data in the CSV files and transposing with SQL, this is the final output that we will create a view of to visualize in Tableau.

#### scheduled_freight_tonne_kilometers table
```
create view scheduled_freight_tonne_kilometers_view as with cte as (select Rank_, Airline, Country, 2022_ value, '2022' 2022_ 
from scheduled_freight_tonne_kilometers
union all
select Rank_, Airline, Country, 2021_ value, '2021' 2021_
from scheduled_freight_tonne_kilometers
union all
select Rank_, Airline, Country, 2020_ value, '2020' 2020_
from scheduled_freight_tonne_kilometers
union all
select Rank_, Airline, Country, 2019_ value, '2019' 2019_
from scheduled_freight_tonne_kilometers
union all
select Rank_, Airline, Country, 2018_ value, '2018' 2018_
from scheduled_freight_tonne_kilometers
union all
select Rank_, Airline, Country, 2017_ value, '2017' 2017_
from scheduled_freight_tonne_kilometers
union all
select Rank_, Airline, Country, 2016_ value, '2016' 2016_
from scheduled_freight_tonne_kilometers
union all
select Rank_, Airline, Country, 2015_ value, '2015' 2015_
from scheduled_freight_tonne_kilometers
union all
select Rank_, Airline, Country, 2014_ value, '2014' 2014_
from scheduled_freight_tonne_kilometers
union all
select Rank_, Airline, Country, 2013_ value, '2013' 2013_
from scheduled_freight_tonne_kilometers
union all
select Rank_, Airline, Country, 2012_ value, '2012' 2012_
from scheduled_freight_tonne_kilometers
)
select Rank_, Airline, Country, value as scheduled_freight_tonne_kilometers_in_millions, 2022_ as years from cte
;
```
#### Output
![Screen Shot 2024-06-14 at 10 25 59 PM](https://github.com/quocduyenanhnguyen/Airlines_Web_Scrapping/assets/92205707/a543a910-1fee-45a3-b023-c381f34d0e60)

-> Similar to the above table.

