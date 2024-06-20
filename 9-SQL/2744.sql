-- Converte as senhas para o modelo MD5
SELECT id, password, MD5(password)
FROM account