-- Encontra a segunda cidade mais populosa e une com a segunda cidade menos populosa, ordenando pelo nome da cidade de forma decrescente.
(SELECT city_name, population
FROM cities
ORDER BY population desc
LIMIT 1 OFFSET 1)
UNION
(SELECT city_name, population
FROM cities
ORDER BY population asc
LIMIT 1 OFFSET 1)
order by city_name desc