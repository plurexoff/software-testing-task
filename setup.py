from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='software-testing-task',
    version='1.0.0',
    description='Тестирование ПО на Python с pytest',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='plurexoff',
    author_email='sanso1737@gmail.com',
    url='https://github.com/plurexoff/software-testing-task',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'pytest>=7.0.0',
        'pytest-cov>=4.0.0',
        'pytest-mock>=3.10.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='testing pytest unit-testing integration-testing',
)
