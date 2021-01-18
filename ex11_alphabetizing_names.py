from typing import List, Dict


PEOPLE = [
    {'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},
    {'first':'Donald', 'last':'Trump', 'email':'president@whitehouse.gov'},
    {'first':'Vladimir', 'last':'Putin', 'email':'president@kremvax.ru'},
    {'first': "Damien", 'last': 'Neveu', 'email': 'damien@Damiens-MacBook-Pro.local'},
    {'first': 'John', 'last': 'Lerner', 'email': 'john@gmail.cc'}
]


def alphabetize_names() -> List[Dict]:
    return sorted(PEOPLE,
                  key=lambda x: (x['last'], x['first']))


print(f"alphabetize_names()={alphabetize_names()}")
