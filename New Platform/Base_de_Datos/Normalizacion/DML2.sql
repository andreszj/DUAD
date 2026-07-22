-- SQLite
-- INSERT INTO makes (make)
--     VALUES 
--     ('Honda'),
--     ('Chevrolet');

-- INSERT INTO models (model,make_id)
--     VALUES
--     ('Accord',1),
--     ('CR-V',1),
--     ('Volt',2);

-- INSERT INTO colors (color)
--     VALUES
--     ('Silver'),
--     ('Blue'),
--     ('Red');

-- INSERT INTO VINs (VIN,model_id,color_id,year)
--     VALUES
--     ('1HGCM82633A',1,1,2003),
--     ('5J6RM4H79EL',2,2,2014),
--     ('1G1RA6EH1FU',3,3,2015);

-- INSERT INTO insurance_policies (policy)
--     VALUES
--     ('Fire & Theft'),
--     ('Full Cover'),
--     ('Collision'),
--     ('Basic Legal');

-- INSERT INTO insurance_companies (company, policy)
--     VALUES 
--     ('ABC Insurance', 'Fire & Theft'),
--     ('XYZ Insurance', 'Full Cover'),
--     ('DEF Insurance', 'Collision'),
--     ('GHI Insurance', 'Basic Legal');

-- INSERT INTO owners (code,name,phone)
--     VALUES
--     (101,'Alice',1234567890),
--     (102,'Bob',9876543210),
--     (103,'Claire',5551234567),
--     (104,'Dave',1112223333);

-- INSERT INTO cars (owner_id,VIN_id,insurance_company_id,insurance_policy_id)
--     VALUES 
--     (1,1,1,1),
--     (2,1,2,2),
--     (3,2,3,3),
--     (4,3,4,4);

-- INSERT INTO cars (VIN,model_id,color_id,year)
--     VALUES
--     ('1HGCM82633A',1,1,2003),
--     ('5J6RM4H79EL',2,2,2014),
--     ('1G1RA6EH1FU',3,3,2015);

-- INSERT INTO owners (code,name,phone)
--     VALUES
--     (101,'Alice',1234567890),
--     (102,'Bob',9876543210),
--     (103,'Claire',5551234567),
--     (104,'Dave',1112223333);

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


