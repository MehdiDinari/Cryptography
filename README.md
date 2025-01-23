# Encryption Application

## Overview
This is a GUI-based encryption and decryption application built using Python and Tkinter. The application supports multiple encryption techniques, including:

- **Caesar Cipher**
- **Vigenère Cipher**
- **Vernam Cipher**
- **XOR Encryption (Coming Soon)**
- **Brute Force Attack on Caesar Cipher**

## Features
- **Encryption** and **Decryption** functionalities.
- **User-friendly GUI** built with Tkinter.
- **Error handling** to ensure proper input validation.
- **Brute force attack on Caesar Cipher** to demonstrate cryptanalysis.

## Installation
### Prerequisites
Ensure you have Python installed (Python 3.x recommended). You can download it from [Python's official website](https://www.python.org/downloads/).

### Required Libraries
Install Tkinter (usually included with Python by default). If necessary, install additional dependencies:
```sh
pip install tkinter
```

### Running the Application
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/encryption-app.git
   ```
2. Navigate to the project directory:
   ```sh
   cd encryption-app
   ```
3. Run the application:
   ```sh
   python encryption_app.py
   ```

## How to Use
### Main Menu
Upon running the application, you will see three main options:
1. **Encrypt a message**
2. **Decrypt a message**
3. **Perform an attack**

### Encryption
- Select a cipher method (**Caesar, Vigenère, Vernam**).
- Enter your plaintext and the corresponding key.
- Click **Encrypt** to get the ciphertext.

### Decryption
- Select a cipher method (**Caesar, Vigenère, Vernam**).
- Enter your ciphertext and the corresponding key.
- Click **Decrypt** to retrieve the original message.

### Brute Force Attack (Caesar)
- Enter a Caesar-encrypted message.
- The app will attempt **all 25 possible shifts** and display the results.

## Code Structure
```
/encryption-app
│── encryption_app.py     # Main application script
│── README.md             # Project documentation
│── requirements.txt      # Dependencies (if needed)
```

## Future Improvements
- Implement **XOR encryption and decryption**.
- Enhance **UI/UX** with a better design framework (e.g., Tkinter ttk or PyQt).
- Improve **error handling and logging**.
- Add **automated tests** for encryption functions.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Author
[Mehdi Dianari]

For any questions or contributions, feel free to contact me via GitHub or email.

