from distutils.core import setup
import py2exe

setup(windows=[{"script":"Main.py"}],
	options={
		"py2exe":{
			"includes":["sip", "PyQt4.QtCore","PyQt4.QtGui","PyQt4.QtNetwork", "lxml", "lxml.etree", "lxml._elementpath", "gzip", "configobj"],
			"compressed":True,
			"optimize":2
		}
	},
	name="AccountEnet",
	author="Juan Daniel Santana Rodes",
	author_email="juandanielsantana@gmail.com"
)
