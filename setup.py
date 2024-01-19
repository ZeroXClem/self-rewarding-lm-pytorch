from setuptools import setup, find_packages

setup(
  name = 'self-rewarding-lm-pytorch',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'Self Rewarding LM - Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/self-rewarding-lm-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'self rewarding',
    'direct preference optimization'
  ],
  install_requires=[
    'einops>=0.7.0',
    'torch>=2.0'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)