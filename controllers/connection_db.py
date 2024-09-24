import sqlite3

import ctypes

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractItemView


def CreateTable(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS REGISTRO_IMOVEIS ('COD_IMOVEL' INTEGER PRIMARY KEY AUTOINCREMENT, 'DESC_CURTA' TEXT,  'TIPO_IMOVEL' TEXT, 'TIPO_NEGOCIACAO' TEXT,'STATUS' TEXT, 'PRECO' REAL, 'CONDICOES' TEXT, 'CEP' TEXT, 'RUA' TEXT, 'NUMERO' TEXT, 'COMPLEMENTO' TEXT, 'BAIRRO' TEXT, 'CIDADE' TEXT, 'ESTADO' TEXT, 'CARACTERISICAS_IMOVEL' TEXT, 'OBSERVACAO' TEXT)")
        conn.commit()
                
    except sqlite3.Error as error:
        ctypes.windll.user32.MessageBoxW(0, f"Erro {str(error)}", "Erro", 0x10)
        
    finally:
        if conn:
            conn.close()
            
            
def RegistrarImovel(path, dados):
    conn = None
    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO REGISTRO_IMOVEIS ('DESC_CURTA', 'TIPO_IMOVEL', 'TIPO_NEGOCIACAO', 'STATUS', 'PRECO', 'CONDICOES', 'CEP', 'RUA', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'CIDADE', 'ESTADO', 'CARACTERISICAS_IMOVEL',  'OBSERVACAO') VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", dados)
        conn.commit()
        
    except sqlite3.Error as error:
        ctypes.windll.user32.MessageBoxW(0, f"Erro {str(error)}", "Erro", 0x10)
        
    finally:
        if conn:
            conn.close()

def AlterarRegistroImovel(cod_imovel, dados):
    conn = None
    try:
        conn = sqlite3.connect("DB_Registro_Imovel.db")
        cursor = conn.cursor()
        cursor.execute(f"""
        UPDATE REGISTRO_IMOVEIS 
        SET {dados} 
        WHERE COD_IMOVEL = {int(cod_imovel)}""")
        conn.commit()
        
    except sqlite3.Error as error:
        ctypes.windll.user32.MessageBoxW(0, f"Erro {str(error)}", "Erro", 0x10)
        
    finally:
        if conn:
            conn.close()
                
            
def ConsultarRegistroImovel(self, filtros):
    self.tb_lista_imov.clearContents()
    self.tb_lista_imov.setRowCount(0)
    self.tb_lista_imov.setColumnCount(0)

    self.conn = sqlite3.connect("DB_Registro_Imovel.db")
    self.cursor = self.conn.cursor()
    self.cursor.execute(f"SELECT * FROM REGISTRO_IMOVEIS {filtros}")
    self.registros = self.cursor.fetchall()

    for column in self.cursor.description:
        utl_coll = self.tb_lista_imov.columnCount()
        self.tb_lista_imov.setColumnCount(utl_coll+1)
        self.tb_lista_imov.setHorizontalHeaderItem(utl_coll, QTableWidgetItem())
        self.tb_lista_imov.horizontalHeaderItem(utl_coll).setText(QCoreApplication.translate("MainWindowComprado", f"{column[0]}", None))


    for row in self.registros:
        utl_row = self.tb_lista_imov.rowCount()
        self.tb_lista_imov.setRowCount(utl_row + 1)
        for lc, column in enumerate(row):                    
            self.tb_lista_imov.setItem(utl_row, lc,QTableWidgetItem(str(column)))    

    tb_lista_imov= self.tb_lista_imov.horizontalHeader()
    tb_lista_imov.setSectionResizeMode(QHeaderView.ResizeToContents) 
    self.tb_lista_imov.setEditTriggers(QAbstractItemView.NoEditTriggers)