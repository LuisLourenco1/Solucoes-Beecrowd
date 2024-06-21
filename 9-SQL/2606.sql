SELECT p.id, p.name -- seleciona o id e o nome dos produtos
FROM products p INNER JOIN categories c ON -- junta a tabela de produtos e a tabela de categorias
    p.id_categories = c.id
WHERE SUBSTRING(c.name, 1, 5) = 'super' -- somente os produtos cuja categoria começa com 'super'