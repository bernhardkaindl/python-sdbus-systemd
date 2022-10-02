# SPDX-License-Identifier: LGPL-2.1-or-later

# Copyright (C) 2022, bernhardkaindl, igo95862

# This file is part of python-sdbus

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
from __future__ import annotations

import pathlib
from setuptools import setup

long_description = pathlib.Path('./README.md').read_text()
setup(
    name='sdbus-systemd',
    description=('Systemd binds for sdbus.'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='1.0.0',
    url='https://github.com/igo95862/python-sdbus',
    author='Bernhard Kaindl',
    author_email='contact@bernhard.kaindl.dev',
    license='LGPL-2.1-or-later',
    keywords='dbus systemd networking linux freedesktop',
    project_urls={
        'Documentation': 'https://python-sdbus-systemd.readthedocs.io/en/latest/',
        'Source': 'https://github.com/bernhardkaindl/python-sdbus-systemd/',
        'Tracker': 'https://github.com/bernhardkaindl/python-sdbus-systemd/issues/',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        (
            'License :: OSI Approved :: '
            'GNU Lesser General Public License v2 or later (LGPLv2+)'
        ),
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=[
        'sdbus_async.systemd',
    ],
    package_data={
        'sdbus_async.systemd': [
            'py.typed',
        ],
    },
    python_requires='>=3.7',
    install_requires=[
        'sdbus>=0.10.2',
    ],
)
