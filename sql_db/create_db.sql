CREATE DATABASE AirportManagement;
GO
USE AirportManagement;
GO

-- טבלת משתמשים
CREATE TABLE Users (
    id INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(50) UNIQUE NOT NULL,
    email NVARCHAR(100) UNIQUE NOT NULL,
    password_hash NVARCHAR(255) NOT NULL,
    role NVARCHAR(10) CHECK (role IN ('user', 'admin')) NOT NULL
);
GO

-- טבלת טיסות
CREATE TABLE Flights (
    id INT PRIMARY KEY IDENTITY(1,1),
    flight_number NVARCHAR(10) NOT NULL,
    airline NVARCHAR(50) NOT NULL,
    origin NVARCHAR(50) NOT NULL,   -- מקור הטיסה
    destination NVARCHAR(50) NOT NULL, -- יעד הטיסה
    terminal INT NOT NULL,
    gate NVARCHAR(10),
    scheduled_time DATETIME NOT NULL,
    updated_time DATETIME,
    status NVARCHAR(10) CHECK (status IN ('scheduled', 'departed', 'arrived', 'delayed', 'cancelled')) NOT NULL
);
GO

-- טבלת מעקב אחרי טיסות
CREATE TABLE Followed_Flights (
    id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT NOT NULL,
    flight_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (flight_id) REFERENCES Flights(id) ON DELETE CASCADE
);
GO
