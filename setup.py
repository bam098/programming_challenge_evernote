try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description' : 'project to solve the evernote challenges',
  'author' : 'bam098',
  'url' : 'https://github.com/bam098/evernote_challenges',
  'download_url' : 'https://github.com/bam098/evernote_challenges/archive/master.zip',
  'author_email' : 'daniel.lehmann85@hotmail.com',
  'version' : '0.1',
  'install_requires' : ['nose'],
  'packages' : ['tools'],
  'scripts' : [],
  'name' : 'evernote_challenges'
}

setup(**config)
