-- מילוי נתונים בטבלת Gates
INSERT INTO Gates (gate_name, location, is_open)
VALUES
('Gate 1', 'Terminal A', 1),
('Gate 2', 'Terminal B', 1),
('Gate 3', 'Terminal C', 0),
('Gate 4', 'Terminal D', 1);

-- מילוי נתונים בטבלת Flights
INSERT INTO Flights (flight_number, departure_airport, arrival_airport, departure_time, arrival_time, status, gate_id)
VALUES
('TLV123', 'Ben Gurion Airport', 'New York JFK', '2025-03-10 10:00:00', '2025-03-10 14:00:00', 'On time', 1),
('TLV124', 'Ben Gurion Airport', 'London Heathrow', '2025-03-10 15:30:00', '2025-03-10 18:45:00', 'Delayed', 2),
('TLV125', 'Ben Gurion Airport', 'Paris Charles de Gaulle', '2025-03-11 08:00:00', '2025-03-11 11:00:00', 'Cancelled', 3),
('TLV126', 'Ben Gurion Airport', 'Dubai International', '2025-03-11 12:00:00', '2025-03-11 16:30:00', 'On time', 4);

-- מילוי נתונים בטבלת Passengers
INSERT INTO Passengers (first_name, last_name, passport_number, flight_id)
VALUES
('David', 'Cohen', 'A12345678', 1),
('Maya', 'Levy', 'B23456789', 2),
('Yoni', 'Ben David', 'C34567890', 3),
('Sarah', 'Mizrahi', 'D45678901', 4);

-- מילוי נתונים בטבלת Flight_Delays
INSERT INTO Flight_Delays (flight_id, delay_time, reason)
VALUES
(2, 45, 'Weather conditions'),
(3, 0, 'No delays'),
(4, 15, 'Security check');
