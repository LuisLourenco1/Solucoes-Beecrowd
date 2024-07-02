SELECT c.name, SUM(p.amount) as sum  -- seleciona o nome da categoria e a soma da quantidade dos produtos
FROM products p INNER JOIN categories c ON  -- junta a tabela de produtos com a tabela de categorias
    p.id_categories = c.id
GROUP BY c.id  -- agrupa por id