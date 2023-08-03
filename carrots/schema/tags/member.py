from pydantic import ConfigDict
from typing import List, Tuple
import json

from ..base import BaseTag, BaseRawTag, FunctionInput
from ..enums import ScopeKind

class MemberRawTag (BaseRawTag):
    """ Base class for raw member tags. Raw member tags are used to generate member tags.
    
    Atributes:
        name (str): The name of the tag.
        path (Path): The path to the file containing the tag.
        pattern (Pattern): The pattern used to find the tag in the file.
        signature (str): The signature of the member.
        scope (str): The scope of the member.
        scopeKind (ScopeKind): The kind of scope of the member. (Default: ScopeKind.CLASS)
    """
    signature: str
    scope: str
    scopeKind: ScopeKind = ScopeKind.CLASS
    
    model_config = ConfigDict(
        extra="forbid"
    )

    def __init__ (self, name: str, path: str, pattern: str, signature: str, scope: str, scopeKind: ScopeKind = ScopeKind.CLASS):
        super().__init__(name=name, path=path, pattern=pattern)
        self.signature = signature
        self.scope = scope
        self.scopeKind = scopeKind
        
    @staticmethod
    def parse (line: str) -> 'MemberRawTag':
        """ Parses a raw member tag from a string.
        
        Args:
            line (str): The string to parse.
            
        Returns:
            MemberRawTag: The parsed raw member tag.
            
        Raises:
            ValueError: If the string does not contain a valid raw member tag.
        """
        dict = json.loads(line)
        
        if not "name" in dict :
            raise ValueError("Invalid member tag: name not found.")
        if not "path" in dict :
            raise ValueError("Invalid member tag: path not found.")
        if not "pattern" in dict :
            raise ValueError("Invalid member tag: pattern not found.")
        if not "signature" in dict :
            raise ValueError("Invalid member tag: signature not found.")
        if not "scope" in dict :
            raise ValueError("Invalid member tag: scope not found.")
        if not "scopeKind" in dict :
            raise ValueError("Invalid member tag: scopeKind not found.")
        
        return MemberRawTag(
            name=dict["name"],
            path=dict["path"],
            pattern=dict["pattern"],
            signature=dict["signature"],
            scope=dict["scope"],
            scopeKind=ScopeKind(dict["scopeKind"])
        )

class MemberTag (BaseTag):
    """ Base class for member tags. Member tags are generated from raw member tags.

    Atributes:
        name (str): The name of the tag.
        path (Path): The path to the file containing the tag.
        pattern (Pattern): The pattern used to find the tag in the file.
        signature (str): The signature of the member.
        scope (str): The scope of the member.
        scopeKind (ScopeKind): The kind of scope of the member. (Default: ScopeKind.CLASS)
        
        description (str): The description of the tag.
        inputs (List[FunctionInput]): A list of the inputs of the function, their names, tyoes and default values.
        returnType (str): The type of the output of the function.
        body (str): The body of the function.
        raises (List[Tuple[str, str]]): A list of exceptions that the function can raise and their descriptions.
    """
    inputs: List[FunctionInput]
    returnType: str = "None"
    body: str
    raises: List[Tuple[str, str]] = []
    
    # TODO: Add support for decorators.
    # TODO: Add a raw tag consumer. RawTag -> Tag.
    