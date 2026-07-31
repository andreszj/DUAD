-- SQLite

CREATE TABLE makes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    make VARCHAR(15) NOT NULL
    );

-- TABLE makes - 1NF: I used 1NF because the table has its own PK, and each record contains unique, individual data

-- DROP TABLE models;

CREATE TABLE models (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    model VARCHAR(15) NOT NULL,
    make_id INT REFERENCES makes(id),
    year_id INT REFERENCES years(id) NOT NULL
    );

-- TABLE models - 3NF: I used 3NF because the table has its own PK, and each record contains FKs that reference related data in the makes and years tables.


CREATE TABLE colors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    color VARCHAR(15) NOT NULL
    );

-- TABLE colors - 1NF: I used 1NF because the table has its own PK, and each record contains unique, individual data

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

-- TABLE owners - 1NF: I used 1NF because the table has its own PK, and each record contains unique, individual data

CREATE TABLE years (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year SMALLINT NOT NULL
    );

-- TABLE years - 1NF: I used 1NF because the table has its own PK, and each record contains unique, individual data

-- DROP TABLE cars;

CREATE TABLE cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    VIN VARCHAR(15) NOT NULL,
    model_id INT REFERENCES models(id) NOT NULL,
    color_id INT REFERENCES colors(id) NOT NULL
    );

-- TABLE cars - 3NF: I used 3NF because the table has its own PK, and each record contains FKs that reference related data in the models and colors tables. Also, models table add more information


-- CREATE TABLE car_owner_insurances (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     owner_id INT REFERENCES owners(id),
--     car_id INT REFERENCES cars(id),
--     insurance_company_id INT REFERENCES insurance_companies(id)
--     );

-- DROP TABLE car_owner_insurances;
-- DROP TABLE insurance_companies;
-- DROP TABLE insurance_policies;

CREATE TABLE insurance_companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company VARCHAR(20) NOT NULL
    );

-- TABLE insurance_companies - 1NF: I used 1NF because the table has its own PK, and each record contains unique, individual data

CREATE TABLE insurance_policies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    policy VARCHAR(20) NOT NULL,
    insurance_company_id INT REFERENCES insurance_companies(id)
    );

-- TABLE insurance_policies - 3NF: I used 3NF because the table has its own PK, and each record contains an FK that references related data in the insurance_companies table


CREATE TABLE car_owner_policy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner_id INT REFERENCES owners(id),
    car_id INT REFERENCES cars(id),
    insurance_policy_id INT REFERENCES insurance_policies(id)
    );

-- TABLE car_owner_policy - 3NF: I used 3NF because the table has its own PK, and each record contains FKs that reference related data in the owners, cars, and insurance_policies tables... reduces data redundancy

