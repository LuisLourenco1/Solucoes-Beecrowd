SELECT m.id, m.name -- seleciona o id e o nome do filme
FROM movies m INNER JOIN prices p ON -- junta a tabela de filmes com a tabela de preços
    m.id_prices = p.id
WHERE p.id = 5 -- seleciona os filmes que possuem o preço de id 5 (promoção)