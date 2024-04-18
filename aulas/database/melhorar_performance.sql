USE dio_db;

-- Comando pra veificar desempenho de querys e informações sobre
EXPLAIN
	SELECT *
    FROM users
    WHERE name = 'Jhonatas Menezes';

-- Criação de index para melhorar performance de querys
CREATE INDEX idx_name ON users (name);
