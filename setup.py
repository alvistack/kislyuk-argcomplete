# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='argcomplete',
    version='3.5.3',
    description='Bash tab completion for argparse',
    author='Andrey Kislyuk',
    author_email='kislyuk@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Shells',
        'Topic :: Terminals',
    ],
    extras_require={
        'test': [
            'coverage',
            'mypy',
            'pexpect',
            'ruff',
            'wheel',
        ],
    },
    entry_points={
        'console_scripts': [
            'activate-global-python-argcomplete = argcomplete.scripts.activate_global_python_argcomplete:main',
            'python-argcomplete-check-easy-install-script = argcomplete.scripts.python_argcomplete_check_easy_install_script:main',
            'register-python-argcomplete = argcomplete.scripts.register_python_argcomplete:main',
        ],
    },
    packages=[
        'argcomplete',
        'argcomplete.packages',
        'argcomplete.scripts',
    ],
)
