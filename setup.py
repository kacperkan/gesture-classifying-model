from setuptools import setup, find_packages

setup(name='gesture_classifying_model',
      version='0.1',
      packages=find_packages(),
      install_requires=['keras==1.2.2',
                        'numpy>=1.11.1',
                        'theano==0.9.0',
                        'tqdm>=4.11.2',
                        'wget>=3.2'],
      author='Kacper Kania',
      author_email='kacper1095@gmail.com',
      description='Classifying model for Sign Language Recognition System',
      license='MIT',
      keywords='sign language classification',
      url='https://github.com/kacper1095/gesture_classifying_model',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
            ]
      )