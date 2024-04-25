from setuptools import setup, find_packages

setup(
    name='dummy_payment',
    version='0.1',
    packages=find_packages(),
    description='A payment processing library for demonstration purposes.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
)
