from crpt import Cryptography

people = {'Dries van Agt': 1, 'Hans Andreus': 3, 'Lodewijk Asscher': 1, 'Ron Blaauw': 2, 'Herman den Blijker': 2, 'Jonnie Boer': 2, 'Eduard Bomhoff': 1, 'Louis Paul Boon': 3, 'Wouter Bos': 1, 'Maartje Boudeling': 2, 'Lourens Jan Brinkhorst': 1, 'Remco Campert': 3, 'Hugo Claus': 3, 'Lodewijk van Deyssel': 0, 'Alphons Diepenbrock': 0, 'Frederik van Eeden': 0, 'Jan Elburg': 3, 'Frans Erens': 0, 'Gaspar Fagel': 4, 'Herman Gorter': 0, 'Thom de Graaf': 1, 'Jan Hanlo': 3, 'Anthonie van der Heim': 4, 'Anthonie Heinsius': 4, 'Cees Helder': 2, 'Sergio Herman': 2, 'Isaac van Hoornbeek': 4, 'Hugo de Jonge': 1, 'Annemarie Jorritsma': 1, 'Willem Kloos': 0, 'Wim Kok': 1, 'Rudolf de Korte': 1, 'Gerrit Kouwenaar': 3, 'Robert Kranenborg': 2, 'Erik van Loo': 2, 'Lucebert': 3, 'Roelof Nelissen': 1, 'Kajsa Ollongren': 1, 'Sybren Polet': 3, 'Johan Remkes': 1, 'Margo Reuten': 2, 'Mario Ridder': 2, 'Lucas Rive': 2, 'Paul Rodenko': 3, 'Andre Rouvoet': 1, 'Bert Schierbeek': 3, 'Angelique Schmeinck': 2, 'Carola Schouten': 1, 'Simon van Slingelandt': 4, 'Paul Snoek': 3, 'Cas Spijkers': 2, 'Helene Swarth': 0, 'Jan Terlouw': 0, 'Mario Uva': 2, 'Maxime Verhagen': 1, 'Albert Verwey': 0, 'Simon Vinkenoog': 3, 'Hans Wiegel': 1, 'Johan de Witt': 4, 'Johan Witteveen': 1, 'Hans van Wolde': 2, 'Gerrit Zalm': 1}
categories = {1: 'vicepremiers', 2: 'chefkoks', 3: 'vijftigers', 4: 'raadpensionarissen'}

crypt = Cryptography()

for person, group in people.items():
  if group in categories:
    key = categories[group]
    crypt.set_decoded_text(person)
    print(person, crypt.encode_bifid(key))