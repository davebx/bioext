#!/usr/bin/env python

from __future__ import division, print_function

import os.path
import numpy

from setuptools import Extension, setup

from BioExt import __version__ as _bioext_version
from BioExt.references._factory import _installrefdirs


np_inc = [os.path.join(os.path.dirname(numpy.__file__), 'core', 'include')]

ext_modules = [
    Extension(
        'BioExt.aligner._align',
        sources=[
            os.path.join('BioExt', 'aligner', '_align.c'),
            os.path.join('BioExt', 'aligner', 'alignment.c')
            ],
        include_dirs=np_inc,
        libraries=['m'],
        extra_compile_args=['-O3']
        )
    ]


setup(
    name='bioext',
    version=_bioext_version,
    description='Misc utilities and definitions not included or hidden in BioPython',
    author='N Lance Hepler',
    author_email='nlhepler@gmail.com',
    url='http://github.com/nlhepler/bioext',
    license='GNU GPL version 3',
    packages=[
        'BioExt',
        'BioExt.aligner',
        'BioExt.collections',
        'BioExt.errorize',
        'BioExt.io',
        'BioExt.io.BamIO',
        'BioExt.io.LazyAlignIO',
        'BioExt.io.SamIO',
        'BioExt.joblib',
        'BioExt.misc',
        'BioExt.orflist',
        'BioExt.phylo',
        'BioExt.references',
        'BioExt.scorematrix',
        'BioExt.stats',
        'BioExt.uds',
        'BioExt.untranslate'
        ],
    package_dir={
        'BioExt': 'BioExt',
        'BioExt.aligner': 'BioExt/aligner',
        'BioExt.collections': 'BioExt/collections',
        'BioExt.errorize': 'BioExt/errorize',
        'BioExt.io': 'BioExt/io',
        'BioExt.io.BamIO': 'BioExt/io/BamIO',
        'BioExt.io.LazyAlignIO': 'BioExt/io/LazyAlignIO',
        'BioExt.io.SamIO': 'BioExt/io/SamIO',
        'BioExt.joblib': 'BioExt/joblib',
        'BioExt.misc': 'BioExt/misc',
        'BioExt.orflist': 'BioExt/orflist',
        'BioExt.phylo': 'BioExt/phylo',
        'BioExt.references': 'BioExt/references',
        'BioExt.scorematrix': 'BioExt/scorematrix',
        'BioExt.stats': 'BioExt/stats',
        'BioExt.uds': 'BioExt/uds',
        'BioExt.untranslate': 'BioExt/untranslate'
        },
    package_data={
        'BioExt': [
            'data/scorematrices/*.txt'
            ] + _installrefdirs
        },
    scripts=[
        'scripts/bealign',
        'scripts/bam2msa'
        ],
    ext_modules=ext_modules,
    requires=[
        'Bio (>=1.58)',
        'numpy (>=1.6)',
        ]
    )
