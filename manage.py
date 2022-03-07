#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

print('\r\n')
print("Hey programmer ===> ")
print("set DJANGO_ENV='mysite.settings.dev' or 'mysite.settings.prod'")
print("once at the beginning of your session.")
print('\r\n')

def main():
    """Run administrative tasks."""
    django_env = os.environ['DJANGO_ENV']
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', django_env)

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
