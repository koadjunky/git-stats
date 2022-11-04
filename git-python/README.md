1. Configure python 3.9.6

   ```pyenv local 3.9.6```

2. Create venv

   ```
   python -m venv .venv
   . .venv/bin/activate
   ```

3. Load requirements

   ```pip install -r requirements.txt```

4. Run application

   ```
   cd src
   python commits.py <directory_holding_repos>
   ```
