from textnode import TextNode, TextType
from gencontent import generate_pages_recursive


def main():
    node=TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    copy_directory("static", "docs")
    print("Copying static files to public directory...")
    copy_directory(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public,basepath)



import sys
if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"

import os
import shutil
dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def copy_directory(src, dst):
    """
    Recursively copy all contents from src directory to dst directory.
    Before copying, delete all contents of dst directory.
    Log each file copied.
    """
    # Remove the destination directory if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
    # Recreate the destination directory
    os.makedirs(dst, exist_ok=True)

    # Walk through the source directory
    for root, dirs, files in os.walk(src):
        # Compute the relative path from the source root
        rel_path = os.path.relpath(root, src)
        # Compute the corresponding destination directory
        dest_dir = os.path.join(dst, rel_path) if rel_path != '.' else dst
        # Ensure the destination directory exists
        os.makedirs(dest_dir, exist_ok=True)
        # Copy files
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copy2(src_file, dest_file)
            print(f"Copied: {src_file} -> {dest_file}")

# Example usage:
# copy_directory("static", "public")
main()

