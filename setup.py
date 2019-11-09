from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='Flask-Discussion',
    version='0.1.0',

    description='Comment system integration for Flask applications',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/rmed/flask-discussion',

    author='Rafael Medina García',
    author_email='rafamedgar@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python'
    ],

    keywords='flask discussion comments commenting',

    packages=find_packages(),

    include_package_data=True,

    install_requires=[
        'Flask>=1.1.1',
    ]
)
