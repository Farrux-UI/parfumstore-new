import os
import re

directory = r"c:\Users\User\Desktop\parfumstore-n\src"

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean Palatino styles and explicitly add font-serif
    def replace_palatino(match):
        class_str = match.group(1)
        if "font-serif" not in class_str:
            class_str += " font-serif tracking-wide"
        return f'class="{class_str}"'

    content = re.sub(r'class="([^"]*?)"\s+style="font-family: [\'"]*Palatino[^\"]*?"', replace_palatino, content)
    
    # Clean Inter styles and explicitly add font-sans
    def replace_inter(match):
        class_str = match.group(1)
        if "font-sans" not in class_str:
            class_str += " font-sans font-light leading-relaxed"
        return f'class="{class_str}"'

    content = re.sub(r'class="([^"]*?)"\s+style="font-family: [\'"]*Inter[^\"]*?"', replace_inter, content)

    # Some times style="font-family:..." is first. Let's just strip remaining styles globally if they only contain font-family.
    content = re.sub(r'\s*style="font-family:[^"]*"\s*', ' ', content)

    # Specific Header update
    if "Header.astro" in file_path:
        content = content.replace(
            'class="flex-1 flex items-center justify-center gap-8 md:gap-14 font-sans text-[10px] md:text-[11px] uppercase tracking-[0.2em] font-medium z-[100] h-full"',
            'class="flex-1 flex items-center justify-center gap-8 md:gap-14 font-serif text-[12px] md:text-sm tracking-[0.15em] uppercase z-[100] h-full"'
        )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.astro'):
            process_file(os.path.join(root, file))

print("Typography updated globally.")
