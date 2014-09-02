#!/usr/bin/env python
#
# Copyright (C) 2010 Linaro Limited
#
# Author: Zygmunt Krynicki <zygmunt.krynicki@linaro.org>
#
# This file is part of linaro-dashboard-bundle.
#
# linaro-dashboard-bundle is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation
#
# linaro-dashboard-bundle is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with linaro-dashboard-bundle.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages


setup(
    name='linaro-dashboard-bundle',
    version=":versiontools:linaro_dashboard_bundle:__version__",
    author = "Linaro Validation Team",
    author_email = "linaro-dev@lists.linaro.org",
    description="Library for manipulating LAVA dashboard bundles",
    packages=find_packages(),
    package_data={
        'linaro_dashboard_bundle': [
            'schemas/*.json',
            'test_documents/*.json',
        ],
    },
    install_requires=[
        'versiontools >= 1.3.1',
        'json-schema-validator >= 2.2',
        'simplejson >= 2.1'],
    setup_requires=['versiontools >= 1.3.1'],
    tests_require=[
        'testtools',
        'testscenarios'],
    url='https://launchpad.net/linaro-python-dashboard-bundle',
    test_suite='linaro_dashboard_bundle.tests',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Testing"],
    zip_safe=True)
