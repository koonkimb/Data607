
Drop Table if Exists #PopularMovies
Drop Table if Exists PopularMovies

create table #PopularMovies (
RespondentInitials nvarchar(10),
Movie nvarchar(200),
Rating nvarchar(30),);

Insert into #PopularMovies 
values
('PH','Deadpool and Wolverine', '5'),
('MM','Deadpool and Wolverine', '3.5'),
('TH','Deadpool and Wolverine', '4'),
('KK','Deadpool and Wolverine', 'N/A'),
('RD','Deadpool and Wolverine', 'NA'),
('PH','Everything, Everywhere, All at Once', '4'),
('MM','Everything, Everywhere, All at Once', '10000000'),
('TH','Everything, Everywhere, All at Once', '4'),
('KK','Everything, Everywhere, All at Once', 'N/A'),
('RD','Everything, Everywhere, All at Once', '5'),
('PH','Barbie', '4'),
('MM','Barbie', 'NA'),
('TH','Barbie', '3'),
('KK','Barbie', '4'),
('RD','Barbie', '3'),
('PH','Oppenheimer', '4'),
('MM','Oppenheimer', '3.8'),
('TH','Oppenheimer', '3'),
('KK','Oppenheimer', '4'),
('RD','Oppenheimer', '5'),
('PH','Spiderman Into the Spiderverse', '5'),
('MM','Spiderman Into the Spiderverse', '3.5'),
('TH','Spiderman Into the Spiderverse', '5'),
('KK','Spiderman Into the Spiderverse', '4'),
('RD','Spiderman Into the Spiderverse', '3'),
('PH','Puss in Boots 2', '5'),
('MM','Puss in Boots 2', '4'),
('TH','Puss in Boots 2', '5'),
('KK','Puss in Boots 2', 'N/A'),
('RD','Puss in Boots 2', 'N.A');

With dataCleaning as (
Select RespondentInitials, 
Movie,
case when isnumeric(Rating) = 1 then round(Rating,0) else '' end as Rating
from #PopularMovies)
Select RespondentInitials, 
Movie,
case when Rating = '' then '' when Rating > 5 then 5 when Rating < 1 then 1 else Rating end as Rating
into PopularMovies
from dataCleaning

Select * from PopularMovies

