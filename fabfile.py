# -*- coding: utf-8 -*-

""" Example Fabfile, for project-related tasks.
"""


from fabric.api import *



def task():
	"""Some random project-related task"""

	print('Example task executed.')


def scrub():
	"""Death to the bytecode!"""

	local("rm -fr dist build")
	local("find . -name \"*.pyc\" -exec rm '{}' ';'")
