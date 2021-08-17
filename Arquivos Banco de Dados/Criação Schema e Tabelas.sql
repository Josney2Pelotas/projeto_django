CREATE SCHEMA projeto_teste;

CREATE TABLE base_tabela1(
  id int NOT NULL AUTO_INCREMENT,
  coluna1 int DEFAULT NULL,
  coluna2 varchar(64) DEFAULT NULL,
  PRIMARY KEY (id)
);

INSERT INTO base_tabela1(coluna1, coluna2) VALUES (10, 'Valor 1'), (20, 'Valor 2'), (30, 'Valor 3'), (40, 'Valor 4'), (50, 'Valor 5'), (60, 'Valor 6'), (70, 'Valor 7'), (80, 'Valor 8'), (90, 'Valor 9'), (100, 'Valor 10');

CREATE TABLE base_tabela2(
  id int NOT NULL AUTO_INCREMENT,
  valor int DEFAULT NULL,
  tabela1_id int DEFAULT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (tabela1_id) REFERENCES base_tabela1(id)
);

INSERT INTO base_tabela2(valor, tabela1_id) VALUES (100, 1), (200, 2), (300, 3), (400, 4), (500, 5), (600, 6), (700, 7), (800, 8), (900, 9), (1000, 10);