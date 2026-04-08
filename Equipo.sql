BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Equipo" (
	"id_equipo"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"posicion"	NUMERIC NOT NULL,
	"liga"	TEXT NOT NULL,
	PRIMARY KEY("id_equipo")
);
INSERT INTO "Equipo" VALUES (1,'Barça','1º','Española');
INSERT INTO "Equipo" VALUES (2,'Real Madrid','2º','Española');
INSERT INTO "Equipo" VALUES (3,'PSG','1º','Ligue 1');
COMMIT;
