from setuptools import find_packages, setup

package_name = 'deneme1_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='meren',
    maintainer_email='merenbasol@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "calistirA = deneme1_pkg.a:main",
            "kamp_kontrol = deneme1_pkg.kamp_kontrol:main",
            "srv_deneme = deneme1_pkg.srv_deneme:main",
            "client_deneme = deneme1_pkg.client_deneme:main"

        ],
    },
)
