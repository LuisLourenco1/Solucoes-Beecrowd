SELECT p.name, f.name, p.price -- seleciona o nome do produto, o nome do fornecedor e o preço do produto
FROM categories c INNER JOIN products p ON -- junta a tabela de categorias com a tabela de produtos
     p.id_categories = c.id INNER JOIN providers f ON -- junta a tabela de produtos com a tabela de fornecedores
     p.id_providers = f.id
WHERE c.name = 'Super Luxury' AND p.price > 1000 -- filtra as categorias que são 'Super Luxury' e o preço do produto é maior que 1000