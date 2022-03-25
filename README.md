# bazel-python-wheel-m1-repro
Demonstrating an issue of not finding Python.h when doing a pip install in Bazel.

Just doing a pip install seems to be fine:
```
$ pip install -r requirements.txt --no-binary asyncpg --no-cache-dir -vvv
```

While running Bazel complains of a missing header file:
```
$ bazel build //...
...
      creating build/temp.macosx-12.3-arm64-3.8/asyncpg/pgproto
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -g0 -I/private/var/tmp/_bazel_user/ae85dee007277800f47f2ad5b2ad18a9/external/python_interpreter/bazel_install/lib/python3.8/config-3.8-darwin/Include -I/private/var/tmp/_bazel_user/ae85dee007277800f47f2ad5b2ad18a9/external/python_interpreter -c asyncpg/pgproto/pgproto.c -o build/temp.macosx-12.3-arm64-3.8/asyncpg/pgproto/pgproto.o -O2 -fsigned-char -Wall -Wsign-compare -Wconversion
      asyncpg/pgproto/pgproto.c:31:10: fatal error: 'Python.h' file not found
      #include "Python.h"
...
```

Happens on:
M1 Pro, macOS Monterey 12.3