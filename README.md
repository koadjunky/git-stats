## Gource compilation

After https://github.com/acaudwell/Gource/blob/master/INSTALL:

Install libraries:

```
SDL 2.0 (libsdl2-dev)
SDL Image 2.0 (libsdl2-image-dev)
PCRE2 (libpcre2-dev)
Freetype 2 (libfreetype6-dev)
GLEW (libglew-dev)
GLM >= 0.9.3 (libglm-dev)
Boost Filesystem >= 1.46 (libboost-filesystem-dev)
PNG >= 1.2 (libpng-dev)
```

Perform:

```
./autogen.sh
./configure
make
sudo make install
```

## Single repository

1. In git folder download Gravatar images:

    ```gource-gravatar.perl```

2. Execute gource:

   ```gource --user-image-dir ./git/avatar -s 1```

## Multiple repositories

Run:

```multi-gsource.bash root_dir```
