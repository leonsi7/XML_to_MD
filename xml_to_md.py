import os
import xml.etree.ElementTree as ET

def xml_to_md(xml_file, md_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(md_file, 'w', encoding='utf-8') as md:
        
        constants_root = root.find('constants')
        if constants_root is not None:
            md.write("## Constants\n\n")
            constants = constants_root.findall('constant')
            for constant in constants:
                md.write(f"### {constant.get('name').replace('#', '').title()}\n\n")
                
                categories = constant.find('categories').findall('category')
                for category in categories:
                    md.write(f"**Category**: {category.get('id').replace('_', ' ').title()}\n")
                
                doc_result = constant.find('documentation').find('result')
                doc_returns = constant.find('documentation').find('returns')
                
                if doc_result is not None:
                    md.write(f"\n**Result**: {doc_result.text}\n")
                if doc_returns is not None:
                    md.write(f"\n**Returns**: {doc_returns.text}\n")
                
                md.write("\n---\n")

        operators_categories = root.find('operatorsCategories')
        if operators_categories is not None:
            md.write("## Operators\n\n")
            for category in operators_categories.iter('category'):
                md.write(f"### {category.get('id').replace('_', ' ').title()}\n\n")
                
                operators = root.find('operators')
                if operators is not None:
                    operators_list = operators.findall('operator')
                    for operator in operators_list:
                        continue_parsing = False
                        if operator.find("operatorCategories") is None:
                            continue
                        for opcategories in operator.find("operatorCategories").findall("category"):
                            print(opcategories.get('id'))
                            print(" ", category.get("id"))
                            if opcategories.get('id') == category.get("id") :
                                continue_parsing = True
                        if continue_parsing == False:
                            continue
                        md.write(f"#### {operator.get('name')}\n\n")
                        if operator.find('concepts') is not None:
                            concepts = operator.find('concepts').findall('concept')
                            for concept in concepts:
                                md.write(f"**Concept**: {concept.get('id').replace('_', ' ').title()}\n")
                        if operator.find('combinaisonIO') is not None:
                            operands = operator.find('combinaisonIO').findall('operands')
                            md.write("\n**Arguments**:\n")
                            for operand in operands:
                                md.write(f"- *{operand.find('operand').get('name')}* ({operand.get('type')})\n")
                        if operator.find('documentation') is not None:
                            doc_result = operator.find('documentation').find('result')
                            if doc_result is not None:
                                md.write(f"\n**Result**: {doc_result.text}\n")
                        if operator.find('documentation') is not None:
                            doc_returns = operator.find('documentation').find('returns')
                            if doc_returns is not None:
                                md.write(f"\n**Returns**: {doc_returns.text}\n")
                        if operator.find('documentation/usagesExamples') is not None:
                            md.write("\n**Usage Examples**:\n")
                            examples = operator.find('documentation/usagesExamples/usage/examples').findall('example')
                            for example in examples:
                                md.write(f"\n - Code: ```\n{example.get('code')} ```\n \n - Returns:  ```\n{example.get('equals')} ```\n\n")
                        
                        md.write("\n---\n")


        species = root.find('speciess').findall('species')
        
        for specie in species:
            md.write(f"## {specie.get('id').replace('_', ' ').title()}\n\n")
            
            actions = specie.find('actions').findall('action')
            
            for action in actions:
                md.write(f"### {action.get('name')}\n\n")
                
                args = action.find('args').findall('arg')
                for arg in args:
                    md.write(f"- *{arg.get('name')}* ({arg.get('type')})\n")
                
                doc_result = action.find('documentation').find('result')
                doc_returns = action.find('documentation').find('returns')
                
                if doc_result is not None:
                    md.write(f"\n**Result**: {doc_result.text}\n")
                if doc_returns is not None:
                    md.write(f"\n**Returns**: {doc_returns.text}\n")
                
                md.write("\n---\n")

"""
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
"""
xml_path = "kDJaymRj.xml"
md_output = "kDJaymRj.md"
# Utilisation du script avec le chemin du fichier XML et le nom du fichier de sortie
xml_to_md(xml_path, md_output)
print(md_output + " has been successfully created.")
