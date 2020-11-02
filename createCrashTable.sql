USE credit_shelf;

DROP TABLE IF EXISTS Crashes;

CREATE TABLE Crashes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  crashDate DATE,
  crashTime TIME,
  borough VARCHAR(255),
  zipCode VARCHAR(255),
  latitude DECIMAL(10,8),
  longitude DECIMAL(11,8),
  crossStreetName VARCHAR(255),
  numberOfPersonsInjured SMALLINT,
  numberOfPersonsKilled SMALLINT,
  numberOfPedestriansInjured SMALLINT,
  numberOfPedestriansKilled SMALLINT,
  numberOfCyclistInjured SMALLINT,
  numberOfCyclistKilled SMALLINT,
  numberOfMotoristInjured SMALLINT,
  numberOfMotoristKilled SMALLINT,
  contributingFactorVehicle1 VARCHAR(255),
  contributingFactorVehicle2 VARCHAR(255),
  collisionId INT,
  vehicleTypeCode1 VARCHAR(255),
  vehicleTypeCode2 VARCHAR(255)
);
