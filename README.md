# Debris-flow Experiments

## Python version
v 3.11
## Instructions to run program
 - Python needs to be preinstalled
 - Create virtual environment
 - Execute this in your bash to install packages  
    ```bash
    pip install -r requirements.txt
    ```
 - Define the configs inside `utis/constants.py` file.
 - To read data from teh raw files and create their corresponding charts run the `main.py` file.
    ```python
    python main.py
    ```
    Note that the charts will be saved as `png` inside the `results` directory. 

 - (Optional) You can generate pdf files for your results by running the `pdf_generator.py` file.
    ```python
    python pdf_generator.py
    ```
    The pdfs will be saved inside the `pdfs` directory.
