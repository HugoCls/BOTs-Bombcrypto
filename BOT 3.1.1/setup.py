from distutils.core import setup
import py2exe

setup(console=['setup_bot.py'])
py2exe.shutil.rmtree('build', ignore_errors=True)