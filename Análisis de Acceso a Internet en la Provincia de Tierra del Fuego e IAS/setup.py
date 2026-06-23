from setuptools import find_packages, setup

setup(
    name='acceso a internet',
    packages=find_packages(),
    version='0.1.0',
    description='Análisis y predicción al acceso de internet',
    author='Marcelo Adrian Cussi',
    license='MIT',
    install_requires=[
        # Lista de dependencias del proyecto
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn'
    ],
    classifiers=[
        # Clasificadores que ayudan a otros usuarios a encontrar tu paquete
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.11.1',
)
