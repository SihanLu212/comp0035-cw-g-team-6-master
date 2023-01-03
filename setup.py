from setuptools import find_packages, setup

setup(
    name='comp0035-cw-2022-23',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'openpyxl'
    ],
)
