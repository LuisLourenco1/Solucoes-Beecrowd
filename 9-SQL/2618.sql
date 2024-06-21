SELECT p.name, f.name, c.name -- seleciona o nome do produto, nome do fornecedor e nome da categoria
FROM products p INNER JOIN providers f ON -- junta a tabela de produtos com a tabela de fornecedores
    p.id_providers = f.id INNER JOIN categories c ON -- junta a tabela resultante com a tabela de categorias
    p.id_categories = c.id
WHERE f.name = 'Sansul SA' AND c.name = 'Imported' -- filtra por fornecedor e por categoria