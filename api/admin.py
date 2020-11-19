from django.contrib import admin

from api.models import Organization, Employee, Contract, ContractEmployee

admin.site.register(Employee)
admin.site.register(Organization)
admin.site.register(Contract)
admin.site.register(ContractEmployee)
