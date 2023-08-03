from pydantic import ConfigDict
from typing import List
import json

from ..base import BaseTag, BaseRawTag
from .member import MemberTag

class ClassRawTag (BaseRawTag):
    """ Base class for raw class tags. Raw class tags are used to generate class tags.

    Atributes:
        name (str): The name of the tag.
        path (Path): The path to the file containing the tag.
        pattern (Pattern): The pattern used to find the tag in the file.
        
    Methods:
        parse (str) -> ClassRawTag: Parses a raw class tag from a string.
    """
    
    model_config = ConfigDict(
        extra="forbid"
    )
    
    def __init__(self, name: str, path: str, pattern: str):
        super().__init__(name=name, path=path, pattern=pattern)
        
    @staticmethod
    def parse (line: str) -> 'ClassRawTag':
        """ Parses a raw class tag from a string.
        
        Args:
            line (str): The string to parse.
            
        Returns:
            ClassRawTag: The parsed raw class tag.
            
        Raises:
            ValueError: If the string does not contain a valid raw class tag.
        """
        
        dict = json.loads(line)
        
        if "name" not in dict :
            raise ValueError("Invalid class tag: name not found.")
        if "path" not in dict :
            raise ValueError("Invalid class tag: path not found.")
        if "pattern" not in dict :
            raise ValueError("Invalid class tag: pattern not found.")

        
        return ClassRawTag(
            name=dict["name"],
            path=dict["path"],
            pattern=dict["pattern"]
        )
        
        

class ClassTag (BaseTag):
    """ Base class for class tags. Class tags are generated from raw class tags.

    Atributes:
        name (str): The name of the tag.
        path (Path): The path to the file containing the tag.
        pattern (Pattern): The pattern used to find the tag in the file.
        
        description (str): The description of the tag.
        attributes (List[Attribute]): A list of the attributes of the class.
        methods (List[MemberTag]): A list of the methods of the class.
    """
    
    # atributes : List[Attribute] TODO: Add support for attributes.
    methods : List[MemberTag]
    
    # TODO: Add a raw tag consumer. RawTag -> Tag.