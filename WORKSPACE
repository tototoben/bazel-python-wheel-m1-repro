workspace(name = "eugh")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Special logic for building python interpreter with OpenSSL from homebrew.
# See https://devguide.python.org/setup/#macos-and-os-x
_py_configure = """
if [[ "$OSTYPE" == "darwin"* ]]; then
    ./configure --prefix=$(pwd)/bazel_install --with-openssl=$(brew --prefix openssl)
else
    ./configure --prefix=$(pwd)/bazel_install
fi
"""

http_archive(
    name = "python_interpreter",
    build_file_content = """
exports_files(["python_bin"])
filegroup(
    name = "files",
    srcs = glob(["bazel_install/**"], exclude = ["**/* *"]),
    visibility = ["//visibility:public"],
)
""",
    patch_cmds = [
        "mkdir $(pwd)/bazel_install",
        _py_configure,
        "make",
        "make install",
        "ln -s bazel_install/bin/python3 python_bin",
    ],
    strip_prefix = "Python-3.8.13",
    urls = ["https://www.python.org/ftp/python/3.8.13/Python-3.8.13.tar.xz"],
)

### Load python rules
http_archive(
    name = "rules_python",
    strip_prefix = "rules_python-0.8.0",
    url = "https://github.com/bazelbuild/rules_python/archive/0.8.0.tar.gz",
)

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    name = "py_deps",
    python_interpreter_target = "@python_interpreter//:python_bin",
    requirements = "//:requirements.txt",
)

register_toolchains("//:my_py_toolchain")
