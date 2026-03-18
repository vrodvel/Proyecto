BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Equipo" (
	"id_equipo"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"posicion"	NUMERIC NOT NULL,
	"liga"	TEXT NOT NULL,
	PRIMARY KEY("id_equipo")
);
CREATE TABLE IF NOT EXISTS "jugadores" (
	"id_jugador"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"apellidos"	TEXT NOT NULL,
	"dorsal"	INTEGER NOT NULL,
	"goles"	INTEGER NOT NULL,
	"id_equipo"	INTEGER,
	FOREIGN KEY("id_equipo") REFERENCES "Equipo"("id_equipo"),
	PRIMARY KEY("id_jugador")
);
CREATE TABLE IF NOT EXISTS "trofeos" (
	"id_trofeos"	INTEGER NOT NULL,
	"nombre"	INTEGER NOT NULL,
	"numero_de_trofeos"	INTEGER NOT NULL,
	"id_equipo"	INTEGER,
	PRIMARY KEY("id_trofeos")
);
INSERT INTO "Equipo" VALUES (1,'Barça','1º','Española');
INSERT INTO "Equipo" VALUES (2,'Real Madrid','2º','Española');
INSERT INTO "Equipo" VALUES (3,'PSG','1º','Ligue 1');
INSERT INTO "jugadores" VALUES (1,'Pedri','Gonzalez',8,30,1);
INSERT INTO "jugadores" VALUES (2,'Vinicius','Junior',7,300,2);
INSERT INTO "jugadores" VALUES (3,'Fabian','Ruiz',8,115,3);
INSERT INTO "trofeos" VALUES (1,'Liga Española',28,1);
INSERT INTO "trofeos" VALUES (2,'Champions',15,2);
INSERT INTO "trofeos" VALUES (3,'Champions',1,3);
COMMIT;
