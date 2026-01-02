-- Create table
CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    region TEXT,
    date DATE,
    units_sold INTEGER,
    revenue REAL
);

-- Insert sample data
INSERT INTO sales (product, region, date, units_sold, revenue)
VALUES
('Widget A','North','2025-01-01',10,100.0),
('Widget B','South','2025-01-01',5,50.0),
('Widget A','North','2025-01-02',12,120.0),
('Widget B','South','2025-01-02',7,70.0);
