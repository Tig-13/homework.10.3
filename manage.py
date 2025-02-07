#!/usr/bin/env python
import os
import sys

def main():
    """Main entry point for the Django manage commands."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH environment."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
