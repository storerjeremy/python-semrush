#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import find_packages, setup
    from setuptools.command.test import test

    is_setuptools = True
except ImportError:
    raise
    from ez_setup import use_setuptools

    use_setuptools()
    from setuptools import find_packages, setup  # noqa
    from setuptools.command.test import test  # noqa

    is_setuptools = False

import codecs
import os
import sys

NAME = "pyrush"
entrypoints = {}
extra = {}

# -*- Classifiers -*-

classes = """
    Development Status :: 4 - Beta
    License :: OSI Approved :: MIT License
    Topic :: System :: Distributed Computing
    Topic :: Software Development :: Object Brokering
    Intended Audience :: Developers
    Programming Language :: Python
    Programming Language :: Python :: 2
    Programming Language :: Python :: 2.6
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.3
    Programming Language :: Python :: 3.4
    Programming Language :: Python :: Implementation :: CPython
    Programming Language :: Python :: Implementation :: PyPy
    Operating System :: OS Independent
    Operating System :: POSIX
    Operating System :: Microsoft :: Windows
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split("\n") if s]

# -*- Distribution Meta -*-

import re

re_meta = re.compile(r"__(\w+?)__\s*=\s*(.*)")
re_vers = re.compile(r"VERSION\s*=.*?\((.*?)\)")
re_doc = re.compile(r'^"""(.+?)"""')
rq = lambda s: s.strip("\"'")


def add_default(m):
    attr_name, attr_value = m.groups()
    return ((attr_name, rq(attr_value)),)


def add_version(m):
    v = list(map(rq, m.groups()[0].split(", ")))
    return (("VERSION", ".".join(v[0:3]) + "".join(v[3:])),)


def add_doc(m):
    return (("doc", m.groups()[0]),)


pats = {re_meta: add_default, re_vers: add_version, re_doc: add_doc}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "pyrush/__init__.py")) as meta_fh:
    meta = {}
    for line in meta_fh:
        if line.strip() == "# -eof meta-":
            break
        for pattern, handler in pats.items():
            m = pattern.match(line.strip())
            if m:
                meta.update(handler(m))

# -*- Installation Requires -*-

py_version = sys.version_info


def strip_comments(l):
    return l.split("#", 1)[0].strip()


def reqs(*f):
    return [
        r
        for r in (
            strip_comments(l)
            for l in open(os.path.join(os.getcwd(), "requirements", *f)).readlines()
        )
        if r
    ]


install_requires = reqs("default.txt")

# -*- Tests Requires -*-

tests_require = reqs("test.txt")

# -*- Entry Points -*- #

# -*- %%% -*-

setup(
    name=NAME,
    version=meta["VERSION"],
    description=meta["doc"],
    author=meta["author"],
    author_email=meta["contact"],
    url=meta["homepage"],
    platforms=["any"],
    license="MIT",
    packages=find_packages(exclude=["tests", "tests.*"]),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite="nose.collector",
    classifiers=classifiers,
    entry_points=entrypoints,
    long_description=long_description,
)
