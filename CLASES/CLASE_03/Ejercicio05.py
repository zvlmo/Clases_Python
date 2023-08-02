from os import system
system("cls")
""" EJERCICIO 05 
MATIAS DI GIROLAMO 1 D """
heroes_info = [
{'Nombre':'Super Girl',
'ID': 1,
'Origen': 'Krypton',
'Habilidades': ['Volar', 'Fuerza', 'Velocidad', 'Volar',
'Fuerza', 'Velocidad'],
'Identidad': 'Kara Zor-El'}, 
{
'Nombre':'Shazam', 'ID':25,'Origen': 'Tierra',
'Habilidades': ['Volar', 'Fuerza', 'Velocidad', 'Magia',
'Fuerza', 'Velocidad'],
'Identidad': 'Billy Batson'},
{
'Nombre':'Power Girl',
'ID': 14,
'Origen': 'Krypton',
'Habilidades': ['Volar', 'Fuerza', 'Congelar', 'Congelar',
'Congelar'],'Identidad': 'Karen Starr'},
{
'Nombre':'Wonder Woman',
'ID': 29,
'Origen': 'Amazonia',
'Habilidades': ['Agilidad', 'Fuerza', 'Lazo de la verdad',
'Escudo'],
'Identidad': 'Diana Prince'
}
]
      
for heroes in heroes_info:
    print(f"ID: {heroes['ID']},Nombre: {heroes['Nombre']}")
    print(f"Identidad: {heroes['Identidad']}, Origen: {heroes['Origen']}")
    print(f"Habilidades:", " / ".join(set(heroes['Habilidades'])))
    print("--------------------------------------------------------------------------------------------")
