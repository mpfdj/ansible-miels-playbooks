#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

import subprocess
import os
import tempfile

DOCUMENTATION = r'''
---
author: tibcobw-amx@ing.nl
'''

EXAMPLES = r'''
# Pass in a password
- name: Test with a message
  tibco_obfuscate:
    password: hello
'''

RETURN = r'''
This module returns an obfuscated password using the tibco obfuscate tool.
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        password=dict(type='str', required=True)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # ------------------------------------------------
    # create tempfile
    # ------------------------------------------------
    tmp = tempfile.NamedTemporaryFile(dir="/tmp", delete=False)
    try:
        tmp_filename = tmp.name
        tmp.write("password=#!" + module.params["password"])
    finally:
        tmp.close()

    # ------------------------------------------------
    # run obfuscate
    # ------------------------------------------------
    os.chdir("/opt/tibco/tra/5.11/bin")
    subprocess.call(["./obfuscate", tmp_filename])

    # ------------------------------------------------
    # read password and return result
    # ------------------------------------------------
    with open(tmp_filename, "r") as f:
        password = f.readline()[9:]

    password = password.replace("\n", "")

    result['password'] = password
    result['changed'] = True

    os.remove(tmp_filename)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
