SELECT id, name -- seleciona o id e o nome do produto
FROM products
WHERE price < 10 OR price > 100 -- filtra os produtos que o preço é menor que 10 ou maior que 100