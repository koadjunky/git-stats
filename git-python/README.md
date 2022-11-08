# Running application

1. Configure python 3.9.6

   ```pyenv local 3.9.6```

2. Create venv

   ```
   python -m venv .venv
   . .venv/bin/activate
   ```

3. Load requirements

   ```pip install -r requirements.txt```

4. Refresh repositories

   ```make root=<repo_root_dir> fetch``` 

5. Prepare data

   ```make root=<repo_root_dir> data```

5. Visualize in jupyter

   ```jupyter/commits_heatmap.ipynb```

# Peparing for commit

1. Run nbstripout on jupyters

   ```make nbstripout```