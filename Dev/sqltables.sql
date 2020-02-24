CREATE TABLE crime (
    time varchar(50)  NOT NULL,
    crime varchar(300)   NOT NULL
     
);

CREATE TABLE lunar (
	phase varchar(500)   NOT NULL,
	sign varchar(500)   NOT NULL,
    time varchar(50)   NOT NULL,
    illumination_percent varchar(5)  NOT NULL
);
    
SELECT lunar.time, crime.crime, lunar.illumination_percent, lunar.phase, lunar.sign 
FROM crime, lunar
WHERE crime.time = lunar.time



