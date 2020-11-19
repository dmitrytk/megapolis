INSERT INTO api_organization(name, type, location)
VALUES ('Client', 'OAO', 'Moscow'),
       ('Contractor', 'OOO', 'Tyumen');

INSERT INTO api_contract(number, content, client_id, contractor_id)
VALUES ('N425-2020', 'Contract data', 1, 2),
       ('N426-2020', 'Another Contract data', 1, 2);

-- INSERT INTO api_employee(first_name, last_name, position, organization_id)
-- VALUES ('Ivan', 'Ivanov', 'executive', 1),
--        ('Petrov', 'Pert', 'manager', 1),
--        ('Dmitry', 'Anisimov', 'executive', 2),
--        ('Alexei', 'Sidorov', 'manager', 2);

INSERT INTO api_contractemployee(contract_id, employee_id)
VALUES (1, 1),
       (1, 2),
       (1, 3),
       (1, 4);

