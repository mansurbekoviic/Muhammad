CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(55),
    last_name VARCHAR(55),
    phone_number int not null
);

INSERT INTO employees (first_name, last_name, phone_number)
VALUES ('Muhammad', 'Ali', +998963223232);

UPDATE employees SET phone_number = +9999999999 WHERE id = 1;

DELETE FROM employees WHERE id = 1;



