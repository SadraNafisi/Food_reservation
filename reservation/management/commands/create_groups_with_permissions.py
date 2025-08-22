from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from reservation.utils.groups_setup import setup_groups_and_permissions


class Command(BaseCommand):
    help = 'Creates staff and manager groups with configured permissions'

    def handle(self, *args, **options):
        setup_groups_and_permissions()
        # # Define permissions for each group
        # group_permissions = {
        #     'staffs': [
        #         {'model': 'food_type', 'permissions': ['add', 'view', 'change', 'delete']},
        #         {'model': 'item', 'permissions': ['add', 'view', 'change', 'delete']},
        #         {'model': 'order', 'permissions': ['add', 'view', 'change', 'delete']},
        #         {'model': 'sub_order', 'permissions': ['add', 'view', 'change', 'delete']},
        #     ],
        #     'managers': [
        #         {'model': 'user', 'permissions': ['add', 'view', 'change', 'delete']},
        #         {'model': 'food_type', 'permissions': ['add', 'view', 'change', 'delete']},
        #         {'model': 'item', 'permissions': ['add', 'view', 'change', 'delete']},
        #         {'model': 'order', 'permissions': ['add', 'view', 'change', 'delete']},
        #         {'model': 'suborder', 'permissions': ['add', 'view', 'change', 'delete']},
        #         {'model': 'group', 'permissions': ['add', 'view', 'change', 'delete']}
        #     ]
        # }
        #
        # for group_name, models in group_permissions.items():
        #     group, created = Group.objects.get_or_create(name=group_name)
        #
        #     if created:
        #         self.stdout.write(self.style.SUCCESS(f'Created group: {group_name}'))
        #     else:
        #         self.stdout.write(self.style.WARNING(f'Group "{group_name}" already exists - updating permissions'))
        #
        #     # Clear existing permissions (optional - comment this out if you want to keep existing permissions)
        #     group.permissions.clear()
        #
        #     # Add new permissions
        #     for model_data in models:
        #         model = model_data['model']
        #         codenames_actions = model_data['permissions']
        #
        #         content_type = ContentType.objects.get(model=model)
        #         for codename_action in codenames_actions:
        #             codename=f"{codename_action}_{model}"
        #             try:
        #                 permission = Permission.objects.get(
        #                     content_type=content_type,
        #                     codename=codename
        #                 )
        #                 group.permissions.add(permission)
        #             except Permission.DoesNotExist:
        #                 self.stdout.write(self.style.ERROR(
        #                     f'Permission "{codename}" for model "{model}" not found. Skipping.'
        #                 ))
        #
        #     self.stdout.write(self.style.SUCCESS(
        #         f'Successfully configured {len(group.permissions.all())} permissions for {group_name}'
        #     ))
