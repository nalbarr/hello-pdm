# tutorial

- Understanding package management and 3 types of dependencies
    - standard library (i.e., python runtime)
    - external dependencies
    - internal (module) imports

- Create working folder
`mkdir <project_name>`

- Initialize default project
`pdm init`

- Understand default pdm project structure
    - i.e, src/, test/
    - i.e., python packages are by extension python (installable) modules
    - compare/contrast to `poetry new --src <package_name>`

- Create simple runnable module (without import dependences)
    - i.e., change src/<module>/__init__.py default to add
        - src/<project_name>/__main__.py

- Understanding import semantics
    - importing from __main__ is different
    - e.g., import <project_name>.__main__

- Understand simple python scripting
    - create python script (outside of src/ and pip installable module)
    - something.py
        - i.e., use if __name__ == "__main__" as script main entry point

    - python3 <script_name> vs. python <script_name> (from .venv)

- Understanding modules
    - i.e., python -m <module_name>
    - `pdm install`
        - by default, this is editable install and source files will not be copied to ./.venv
        - e.g., <PROJECT_ROOT>/.venv/lib/python3.10/site-packages/hello_pdm-0.1.0+editable.dist-info
    -`cat <PROJECT_ROOT>/.venv/lib/python3.10/site-packages/hello_pdm-0.1.0+editable.dist-info/direct_url.json`

```{
  "url": "file:///<PROJECT_ROOT>/../hello-pdm/.venv/lib/python3.10/site-packages/hello_pdm-0.1.0+editable.dist-info",
  "dir_info": {
    "editable": true
  }
}```
    - Note, a python module name is NOT the same as the python package name as constrained by python naming standards
        - e.g., hello-pdm module name vs. hello_pdm package name and namespacing

- List pdm installed modules (which will differ from pip freeze and conda list)
  - `pdm list`
  - `pip freeze`

- Review Makefile
    - `make clean`
    - `make install`
    - `make pdm-install`
    - `make run-script-explicit`
    - `make run-module`
    - `make run-script`
    - `make run-module-with-script`
    - `make clean`

- Activate virtual environment
    - i.e., source .venv/bin/activate

- List installed modules
    - i.e., `pdm list` or `pdm list| grep <module_name>`

- Try exercise different scenarios
    - add an external dependency
        - `pdm add requests`
    - update dependency versions
        - `pdm update`
    - understand dependency notations
        - Compare and contrast pythonic, poetry and others
        - Caret and tilde notations

- Run external dependency
    - `make run-module-requests`

- Make project installable
    - 