from setuptools import setup, find_packages


attrs = dict(
    name='tkterminal',
    version='0.1.0.b1',
    packages=find_packages(),
    description='Terminal widget for Tkinter library.',
    author='Saad Mairaj',
    author_email='Saadmairaj@yahoo.in',
    url='https://github.com/Saadmairaj/tkterminal',
    license='Apache',
    keywords=[
        'tkinter',
        'terminal',
        'subprocess',
        'tkinter-widget',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
        'Documentation': 'https://github.com/Saadmairaj/tkterminal#documentation',
        'Bug Report': 'https://github.com/Saadmairaj/tkterminal/issues',
    },
    include_package_data_info=True,
)

setup(**attrs)
