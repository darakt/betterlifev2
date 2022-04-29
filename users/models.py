from django.db import models
from django.contrib.auth.models import AbstractUser

attributeWhiteListed = [
    'id',
    'username',
    'first_name',
    'last_name',
    'email',
    'date_joined',
    'role'
]

def get_owner_for_deleted_comment(): # TODO change name
    return User.objects.get_or_create(id=1)

def get_user_from_id_and_check_role(id, role):
    return User.objects.get(id=id)

def get_users_from_ids(ids):
    users = []
    for id in ids:
        users.append(User.objects.get(id=id))
    return users;

class User(AbstractUser):
    superuser = 1
    organization_admin = 2
    organization_member = 3
    project_owner = 4
    project_member = 5

    roles = (
        (superuser, 'superuser'),
        (organization_admin, 'organization admin'),
        (organization_member, 'organization member'),
        (project_owner, 'project owner'),
        (project_member, 'project member'),
    )
    role = models.PositiveSmallIntegerField(choices=roles, default=5)
    def toJson(self):
        jsonified = {}
        for key in self.__dict__.keys():
            if self.__dict__[key] is not None and key in attributeWhiteListed and self.__dict__[key] != '':
                # print('[{}] = {}'.format(key, self.__dict__[key]))
                jsonified[key] = self.__dict__[key]
        return jsonified
    class Meta:
        permissions = [
            ('can_create_a_superuser', 'can create a super user'),
            ('can_create_an_org_admin', 'can create an org admin'),
            ('can_create_a_project_owner', 'can create an org admin'),
            ('can_create_an_org_member', 'can create an org member'),
            ('can_create_a_project_member', 'can create an project member'),
            ('can_read_user','can read user'), # superuser must be excluded here !!!!!
            ('can_update_user', 'can update user'),
            ('can_delete_user', 'can delete user')
            ]
