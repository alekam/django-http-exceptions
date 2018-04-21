from setuptools import setup, find_packages

version = __import__('http_exceptions').get_version()


def get_requires_list(filename):
    s = open(filename).read().split("\n")
    dependenses = []
    if len(s):
        for pkg in s:
            if pkg.strip() == '' or pkg.startswith("#"):
                continue
            if pkg.startswith("-e"):
                continue
                try:
                    p = pkg.split("#egg=")[1]
                    dependenses += [p, ]
                except:
                    continue
            else:
                dependenses += [pkg, ]
    return dependenses


setup(
    name = 'django-http-exceptions',
    version = version,
    description = "Process HTTP exceptions raised in Dajngo Views",
    long_description = open('README.md').read(),
    keywords='django exceptions middleware',
    url = 'https://github.com/alekam/django-http-exceptions',
    license = 'Private',
    platforms = ['any'],
    classifiers = ['Development Status :: 0 - Alfa',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requires_list('requirements.txt'),
)
