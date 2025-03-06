CREATE database Airport_DB

USE Airport_DB

-- יצירת טבלת Flights
CREATE TABLE Flights (
    flight_id INT PRIMARY KEY IDENTITY(1,1),
    flight_number VARCHAR(50) NOT NULL,
    departure_airport VARCHAR(100),
    arrival_airport VARCHAR(100),
    departure_time DATETIME,
    arrival_time DATETIME,
    status VARCHAR(50),
    gate_id INT,
    FOREIGN KEY (gate_id) REFERENCES Gates(gate_id)
);

-- יצירת טבלת Passengers
CREATE TABLE Passengers (
    passenger_id INT PRIMARY KEY IDENTITY(1,1),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    passport_number VARCHAR(50),
    flight_id INT,
    FOREIGN KEY (flight_id) REFERENCES Flights(flight_id)
);

-- יצירת טבלת Gates
CREATE TABLE Gates (
    gate_id INT PRIMARY KEY IDENTITY(1,1),
    gate_name VARCHAR(50) NOT NULL,
    location VARCHAR(100),
    is_open BIT -- שדה המצב אם השער פתוח או סגור
);

-- יצירת טבלת Flight_Delays
CREATE TABLE Flight_Delays (
    delay_id INT PRIMARY KEY IDENTITY(1,1),
    flight_id INT,
    delay_time INT, -- זמן העיכוב בדקות
    reason VARCHAR(255),
    FOREIGN KEY (flight_id) REFERENCES Flights(flight_id)
);
