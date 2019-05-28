import os
import random
from jinja2 import Template


DEFAULT_PROJECT_NAME = 'django_project'
# PROJECT_SLUG = input('Enter your project\'s slug: ')
# PROJECT_NAME = input('Enter your project\'s name: ')

# Refresh all SECRET_KEYs in the settings files
# Use this snippet: https://gist.github.com/ndarville/3452907
def generate_secret_keys():
    setting_file = open('%s/main/settings/local.py' % DEFAULT_PROJECT_NAME, mode='r')
    template = Template(setting_file.read())
    setting_file.close()

    context = {
        'secret_key': ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])}

    content = template.render(context) + '\n'

    setting_file = open('%s/main/settings/local.py' % DEFAULT_PROJECT_NAME, mode='w')
    setting_file.write(content)
    setting_file.close()


# Replace "{{django_project}}" with the project name from production.yml and local.yml

# Replace "{{django_project}}" with the project name evereywhere

# Create .env file with:

# Rename the "django_project" folder name
def rename_project_folder():
    os.rename('django_project', PROJECT_SLUG)


def main():
    generate_secret_keys()
    # rename_project_folder()


if __name__ == '__main__':
    main()