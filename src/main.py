import os
import shutil

from textnode import TextNode

def main():
    generate_website()

# Generate static website
def generate_website():
    public_path = "public"
    static_path = "static"

    # Verify if 'static' directory exists
    # Raise an exception if it does not exist
    if not os.path.exists(static_path):
        raise Exception(f"\'{static_path}\' does not exist!")

    empty_public(public_path)
    copy_static(static_path, public_path)

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
def copy_static(source, destination):
    for entry in os.listdir(source):
        path = os.path.join(source, entry)

        # Copy file from 'static' to the same position in 'public'
        if os.path.isfile(path):
            print(f"Copying \'{path}\' to \'{destination}\'...")
            shutil.copy(path, destination)
            print(f"Successfully copied \'{path}\'!")

        # Copy directory from 'static' to 'public' and recurse through that directory
        else:
            make_dir = os.path.join(destination, entry)
            print(f"Copying \'{path}\' to \'{make_dir}\'...")
            os.mkdir(make_dir)
            copy_static(path, make_dir)
            print(f"Successfully copied \'{make_dir}\'!")
        


main()