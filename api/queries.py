# Поиск сотрудников по договору
CONTRACT_EMPLOYEE_QUERY = """
select contract.id contract_id,
       contract.number number,
       employee.id id,
       employee.first_name first_name,
       employee.last_name last_name,
       employee.position postion
from api_contract contract
         join api_contractemployee ce on contract.id = ce.contract_id
         join api_employee employee on ce.employee_id = employee.id
where contract.id = %(contract_id)s and employee.organization_id = %(organization_id)s;
"""
