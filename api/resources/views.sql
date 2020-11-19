DROP VIEW IF EXISTS api_contract_view;
CREATE VIEW api_contract_view AS
SELECT c.id,
       c.number,
       c.content,
       ao.name client,
       ac.name contractor,
       ao.id   client_id,
       ac.id   contractor_id
FROM api_contract c
         JOIN api_organization ao ON ao.id = c.client_id
         JOIN api_organizatiON ac on ac.id = c.contractor_id;