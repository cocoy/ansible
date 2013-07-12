# (c) 2012, Michael DeHaan <michael.dehaan@gmail.com>
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

from ansible.utils import template
import ansible.utils as utils

class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, inject=None, **kwargs):
<<<<<<< HEAD
<<<<<<< HEAD
        return utils.template_from_file(self.basedir, terms, inject)

=======
        if isinstance(terms, basestring):
            terms = [ terms ]
=======

        terms = utils.listify_lookup_plugin_terms(terms, self.basedir, inject) 

>>>>>>> fba1f7ef4288ac4cf4b35e5f0dee908ae081ce25
        ret = []
        for term in terms:
            ret.append(template.template_from_file(self.basedir, term, inject))
        return ret
>>>>>>> ansible/devel
