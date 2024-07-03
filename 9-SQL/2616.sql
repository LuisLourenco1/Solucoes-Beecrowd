SELECT c.id, c.name  -- seleciona o id e o nome do cliente
FROM customers c LEFT JOIN locations l ON  -- junta a tabela customers com a tabela locations com LEFT JOIN
    c.id = l.id_customers
WHERE l.id_customers IS NULL  -- filtra os clientes que nunca alugaram um filme
ORDER BY c.id ASC;  -- ordena os resultados pelo id do cliente