import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name='ci_testing',
        version="alpha",
        description='A repository for CI testing.',
        author='MolSSI',
        author_email='tbarnes1@vt.edu',
        url="https://github.com/taylor-a-barnes/ci_testing",
        license='BSD-3C',
        packages=setuptools.find_packages(),
        extras_require={
            'tests': [
                'pytest',
                'pytest-cov',
                'pytest-pep8',
                'tox',
            ],
        },

        tests_require=[
            'pytest',
            'pytest-cov',
            'pytest-pep8',
            'tox',
        ],

        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
        ],
        zip_safe=True,
    )
