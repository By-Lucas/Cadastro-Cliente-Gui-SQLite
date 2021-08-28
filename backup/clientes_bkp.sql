BEGIN TRANSACTION;
CREATE TABLE clientes (
                cod INTEGER NOT NULL PRIMARY KEY,
                nome TEXT (50)NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL,
                cidade INTEGER NOT NULL,
                idmt5 INTEGER NOT NULL,
                senhamt5 INTEGER NOT NULL,
                vencimento DATE NOT NULL,
                corretora TEXT NOT NULL
        );
INSERT INTO "clientes" VALUES(1,'Lucas Silva','lucas@gmail.com','74981199190','CG-Ba',12345,123,'20/05/2022','Robo Forex');
INSERT INTO "clientes" VALUES(2,'Mônica Libório','monica@gmail.com','74980005226','Caém-ba',12345,123,'05/10/2050','Robo Forex');
INSERT INTO "clientes" VALUES(3,'Meus Irmãos','irmaos@gmail.com','74981199190','CG-Ba',12345,123,'20/05/2022','Robo Forex');
INSERT INTO "clientes" VALUES(4,'Carlos Bispo ','carlos@gmail.com','74981125565','São Paulo',123456,123,'05/02/2050','IC Markets');
INSERT INTO "clientes" VALUES(5,'Valdelice Silva','valdelice@gmail.com','74981125565','São Paulo',123456,123,'05/02/2050','IC Markets');
INSERT INTO "clientes" VALUES(6,'Maria Baraunas','maria@gmail.com','7498227635','Caém-ba',123456,123,'02/12/2050','IC Markets');
INSERT INTO "clientes" VALUES(7,'Larissa','larissa@gmail.com','7498112762','Sao Paulo',12345,123,'02/12/2050','Robo Forex');
COMMIT;
