import os
import shutil

from block_to_html import markdown_to_html_node, extract_title
from textnode import TextNode

def main():
    generate_website()

# Generate static website
def generate_website():
    public_path = "public"
    static_path = "static"
    from_path = "content"
    template_path = "template.html"

    # Verify if 'static' directory exists
    # Raise an exception if it does not exist
    if not os.path.exists(static_path):
        raise Exception(f"\'{static_path}\' does not exist!")

    empty_public(public_path)
    copy_static(static_path, public_path)
    generate_pages_recursive(from_path, template_path, public_path)

# Empty contents of the 'public' directory
def empty_public(path):
    # Create 'public' if it does not exist
    if not os.path.exists(path):
        print(f"\'{path}\' does not exist!")
        os.mkdir(path)
        print(f"\'{path}\' created!")
        return
    
    # Delete and remake 'public'
    print(f"Deleteing \'{path}\' directory contents...")
    shutil.rmtree(path)
    os.mkdir(path)
    print(f"Succesfully deleted \'{path}\' contents!")

# Copy all contents of 'static' to 'public'
def copy_static(from_path, dest_path):
    for entry in os.listdir(from_path):
        path = os.path.join(from_path, entry)

        # Copy file from 'static' to the same position in 'public'
        if os.path.isfile(path):
            print(f"Copying \'{path}\' to \'{dest_path}\'...")
            shutil.copy(path, dest_path)
            print(f"Successfully copied \'{path}\'!")

        # Copy directory from 'static' to 'public' and recurse through that directory
        else:
            make_dir = os.path.join(dest_path, entry)
            print(f"Copying \'{path}\' to \'{make_dir}\'...")
            os.mkdir(make_dir)
            copy_static(path, make_dir)
            print(f"Successfully copied \'{make_dir}\'!")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from \'{from_path}\' to \'{dest_path}\' using \'{template_path}\'...")
    with open(from_path) as md:
        markdown = md.read()
    with open(template_path) as base:
        template = base.read()

    content = markdown_to_html_node(markdown)
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    with open(f"{dest_path}/index.html", "w") as index:
        index.write(template)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        path = os.path.join(dir_path_content, entry)

        # Generate 'index.html' file in public from 'index.md' in 'content' (same nesting)
        if os.path.isfile(path) and path[-3:] == ".md":
            generate_page(path, template_path, dest_dir_path)
            print(f"Copying \'{path}\' to \'{dest_dir_path}\'...")
            shutil.copy(path, dest_dir_path)
            print(f"Successfully copied \'{path}\'!")

        # Copy directory from 'content' to 'public' and recurse through that directory
        else:
            make_dir = os.path.join(dest_dir_path, entry)
            print(f"Copying \'{path}\' to \'{make_dir}\'...")
            os.mkdir(make_dir)
            generate_pages_recursive(path, template_path, make_dir)

main()