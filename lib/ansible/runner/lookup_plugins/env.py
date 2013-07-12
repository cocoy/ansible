# (c) 2012, Jan-Piet Mens <jpmens(at)gmail.com>
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

from ansible import utils, errors
import os

class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

<<<<<<< HEAD
    def run(self, terms, **kwargs):
<<<<<<< HEAD

        var = terms.split()[0]
        return os.getenv(var, '')
=======
=======
    def run(self, terms, inject=None, **kwargs):

        terms = utils.listify_lookup_plugin_terms(terms, self.basedir, inject) 

>>>>>>> fba1f7ef4288ac4cf4b35e5f0dee908ae081ce25
        if isinstance(terms, basestring):
            terms = [ terms ]

        ret = []
        for term in terms:
            var = term.split()[0]
            ret.append(os.getenv(var, ''))
        return ret
>>>>>>> ansible/devel
