Download Code
=============

A web application that allows users to download a file using unique download codes.

Usage
=====

Requirements
------------

* flask-wtf
* flask-sqlalchemy

Configuration
-------------

You'll need to create a `config.py` file, which specifies details about the file to
download and the number of times it can be accessed. A sample configuration file can be
found at `sample_config.py`.

For the sake of simplicity, it is recommended that you store the file to be downloaded in
the `download/static/` directory.

Starting the Server
-------------------

Start the server with `run.py`. By default it will be accessible at `localhost:9999`. To
make the server world-accessible or for other options, see `run.py -h`.

If you're having trouble configuring your sever, I wrote a
[blog post](http://blog.spurll.com/2015/02/configuring-flask-uwsgi-and-nginx.html)
explaining how you can get Flask, uWSGI, and Nginx working together.

Creating Download Codes
-----------------------

To create download codes, simply run Python, import the module, and run
`models.create_code`, optionally passing the number of codes you'd like to create (the
default is one):

```python
import download
download.models.create_code(3)
```

The new download codes will be added to the database, displayed on the screen, and
returned (in the form of UUID objects) in case you want to fiddle with them:

```
The following new download codes are available for use:
08B50BA1-8091-47AF-93D4-21E2EF626B86
ED536F30-7553-4DD8-A8EF-E5279260692B
A91A237F-9A0F-459D-8F01-0798D887D68C
```

The codes are case-insensitive, ignore hyphens, and (because they're hexadecimal) treat
the letter `O` as a zero to avoid potential confusion for users.

Bugs and Feature Requests
=========================

Feature Requests
----------------

None

Known Bugs
----------

None

License Information
===================

Written by Gem Newman. [Website](http://spurll.com) | [GitHub](https://github.com/spurll/) | [Twitter](https://twitter.com/spurll)

This work is licensed under Creative Commons [BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).

Remember: [GitHub is not my CV.](https://blog.jcoglan.com/2013/11/15/why-github-is-not-your-cv/)
