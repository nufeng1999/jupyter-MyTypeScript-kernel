from setuptools import setup

setup(name='jupyter_MyTypeScript_kernel',
      version='0.0.1',
      description='Minimalistic Nodejs kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyTypeScript-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyTypeScript-kernel/tarball/0.0.1',
      packages=['jupyter_MyTypeScript_kernel'],
      scripts=['jupyter_MyTypeScript_kernel/install_MyTypeScript_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'TypeScript','ts'],
      include_package_data=True
      )
