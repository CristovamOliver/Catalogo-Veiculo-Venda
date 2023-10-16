CREATE DATABASE Veiculo;


USE Veiculo;


CREATE TABLE CARROS(
	id INTEGER NOT NULL auto_increment,
	marca CHAR(15),
	modelo CHAR(15),
	ano SMALLINT,
	cor CHAR(25),
	km INTEGER,
	preco INTEGER,
	foto varchar(400),
	PRIMARY KEY (id)

);


SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;


INSERT INTO CARROS (marca, modelo, ano, cor, km, preco, foto) 
VALUES
('Fiat', 'Marea', 1998, 'Azul', 89000, 10.000, 'foto'),
('Toyota', 'Corolla', 2009, 'Preto', 56000, 10.000, 'foto'),
('Honda', 'Civic', 1993, 'Branco', 100000, 10.000, 'foto');

