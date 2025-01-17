# QuickLauncher

QuickLauncher is a simple Python application that allows users to create keyboard shortcuts to launch applications faster on Windows. This tool can be customized with different key-command pairs to enhance productivity and streamline workflows by reducing the time to open frequently used applications.

## Features

- **Add Shortcuts:** Easily configure new keyboard shortcuts for your favorite applications.
- **Remove Shortcuts:** Remove shortcuts that you no longer need.
- **Run in Background:** Continuously listens for specified keyboard shortcuts while running in the background.

## Requirements

- Python 3.x
- [pynput](https://pypi.org/project/pynput/) library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/quicklauncher.git
   ```

2. Navigate to the project directory:

   ```bash
   cd quicklauncher
   ```

3. Install the required dependencies:

   ```bash
   pip install pynput
   ```

## Usage

1. Run the application:

   ```bash
   python quick_launcher.py
   ```

2. Follow on-screen prompts to add or remove shortcuts.

3. Use configured shortcuts to quickly launch applications.

## Configuration

Shortcuts are stored in a JSON file named `shortcuts.json`. This file is automatically created in the same directory as the script when you add a shortcut. You can manually edit this file to add or modify shortcuts as needed.

## Contributing

Contributions are welcome! Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This is a simple tool meant for educational purposes and personal productivity enhancement. Use it at your own risk.