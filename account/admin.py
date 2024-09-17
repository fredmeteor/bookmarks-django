from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import Group, Permission




@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']

# # Create a new group for managers
# manager_group, created = Group.objects.get_or_create(name='Manager')

# # Assign permissions to the manager group
# permissions = Permission.objects.filter(codename__in=['add_user', 'change_user', 'delete_user'])
# manager_group.permissions.add(*permissions)


# # Create a new group for managers
# manager_group, created = Group.objects.get_or_create(name='Manager')

# # Assign permissions to the manager group
# permissions = Permission.objects.filter(codename__in=['add_user', 'change_user', 'delete_user'])
# manager_group.permissions.add(*permissions)

# # Assign a user to the manager group
# #user = User.objects.get(username='hp')
# user.groups.add(manager_group)
