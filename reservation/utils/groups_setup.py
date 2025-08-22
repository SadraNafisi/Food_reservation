
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# myapp/utils/group_setup.py
def _write(stdout, msg, style=None):
    if not stdout:
        return
    if hasattr(stdout, "style") and style:
        stdout.write(style(msg))
    else:
        stdout.write(msg + "\n")


def setup_groups_and_permissions():
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType

    group_permissions = {
        'staffs': [
            {'model': 'food_type', 'permissions': ['add', 'view', 'change', 'delete']},
            {'model': 'item', 'permissions': ['add', 'view', 'change', 'delete']},
            {'model': 'order', 'permissions': ['add', 'view', 'change', 'delete']},
            {'model': 'sub_order', 'permissions': ['add', 'view', 'change', 'delete']},
        ],
        'managers': [
            {'model': 'user', 'permissions': ['add', 'view', 'change', 'delete']},
            {'model': 'food_type', 'permissions': ['add', 'view', 'change', 'delete']},
            {'model': 'item', 'permissions': ['add', 'view', 'change', 'delete']},
            {'model': 'order', 'permissions': ['add', 'view', 'change', 'delete']},
            {'model': 'suborder', 'permissions': ['add', 'view', 'change', 'delete']},
            {'model': 'group', 'permissions': ['add', 'view', 'change', 'delete']},
        ]
    }

    for group_name, models in group_permissions.items():
        group, created = Group.objects.get_or_create(name=group_name)
        if not created:
            postive_answers=('yes','y','yep')
            negative_answers=('no','n','nope')
            while(True):
                choice = input(f"{group_name} already exists! do you want override?\n")
                if choice.lower() in (
                        negative_answers + postive_answers ):

                    break
                else:print(f'{choice} is not a clear answer, asking question again\n')

            if choice in postive_answers:
                print('overriding ...\n')
                group.permissions.clear()
            elif choice in negative_answers:
                print('ignore overridding ...\n')
                continue

        else:
            print(f'Created group: {group_name}')

        for model_data in models:
            model = model_data['model']
            actions = model_data['permissions']

            try:
                content_type = ContentType.objects.get(model=model)
            except ContentType.DoesNotExist:
                continue

            for action in actions:
                codename = f"{action}_{model}"
                try:
                    permission = Permission.objects.get(
                        content_type=content_type,
                        codename=codename
                    )
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    print( f'Permission "{codename}" for model "{model}" not found. Skipping.')
