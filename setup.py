from setuptools import setup, find_packages

setup(
    name='Flask-Discussion',
    version='0.1.0',

    description='Comment system integration for Flask applications',
    long_description='',

    url='https://github.com/rmed/flask-discussion',

    author='Rafael Medina García',
    author_email='rafamedgar@gmail.com',

    license='MIT',

    classifiers=[],

    keywords='flask discussion comments commenting',

    packages=find_packages(),

    include_package_data=True,

    zip_safe=False,

    install_requires=[
        'Flask>=1.1.1',
    ]
)
