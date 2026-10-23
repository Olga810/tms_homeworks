lesson15=> CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);
CREATE TABLE
lesson15=> CREATE TABLE books (
lesson15(>     id SERIAL PRIMARY KEY,
lesson15(>     title VARCHAR(150) NOT NULL,
lesson15(>     author_id INT REFERENCES authors(id) ON DELETE SET NULL,
lesson15(>     publication_year INT
lesson15(> );
CREATE TABLE
lesson15=> CREATE TABLE sales (
lesson15(>     id SERIAL PRIMARY KEY,
lesson15(>     book_id INT REFERENCES books(id) ON DELETE CASCADE,
lesson15(>     quantity INT NOT NULL CHECK (quantity > 0)
lesson15(> );
CREATE TABLE
lesson15=> 
INSERT INTO authors (first_name, last_name) VALUES
            ('Лев', 'Толстой'),
            ('Федор', 'Достоевский'),
            ('Александр', 'Пушкин'),
            ('Джордж', 'Оруэлл');
INSERT INTO books (title, author_id, publication_year) VALUES
            ('Война и мир', 1, 1869),
            ('Преступление и наказание', 2, 1866),
            ('Евгений Онегин', 3, 1833),
            ('Капитанская дочка', 3, 1836),
            ('Слово о полку Игореве', NULL, 1800);
INSERT INTO sales (book_id, quantity) VALUES
            (1, 10),
            (1, 5),
            (2, 20),
            (4, 7);
SELECT b.title, a.first_name, a.last_name
FROM books b
INNER JOIN authors a ON b.author_id = a.id;

SELECT a.first_name, a.last_name, b.title
FROM authors a
LEFT JOIN books b ON a.id = b.author_id;

SELECT b.title, a.first_name, a.last_name
FROM authors a
RIGHT JOIN books b ON a.id = b.author_id;

SELECT b.title, a.first_name, a.last_name, s.quantity
FROM books b
INNER JOIN authors a ON b.author_id = a.id
INNER JOIN sales s ON b.id = s.book_id;

SELECT a.first_name, a.last_name, b.title, s.quantity
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
LEFT JOIN sales s ON b.id = s.book_id;