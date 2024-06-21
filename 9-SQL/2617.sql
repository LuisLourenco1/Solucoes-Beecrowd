SELECT p.name, f.name -- seleciona o nome do produto e o nome do fornecedor
FROM products p INNER JOIN providers f ON -- junta a tabela de produtos com a tabela de fornecedores
    p.id_providers = f.id
WHERE f.name = 'Ajax SA' -- filtra os produtos que são fornecidos pela 'Ajax SA'