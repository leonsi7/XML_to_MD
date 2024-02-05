import os
import xml.etree.ElementTree as ET

def xml_to_md(xml_file, md_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(md_file, 'w', encoding='utf-8') as md:
        for concept in root.find('conceptList').iter('concept'):
            md.write(f"## {concept.get('id').replace('_', ' ').title()}\n\n")
            
            for action in root.find('speciess').iter('action'):
                md.write(f"### {action.get('name')}\n\n")
                
                for arg in action.iter('arg'):
                    md.write(f"- *{arg.get('name')}* ({arg.get('type')})\n")
                
                doc_result = action.find('documentation').find('result')
                doc_returns = action.find('documentation').find('returns')
                
                if doc_result is not None:
                    md.write(f"\n**Result**: {doc_result.text}\n")
                if doc_returns is not None:
                    md.write(f"\n**Returns**: {doc_returns.text}\n")
                
                md.write("\n---\n")

# Demander à l'utilisateur d'entrer le nom du fichier XML
xml_input = input("Enter XML file or path: ")

# Vérifier si le fichier existe dans le dossier local ou s'il s'agit d'un chemin absolu
if os.path.isfile(xml_input):
    xml_path = xml_input
else:
    if os.path.isabs(xml_input):
        xml_path = xml_input
    else:
        print("The file selected is not in the current folder or not an absolut file path.")
        exit()

# Construire le nom du fichier de sortie avec l'extension .md
md_output = os.path.splitext(xml_path)[0] + ".md"

# Utilisation du script avec le chemin du fichier XML et le nom du fichier de sortie
xml_to_md(xml_path, md_output)
print(md_output + " has been successfully created.")
