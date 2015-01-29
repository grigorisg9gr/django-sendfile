#!/usr/bin/env python
from __future__ import absolute_import
import sys, os
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
#from django.core.management import execute_manager
#try:
#    from . import settings  # Assumed to be in the same directory.
#except ImportError:
#    import sys
#    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
#    sys.exit(1)
#from django.core.management import execute_from_command_line
#if __name__ == "__main__":
#    execute_manager(settings)
#    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


