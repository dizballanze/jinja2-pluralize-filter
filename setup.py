from distutils.core import setup

setup(
    name='jinja2-pluralize-filter',
    version='0.0.1',
    author='Yuri Shikanov',
    author_email='dizballanze@gmail.com',
    packages=['pluralize'],
    # scripts=[],
    url='https://github.com/dizballanze/jinja2-pluralize-filter',
    license='LICENSE',
    description='Simple jinja2 filter to choose correct plural form for Russian language.',
    long_description=open('README.rest').read(),
    install_requires=[
        "pytils == 0.2.3",
    ],
)