import ply.yacc as yacc
from Utilities.Utilities import *
#from lexico import tokens

#================================ PRODUCCION INICIAL =================================
def p_command(p):
    '''command : execute_command
               | mkdisk_command
               | rmdisk_command
               | fdisk_command
               | mount_command
               | mkfs_command
               | login_command
               | logout_command
               | mkgrp_command
               | rmgrp_command
               | mkusr_command
               | rmusr_command
               | mkfile_command
               | mkdir_command
               | pause_command
               | rep_command
    '''
    p[0] = p[1]

# =============================== Reglas de producción para MKDISK ===============================
def p_mkdisk_command(p):
    '''mkdisk_command : MKDISK opciones'''
    #Se guarda el contenido
    p[0] = {
        'command': 'mkdisk',
        **p[2],
    }
    
def p_opciones(p):
    '''opciones : opciones opciones_element 
                | opciones_element'''
    #Se guarda el contenido
    if len(p) > 2:
        p[0] = {
            **p[1],
            **p[2]
        }
    else:
        p[0] = {
            **p[1]
        }
def p_opciones_element(p):
    '''opciones_element : opcion_size
                        | opcion_path
                        | opcion_unit
                        | opcion_fit'''
    p[0] = {
        **p[1]
    }

def p_opcion_size(p):
    '''opcion_size : SIZE IGUAL NUMERO'''
    #Se guarda el contenido
    p[0] = {
        'size': p[3]
    }

def p_opcion_path(p):
    '''opcion_path : PATH IGUAL RUTA ID
                   | PATH IGUAL CADENA'''
    #Se guarda el contenido
    if len(p) == 4:
        p[3] = p[3][1:len(p[3])-1]  
        p[0] = {
            'path': p[3]
        }
    else:
        p[0] = {
            'path': p[3] + '.' + p[4]
        }

def p_opcion_unit(p):
    '''opcion_unit : UNIT IGUAL ID'''
    #Se guarda el contenido
    p[0] = {
        'unit': p[3]
    }

def p_opcion_fit(p):
    '''opcion_fit : FIT IGUAL ID'''
    #Se guarda el contenido
    p[0] = {
        'fit': p[3]
    }
    
# =============================== FIN MKDISK ===============================

# =============================== Reglas de producción para EXECUTE ===============================
def p_execute_command(p):
    '''execute_command : EXECUTE PATH IGUAL RUTA ID
                       | EXECUTE PATH IGUAL CADENA'''
    #Se guarda el contenido
    if len(p) == 6:
        p[0] = {
            'command': 'execute',
            'path': p[4] + '.' +p[5]
        }
    else:
        p[4] = p[4][1:len(p[4])-1]
        p[0] = {
            'command': 'execute',
            'path': p[4]
        }
    
# =============================== FIN EXECUTE ===============================

#============================== Reglas de producción para RMDISK ===============================
def p_rmdisk_command(p):
    '''rmdisk_command : RMDISK PATH IGUAL RUTA ID
                      | RMDISK PATH IGUAL CADENA'''
                    
    #Se guarda el contenido
    if len(p) == 6:
        p[0] = {
            'command': 'rmdisk',
            'path': p[4] + '.' + p[5]
        }
    else:
        p[4] = p[4][1:len(p[4])-1]
        p[0] = {
            'command': 'rmdisk',
            'path': p[4]
        }
#============================== FIN RMDISK ===============================

#============================== Reglas de producción para FDISK ===============================
def p_fdisk_command(p):
    '''fdisk_command : FDISK opciones_fdisk'''
    #Se guarda el contenido
    p[0] = {
        'command': 'fdisk',
        **p[2],
    }
def p_opciones_fdisk(p):
    '''opciones_fdisk : opciones_fdisk opciones_element_fdisk 
                      | opciones_element_fdisk'''
    #Se guarda el contenido
    if len(p) > 2:
        p[0] = {
            **p[1],
            **p[2]
        }
    else:
        p[0] = {
            **p[1]
        }
def p_opciones_element_fdisk(p):
    '''opciones_element_fdisk : opcionfdisk_size
                              | opcionfdisk_path
                              | opcionfdisk_name
                              | opcionfdisk_unit
                              | opcionfdisk_type
                              | opcionfdisk_fit
                              | opcionfdisk_delete
                              | opcionfdisk_add'''
    p[0] = {
        **p[1]
    }
def p_opcionfdisk_size(p):
    '''opcionfdisk_size : SIZE IGUAL NUMERO'''
    #Se guarda el contenido
    p[0] = {
        'size': p[3]
    }
def p_opcionfdisk_path(p):
    '''opcionfdisk_path : PATH IGUAL RUTA ID
                        | PATH IGUAL CADENA'''
    #Se guarda el contenido
    if len(p) == 4:
        p[3] = p[3][1:len(p[3])-1]  
        p[0] = {
            'path': p[3]
        }
    else:
        p[0] = {
            'path': p[3] + '.' + p[4]
        }
def p_opcionfdisk_name(p):
    '''opcionfdisk_name : NAME IGUAL ID
                        | NAME IGUAL CADENA'''
    #Se guarda el contenido
    if(p[3][0] == '\"'):
            p[3] = p[3][1:len(p[3])-1] 
    p[0] = {
        'name': p[3]
    }
def p_opcionfdisk_unit(p):
    '''opcionfdisk_unit : UNIT IGUAL ID'''
    #Se guarda el contenido
    p[0] = {
        'unit': p[3]
    }
def p_opcionfdisk_type(p):
    '''opcionfdisk_type : TYPE IGUAL ID'''
    #Se guarda el contenido
    p[0] = {
        'type': p[3]
    }
def p_opcionfdisk_fit(p):
    '''opcionfdisk_fit : FIT IGUAL ID'''
    #Se guarda el contenido
    p[0] = {
        'fit': p[3]
    }
def p_opcionfdisk_delete(p):
    '''opcionfdisk_delete : DELETE IGUAL ID'''
    #Se guarda el contenido
    p[0] = {
        'delete': p[3]
    }
def p_opcionfdisk_add(p):
    '''opcionfdisk_add : ADD IGUAL NUMERO
                       | ADD IGUAL ID'''
    #Se guarda el contenido
    p[0] = {
        'add': p[3]
    }
#============================== FIN FDISK =====================================================================
#==============================COMANDO MOUNT===================================================================
def p_mount_command(p):
    '''mount_command : MOUNT opciones_mount'''
    p[0] = {
        'command': 'mount',
        **p[2],
    }
def p_opciones_mount(p):
    '''opciones_mount : opciones_mount opciones_element_mount 
                      | opciones_element_mount'''
    #Se guarda el contenido
    if len(p) > 2:
        p[0] = {
            **p[1],
            **p[2]
        }
    else:
        p[0] = {
            **p[1]
        }
def p_opciones_element_mount(p):
    '''opciones_element_mount : opcionmount_path
                              | opcionmount_name'''
    p[0] = {
        **p[1]
    }
def p_opcionmount_path(p):
    '''opcionmount_path : PATH IGUAL RUTA ID
                        | PATH IGUAL CADENA'''
    #Se guarda el contenido
    if len(p) == 4:
        p[3] = p[3][1:len(p[3])-1]  
        p[0] = {
            'path': p[3]
        }
    else:
        p[0] = {
            'path': p[3] + '.' + p[4]
        }
def p_opcionmount_name(p):
    '''opcionmount_name : NAME IGUAL ID
                        | NAME IGUAL CADENA'''
    #Se guarda el contenido
    if(p[3][0] == '\"'):
            p[3] = p[3][1:len(p[3])-1] 
    p[0] = {
        'name': p[3]
    }
    
#====================FIN COMANDO MOUNT===================================================================
#=====================COMANDO MKFS=========================================================================
def p_mkfs_command(p):
    '''mkfs_command : MKFS opciones_mkfs'''
    p[0] = {
        'command': 'mkfs',
        **p[2],
    }
def p_opciones_mkfs(p):
    '''opciones_mkfs : opciones_mkfs opciones_element_mkfs 
                      | opciones_element_mkfs'''
    #Se guarda el contenido
    if len(p) > 2:
        p[0] = {
            **p[1],
            **p[2]
        }
    else:
        p[0] = {
            **p[1]
        }
def p_opciones_element_mkfs(p):
    '''opciones_element_mkfs : opcionmkfs_id
                              | opcionmkfs_type
                              | opcionmkfs_fs'''
    p[0] = {
        **p[1]
    }
def p_opcionmkfs_id(p):
    '''opcionmkfs_id : ID_CMD IGUAL NUMERO ID'''
    #Se guarda el contenido
    p[0] = {
        'id': p[3] + p[4]
    }
def p_opcionmkfs_type(p):
    '''opcionmkfs_type : TYPE IGUAL ID'''
    #Se guarda el contenido
    p[0] = {
        'type': p[3]
    }
def p_opcionmkfs_fs(p):
    '''opcionmkfs_fs : FS IGUAL NUMERO ID'''
    #Se guarda el contenido
    p[0] = {
        'fs': p[3] + p[4]
    }
    
#====================FIN COMANDO MKFS===================================================================
#======================COMANDO LOGIN====================================================================
def p_login_command(p):
    '''login_command : LOGIN opciones_login'''
    p[0] = {
        'command': 'login',
        **p[2],
    }
def p_opciones_login(p):
    '''opciones_login : opciones_login opciones_element_login 
                      | opciones_element_login'''
    #Se guarda el contenido
    if len(p) > 2:
        p[0] = {
            **p[1],
            **p[2]
        }
    else:
        p[0] = {
            **p[1]
        }
def p_opciones_element_login(p):
    '''opciones_element_login : opcionlogin_usr
                              | opcionlogin_pwd
                              | opcionlogin_id'''
    p[0] = {
        **p[1]
    }
def p_opcionlogin_usr(p):
    '''opcionlogin_usr : USER IGUAL ID
                        | USER IGUAL CADENA'''
    #Se guarda el contenido    
    if(p[3][0] == '\"'):
            p[3] = p[3][1:len(p[3])-1] 
    p[0] = {        
        'user': p[3]
    }
def p_opcionlogin_pwd(p):
    '''opcionlogin_pwd : PASS IGUAL ID
                        | PASS IGUAL NUMERO
                        | PASS IGUAL CADENA
                        | PASS IGUAL NUMERO ID'''
                        
    #Se guarda el contenido
    if(len(p) == 4):
        if(p[3][0] == '\"'):
            p[3] = p[3][1:len(p[3])-1]            
        p[0] = {
            'pass': p[3]
        }
    elif(len(p) == 5):
        p[0] = {
            'pass': p[3] + p[4]
        }
def p_opcionlogin_id(p):
    '''opcionlogin_id : ID_CMD IGUAL NUMERO ID'''
    #Se guarda el contenido
    p[0] = {
        'id': p[3] + p[4]
    }
#====================FIN COMANDO LOGIN===================================================================
#=======================COMANDO LOGOUT===================================================================
def p_logout_command(p):
    '''logout_command : LOGOUT'''
    p[0] = {
        'command': 'logout',
    }
#====================FIN COMANDO LOGOUT===================================================================
#========================COMANDO MKGRP===================================================================
def p_mkgrp_command(p):
    '''mkgrp_command : MKGRP NAME IGUAL ID
                     | MKGRP NAME IGUAL CADENA'''
                     
    if(p[4][0] == '\"'):
        p[4] = p[4][1:len(p[4])-1]  
    p[0] = {
        'command': 'mkgrp',
        'name': p[4]
    }
#====================FIN COMANDO MKGRP===================================================================
#========================COMANDO RMGRP===================================================================
def p_rmgrp_command(p):
    '''rmgrp_command : RMGRP NAME IGUAL ID
                     | RMGRP NAME IGUAL CADENA'''
                     
    if(p[4][0] == '\"'):
        p[4] = p[4][1:len(p[4])-1]  
    p[0] = {
        'command': 'rmgrp',
        'name': p[4]
    }
#====================FIN COMANDO RMGRP===================================================================
#========================COMANDO MKUSR===================================================================
def p_mkusr_command(p):
    '''mkusr_command : MKUSR opciones_mkusr'''
    p[0] = {
        'command': 'mkusr',
        **p[2],
    }
def p_opciones_mkusr(p):
    '''opciones_mkusr : opciones_mkusr opciones_element_mkusr 
                      | opciones_element_mkusr'''
    #Se guarda el contenido
    if len(p) > 2:
        p[0] = {
            **p[1],
            **p[2]
        }
    else:
        p[0] = {
            **p[1]
        }
def p_opciones_element_mkusr(p):
    '''opciones_element_mkusr : opcionmkusr_usr
                              | opcionmkusr_pwd
                              | opcionmkusr_grp'''
    p[0] = {
        **p[1]
    }
def p_opcionmkusr_usr(p):
    '''opcionmkusr_usr : USER IGUAL ID
                        | USER IGUAL CADENA'''
    #Se guarda el contenido    
    if(p[3][0] == '\"'):
            p[3] = p[3][1:len(p[3])-1] 
    p[0] = {        
        'user': p[3]
    }
def p_opcionmkusr_pwd(p):
    '''opcionmkusr_pwd : PASS IGUAL ID
                        | PASS IGUAL NUMERO
                        | PASS IGUAL CADENA
                        | PASS IGUAL NUMERO ID'''
                        
    #Se guarda el contenido
    if(len(p) == 4):
        if(p[3][0] == '\"'):
            p[3] = p[3][1:len(p[3])-1]            
        p[0] = {
            'pass': p[3]
        }
    elif(len(p) == 5):
        p[0] = {
            'pass': p[3] + p[4]
        }
def p_opcionmkusr_grp(p):
    '''opcionmkusr_grp : GRP IGUAL ID
                        | GRP IGUAL CADENA'''
    #Se guarda el contenido    
    if(p[3][0] == '\"'):
            p[3] = p[3][1:len(p[3])-1] 
    p[0] = {        
        'grp': p[3]
    }
#====================FIN COMANDO MKUSR===================================================================
#========================COMANDO RMUSR===================================================================
def p_rmusr_command(p):
    '''rmusr_command : RMUSR USER IGUAL ID
                     | RMUSR USER IGUAL CADENA'''
                     
    if(p[4][0] == '\"'):
        p[4] = p[4][1:len(p[4])-1]  
    p[0] = {
        'command': 'rmusr',
        'user': p[4]
    }
#====================FIN COMANDO RMUSR===================================================================
#========================COMANDO MKFILE===================================================================
def p_mkfile_command(p):
    '''mkfile_command : MKFILE opciones_mkfile'''
    p[0] = {
        'command': 'mkfile',
        **p[2],
    }
def p_opciones_mkfile(p):
    '''opciones_mkfile : opciones_mkfile opciones_element_mkfile 
                      | opciones_element_mkfile'''
    #Se guarda el contenido
    if len(p) > 2:
        p[0] = {
            **p[1],
            **p[2]
        }
    else:
        p[0] = {
            **p[1]
        }
def p_opciones_element_mkfile(p):
    '''opciones_element_mkfile : opcionmkfile_path
                              | opcionmkfile_r
                              | opcionmkfile_size
                              | opcionmkfile_cont'''
    p[0] = {
        **p[1]
    }
def p_opcionmkfile_path(p):
    '''opcionmkfile_path : PATH IGUAL RUTA ID
                        | PATH IGUAL CADENA'''
    #Se guarda el contenido
    if len(p) == 4:
        p[3] = p[3][1:len(p[3])-1]  
        p[0] = {
            'path': p[3]
        }
    else:
        p[0] = {
            'path': p[3] + '.' + p[4]
        }
def p_opcionmkfile_r(p):
    '''opcionmkfile_r : R'''
    #Se guarda el contenido
    p[0] = {
        'r': True
    }
def p_opcionmkfile_size(p):
    '''opcionmkfile_size : SIZE IGUAL NUMERO'''
    #Se guarda el contenido
    p[0] = {
        'size': p[3]
    }
def p_opcionmkfile_cont(p):
    '''opcionmkfile_cont : CONT IGUAL CADENA
                        | CONT IGUAL RUTA ID'''
    #Se guarda el contenido
    if(len(p) == 4):
        p[3] = p[3][1:len(p[3])-1]  
        p[0] = {
            'cont': p[3]
        }
    else:
        p[0] = {
            'cont': p[3] + "." + p[4]
        }
#====================FIN COMANDO MKFILE===================================================================

#========================COMANDO MKDIR===================================================================
def p_mkdir_command(p):
    '''mkdir_command : MKDIR opciones_mkdir'''
    p[0] = {
        'command': 'mkdir',
        **p[2],
    }
def p_opciones_mkdir(p):
    '''opciones_mkdir : opciones_mkdir opciones_element_mkdir 
                      | opciones_element_mkdir'''
    #Se guarda el contenido
    if len(p) > 2:
        p[0] = {
            **p[1],
            **p[2]
        }
    else:
        p[0] = {
            **p[1]
        }
def p_opciones_element_mkdir(p):
    '''opciones_element_mkdir : opcionmkdir_path
                              | opcionmkdir_r'''
    p[0] = {
        **p[1]
    }
def p_opcionmkdir_path(p):
    '''opcionmkdir_path : PATH IGUAL RUTA
                        | PATH IGUAL CADENA'''
    #Se guarda el contenido
    if p[3][0] == '\"':
        p[3] = p[3][1:len(p[3])-1]  
   
    p[0] = {
        'path': p[3]
    }
def p_opcionmkdir_r(p):
    '''opcionmkdir_r : R'''
    #Se guarda el contenido
    p[0] = {
        'r': True
    }
    
#====================FIN COMANDO MKDIR===================================================================

#======================== PAUSE ===================================================================
def p_pause_command(p):
    '''pause_command : PAUSE'''
    p[0] = {
        'command': 'pause',
    }
#====================FIN PAUSE===================================================================

#======================== COMANDO REP ===================================================================
def p_rep_command(p):
    '''rep_command : REP opciones_rep'''
    p[0] = {
        'command': 'rep',
        **p[2],
    }
def p_opciones_rep(p):
    '''opciones_rep : opciones_rep opciones_element_rep 
                      | opciones_element_rep'''
    #Se guarda el contenido
    if len(p) > 2:
        p[0] = {
            **p[1],
            **p[2],
        }
    else:
        p[0] = {
            **p[1]
        }
def p_opciones_element_rep(p):
    '''opciones_element_rep : opcionrep_id
                              | opcionrep_path
                              | opcionrep_name
                              | opcionrep_ruta'''
    p[0] = {
        **p[1]
    }
def p_opcionrep_id(p):
    '''opcionrep_id : ID_CMD IGUAL NUMERO ID'''
    #Se guarda el contenido
    p[0] = {
        'id': p[3] + p[4]
    }
def p_opcionrep_path(p):
    '''opcionrep_path : PATH IGUAL RUTA ID
                        | PATH IGUAL RUTA
                        | PATH IGUAL CADENA'''
    #Se guarda el contenido
    if len(p) == 4:
        if(p[3][0] == '\"'):
            p[3] = p[3][1:len(p[3])-1]
        p[0] = {
            'path': p[3]
        }
    else:
        p[0] = {
            'path': p[3] + '.' + p[4]
        }
def p_opcionrep_name(p):
    '''opcionrep_name : NAME IGUAL ID
                        | NAME IGUAL CADENA'''
    #Se guarda el contenido
    if(p[3][0] == '\"'):
        p[3] = p[3][1:len(p[3])-1]
    p[0] = {
        'name': p[3]
    }
def p_opcionrep_ruta(p):
    '''opcionrep_ruta : RUTAC IGUAL RUTA ID
                        | RUTAC IGUAL RUTA
                        | RUTAC IGUAL CADENA'''
    #Se guarda el contenido
    if len(p) == 4:
        if(p[3][0] == '\"'):
            p[3] = p[3][1:len(p[3])-1]
        p[0] = {
            'ruta': p[3]
        }
    else:
        p[0] = {
            'ruta': p[3] + '.' + p[4]
        }
    
# Error rule for syntax errors
def p_error(p):
    if p != None:
        printError("\t josep-ubu@Leon-Ubuntu>>> No se reconocio el comando " + str(p) + "\n")
    pass

