from pydantic import ConfigDict
import json

from ..base import BaseTag, BaseRawTag

class VariableRawTag (BaseRawTag):
    """ Base class for raw variable tags. Raw variable tags are used to generate variable tags.

    Atributes:
        name (str): The name of the tag.
        path (Path): The path to the file containing the tag.
        pattern (Pattern): The pattern used to find the tag in the file.    
    """
    
    model_config = ConfigDict(
        extra="forbid"
    )
    
    @staticmethod
    def parse (line: str) -> 'VariableRawTag' :
        """ Parses a raw variable tag from a string.
        
        Args:
            line (str): The string to parse.
        
        Returns:
            VariableRawTag: The parsed raw variable tag.
            
        Raises:
            ValueError: If the string does not contain a valid raw variable tag.
        """
        dict = json.loads(line)
        
        if not "name" in dict :
            raise ValueError("Invalid variable tag: name not found.")
        if not "path" in dict :
            raise ValueError("Invalid variable tag: path not found.")
        if not "pattern" in dict :
            raise ValueError("Invalid variable tag: pattern not found.")
        
        return VariableRawTag(
            name=dict["name"],
            path=dict["path"],
            pattern=dict["pattern"]
        )
    
class VariableTag (BaseTag):
    """ Base class for variable tags. Variable tags are generated from raw variable tags.

    Atributes:
        name (str): The name of the tag.
        path (Path): The path to the file containing the tag.
        pattern (Pattern): The pattern used to find the tag in the file.
        
        description (str): The description of the tag.
        type (str): The type of the variable.
        * not implemented * value (str): The value of the variable.
    """
    
    type: str
    # value: str # TODO: decide if this is needed, and if so, how to implement it.
    
    model_config = ConfigDict(
        extra="forbid"
    )
    
    # TODO: Add a raw tag consumer. RawTag -> Tag.