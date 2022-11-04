#!/usr/bin/python

from ansible.module_utils.basic import *


def github_repo_present(data):
  has_changed = False
  meta = {"present": "not yet implemented"}
  return has_changed, meta


def github_repo_absent(data=None):
  has_changed = False
  meta = {"absent": "not yet implemented"}


def main():

  fields = {
    "github_auth_key": {"required": True, "type": "str"},
    "name": {"required": True, "type": "str" },
    "description": {"required": False, "type": "str"},
    "private": {"default": False, "type": "bool" },
    "has_issues": {"default": True, "type": "bool" },
    "has_wiki": {"default": True, "type": "bool" },
    "has_downloads": {"default": True, "type": "bool" },
    "state": {
      "default": "present",
      "choices": ['present', 'absent'],
      "type": 'str'
    },
  }

  choice_map = {
    "present": github_repo_present,
    "absent": github_repo_absent,
  }

  module = AnsibleModule(argument_spec=fields)
  has_changed, result = choice_map.get(module.params['state'])(module.params)
  module.exit_json(changed=False, meta=module.params)


if __name__ == '__main__':
    main()
