CREATE DATABASE Veiculo;


USE Veiculo;


CREATE TABLE USUARIO(
    usuarioid INTEGER NOT NULL auto_increment,
    usuario varchar(40),
    senha varchar(40),
    categoria BIT(1),
    PRIMARY KEY (usuarioid)

);


CREATE TABLE CARROS(
	carroid INTEGER NOT NULL auto_increment,
	marca CHAR(15),
	modelo CHAR(15),
	ano SMALLINT,
	cor CHAR(25),
	km INTEGER,
	preco INTEGER,
	foto varchar(400),
	usuarioid INTEGER,
	PRIMARY KEY (carroid),
    CONSTRAINT FK_usuarioid FOREIGN KEY (usuarioid)
    REFERENCES USUARIO(usuarioid)

);


SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;


INSERT INTO USUARIO (usuario, senha, categoria)
VALUES
('admin', 'admin', 0),
('user', 'user', 1);


INSERT INTO CARROS (marca, modelo, ano, cor, km, preco, foto)
VALUES
('Fiat', 'Marea', 1998, 'Azul', 89000, 10.000, 'foto'),
('Toyota', 'Corolla', 2009, 'Preto', 56000, 10.000, 'foto'),
('Honda', 'Civic', 1993, 'Branco', 100000, 10.000, 'foto');