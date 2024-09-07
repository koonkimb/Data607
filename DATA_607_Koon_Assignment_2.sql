
Drop Table if Exists #PopularMovies
Drop Table if Exists PopularMovies

create table #PopularMovies (
RespondentInitials nvarchar(10),
Deadpool3 nvarchar(30),
EverythingEverywhere nvarchar(30),
Barbie nvarchar(30),
Oppenheimer nvarchar(30),
IntotheSpiderverse nvarchar(30),
PussInBoots2 nvarchar(30));

Insert into #PopularMovies 
values
('PH','5','4','4','4','5','5'),
('MM','3.5','10000000','NA','3.8','3.5','4'),
('TH','4','4','3','3','5','5'),
('KK','N/A','N/A','4','4','4','N/A'),
('RD','NA','5','3','5','3','NA');

With dataCleaning as (
Select RespondentInitials, 
case when isnumeric(Deadpool3) = 1 then round(Deadpool3,0) else '' end as Deadpool3,
case when isnumeric(EverythingEverywhere) = 1 then round(EverythingEverywhere,0) else '' end as EverythingEverywhere,
case when isnumeric(Barbie) = 1 then round(Barbie,0) else '' end as Barbie,
case when isnumeric(Oppenheimer) = 1 then round(Oppenheimer,0) else '' end as Oppenheimer,
case when isnumeric(IntotheSpiderverse) = 1 then round(IntotheSpiderverse,0) else '' end as IntotheSpiderverse,
case when isnumeric(PussInBoots2) = 1 then round(PussInBoots2,0) else '' end as PussInBoots2
from #PopularMovies)
Select RespondentInitials, 
case when Deadpool3 = '' then '' when Deadpool3 > 5 then 5 when Deadpool3 < 1 then 1 else Deadpool3 end as Deadpool3,
case when EverythingEverywhere = '' then '' when EverythingEverywhere > 5 then 5 when EverythingEverywhere < 1 then 1 else EverythingEverywhere end as EverythingEverywhere,
case when Barbie = '' then '' when Barbie > 5 then 5 when Barbie < 1 then 1 else Barbie end as Barbie,
case when Oppenheimer = '' then '' when Oppenheimer > 5 then 5 when Oppenheimer < 1 then 1 else Oppenheimer end as Oppenheimer,
case when IntotheSpiderverse = '' then '' when IntotheSpiderverse > 5 then 5 when IntotheSpiderverse < 1 then 1 else IntotheSpiderverse end as IntotheSpiderverse,
case when PussInBoots2 = '' then '' when PussInBoots2 > 5 then 5 when PussInBoots2 < 1 then 1 else PussInBoots2 end as PussInBoots2
into PopularMovies
from dataCleaning

Select * from PopularMovies

