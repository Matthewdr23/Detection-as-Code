# Detection as Code Project

This project demonstrates how to manage security detections as code. The example includes a simple directory structure, a basic detection rule, and instructions for using the project.

## Directory Structure

```plaintext
.
├── README.md
├── detections
│   ├── windows
│   │   └── suspicious_process_creation.yml
│   └── linux
│       └── unauthorized_user_addition.yml
└── scripts
    └── validate_detections.py
