from ..base import SubModule


# Eine bunte Sammlung Compiler, SDKs und co
class Programmiersprachen(SubModule):
    def __init__(self):
        super().__init__(
            "programmiersprachen",
            native_packages=[
                # JS/TS/Node
                "npm",
                "pnpm",
                # PHP
                "php",
                # Java
                "jdk-openjdk",
                "jdk8-openjdk",
                "maven",
                # Python
                "python",
                "pyenv",
                # Rust
                "rust",
                # Ruby
                "ruby-bundler",
                "rbenv",
                # C
                "cmake",
                # Docker
                "docker",
                "docker-compose"
            ],
            aur_packages=[
                "python39"
            ]
        )
