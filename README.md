# Industrialization
**This project is a training python project, it is associated with a google 
presentation on code's industrialization in python, project goals:**
1. Have a better understanding of industrialized projects architecture
2. Have a look on good practices in industrialized project 
3. Create a template of code's industrialization

## Environment:
- This project use a Python3 version

## Set your interpreter:
> The better way to manage packages project is to use a virtual environment (install pipenv could be a good choice)
- With pipenv https://www.jetbrains.com/help/pycharm/pipenv.html#
- Without pipenv select your local interpreter Python or create a virtual environment with PyCharm
- **Don't forget to install requirements**

## Checking Installation:
- run the check_installation.py file in your IDE or `pipenv run python check_installation.py` or 
`python check_installation.py`  

## Run tests:
- `python -m test_folder.test_object`

## Set checker and formatter Python Style  (Optional)

Linter :

`pylint` is a python linter which ensure your IDE take the python code style

For **Pycharm** follow instructions <a href=http://pylint.pycqa.org/en/latest/user_guide/ide-integration.html#pylint-in-pycharm>here</a>.
Furthermore in nantosuelta root project you will find a `.pylintrc` file, please add it to the Pycharm config

For **Visual Studio Code**, go to your `settings.json` file under `.vscode folder/` and paste those lines :

> "python.linting.enabled": true,
>
> "python.linting.pylintEnabled": true,
>
> "python.linting.lintOnSave": true,
>
> "python.linting.pylintPath": "/Users/amso/.pyenv/shims/pylint"

Code formatter **Black**:

`black` is a python formatter to automatically take care of the python style but it doesn't ensure all code style rules.

For **PyCharm** follow instructions <a href=https://black.readthedocs.io/en/stable/editor_integration.html>here</a> 
and add the following default arguments to the black config :

>["--style", "{based_on_style: google}", "--max-line-length", "90"],


## Contribution:
- Contributions are not welcome (it's just an example project)

## Author:
- **Hugo Prat** - [GitHub](https://github.com/PratHugo) - [email](mailto:hugoprat95@gmail.com) 

## Contact:
- email work group owner: *[ebargain@hotmail.com](mailto:ebargain@hotmail.com])*
and *[arnold.vialfont@u-pec.fr](mailto:arnold.vialfont@u-pec.fr)*