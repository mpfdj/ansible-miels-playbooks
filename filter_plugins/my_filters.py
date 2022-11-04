# github.com
# https://gist.github.com/tuxfight3r/37048ba536575277f5f4d26813d69489
# https://gist.github.com/37048ba536575277f5f4d26813d69489.git


#place the file in your ansible playbook director under filter_plugins
#/home/user/my_playbook.yml
#/home/user/filter_plugins/my_filters.py

#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'a_filter': self.a_filter,
            'another_filter': self.b_filter
        }

    def a_filter(self, a_variable):
        a_new_variable = a_variable + ' CRAZY NEW FILTER'
        return a_new_variable

    def b_filter(self, a_variable, another_variable, yet_another_variable):
        a_new_variable = a_variable + ' - ' + another_variable + ' - ' + yet_another_variable
        return a_new_variable
