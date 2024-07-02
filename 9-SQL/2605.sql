SELECT p.name, f.name  -- seleciona o nome do produto e o nome do fornecedor
FROM products p INNER JOIN providers f ON  -- junta a tabela de produtos e a tabela de fornecedores
    p.id_providers = f.id INNER JOIN categories c ON  -- junta a tabela de categorias
    p.id_categories = c.id
WHERE c.id = 6  -- somente os produtos da categoria 6