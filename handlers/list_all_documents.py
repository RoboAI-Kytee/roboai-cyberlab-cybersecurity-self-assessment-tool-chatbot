import yaml
import os
# Load the YAML configuration file
config = yaml.safe_load(open("config/config.yml"))

def list_pdfs_in_folder():
    pdf_paths = []
    for root, _, files in os.walk(config['pdf_folder']):
        for file in files:
            if file.lower().endswith('.pdf'):  # Filter only PDF files
                full_path = os.path.join(root, file)
                pdf_paths.append(full_path)
    return pdf_paths
