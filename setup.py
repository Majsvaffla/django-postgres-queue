from setuptools import setup


setup(
    name='makavafal-django-postgres-queue',
    version='1.0.1',
    packages=[
        'dpq',
        'dpq.migrations',
        'dpq_scheduler',
        'dpq_scheduler.migrations',
    ],
    license='BSD',
    long_description=open('README.rst').read(),
    author="David Svenson",
    author_email="davidsvenson@outlook.com",
    url="https://github.com/majsvaffla/django-postgres-queue",
    install_requires=[
        'Django>=1.11',
    ]
)
