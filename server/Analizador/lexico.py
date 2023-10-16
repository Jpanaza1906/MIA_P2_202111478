import ply.lex as lex

# Lista de palabras reservadas
reserved = {
    #COMANDOS    
    'execute': 'EXECUTE',
    'mkdisk': 'MKDISK',
    'rmdisk': 'RMDISK',
    'fdisk': 'FDISK',
    'mount': 'MOUNT',
    'mkfs': 'MKFS',
    'login': 'LOGIN',
    'logout': 'LOGOUT',
    'mkgrp': 'MKGRP',  
    'rmgrp': 'RMGRP',
    'mkusr': 'MKUSR',
    'rmusr': 'RMUSR',
    'mkfile': 'MKFILE',
    'mkdir': 'MKDIR',
    'pause': 'PAUSE',
    'rep': 'REP',
    #PARAMETROS
    '-path': 'PATH',
    '-unit': 'UNIT',
    '-fit': 'FIT',
    '-size': 'SIZE',
    '-name': 'NAME',
    '-type': 'TYPE',
    '-delete': 'DELETE',
    '-id': 'ID_CMD',
    '-add': 'ADD',
    '-fs': 'FS',
    '-user': 'USER',
    '-pass': 'PASS',
    '-grp': 'GRP',
    '-r': 'R',
    '-cont': 'CONT',
    '-ruta': 'RUTAC',
}

# Lista de tokens
tokens = [
    'ID',
    'RUTA',
    'IGUAL',
    'NUMERO',
    'CADENA',
] + list(reserved.values())

# Expresiones regulares para tokens simples
t_RUTA = r'\/[^\.\r\n\" ]*'
t_NUMERO = r'\d+'
t_IGUAL = r'\='
t_CADENA = r'\"[^\r\n\"]*\"'


# Función para manejar palabras reservadas
def t_ID(t):
    r'[a-zA-Z_-][a-zA-Z0-9_-]*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t


# Función para manejar saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_COMMENT(t):
    r'\#\s*.*'
    pass

# Ignorar espacios y tabulaciones
t_ignore = ' \t'



# Función para manejar errores de token
def t_error(t):
    #print(f"Carácter inesperado: '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

