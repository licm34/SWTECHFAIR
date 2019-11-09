from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)

class UserManager(BaseUserManager):
    def create_user(self,UserName,CardId,password=None):
        if not UserName:
            raise ValueError('학번을 입력해주세요')

        user = self.model(
            UserName=UserName,
            CardId = CardId,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,UserName,CardId,password):
        user = self.create_user(
            UserName=UserName,
            CardId=CardId,
            password=password,
        )

        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    UserName = models.CharField(max_length=8,blank=False,unique=True)
    CardId = models.CharField(max_length=12,null=True,blank=True)
    Penalty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'UserName'
    REQUIRED_FIELDS = ['CardId',]

    def __str__(self):
        return self.UserName

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin