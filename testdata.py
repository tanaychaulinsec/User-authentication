import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CloudxLabAssignment.settings')

import django
# Import settings
django.setup()

import random
from usersAccount.models import Users
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name=fakegen.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        fake_phoneNumber = fakegen.phoneNumber
        fake_username=fakegen.username
        fake_password=fakegen.password
        fake_email = fakegen.email()

        # Create new Webpage Entry
        usr = Users.objects.get_or_create(first_name=fake_fname,last_name=fake_lname,email=fake_email)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
