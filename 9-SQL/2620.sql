SELECT c.name, o.id  -- seleciona o nome do cliente e o id do pedido
FROM customers c INNER JOIN orders o ON  -- junta a tabela customers com a tabela orders com INNER JOIN
    o.id_customers = c.id
WHERE EXTRACT(YEAR FROM o.orders_date) = 2016 AND EXTRACT(MONTH FROM o.orders_date) < 7;  -- filtra os pedidos feitos até a metade de 2016