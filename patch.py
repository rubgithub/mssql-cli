import os
import re

def apply_comprehensive_patch():
    # 1. Corrigir imports de collections em todos os arquivos .py
    regex_collections = re.compile(r'from collections import (Mapping|Iterable|Callable|Sequence|MutableMapping)')
    
    print("--- Corrigindo imports de collections ---")
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if regex_collections.search(content):
                    print(f"Corrigindo: {path}")
                    new_content = regex_collections.sub(r'from collections.abc import \1', content)
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

    # 2. Corrigir setup.py (Dependências e Classifiers)
    setup_path = 'setup.py'
    if os.path.exists(setup_path):
        print("\n--- Atualizando setup.py ---")
        with open(setup_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            # Adiciona o 'six' se não estiver na lista
            if 'install_requires' in line:
                new_lines.append(line)
                new_lines.append("        'six >= 1.15.0',\n")
                continue
            
            # Atualiza cli_helpers para versão compatível com 3.10
            line = line.replace("'cli_helpers >= 1.2.0'", "'cli_helpers >= 2.2.1'")
            
            # REMOVE enum34 (causa quebra no Python 3.10)
            if 'enum34' in line:
                print("Removendo dependência obsoleta: enum34")
                continue
                
            # Adiciona Classifier para Python 3.10
            if "'Programming Language :: Python :: 3.9'," in line:
                new_lines.append(line)
                new_lines.append("        'Programming Language :: Python :: 3.10',\n")
                new_lines.append("        'Programming Language :: Python :: 3.11',\n")
                continue

            new_lines.append(line)

        with open(setup_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print("setup.py atualizado com sucesso.")

if __name__ == "__main__":
    apply_comprehensive_patch()
    print("\n✅ Patch V2 aplicado! O erro do 'six' deve ser resolvido agora.")
