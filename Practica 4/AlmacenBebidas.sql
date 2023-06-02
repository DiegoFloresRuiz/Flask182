CREATE DATABASE AlmacenBebidas;
use AlmacenBebidas;

CREATE TABLE Almacen (
  id INT,
  nombre VARCHAR(20) NOT NULL,
  Precio float NOT NULL,
  Clasificacion VARCHAR(20),
  Marca VARCHAR(20)
);