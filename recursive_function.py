"""
Recursive function
====================
Basic example of recursive function
"""

# pip install Faker==23.2.1  (Git: https://pypi.org/project/Faker/)
from faker import Faker

# Initialise "Faker" object
fake = Faker()


def get_name():
  """
  Generate random name using Faker object.  
  If the generated name contains any of the prohibited (listed) saluations, the function calls itself and generates a new name. The recursion continues until we get a valid name i.e. without mentioned salutations.

  Also, the function is a generator. It returns generator object instead of string.
  """
  
    salutations = ['Dr.', 'Mr.', 'Mrs.', 'MD', 'Jr.']
    gen_name = fake.name()  # generated name

    if any(_sal in gen_name for _sal in salutations):
        print(f"Got a false name: {gen_name}")
        yield from get_name()
    else:
        yield gen_name


if __name__ == '__main__':
  random_name = next(get_name())
  print(random_name)
