from pydantic import ConfigDict
from typing import List, Tuple
import json

from ..base import BaseTag, BaseRawTag, FunctionInput

class FunctionRawTag (BaseRawTag):
    """ Base class for raw function tags. Raw function tags are used to generate function tags.

    Atributes:
        name (str): The name of the tag.
        path (Path): The path to the file containing the tag.
        pattern (Pattern): The pattern used to find the tag in the file.
        signature (str): The signature of the function.
    """
    
    signature: str
    
    model_config = ConfigDict(
        extra="forbid"
    )
    
    def __init__(self, name: str, path: str, pattern: str, signature: str):
        super().__init__(name=name, path=path, pattern=pattern)
        self.signature = signature
        
    @staticmethod
    def parse (line: str) -> 'FunctionRawTag':
        """ Parses a raw function tag from a string.
        
        Args:
            line (str): The string to parse.
            
        Returns:
            FunctionRawTag: The parsed raw function tag.
            
        Raises:
            ValueError: If the string does not contain a valid raw function tag.
        """
        dict = json.loads(line)
        
        if not "name" in dict :
            raise ValueError("Invalid function tag: name not found.")
        if not "path" in dict :
            raise ValueError("Invalid function tag: path not found.")
        if not "pattern" in dict :
            raise ValueError("Invalid function tag: pattern not found.")
        if not "signature" in dict :
            raise ValueError("Invalid function tag: signature not found.")
        
        return FunctionRawTag(
            name=dict["name"],
            path=dict["path"],
            pattern=dict["pattern"],
            signature=dict["signature"]
        )

        
class FunctionTag (BaseTag):
    """ Base class for function tags. Function tags are generated from raw function tags.

    Atributes:
        name (str): The name of the tag.
        path (Path): The path to the file containing the tag.
        pattern (Pattern): The pattern used to find the tag in the file.
        signature (str): The signature of the function.
        
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
    