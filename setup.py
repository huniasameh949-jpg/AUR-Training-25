from setuptools import find_packages, setup

package_name = 'turtlenew_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch',['launch/turtle_chase_launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='huniasameh949-jpg',
    maintainer_email='huniasameh949@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtle_chase=turtlenew_pkg.turtle_chase:main'
        ],
    },
)
