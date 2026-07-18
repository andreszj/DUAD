-- SQLite

-- CREATE TABLE makes (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     make VARCHAR(15) NOT NULL
--     );

-- CREATE TABLE models (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     model VARCHAR(15) NOT NULL,
--     make_id INT REFERENCES makes(id)
--     );

-- CREATE TABLE colors (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     color VARCHAR(15) NOT NULL
--     );

-- CREATE TABLE VINs (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     VIN VARCHAR(15) NOT NULL,
--     model_id INT REFERENCES models(id) NOT NULL,
--     color_id INT REFERENCES colors(id) NOT NULL,
--     year SMALLINT NOT NULL
--     );

-- CREATE TABLE insurance_policies (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     policy VARCHAR(20) NOT NULL
--     );

-- DROP TABLE insurance_policies;
-- CREATE TABLE insurance_companies (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     company VARCHAR(20) NOT NULL
--     );

-- DROP TABLE insurance_companies;

-- CREATE TABLE insurance_companies (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     company VARCHAR(20) NOT NULL,
--     policy VARCHAR(20) NOT NULL
--     );

-- CREATE TABLE owners (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     code SMALLINT NOT NULL,
--     name VARCHAR(25) NOT NULL,
--     phone INT NOT NULL
--     );

-- CREATE TABLE cars (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     owner_id INT REFERENCES owners(id),
--     VIN_id INT REFERENCES VINs(id),
--     insurance_company_id INT REFERENCES insurance_companies(id),
--     insurance_policy_id INT REFERENCES insurance_policies(id)
--     );

-- DROP TABLE cars;
-- DROP TABLE VINs;
-- DROP TABLE owners;

CREATE TABLE owners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code SMALLINT NOT NULL,
    name VARCHAR(25) NOT NULL,
    phone VARCHAR(20) NOT NULL
    );

CREATE TABLE cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    VIN VARCHAR(15) NOT NULL,
    model_id INT REFERENCES models(id) NOT NULL,
    color_id INT REFERENCES colors(id) NOT NULL,
    year SMALLINT NOT NULL
    );

CREATE TABLE car_owner_insurances (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INT REFERENCES owners(id),
    car_id INT REFERENCES cars(id),
    insurance_company_id INT REFERENCES insurance_companies(id)
    );
