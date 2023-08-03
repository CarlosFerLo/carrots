from enum import Enum

class TagKind (Enum, str) :
    FUNCTION = "function"
    CLASS = "class"
    VARIABLE = "variable"
    MEMBER = "member"

class ScopeKind (Enum, str) :
    CLASS = "class"
    SECTION = "section"
    CHAPTER = "chapter"