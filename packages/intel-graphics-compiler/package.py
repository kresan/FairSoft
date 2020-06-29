# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install intel-graphics-compiler
#
# You can edit this file again by typing:
#
#     spack edit intel-graphics-compiler
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class IntelGraphicsCompiler(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/intel/intel-graphics-compiler/archive/igc-1.0.4155.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.0.4155', sha256='d5ac4dce02c36be1d15dfc253224bfc47eaf7538b5563a492fd3e4658649f78e')

    # FIXME: Add dependencies if required.
    depends_on('cmake', type='build')
    depends_on('llvm')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
