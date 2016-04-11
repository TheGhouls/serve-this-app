from setuptools import setup

setup(
    name='serve-this-app',
    version='0.1',
    author='TheGhouls',
    author_email='manu.valette@gmail.com',
    packages=['serve_this_app'],
    description="very simple tool to serve web app from any port",
    url='https://github.com/TheGhouls/serve_this_app',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={'console_scripts': [
        'serve-this-app = serve_this_app.serve_this_app:main'
    ]},
)
