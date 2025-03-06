USE AirportManagement;
GO

-- הוספת משתמשים
INSERT INTO Users (username, email, password_hash, role) VALUES
('user1', 'user1@example.com', 'hashed_password1', 'user'),
('user2', 'user2@example.com', 'hashed_password2', 'user'),
('admin1', 'admin1@example.com', 'hashed_password3', 'admin');
GO

-- הוספת טיסות (המראות ונחיתות)
INSERT INTO Flights (flight_number, airline, origin, destination, terminal, gate, scheduled_time, updated_time, status) VALUES
-- המראות
INSERT INTO Flights (flight_number, airline, origin, destination, terminal, gate, scheduled_time, updated_time, status) VALUES
('1001', 'El Al', 'Ben Gurion', 'New York', 3, 'A10', '2025-03-07 06:00', NULL, 'scheduled'),
('1002', 'Turkish Airlines', 'Ben Gurion', 'Istanbul', 3, 'C12', '2025-03-07 06:45', NULL, 'scheduled'),
('1003', 'Lufthansa', 'Ben Gurion', 'Munich', 3, 'B14', '2025-03-07 07:15', NULL, 'scheduled'),
('1004', 'Wizz Air', 'Ben Gurion', 'Vienna', 3, 'D20', '2025-03-07 07:50', NULL, 'scheduled'),
('1005', 'Delta', 'Ben Gurion', 'Atlanta', 3, 'A18', '2025-03-07 08:30', NULL, 'scheduled'),
('1006', 'Ryanair', 'Ben Gurion', 'Rome', 3, 'D25', '2025-03-07 09:00', NULL, 'scheduled'),
('1007', 'EasyJet', 'Ben Gurion', 'Amsterdam', 3, 'E22', '2025-03-07 10:30', NULL, 'scheduled'),
('1008', 'Arkia', 'Ben Gurion', 'Eilat', 3, 'G5', '2025-03-07 11:00', NULL, 'scheduled'),

-- נחיתות
('7862', 'Aeroméxico', 'Paris', 'Ben Gurion', 3, NULL, '2025-03-06 19:55', '2025-03-06 20:35', 'arrived'),
('324', 'El Al', 'Paris', 'Ben Gurion', 3, NULL, '2025-03-06 19:55', '2025-03-06 20:35', 'arrived'),
('3160', 'Scandinavian', 'Paris', 'Ben Gurion', 3, NULL, '2025-03-06 19:55', '2025-03-06 20:35', 'arrived'),
('5104', 'El Al', 'London', 'Ben Gurion', 3, NULL, '2025-03-06 20:05', '2025-03-06 19:35', 'arrived'),
('131', 'Bluebird', 'Rome', 'Ben Gurion', 3, NULL, '2025-03-06 20:05', '2025-03-06 20:23', 'arrived'),
('447', '5F', 'Kishinev', 'Ben Gurion', 3, NULL, '2025-03-06 20:30', '2025-03-06 20:16', 'arrived'),
('7494', 'Virgin Atlantic', 'London', 'Ben Gurion', 3, NULL, '2025-03-06 21:35', NULL, 'scheduled'),
('827', 'Arkia', 'Ramon', 'Ben Gurion', 3, 'G20', '2025-03-06 20:00', '2025-03-06 20:06', 'departed'),
('891', 'Israir', 'Tbilisi', 'Ben Gurion', 3, 'G1', '2025-03-06 20:00', '2025-03-06 20:30', 'departed'),
('925', 'Aegean', 'Athens', 'Ben Gurion', 3, 'A24', '2025-03-06 20:10', '2025-03-06 20:59', 'departed'),
('087', 'El Al', 'Phuket', 'Ben Gurion', 3, 'D78', '2025-03-06 20:25', '2025-03-06 20:46', 'departed'),
('322', 'Azerbaijan', 'Baku', 'Ben Gurion', 3, 'B52', '2025-03-06 20:45', '2025-03-06 20:44', 'departed'),
('4580', 'Thai Airways', 'Phuket', 'Ben Gurion', 3, 'D78', '2025-03-06 20:25', '2025-03-06 20:46', 'departed'),
('9955', 'El Al', 'Baku', 'Ben Gurion', 3, 'B52', '2025-03-06 20:45', '2025-03-06 20:44', 'departed'),

-- טיסות נוספות עם מצבים שונים
('2301', 'Turkish Airlines', 'Istanbul', 'Ben Gurion', 3, 'C10', '2025-03-07 06:30', NULL, 'scheduled'),
('1102', 'Lufthansa', 'Frankfurt', 'Ben Gurion', 3, 'B22', '2025-03-07 07:00', NULL, 'scheduled'),
('8831', 'Delta', 'New York', 'Ben Gurion', 3, 'A15', '2025-03-07 08:45', NULL, 'scheduled'),
('2055', 'Ryanair', 'Madrid', 'Ben Gurion', 3, 'D33', '2025-03-07 09:15', NULL, 'scheduled'),
('9091', 'EasyJet', 'Berlin', 'Ben Gurion', 3, 'E20', '2025-03-07 10:00', NULL, 'scheduled');
GO

-- הוספת מעקב אחרי טיסות
INSERT INTO Followed_Flights (user_id, flight_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(1, 6),
(2, 7),
(3, 8),
(1, 9),
(2, 10),
(3, 11),
(1, 12),
(2, 13),
(3, 14),
(1, 15);
GO
