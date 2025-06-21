-- 1. Customers Table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    address VARCHAR(255)
);

-- 2. Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

-- 3. Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- 4. Order Items Table
CREATE TABLE order_items (
    item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- 5. Payments Table
CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    amount DECIMAL(10, 2),
    payment_date DATE,
    method VARCHAR(50),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- 6. Delivery Table
CREATE TABLE delivery (
    delivery_id INT PRIMARY KEY,
    order_id INT,
    delivery_status VARCHAR(50),
    delivery_date DATE,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
INSERT INTO customers VALUES
(1, 'Ravi Teja', 'ravi@email.com', '9876543210', 'Hyderabad'),
(2, 'John Doe', 'john@email.com', '9123456780', 'Mumbai'),
(3, 'Alice Smith', 'alice@email.com', '9988776655', 'Delhi'),
(4, 'Bob Johnson', 'bob@email.com', '9876543211', 'Chennai'),
(5, 'Emma Brown', 'emma@email.com', '8765432190', 'Bangalore'),
(6, 'David Lee', 'david@email.com', '9654321876', 'Pune'),
(7, 'Olivia Garcia', 'olivia@email.com', '9234567890', 'Kolkata'),
(8, 'Liam Wilson', 'liam@email.com', '9345678901', 'Ahmedabad'),
(9, 'Sophia Patel', 'sophia@email.com', '9456789012', 'Jaipur'),
(10, 'Noah Kim', 'noah@email.com', '9567890123', 'Lucknow');

INSERT INTO products VALUES
(1, 'Pen', 'Stationery', 5.00),
(2, 'Notebook', 'Stationery', 20.00),
(3, 'Laptop', 'Electronics', 50000.00),
(4, 'Mouse', 'Electronics', 500.00),
(5, 'Keyboard', 'Electronics', 1000.00),
(6, 'Monitor', 'Electronics', 10000.00),
(7, 'Chair', 'Furniture', 3000.00),
(8, 'Table', 'Furniture', 4000.00),
(9, 'Water Bottle', 'Utility', 200.00),
(10, 'Backpack', 'Accessories', 1500.00);

INSERT INTO orders VALUES
(1, 1, '2024-06-01'),
(2, 2, '2024-06-02'),
(3, 3, '2024-06-03'),
(4, 4, '2024-06-04'),
(5, 5, '2024-06-05'),
(6, 6, '2024-06-06'),
(7, 7, '2024-06-07'),
(8, 8, '2024-06-08'),
(9, 9, '2024-06-09'),
(10, 10, '2024-06-10');

INSERT INTO order_items VALUES
(1, 1, 1, 10),
(2, 2, 3, 1),
(3, 3, 2, 5),
(4, 4, 4, 2),
(5, 5, 5, 1),
(6, 6, 6, 1),
(7, 7, 7, 1),
(8, 8, 8, 1),
(9, 9, 9, 3),
(10, 10, 10, 2);

INSERT INTO payments VALUES
(1, 1, 50.00, '2024-06-01', 'UPI'),
(2, 2, 50000.00, '2024-06-02', 'Credit Card'),
(3, 3, 100.00, '2024-06-03', 'Cash'),
(4, 4, 1000.00, '2024-06-04', 'Debit Card'),
(5, 5, 1000.00, '2024-06-05', 'UPI'),
(6, 6, 10000.00, '2024-06-06', 'Net Banking'),
(7, 7, 3000.00, '2024-06-07', 'Cash'),
(8, 8, 4000.00, '2024-06-08', 'UPI'),
(9, 9, 600.00, '2024-06-09', 'UPI'),
(10, 10, 3000.00, '2024-06-10', 'UPI');

INSERT INTO delivery VALUES
(1, 1, 'Delivered', '2024-06-03'),
(2, 2, 'Shipped', '2024-06-04'),
(3, 3, 'Delivered', '2024-06-05'),
(4, 4, 'Pending', NULL),
(5, 5, 'Delivered', '2024-06-07'),
(6, 6, 'Shipped', '2024-06-08'),
(7, 7, 'Delivered', '2024-06-09'),
(8, 8, 'Pending', NULL),
(9, 9, 'Delivered', '2024-06-11'),
(10, 10, 'Delivered', '2024-06-12');
