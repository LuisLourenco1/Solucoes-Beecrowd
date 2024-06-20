SELECT name, street -- seleciona as colunas nome e rua
FROM customers  -- do banco de dados clientes
WHERE LOWER(city) = 'porto alegre' -- onde a cidade é porto alegre