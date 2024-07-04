# scripts/validate_detections.py
import os
import yaml

def validate_yaml(file_path):
    with open(file_path, 'r') as stream:
        try:
            yaml.safe_load(stream)
            print(f"Validation passed for {file_path}")
        except yaml.YAMLError as exc:
            print(f"Validation failed for {file_path}: {exc}")

def main():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    detections_dir = os.path.join(base_dir, 'detections')

    for root, _, files in os.walk(detections_dir):
        for file in files:
            if file.endswith('.yml') or file.endswith('.yaml'):
                validate_yaml(os.path.join(root, file))

if __name__ == "__main__":
    main()
