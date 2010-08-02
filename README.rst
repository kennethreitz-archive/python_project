Example
=======

This is an example Python project.

Example Usage
-------------

::

    from gistapi import Gist, Gists

    gist = Gist('d4507e882a07ac6f9f92')
    gist.description   # 'Example Gist for gist.py'
    gist.files         # {'exampleFile': 'Example file content.', 'exampleEmptyFile': ''} 


Installation
------------

	pip install example
	
Or, if you must: 

	easy_install example
	

Roadmap
-------

* List of various project goals
	- Token based Authentication
* Possibly use other hacks in the meantime
* Possibly add nicer command line interface

