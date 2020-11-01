USE credit_shelf;

DROP TABLE IF EXISTS Stations;

CREATE TABLE Stations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  stationId INT,
  name VARCHAR(255),
  latitude DECIMAL(10,8),
  longitude DECIMAL(11,8)
);
