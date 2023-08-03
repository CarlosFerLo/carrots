from pydantic import BaseModel, ConfigDict
from typing import List
from pathlib import Path
from re import Pattern, compile

class BaseRawTag (BaseModel):
    """ Base class for carrots raw tags.
        This class is used to parse the raw tags output by the u-ctags command.

    Attributes:
        name (str): The name of the tag.
        path (Path): The path to the file containing the tag.
        pattern (Pattern): The pattern used to find the tag in the file.
    """
    name: str
    path: Path
    pattern: Pattern
    
    model_config = ConfigDict(
        extra="allow"
    )
    
    def __init__(self, name: str, path: str, pattern: str):
        """ Constructor for the BaseRawTag class. 
        
            Uses the pydantic BaseModel constructor to initialize the class.
        """
        super().__init__(name=name, path=path, pattern=pattern)
        self.name = name
        self.path = Path(path)
        self.pattern = compile(pattern)
        
class BaseTag (BaseModel):
    """ Base class for carrots tags. Tags are generated from raw tags.

    Attributes:
        name (str): The name of the tag.
        path (Path): The path to the file containing the tag.
        pattern (Pattern): The pattern used to find the tag in the file.
        
        description (str): The description of the tag.    
    """
    name: str
    path: Path
    pattern: Pattern
    
    description: str 
    
    model_config = ConfigDict(
        extra="allow"
    )
    
class BaseFile (BaseModel) :
    """ Base class for files. Files are stored in directories and contain tags.

    Atributes:
        name (str): The name of the file (without the extension)
        path (Path): The path to the file.
        tags (List[BaseTag]): A list of tags in the file.
    """
    name: str
    path: Path
    tags: List[BaseTag]
    
    model_config = ConfigDict(
        
    )
    
class Directory (BaseModel) :
    """ Class for directories. Directories contain files and other directories.
    
    Atributes:
        name (str): The name of the directory.
        path (Path): The path to the directory.
        files (List[BaseFile]): A list of files in the directory.
        directories (List[Directory]): A list of directories in the directory.
    """ 
    name: str
    path: Path
    files: List[BaseFile]
    directories: List['Directory']
    
    model_config = ConfigDict(
        
    )
    
class FunctionInput (BaseModel):
    """ Class for function inputs.
    
    Atributes:
        name (str): The name of the input.
        type (str): The type of the input.
        default (str): The default value of the input.
    """
    name: str
    type: str
    default: str
    
    model_config = ConfigDict(
        extra="forbid"
    )