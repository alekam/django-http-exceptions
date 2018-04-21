#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner


def main():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
    django.setup()

    options = {}
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-v', '--verbosity']:
            options = {'verbosity': int(sys.argv[2])}

    TestRunner = get_runner(settings)
    test_runner = TestRunner(**options)
    failures = test_runner.run_tests(["tests"])

    sys.exit(bool(failures))


if __name__ == '__main__':
    main()
