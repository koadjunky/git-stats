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

   ```make root=<repo_root_dir> pull``` 

5. Prepare data

   ```make root=<repo_root_dir> prefix=<gitlab group> commits survived```

6. Merge data

   ```make merge-commits```

7. Visualize in jupyter

   ```jupyter/commits_heatmap.ipynb```

# Peparing for commit

1. Run nbstripout on jupyters

   ```make nbstripout```

# Tools

Clone all repositories from GitLab:

```
python src/create_clone_script.py > run.bash
chmod u+x run.bash
./run.bash
```
