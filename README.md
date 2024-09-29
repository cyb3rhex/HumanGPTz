# HumanGPTz

## Description

The HumanGPTz is a Python application that uses natural language processing techniques to modify text, making it appear more human-written. This tool is designed to introduce subtle variations and imperfections typically found in human written text, while maintaining the original meaning.

**Note:** This tool is for educational and research purposes only. It should not be used to generate misleading content or for any unethical purposes.

## Features

- Introduces minor grammatical imperfections
- Varies sentence structures
- Adds conversational elements
- Maintains semantic similarity to the original text
- User friendly GUI

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/cyb3rhex/HumanGPTz.git
   cd HumanGPTz
   ```

2. Install the required dependencies:
   ```
   pip install PyQt6 spacy sentence-transformers nltk
   ```

3. Download the required spaCy model:
   ```
   python -m spacy download en_core_web_sm
   ```

4. Download nltk
    ```
    python3 -m nltk.downloader all
    ```

## Usage

1. Run the application:
   ```
   python humangptz.py
   ```

2. Enter the text you want to humanize in the input field.

3. Click the "Humanize Text" button.

4. The humanized version of your text will appear in the output field.

## Dependencies

- Python 3.7+
- PyQt6
- spaCy
- NLTK
- sentence-transformers

## Limitations

- The quality of the output may vary depending on the input text.
- The tool may occasionally produce unexpected results.
- It's not designed to generate entirely new content or change the meaning of the input text.

## Contributing

Contributions to improve the Advanced Text Humanizer are welcome. Please feel free to submit pull requests or open issues to discuss potential enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


```
Dev: LSDeep
Version: 1.0
www.HTDark.com
```