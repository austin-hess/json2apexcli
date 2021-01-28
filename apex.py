from enum import Enum
import hashlib
import codecs

CURRENT_API_VERSION = '50.0'
DEFAULT_STATUS = 'Active'

class ShareType(Enum):
    WITH_SHARE = "with sharing"
    WITHOUT_SHARE = "without sharing"
    INHERIT_SHARE = "inherited sharing"
    
class ClassAccessType(Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    GLOBAL = "global"

class ClassDefinitionType(Enum):
    CONCRETE = ""
    ABSTRACT = "abstract"
    VIRTUAL = "virtual"
    INTERFACE = "interface"

class MemberAccessType(Enum):
    PUBLIC = "public"
    PRIVATE = "private"
    GLOBAL = "global"
    PROTECTED = "protected"

class Class:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.sharing = ShareType.WITHOUT_SHARE if 'sharing' not in kwargs else kwargs['sharing']
        self.access_mod = ClassAccessType.PUBLIC if 'access_mod' not in kwargs else kwargs['access_mod']
        self.definition_mod = ClassDefinitionType.CONCRETE if 'definition_mod' not in kwargs else kwargs['definition_mod']
        self.extends = [] if 'extends' not in kwargs else kwargs['extends']
        self.implements = [] if 'implements' not in kwargs else kwargs['implements']
        self.methods = [] if 'methods' not in kwargs else kwargs['methods']
        self.members = [] if 'members' not in kwargs else kwargs['members']
    
    def write(self, no_name=False):
        cls_output = (
            "{} {} {} class {} {{\n".format(self.access_mod.value, self.definition_mod.value, self.sharing.value, "" if no_name else self.name) 
                if self.definition_mod is not ClassDefinitionType.INTERFACE
            else "{} interface {} {\n".format(self.access_mod, self.name)
        )
        for member in sorted(self.members, key=lambda x: getattr(x, 'name')):
            cls_output += "\t{}\n".format(member.write())
        cls_output += "}"
        return cls_output

    @staticmethod
    def write_meta(*args,**kwargs):
        api_version = CURRENT_API_VERSION if 'api_version' not in kwargs else kwargs['api_version']
        status = DEFAULT_STATUS if 'status' not in kwargs else kwargs['status']
        return "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
                    \n<ApexClass xmlns=\"http://soap.sforce.com/2006/04/metadata\">\
                        \n\t<apiVersion>{}</apiVersion>\
                        \n\t<status>{}</status>\
                    \n</ApexClass>".format(api_version, status)
    
    def __hash__(self):
        h = hashlib.sha256()
        h.update(str.encode(self.write(no_name=True)))
        return int.from_bytes(h.digest(), byteorder="little")

    def __eq__(self, other):
        return hash(self) == hash(other)
    

class Member:
    def __init__(self, name, data_type, *args, **kwargs):
        self.name = name if name not in KEYWORDS else "{}_x".format(name)
        self.data_type = data_type
        self.access_mod = MemberAccessType.PUBLIC if 'access_mod' not in kwargs else kwargs['access_mod']
        self.is_static = False if 'is_static' not in kwargs else kwargs['is_static']
        self.is_final = False if 'is_final' not in kwargs else kwargs['is_final']
    
    def write(self):
        return "{} {}{}{} {};".format(self.access_mod.value, "static" if self.is_static else "", "final" if self.is_final else "", self.data_type, self.name)

KEYWORDS = ["abstract",
"activate",
"and",
"any",
"array",
"as",
"asc",
"autonomous",
"begin",
"bigdecimal",
"blob",
"boolean",
"break",
"bulk",
"by",
"byte",
"case",
"cast",
"catch",
"char",
"class",
"collect",
"commit",
"const",
"continue",
"currency",
"date",
"datetime",
"decimal",
"default",
"delete",
"desc",
"do",
"double",
"else",
"end",
"enum",
"exception",
"exit",
"export",
"extends",
"false",
"final",
"finally",
"float",
"for",
"from",
"global",
"goto",
"group",
"having",
"hint",
"if",
"implements",
"import",
"in",
"inner",
"insert",
"instanceof",
"int",
"integer",
"interface",
"into",
"join",
"like",
"limit",
"list",
"long",
"loop",
"map",
"merge",
"new",
"not",
"null",
"nulls",
"number",
"object",
"of",
"on",
"or",
"outer",
"override",
"package",
"parallel",
"pragma",
"private",
"protected",
"public",
"retrieve",
"return",
"rollback",
"select",
"set",
"short",
"sObject",
"sort",
"static",
"string",
"super",
"switch",
"synchronized",
"system",
"testmethod",
"then",
"this",
"throw",
"time",
"transaction",
"trigger",
"true",
"try",
"undelete",
"update",
"upsert",
"using",
"virtual",
"void",
"webservice",
"when",
"where",
"while"]