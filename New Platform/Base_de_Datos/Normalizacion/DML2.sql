-- SQLite
INSERT INTO makes (make)
    VALUES 
    ('Honda'),
    ('Chevrolet');

INSERT INTO models (model,make_id,year_id)
    VALUES
    ('Accord',1,1),
    ('CR-V',1,2),
    ('Volt',2,3);

INSERT INTO colors (color)
    VALUES
    ('Silver'),
    ('Blue'),
    ('Red');

INSERT INTO years (year)
    VALUES
    (2003),
    (2014),
    (2015);

INSERT INTO cars (VIN,model_id,color_id)
    VALUES
    ('1HGCM82633A',1,1),
    ('5J6RM4H79EL',2,2),
    ('1G1RA6EH1FU',3,3);

INSERT INTO owners (code,name,phone)
    VALUES
    (101,'Alice',1234567890),
    (102,'Bob',9876543210),
    (103,'Claire',5551234567),
    (104,'Dave',1112223333);

INSERT INTO insurance_companies (company)
    VALUES 
    ('ABC Insurance'),
    ('XYZ Insurance'),
    ('DEF Insurance'),
    ('GHI Insurance');

INSERT INTO insurance_policies (policy,insurance_company_id)
    VALUES
    ('Fire & Theft',1),
    ('Full Cover',2),
    ('Collision',3),
    ('Basic Legal',4);

INSERT INTO car_owner_policy (owner_id,car_id,insurance_policy_id)
    VALUES 
    (1,1,1),
    (2,1,2),
    (3,2,3),
    (4,3,4);