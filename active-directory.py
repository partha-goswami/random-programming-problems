'''
Class declaration as is given in the problem definition at Udacity
'''
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name





def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # Edge cases
    if user == '' or group == []:
        return False
    
    # Users and group collection
    users = group.get_users()
    groups = group.get_groups()
    
    # If user is present, let's return true
    if user in users:
        return True
    
    # If user isn't already present and there is nowhere to look further
    # then return false
    elif groups == []:
        return False
    
    # Else let's call this method recursively
    for grp in groups:
        return is_user_in_group(user, grp)

    # If control comes here, that means we have exhausted everything
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# Tests
print(is_user_in_group(sub_child_user, child))
print(is_user_in_group(sub_child_user, parent)) 
