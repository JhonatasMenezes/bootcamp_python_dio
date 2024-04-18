USE dio_db;

INSERT INTO users (name, email, birthDate, address) 
VALUES ('Jhonatas Menezes', 'teste@teste.com', 
        '1997-02-12', 'Rua Dois, 240, São Paulo, SP'),
	   ('Maria Rosa', 'teste2@teste.com', 
        '1989-08-30', 'Av Paulo Silveira Dois, 8773, São Paulo, SP'),
	   ('Paulo Silva', 'teste3@teste.com', 
        '1975-06-19', 'Rua Tres, 236, Araraquara, SP'),
	   ('Jorginho Ribeiro', 'teste4@teste.com', 
        '1999-01-21', 'Rua Dois, 59, Rio de Janeiro, RJ');

INSERT INTO destiny (name, description) 
VALUES ('Praia do Rosa', 'Linda praia com águas cristalinas'),
	   ('Cristo Redentor', 'Maior estatua do Brasil'),
       ('Porto de Galinhas', 'Linda praia do litoral nordestino'),
       ('Campos do Jordão', 'Lugar turístico com atrações de inverno');

INSERT INTO reservations (user_id, destiny_id, date, status) 
VALUES (1, 1, '2024-04-17','pendente'),
	   (2, 4, '2023-06-28','finalizada'),
       (3, 2, '2024-02-12','finalizada'),
       (4, 3, '2024-10-08','pendente');

SELECT *
FROM users;

SELECT *
FROM destiny;

SELECT *
FROM reservations;
