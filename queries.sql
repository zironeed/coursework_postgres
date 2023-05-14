CREATE DATABASE 'name'

CREATE TABLE employees (
id int PRIMARY KEY,
title varchar NOT NULL,
url varchar NOT NULL,
vacancy_count int
);

CREATE TABLE vacancies (
employee_id int REFERENCES employees (id),
title varchar NOT NULL,
url varchar NOT NULL,
salary_from float,
salary_to float
)