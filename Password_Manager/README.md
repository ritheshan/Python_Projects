# Password Manager

A secure command-line based Password Manager that stores, retrieves, and encrypts passwords using Python’s `cryptography` library.

## Features:
- **Encryption**: Passwords are encrypted using the `Fernet` symmetric encryption from the `cryptography` library.
- **Password Storage**: Save and retrieve passwords for different websites securely.
- **Secure Key Generation**: Automatically generates and stores encryption keys for enhanced security.

## Installation and Setup:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
2. Navigate to the Password Manager directory:
    cd Password_Manager
3. Create a virtual environment:
    python3 -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
4. Install the required dependencies:
    pip install -r requirements.txt

    
Password_Manager/
│
├── main.py            # Main Python file
├── requirements.txt   # Dependencies
├── secret.key         # Encryption key (auto-generated)
└── passwords.txt      # Encrypted password storage



