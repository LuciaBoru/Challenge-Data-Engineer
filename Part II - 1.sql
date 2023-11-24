CREATE TABLE Clinte(
	ClieteID INT,
	Nombre VARCHAR(10),
	Apellidos VARCHAR(30),
	Telefono VARCHAR(10), 
	CURP VARCHAR(18), 
	RFC VARCHAR(13), 
	Direccion VARCHAR(25),
	PRIMARY KEY(ClieteID)
);

CREATE TABLE Articulo(
	ArticuloID INT,
	NombreArt VARCHAR(25),
	PrecioArt DECIMAL(10,2),
	PRIMARY KEY(ArticuloID)
);

CREATE TABLE Tienda(
	TiendaID INT,
	NombreT VARCHAR(10),
	CoordenadasT VARCHAR(50),
	PRIMARY KEY(TiendaID)
);
