SELECT c.name, r.rentals_date  -- seleciona o nome do cliente e a data do aluguel
FROM customers c INNER JOIN rentals r ON  -- junta a tabela customers com a tabela rentals com INNER JOIN
    r.id_customers = c.id
WHERE EXTRACT(YEAR FROM r.rentals_date) = 2016 AND EXTRACT(MONTH FROM r.rentals_date) = 9;  -- filtra os aluguéis de setembro de 2016