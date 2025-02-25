from setuptools import setup, find_packages

setup(
    name='praytimes',
    version='0.1.0',  # Or whatever version you want
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here, if any. For example:
        # 'requests>=2.20.0',
    ],
    author='Abdelouahab B.', #or whatever the author is
    author_email='your_email@example.com', # add an email address
    description='A Python library for calculating prayer times.',
    long_description=open('README.md').read(), #if a README file exists
    long_description_content_type='text/markdown', #if the README is markdown
    url='https://github.com/abdelouahabb/praytimes',
    classifiers=[
        'Development Status :: 3 - Alpha',  # Or other status
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License', # or whatever license
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.6', #or your minimum python version
)
