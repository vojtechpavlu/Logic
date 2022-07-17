""""""

from typing import Iterable


class Declaration:
    """"""

    def __init__(self, declaration_name: str, value: bool):
        """"""
        self._declaration_name = declaration_name
        self._value = value

    @property
    def declaration_name(self) -> str:
        return self._declaration_name

    @property
    def value(self) -> bool:
        return self._value


class Environment:
    """"""

    def __init__(self):
        self._declarations: list[Declaration] = []

    @property
    def declarations(self) -> tuple[Declaration]:
        """"""
        return tuple(self._declarations)

    @property
    def declaration_names(self) -> tuple[str]:
        """"""
        return tuple(map(lambda d: str(d.declaration_name), self.declarations))

    @property
    def size(self) -> int:
        """"""
        return len(self.declarations)

    @property
    def is_empty(self) -> bool:
        """"""
        return self.size == 0

    def declaration(self, declaration_name: str) -> Declaration:
        """"""
        for declaration in self.declarations:
            if declaration.declaration_name == declaration_name:
                return declaration

    def has_declaration(self, declaration_name: str) -> bool:
        """"""
        return self.declaration(declaration_name) is not None

    def add_declaration(self, declaration: Declaration):
        """"""
        if not self.has_declaration(declaration.declaration_name):
            self._declarations.append(declaration)
        else:
            raise Exception(f"Declaration '{declaration.declaration_name}' "
                            f"is already registered.")

    def add_values(self, declaration_name: str, value: bool):
        """"""
        self.add_declaration(Declaration(declaration_name, value))

    def add_all_declarations(self, declarations: Iterable[Declaration]):
        """"""
        for declaration in declarations:
            self.add_declaration(declaration)





