# https://docs.ansible.com/ansible/latest/user_guide/collections_using.html
# https://docs.ansible.com/ansible/latest/collections/index.html

cd ansible-miels-playbooks
mkdir collections
ansible-galaxy collection install community.crypto --collections-path ./collections
ansible-galaxy collection install community.general --collections-path ./collections

ansible-playbook ./test-json_query.yml
ansible-playbook ./test-my_test.yml
ansible-playbook ./test-role-with-my_test-module.yml
ansible-playbook ./test-x509_certificate_info.yml

# https://coderwall.com/p/tx91cw/run-ansible-on-a-single-host
# Don't forget to add the comma!
# Don't forget to update hosts tag in test-role-with-my_test-module.yml
ansible-playbook ./test-role-with-my_test-module.yml -i clrv0000xxxxxx, --user to11rc --ask-pass


# List of collections
https://galaxy.ansible.com/community

# Create a collection
# https://docs.ansible.com/ansible/latest/dev_guide/developing_collections_creating.html
cd collections/ansible_collections
ansible-galaxy collection init miel.my_collection
mkdir collections/ansible_collections/miel/my_collection/modules
cp my_test.py collections/ansible_collections/miel/my_collection/modules





root@1cbee9f7f8a3:/# ansible --version
ansible [core 2.12.6]
config file = /etc/ansible/ansible.cfg
configured module search path = ['/root/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
ansible python module location = /usr/local/lib/python3.10/dist-packages/ansible
ansible collection location = /root/.ansible/collections:/usr/share/ansible/collections
executable location = /usr/local/bin/ansible
python version = 3.10.4 (main, Apr  2 2022, 09:04:19) [GCC 11.2.0]
jinja version = 3.0.3
libyaml = False

