SELECT m.id, m.name  -- seleciona o id e o nome do filme
FROM movies m INNER JOIN genres g ON  -- junta a tabela movies com a tabela genres
    m.id_genres = g.id
WHERE g.description = 'Action'  -- filtra os filmes que possuem o gênero Action