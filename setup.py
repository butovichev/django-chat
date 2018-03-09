from setuptools import setup


setup(
    name='django-chat',
    version='0.1',
    description='',
    classifiers=[
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
    ],
    author='Grigoriy Butovichev',
    author_email='butovichev@yandex.ru',
    url='https://github.com/butovichev/django-chat',
    keywords=['django', 'chat', 'chanels'],
    packages=['django-chat'],
    install_requires=[
        'django',
        'psycopg2',
    ],
)