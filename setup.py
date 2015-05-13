from distutils.core import setup

add_keywords = dict(
    entry_points = {
        'console_scripts': ['powerclone = powerclone.main:main'],
    },
)

fhan = open('requirements.txt', 'rU')
requires = [line.strip() for line in fhan.readlines()]
fhan.close()
#print('We require: ', requires)
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    fhan = open('README.txt')
    long_description = fhan.read()
    fhan.close()

setup(
        name='PowerClone',
        description='PowerClone helps you clone all repos of an organisation on github',
        version='0.0.1',
        packages=['powerclone'],
        license='GPLv3+',
        author='Shubham Chaudhary',
        author_email='me@shubhamchaudhary.in',
        url='https://github.com/shubhamchaudhary/PowerClone',
        long_description=long_description,
        install_requires=requires,
        **add_keywords
)

