CREATE SCHEMA projeto_teste;

CREATE TABLE base_tabela1(
  id int NOT NULL AUTO_INCREMENT,
  coluna1 int DEFAULT NULL,
  coluna2 varchar(64) DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE base_tabela2(
  id int NOT NULL AUTO_INCREMENT,
  valor int DEFAULT NULL,
  tabela1_id int DEFAULT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (tabela1_id) REFERENCES base_tabela1(id)
);