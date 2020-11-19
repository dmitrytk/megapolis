from django.contrib.auth.models import (
    BaseUserManager
)


# Кастомный менеджер пользователей
class MyUserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, organization, password=None):
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            organization_id=organization,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, organization, password=None):
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            organization_id=organization,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
