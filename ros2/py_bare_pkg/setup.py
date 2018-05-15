from setuptools import find_packages
from setuptools import setup

package_name = 'pkg_name'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Vincent Rousseau',
    author_email='vincent.rousseau@irstea.fr',
    maintainer='Vincent Rousseau',
    maintainer_email='vincent.rousseau@irstea.fr',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'Python nodes'
        'description'
    ),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = scripts.talker:main',
        ],
    },
)
