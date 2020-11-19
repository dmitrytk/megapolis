from django.urls import path

from api.views import contracts, contract_detail, contract_employees, organization_employees, delete_contract_employee
from api.views_auth import user, authenticate_user

urlpatterns = [
    path('auth/user', user, name='user'),
    path('auth/login', authenticate_user, name='authenticate_user'),
    path('contracts/', contracts, name='contracts'),
    path('contracts/<int:pk>', contract_detail, name='contract_detail'),
    path('contracts/<int:pk>/employees', contract_employees, name='contract_employees'),
    path('contracts/<int:contract_id>/employees/<int:employee_id>', delete_contract_employee,
         name='delete_contract_employees'),
    path('organizations/<int:pk>/employees', organization_employees, name='organization_employees'),
]
