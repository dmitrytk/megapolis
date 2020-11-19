from django.db import IntegrityError
from django.db.models import Q
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

from api.models import ContractView, Employee, ContractEmployee, Contract
from api.queries import CONTRACT_EMPLOYEE_QUERY
from api.serializers import ContractViewSerializer, EmployeeSerializer

# Пользователи имеющие доступ к договорам
PERMITTED_POSITIONS = ['EXECUTIVE', 'MANAGER']


# Все контракты
@api_view(['GET'])
def contracts(request):
    current_user = request.user
    print(current_user)
    contracts = ContractView.objects.all().filter(
        Q(contractor_id=current_user.organization_id) | Q(client_id=current_user.organization_id))
    serializer = ContractViewSerializer(contracts, many=True)
    return JsonResponse(serializer.data, safe=False)


# Данные контракта
@api_view(['GET'])
def contract_detail(request, pk):
    current_user = request.user
    # Должность по контракту
    user_contract_position = get_object_or_404(ContractEmployee, contract_id=pk, employee_id=current_user.id).position
    contract = ContractView.objects.get(pk=pk)
    if contract.client_id == current_user.organization_id or contract.contractor_id == current_user.organization_id:
        if user_contract_position in PERMITTED_POSITIONS:
            serializer = ContractViewSerializer(contract)
            return JsonResponse(serializer.data)
    return JsonResponse({'message': 'Отказано в доступе'}, status=status.HTTP_403_FORBIDDEN)


# Работники по контракту
@api_view(['GET', 'POST'])
def contract_employees(request, pk):
    current_user = request.user
    # Должность по контракту
    user_contract_position = get_object_or_404(ContractEmployee, contract_id=pk, employee_id=current_user.id).position
    if request.method == 'GET':
        if user_contract_position not in PERMITTED_POSITIONS:
            return JsonResponse({'message': 'Отказано в доступе'}, status=status.HTTP_403_FORBIDDEN)
        employees = Employee.objects.raw(CONTRACT_EMPLOYEE_QUERY,
                                         {'contract_id': pk, 'organization_id': current_user.organization_id})
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        if user_contract_position not in PERMITTED_POSITIONS:
            return JsonResponse({'message': 'Отказано в доступе'}, status=status.HTTP_403_FORBIDDEN)
        employee_id = request.data['employee_id']
        print(employee_id)
        contract = get_object_or_404(Contract, pk=pk)
        print(contract)
        employee = get_object_or_404(Employee, pk=employee_id)
        print(employee_id)
        try:
            ContractEmployee.objects.create(contract=contract, employee=employee, position='SENIOR')
            return JsonResponse({'message': 'Пользователь добавлен в контракт'}, status=status.HTTP_200_OK)
        except IntegrityError as e:
            return JsonResponse({'message': 'Пользователь уже существует в данном контракте'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Удалить работника из контракта
@api_view(['DELETE'])
def delete_contract_employee(request, contract_id, employee_id):
    current_user = request.user
    # Должность по контракту
    user_contract_position = get_object_or_404(ContractEmployee, contract_id=contract_id,
                                               employee_id=current_user.id).position
    if user_contract_position not in PERMITTED_POSITIONS:
        return JsonResponse({'message': 'Отказано в доступе'}, status=status.HTTP_403_FORBIDDEN)
    contract_employee = ContractEmployee.objects.get(contract_id=contract_id,
                                                     employee_id=employee_id)
    try:
        contract_employee.delete()
        return JsonResponse({'message': 'Пользователь удален из договора'}, status=status.HTTP_200_OK)
    except IntegrityError as e:
        return JsonResponse({'message': 'Ошибка удаления пользователя'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Работники организации
@api_view(['GET'])
def organization_employees(request, pk):
    current_user = request.user
    if current_user.organization_id != pk or current_user.position not in PERMITTED_POSITIONS:
        return JsonResponse({'message': 'Отказано в доступе'}, status=status.HTTP_403_FORBIDDEN)
    employees = Employee.objects.filter(Q(organization_id=current_user.organization_id), Q(organization_id=pk))
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)
