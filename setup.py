from setuptools import setup, find_packages


def get_long_description(path):
    """Opens and fetches text of long descrition file."""
    with open(path, 'r') as f:
        text = f.read()
    return text


attrs = dict(
    name='tkterminal',
    version='0.1.0',
    packages=find_packages(),
    long_description=get_long_description('README.md'),
    description='Terminal widget for Tkinter library.',
    long_description_content_type='text/markdown',
    author='Saad Mairaj',
    author_email='Saadmairaj@yahoo.in',
    url='https://github.com/Saadmairaj/tkterminal',
    license='Apache',
    keywords=[
        'tkinter',
        'terminal',
        'subprocess',
        'tkinter-widget',
        'shell',
        'bash/sh',
        'bash',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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
