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
#     spack install intel-compute-runtime
#
# You can edit this file again by typing:
#
#     spack edit intel-compute-runtime
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class IntelComputeRuntime(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://software.intel.com/content/www/us/en/develop/articles/opencl-drivers.html"
    url      = "https://github.com/intel/compute-runtime/archive/20.24.17065.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('20.24.17065', sha256='49e30c184299a8f65023d4e189ca84a3d24c1a41a95bb9159b0898d916fbc9be')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        spec = self.spec
        options = []
        return options

