#COMANDO REPORTE
import os
from .Estructura.Load import *
from .Estructura.Mbr import *
from .Estructura.Ebr import *
from .Estructura.Partition import *
from .Estructura.Super_block import *
from .Estructura.Table_inode import *
from .Estructura.Folder_block import *
from .Estructura.File_block import *
from .Estructura.Funcs import *
from Utilities.Utilities import *
from Global.Global import *

class Rep():
    
    #Contructor --------------------------------------------------------------------------------------
    
    def __init__(self):
        self.name = None
        self.path = None
        self.id = None
        self.ruta = None
        self.rutaquemada = None
        
    #Setters-----------------------------------------------------------------------------------------
    
    def set_name(self, name):
        if name == None or name == '':
            printError("\t Rep>>> Falta el nombre del reporte\n")
            return False
        self.name = name
        return True

    def set_path(self, path):
        if path == None or path == '':
            printError("\t Rep>>> Falta el path del reporte\n")
            return False
        self.path = path
        return True
    
    def set_id(self, id):
        if id == None or id == '':
            printError("\t Rep>>> Falta el id de la particion\n")
            return False
        self.id = id
        return True
    
    def set_ruta(self, ruta):
        self.ruta = ruta
        return True
    def set_rutaquemada(self):
        ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
        # ruta_proyecto tiene la carpeta padre Comandos, se la quitamos /server/Comandos --> /server
        ruta_proyecto = os.path.dirname(ruta_proyecto)
        # Define la ruta relativa a la carpeta donde quieres crear el archivo (por ejemplo, "reportes")
        carpeta_reportes = "Reportes"

        # Combina la ruta del proyecto con la ruta de la carpeta de reportes
        self.rutaquemada = os.path.join(ruta_proyecto, carpeta_reportes)
        #reporte = 'r\'' + reporte + '\''
        # Obtener el nombre del archivo y la extensión
        nombre_archivo, extension = os.path.splitext(os.path.basename(self.path))
        #le quitamos el punto a la extension
        extension = extension[1:]           
            
        #ruta final con el nombre y la extension en la ruta quemada
        self.rutaquemada = self.rutaquemada + "/" + nombre_archivo + "." + extension 
        
    
    #Definir el REP--------------------------------------------------------------------------------
    
    def run(self, name, path, id, ruta):
        if(not self.set_name(name)): return False
        if(not self.set_path(path)): return False
        if(not self.set_id(id)): return False
        if(not self.set_ruta(ruta)): return False
        self.set_rutaquemada()
        
        if(self.crear_reporte()):
            printText("\t Rep>>> Reporte creado con exito\n")
            return True
        return False
    
    #Crear un reporte-----------------------------------------------------------------------------------
    
    def crear_reporte(self):
        #Se verifica que exista la particion
        crrpartition = buscar_particion(self.id)
        
        if crrpartition == None:
            printError("\t Rep>>> No existe la particion\n")
            return False
        
        #Se hace un switch para saber que reporte se va a crear
        match self.name.lower():
            case 'mbr':
                if self.reporte_mbr(crrpartition):
                    return True
                return False
            case 'disk':
                if self.reporte_disk(crrpartition):
                    return True
                return False
            case 'bm_inode':
                if self.reporte_bm_inode(crrpartition):
                    return True
                return False
            case 'bm_block':
                if self.reporte_bm_block(crrpartition):
                    return True
                return False
            case 'tree':
                if self.reporte_tree(crrpartition):
                    return True
                return False
            case 'sb':
                if self.reporte_sb(crrpartition):
                    return True
                return False
            case 'file':
                if self.reporte_file(crrpartition):
                    return True
                return False
            case _:
                printError("\t Rep>>> No existe el reporte\n")
                return False

    #Reporte MBR --------------------------------------------------------------------------------------
    def reporte_mbr(self, mtpartition):
        try:
            #Se abre el archivo con el path donde esta ubicado el Disco
            file = open(mtpartition.path, "rb+")
            crr_mbr = Mbr()
            
            #Se lee el Mbr
            Fread_displacement(file, 0, crr_mbr)
            
            #Se crea el reporte
            reporte = "digraph G{rankdir=TB  node [shape=plaintext]"
            #Se crea la tabla
            reporte += "tabla[label = <<table border=\"0\" cellborder=\"1\" cellspacing=\"0\">"
            #Se crea el encabezado
            reporte += "<tr><td colspan=\"2\" bgcolor=\"#5004a4\"><font color=\"white\"><b>REPORTE DEL MBR</b></font></td></tr>"
            
            reporte += crr_mbr.generar_reporte(mtpartition.path)
            
            #Se cierra la tabla
            reporte += "</table>>];}"
            
            
            #Se cierra el archivo
            file.close()
            
            if self.CreateGraph(reporte):
                return True
            
            return False
        except Exception as e:
            printError("\t Rep>>> Error al crear el reporte MBR\n")
            print(e)
            return False
    
    #Reporte DISK --------------------------------------------------------------------------------------
    def reporte_disk(self, mtpartition):
        try :
            #Se abre el archivo con el path donde esta ubicado el Disco
            file = open(mtpartition.path, "rb+")
            crr_mbr = Mbr()
            
            #Se lee el Mbr
            Fread_displacement(file, 0, crr_mbr)
            
            #Se crea el reporte
            reporte = "digraph G{ rankdir=TB  node [shape=plaintext]"
            #Se crea la tabla
            reporte += "tabla[label = <<table border=\"1\" cellborder=\"1\" cellspacing=\"0\">"

            completesize = crr_mbr.mbr_tamano
            
            #porcetaje del mbr
            
            #Se crea el bloque MBR
            reporte += "<tr><td rowspan=\"2\" ><b>MBR</b></td>"
            
            #se recorren las particiones
            seek = 133            
            cont = 0
            porcenext = 0
            for partition in crr_mbr.mbr_partition:
                if(partition.part_status.decode() == '0'):
                    porcentaje = ((partition.part_start - seek) * 100) / completesize
                    porcentaje = round(porcentaje, 2)
                    reporte += "<td rowspan=\"2\" width=\"" + str(porcentaje) + "%\"><b>Libre " + str(porcentaje) +"%" +" del disco</b></td>"
                    seek = partition.part_start + partition.part_size
                    continue
                #Se calcula el porcentaje de la particion
                porcentaje = (partition.part_size * 100) / completesize
                porcentaje = round(porcentaje, 2)
                if partition.part_type.decode().lower() != 'e':
                    #Se crea el bloque de la particion
                    reporte += "<td rowspan=\"2\" width=\"" + str(porcentaje) + "%\"><b> Primaria " + str(porcentaje) + "%" +" del disco</b></td>"
                    seek = partition.part_start + partition.part_size
                    continue
                porcenext = porcentaje
                startp = partition.part_start
                while (startp != -1):
                    if(startp > seek):
                        porcentaje = ((startp - seek) * 100) / completesize
                        porcentaje = round(porcentaje, 2)
                        reporte += "<td width=\"" + str(porcentaje) + "%\"><b>Libre " + str(porcentaje) +"%" +" del disco</b></td>"
                        seek = startp
                        cont += 1
                        continue
                    ebr = Ebr()
                    Fread_displacement(file, startp, ebr)                    
                    porcentaje = (ebr.part_size * 100) / completesize
                    porcentaje = round(porcentaje, 2)
                    #Se crea el bloque de la particion
                    reporte += "<td>EBR</td><td width=\"" + str(porcentaje) + "%\"><b> Logica " + str(porcentaje) + "%"+" del disco</b></td>"
                    startp = ebr.part_next
                    seek = startp
                    cont += 2            
            reporte += "</tr>"
            if (cont > 0):
                reporte += "<tr>"                
                reporte += "<td colspan=\"" + str(cont) + "\"><b>Extendida "+ str(porcenext) + "%" +" del disco</b></td>"
                reporte += "</tr>"
            #Se cierra la tabla
            reporte += "</table>>];}"
            
            
            #Se cierra el archivo
            file.close()
            
            if self.CreateGraph(reporte):
                return True
            
            return False
            
        
        except Exception as e:
            printError("\t Rep>>> Error al crear el reporte MBR\n")
            print(e)
            return False
        
    #Reporte SB --------------------------------------------------------------------------------------
    def reporte_sb(self, mtpartition):
        try:        
            temp_suberBlock = Super_block()
            
            file = open(mtpartition.path, "rb+")
            
            WriteStart = mtpartition.partition.part_start
            
            #Si es una particion logica se le suma el inicio de la particion extendida
            if mtpartition.islogic:
                WriteStart += struct.calcsize(Ebr().get_const())
                Fread_displacement(file, mtpartition.partition.part_start + struct.calcsize(Ebr().get_const(), temp_suberBlock))
            else:
                Fread_displacement(file, mtpartition.partition.part_start, temp_suberBlock)
                
            #Se crea el reporte
            reporte = "digraph G{ rankdir=TB  node [shape=plaintext]"
            #Se crea la tabla
            reporte += "tabla[label = <<table border='1' cellborder='1' cellspacing='0'>"
            #Se crea el encabezado
            reporte += "<tr><td colspan='2' bgcolor='#00952d'><font color='white'><b>REPORTE DEL SUPER BLOQUE</b></font></td></tr>"
            
            reporte += temp_suberBlock.generar_reporte()
            
            #Se cierra la tabla
            reporte += "</table>>];}"
            
            #Se cierra el archivo
            file.close()
            
            if self.CreateGraph(reporte):
                return True

            return False
        except Exception as e:
            printError("\t Rep>>> Error al crear el reporte SB\n")
            print(e)
            return False
    
     
        
    #Reporte BM_INODE --------------------------------------------------------------------------------------
    def bytes_to_binary_string(self, byte_data):
        return ''.join(['1' if b == 1 else '0' for b in byte_data])
    
    def reporte_bm_inode(self, mtpartition):
        try:
            temp_suberBlock = Super_block()
            file = open(mtpartition.path, "rb+")
            WriteStart = mtpartition.partition.part_start
            
            #Si es una particion logica se le suma el inicio de la particion extendida
            if mtpartition.islogic:
                WriteStart += struct.calcsize(Ebr().get_const())
                Fread_displacement(file, mtpartition.partition.part_start + struct.calcsize(Ebr().get_const(), temp_suberBlock))
            else:
                Fread_displacement(file, mtpartition.partition.part_start, temp_suberBlock)
                
            #Se obtiene el inicio del bitmap de inodos
            inciobitmapinodo = temp_suberBlock.bm_inode_start
            
            bitmap = Fread_displacement_normal(file, inciobitmapinodo, temp_suberBlock.bm_block_start)
            
            
            # Convertir los bytes en una cadena de 1s y 0s
            bitmap_binary = self.bytes_to_binary_string(bitmap)

            # Dividir la cadena binaria en grupos de 20 caracteres
            segment_size = 20
            segments = [bitmap_binary[i:i+segment_size] for i in range(0, len(bitmap_binary), segment_size)]

            # Unir los segmentos con saltos de línea
            reporte = '\n'.join(segments)

            # Cerrar el archivo original
            file.close()
            print(self.rutaquemada)
            with open(self.rutaquemada, "w") as file:
                file.write(reporte)         
            
            return True
        except Exception as e:
            printError("\t Rep>>> Error al crear el reporte BM_INODE\n")
            print(e)
            return False
        
    #Reporte BM_BLOCK --------------------------------------------------------------------------------------
    
    def reporte_bm_block(self, mtpartition):
        try:
            temp_suberBlock = Super_block()
            file = open(mtpartition.path, "rb+")
            WriteStart = mtpartition.partition.part_start
            
            #Si es una particion logica se le suma el inicio de la particion extendida
            if mtpartition.islogic:
                WriteStart += struct.calcsize(Ebr().get_const())
                Fread_displacement(file, mtpartition.partition.part_start + struct.calcsize(Ebr().get_const(), temp_suberBlock))
            else:
                Fread_displacement(file, mtpartition.partition.part_start, temp_suberBlock)
                
            #Se obtiene el inicio del bitmap de inodos
            inciobitmapblock = temp_suberBlock.bm_block_start
            
            bitmap = Fread_displacement_normal(file, inciobitmapblock, temp_suberBlock.inode_start)
            
            
            # Convertir los bytes en una cadena de 1s y 0s
            bitmap_binary = self.bytes_to_binary_string(bitmap)

            # Dividir la cadena binaria en grupos de 20 caracteres
            segment_size = 20
            segments = [bitmap_binary[i:i+segment_size] for i in range(0, len(bitmap_binary), segment_size)]

            # Unir los segmentos con saltos de línea
            reporte = '\n'.join(segments)

            # Cerrar el archivo original
            file.close()

            with open(self.rutaquemada, "w") as file:
                file.write(reporte)         
            
            return True
        except Exception as e:
            printError("\t Rep>>> Error al crear el reporte BM_BLOCK\n")
            print(e)
            return False
        
        
    #Reporte TREE --------------------------------------------------------------------------------------
    def reporte_tree(self, mtpartition):
        try:
            temp_suberBlock = Super_block()
            file = open(mtpartition.path, "rb+")
            WriteStart = mtpartition.partition.part_start
            
            #Si es una particion logica se le suma el inicio de la particion extendida
            if mtpartition.islogic:
                WriteStart += struct.calcsize(Ebr().get_const())
                Fread_displacement(file, mtpartition.partition.part_start + struct.calcsize(Ebr().get_const(), temp_suberBlock))
            else:
                Fread_displacement(file, mtpartition.partition.part_start, temp_suberBlock)
                
            #Se obtiene el inicio del inodo
            reporte = "digraph G{ graph [pad=\"0.5\", nodesep=\"0.5\", ranksep=\"1\"];node [shape=plaintext] rankdir=LR;"
            reporte += reporteTree(self.id)
            reporte += "}"
            
            file.close()
            
            if self.CreateGraph(reporte):
                return True
            return False
        except Exception as e:
            printError("\t Rep>>> Error al crear el reporte TREE\n")
            print(e)
            return False
    
        
    #Reporte FILE --------------------------------------------------------------------------------------
    def reporte_file(self, mtpartition):
        try:    
            
            vecArch = getFileContentFromPath(self.id, self.ruta)
            
            contenidoarch = ['']
            for contenido in vecArch:
                contenidoarch[0] = contenidoarch[0] + contenido[0]
            
            contenidoleido = "Contenido del archivo " + self.ruta + ":\n"
            contenidoleido = contenidoleido + contenidoarch[0]
            
            with open(self.rutaquemada, "w") as file:
                file.write(contenidoleido)         
            
            return True
            
        except Exception as e:
            printError("\t Rep>>> Error al crear el reporte FILE\n")
            print(e)
            return False
    
    
    #Funcion para crear la grafica con graphviz---------------------------------------------------------------------------
    
    def CreateGraph(self, reporte):
        try:            
            ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
            # ruta_proyecto tiene la carpeta padre Comandos, se la quitamos /server/Comandos --> /server
            ruta_proyecto = os.path.dirname(ruta_proyecto)
                # Define la ruta relativa a la carpeta donde quieres crear el archivo (por ejemplo, "reportes")
            carpeta_reportes = "Reportes"

                # Combina la ruta del proyecto con la ruta de la carpeta de reportes
            self.rutaquemada = os.path.join(ruta_proyecto, carpeta_reportes)
            #reporte = 'r\'' + reporte + '\''
            # Obtener el nombre del archivo y la extensión
            nombre_archivo, extension = os.path.splitext(os.path.basename(self.path))
            #le quitamos el punto a la extension
            extension = extension[1:]           
            
            # ESCRIBO EL ARCHIVO TXT 
            documento = self.rutaquemada + "/" + nombre_archivo + ".txt"
            
            #ruta final con el nombre y la extension en la ruta quemada
            self.rutaquemada = self.rutaquemada + "/" + nombre_archivo + "." + extension 

            with open(documento, 'w', encoding='unicode_escape') as archivo:
                archivo.write(reporte)

            # GENERO LA IMAGEN
            
            os.system("dot -T" + extension + " " + documento + " -o " + self.rutaquemada)
            
            return True
        except Exception as e:
            printError("\t Rep>>> Error al crear el reporte MBR\n")
            print(e)
            return False
    
        