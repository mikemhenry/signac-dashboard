#!/usr/bin/env python3
# Copyright (c) 2018 The Regents of the University of Michigan
# All rights reserved.
# This software is licensed under the BSD 3-Clause License.
from signac_dashboard import Dashboard
from signac import init_project

if __name__ == '__main__':
    project = init_project('dashboard-test-project')
    for a in range(10):
        for b in range(10):
            project.open_job({'a': a, 'b': b}).init()
    Dashboard().main()
