from yargy.interpretation import InterpretationEngine

from natasha import Combinator
from natasha.grammars import Person, Organisation, Location
from natasha.grammars.person import PersonObject 
from natasha.grammars.organisation import OrganisationObject
from natasha.grammars.location import LocationObject, AddressObject

text = 'василий петрович пришел в Санкт-Петербургский государственный университет'

text = """
Иванов Иван Иванович был профессором в Санкт-Петербургском государственном университете.
Он жил в городе Санкт-Петербург на набережной реки Мойки, дом 33.
Улица Арбат дом 7 квартира 17
"""

combinator = Combinator([
    Person,
    Organisation,
    Location
])
# Определение Персоны
matches = combinator.resolve_matches(combinator.extract(text))
enjine_person = InterpretationEngine(PersonObject)
persons = list(enjine_person.extract(matches))
for i in range(len(persons)):
    print('имя:', str(persons[i].firstname).split('\'')[1] if str(persons[i].firstname) != 'None' else 'None')
    print('отчество:', str(persons[i].middlename).split('\'')[1] if str(persons[i].middlename) != 'None' else 'None')
    print('фамилия:', str(persons[i].lastname).split('\'')[1] if str(persons[i].lastname) != 'None' else 'None')
    print('должность:', str(persons[i].descriptor).split('\'')[1] if str(persons[i].descriptor) != 'None' else 'None')
    print('несклоняемая часть должности:', str(persons[i].descriptor_destination).split('\'')[1] if str(persons[i].descriptor_destination) != 'None' else 'None')
print('-------------------------------')
print()
# Определение организации
matches = combinator.resolve_matches(combinator.extract(text))
enjine_organiztion = InterpretationEngine(OrganisationObject)
organizations = list(enjine_organiztion.extract(matches))
for i in range(len(organizations)):
    print('название:', str(organizations[i].name).split('\'')[1] if str(organizations[i].name) != 'None' else 'None')
    print('дескриптор:', str(organizations[i].descriptor).split('\'')[1] if str(organizations[i].descriptor) != 'None' else 'None')
print('-------------------------------')
print()

# Определение Локации
matches = combinator.resolve_matches(combinator.extract(text))
enjine_location = InterpretationEngine(LocationObject)
locations = list(enjine_location.extract(matches))
for i in range(len(locations)):
    print('название:', str(locations[i].name).split('\'')[1] if str(locations[i].name) != 'None' else 'None')
    print('дескриптор:', str(locations[i].descriptor).split('\'')[1] if str(locations[i].descriptor) != 'None' else 'None')
print('-------------------------------')
print()

# Определение Адрессов
matches = combinator.resolve_matches(combinator.extract(text))
enjine_address = InterpretationEngine(AddressObject)
addresses = list(enjine_address.extract(matches))
for i in range(len(addresses)):
    print('название улицы:', str(addresses[i].name).split('\'')[1] if str(addresses[i].name) != 'None' else 'None')
    print('дескриптор улицы', str(addresses[i].descriptor).split('\'')[1] if str(addresses[i].descriptor) != 'None' else 'None')
    print('номер дома:', str(addresses[i].house_number).split('\'')[1] if str(addresses[i].house_number) != 'None' else 'None')
    print('литера дома:', str(addresses[i].house_number_letter).split('\'')[1] if str(addresses[i].house_number_letter) != 'None' else 'None')
print('-------------------------------')
print()



# assert len(persons) == 1

# print('Аттрибуты (оригинальное значение)')
# print('Имя:', persons[0].firstname)
# print('Отчество:', persons[0].middlename)
# print('Фамилия:', persons[0].lastname)