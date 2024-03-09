# Unprivilaged mountpoints in Docker

* A background service that stores a mapping between mountpoints and FUSE plugins
* `fusermount` replacement that adds it to the service
* A `LD_PRELOAD` shim that replaces kernel calls and forwards them to the service
  if they match the given path

It'd be slow, but it'd mean we could mount filesystems in Docker.

```C
#define _GNU_SOURCE
#include <dlfcn.h>
#include <stdio.h>

int open(const char *pathname, int flags) {
    // Custom FUSE logic here
    
    ...

    // Call the original libc open
    int (*original_open)(const char*, int);
    original_open = dlsym(RTLD_NEXT, "open");
    return original_open(pathname, flags);
}
```

```bash
gcc -shared -fPIC my_fuse_shim.c -o my_fuse_shim.so -ldl
LD_PRELOAD=./my_fuse_shim.so your_program
```


