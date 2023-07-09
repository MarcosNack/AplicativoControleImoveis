import sys
from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView, QAbstractItemView
from views.Ui_main_interface import Ui_MainWindow
import sqlite3

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Controle Regristro Imóveis")
        
        #-- Funções Configuração Inicialização --# 
        self.CreateTable()
        self.ConfiguracaoInicial()
        self.ConfiguracaoButtons()
        


    def ConfiguracaoInicial(self):
        #--------------------- Configuração Pagina Inicial ---------------------# 
        self.stackedWidget.setCurrentWidget(self.pg_consulta_imovel)
        self.lb_identificacao.setText("Consultar Registro Imóveis")
        self.ConsultarRegistroImovel("")
        self.qf_home.setVisible(False)    
        
        
    def ConfiguracaoButtons(self):  
        #--------------------- Configuração Button HOME ---------------------# 
        #Configução QPushButton
        self.btn_home.clicked.connect(lambda: self.qf_home.setVisible(True))
        #--------------------------------------------------------------------#

        #--------------------- Configuração ABA HOME ---------------------#
        #Configuração HOME Button Cunsultar Registo
        self.btn_home_con_regist_imovel.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_consulta_imovel))        
        self.btn_home_con_regist_imovel.clicked.connect(lambda: self.qf_home.setVisible(False))
        self.btn_home_con_regist_imovel.clicked.connect(lambda: self.lb_identificacao.setText("Consultar Registro Imóveis"))
        self.btn_home_con_regist_imovel.clicked.connect(lambda: self.ConsultarRegistroImovel(""))
        self.txt_con_imv_cep.setMaxLength(8)
        self.txt_con_imv_cep.editingFinished.connect(lambda: self.txt_con_imv_cep.setMaxLength(9))
        self.txt_con_imv_cep.editingFinished.connect(lambda: self.txt_con_imv_cep.setInputMask("00000-000"))
        
        #Configuração HOME Button registro imovel
        self.btn_home_regist_imovel.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_registrar_imovel))
        self.btn_home_regist_imovel.clicked.connect(lambda: self.qf_home.setVisible(False))
        self.btn_home_regist_imovel.clicked.connect(lambda: self.lb_identificacao.setText("Registrar Imóveis"))
        self.txt_reg_imov_cep.setMaxLength(8)
        self.txt_reg_imov_cep.editingFinished.connect(lambda: self.txt_reg_imov_cep.setMaxLength(9))
        self.txt_reg_imov_cep.editingFinished.connect(lambda: self.txt_reg_imov_cep.setInputMask("00000-000"))
        
        #Configuração HOME Button alterar registro imóvel
        self.btn_home_alt_regist_imovel.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_alterar_imovel))
        self.btn_home_alt_regist_imovel.clicked.connect(lambda: self.qf_home.setVisible(False))
        self.btn_home_alt_regist_imovel.clicked.connect(lambda: self.lb_identificacao.setText("Alterar Registro Imóveis"))

        self.txt_alt_imov_cep.setMaxLength(8)
        self.txt_alt_imov_cep.editingFinished.connect(lambda: self.txt_alt_imov_cep.setMaxLength(9))
        self.txt_alt_imov_cep.editingFinished.connect(lambda: self.txt_alt_imov_cep.setInputMask("00000-000"))
        #--------------------------------------------------------------------#

        #--------------------- Configuração page Consulta ---------------------#
        #Configução QPushButton
        self.btn_consulta_alt.clicked.connect(self.BTNConsultaAlt)
        self.btn_consulta.clicked.connect(self.FiltrosRegistrarImoveis)
        #--------------------------------------------------------------------#

        #--------------------- Configuração page Registrar imóveis ---------------------#
        #Configução QPushButton
        self.btn_registro.clicked.connect(self.BTNRegistrarImoveis)
        #Configução QLineEdit
        self.txt_reg_imov_preco.setValidator(QDoubleValidator(0.99,99.99,2))
        self.txt_reg_imov_desc_imov.setMaxLength(60)
        self.txt_reg_imov_desc_imov.editingFinished.connect(self.PreencherTxtCaracteristica)
        self.txt_reg_imov_preco.editingFinished.connect(self.PreencherTxtCaracteristica)
        self.txt_reg_imov_cond.editingFinished.connect(self.PreencherTxtCaracteristica)
        self.txt_reg_imov_cep.editingFinished.connect(self.PreencherTxtCaracteristica)
        self.txt_reg_imov_rua.editingFinished.connect(self.PreencherTxtCaracteristica)
        self.txt_reg_imov_n.editingFinished.connect(self.PreencherTxtCaracteristica)
        self.txt_reg_imov_comp.editingFinished.connect(self.PreencherTxtCaracteristica)
        self.txt_reg_imov_bairro.editingFinished.connect(self.PreencherTxtCaracteristica)
        self.txt_reg_imov_estado.editingFinished.connect(self.PreencherTxtCaracteristica)
        self.txt_reg_imov_cidade.editingFinished.connect(self.PreencherTxtCaracteristica)
        self.txt_reg_imov_cep.editingFinished.connect(lambda: self.txt_reg_imov_cep.setInputMask('00000-000')) 
        self.txt_reg_imov_desc_imov.editingFinished.connect(lambda: self.txt_reg_imov_desc_imov.setText(self.txt_reg_imov_desc_imov.text().upper())) 

        #Configução QComboBox
        self.cmb_reg_imov_tp_neg.currentTextChanged.connect(self.PreencherTxtCaracteristica)
        self.cmb_reg_imov_status.currentTextChanged.connect(self.PreencherTxtCaracteristica)
        self.cmb_reg_imov_tp_imov.currentTextChanged.connect(self.PreencherTxtCaracteristica)
        #-------------------------------------------------------------------------------#

        #--------------------- Configuração page Alterar Registrar imóveis ---------------------#
        #Configução QPushButton
        self.btn_alterar.clicked.connect(self.BTNAlterarRegistrarImoveis)
        #Configução QLineEdit
        self.txt_alt_imov_desc_imov.editingFinished.connect(self.PreencherTxtCaracteristicaAlteracao)
        self.txt_alt_imov_preco.editingFinished.connect(self.PreencherTxtCaracteristicaAlteracao)
        self.txt_alt_imov_cond.editingFinished.connect(self.PreencherTxtCaracteristicaAlteracao)
        self.txt_alt_imov_cep.editingFinished.connect(self.PreencherTxtCaracteristicaAlteracao)
        self.txt_alt_imov_rua.editingFinished.connect(self.PreencherTxtCaracteristicaAlteracao)
        self.txt_alt_imov_n.editingFinished.connect(self.PreencherTxtCaracteristicaAlteracao)
        self.txt_alt_imov_comp.editingFinished.connect(self.PreencherTxtCaracteristicaAlteracao)
        self.txt_alt_imov_bairro.editingFinished.connect(self.PreencherTxtCaracteristicaAlteracao)
        self.txt_alt_imov_estado.editingFinished.connect(self.PreencherTxtCaracteristicaAlteracao)
        self.txt_alt_imov_cidade.editingFinished.connect(self.PreencherTxtCaracteristicaAlteracao)
        #Configução QComboBox
        self.cmb_alt_imov_tp_negoc.currentTextChanged.connect(self.PreencherTxtCaracteristicaAlteracao)
        self.cmb_alt_imov_status.currentTextChanged.connect(self.PreencherTxtCaracteristicaAlteracao)
        self.cmb_alt_imov_tp_imov.currentTextChanged.connect(self.PreencherTxtCaracteristicaAlteracao)
        #--------------------------------------------------------------------------------------#

    def BTNConsultaAlt(self):
        #ls = Linha selecionada tabela registro imoveis pagina consulta
        ls = self.tb_lista_imov.currentRow()
        if ls != -1:
            self.txt_alt_imov_cod_imov.setText(self.tb_lista_imov.item(ls, 0).text())
            self.txt_alt_imov_desc_imov.setText(self.tb_lista_imov.item(ls, 1).text())
            self.cmb_alt_imov_tp_imov.setCurrentText(self.tb_lista_imov.item(ls, 2).text())

            self.cmb_alt_imov_tp_negoc.setCurrentText(self.tb_lista_imov.item(ls, 3).text())
            self.cmb_alt_imov_status.setCurrentText(self.tb_lista_imov.item(ls, 4).text())
            self.txt_alt_imov_preco.setText(self.tb_lista_imov.item(ls, 5).text())
            self.txt_alt_imov_cond.setText(self.tb_lista_imov.item(ls, 6).text())

            self.txt_alt_imov_cep.setText(self.tb_lista_imov.item(ls, 7).text())
            self.txt_alt_imov_rua.setText(self.tb_lista_imov.item(ls, 8).text())
            self.txt_alt_imov_n.setText(self.tb_lista_imov.item(ls, 9).text())
            self.txt_alt_imov_comp.setText(self.tb_lista_imov.item(ls, 10).text())
            self.txt_alt_imov_bairro.setText(self.tb_lista_imov.item(ls, 11).text())
            self.txt_alt_imov_cidade.setText(self.tb_lista_imov.item(ls, 12).text())
            self.txt_alt_imov_estado.setText(self.tb_lista_imov.item(ls, 13).text())
            self.ptxt_alt_imov_obs.setPlainText(self.tb_lista_imov.item(ls, 14).text())
            self.ptxt_alt_imov_caract.setPlainText(self.tb_lista_imov.item(ls, 15).text())

            self.stackedWidget.setCurrentWidget(self.pg_alterar_imovel)

        else:
            self.MsgErro("Não foi selecionado nenhum imóvel.")


    def PreencherTxtCaracteristicaAlteracao(self):
        caract_imovel = []
        if self.txt_alt_imov_desc_imov.text() != "":
            caract_imovel.append(f"Descrição do Imóvel: {self.txt_alt_imov_desc_imov.text().upper()}")

        if self.cmb_alt_imov_tp_imov.currentText() != "TIPO IMÓVEL":
            caract_imovel.append(f"Tipo Imóvel: {self.cmb_alt_imov_tp_imov.currentText().upper()}")    


        if self.cmb_alt_imov_tp_negoc.currentText() != "TIPO DE NEGOCIAÇÃO":
            caract_imovel.append(f"Tipo de Negociação: {self.cmb_alt_imov_tp_negoc.currentText().upper()}")

        if self.cmb_alt_imov_status.currentText() != "STATUS":
            caract_imovel.append(f"Status: {self.cmb_alt_imov_status.currentText().upper()}")
        
        if self.txt_alt_imov_preco.text() != "":
            caract_imovel.append(f"Preço: {self.txt_alt_imov_preco.text().upper()}")

        if self.txt_alt_imov_cond.text() != "":
            caract_imovel.append(f"Condições: {self.txt_alt_imov_cond.text().upper()}")
        
        if self.txt_alt_imov_cep.text() != "":
            caract_imovel.append(f"CEP: {self.txt_alt_imov_cep.text().upper()}")
        
        if self.txt_alt_imov_rua.text() != "":
            caract_imovel.append(f"RUA: {self.txt_alt_imov_rua.text().upper()}")
        
        if self.txt_alt_imov_n.text() != "":
            caract_imovel.append(f"N°: {self.txt_alt_imov_n.text().upper()}")
        
        if self.txt_alt_imov_comp.text() != "":
            caract_imovel.append(f"Complemento: {self.txt_alt_imov_comp.text().upper()}")
        
        if self.txt_alt_imov_bairro.text() != "":
            caract_imovel.append(f"Bairro: {self.txt_alt_imov_bairro.text().upper()}")

        if self.txt_alt_imov_cidade.text() != "":   
            caract_imovel.append(f"Cidade: {self.txt_alt_imov_cidade.text().upper()}")

        if self.txt_alt_imov_estado.text() != "":
            caract_imovel.append(f"Estado: {self.txt_alt_imov_estado.text().upper()}")

        self.ptxt_alt_imov_caract.setPlainText("\n".join(caract_imovel)) 


    def PreencherTxtCaracteristica(self):
        caract_imovel = []
        if self.txt_reg_imov_desc_imov.text() != "":
            caract_imovel.append(f"Descrição do Imóvel: {self.txt_reg_imov_desc_imov.text().upper()}")

        if self.cmb_reg_imov_tp_imov.currentText() != "TIPO IMÓVEL":
            caract_imovel.append(f"Tipo Imóvel: {self.cmb_reg_imov_tp_imov.currentText().upper()}")    


        if self.cmb_reg_imov_tp_neg.currentText() != "TIPO DE NEGOCIAÇÃO":
            caract_imovel.append(f"Tipo de Negociação: {self.cmb_reg_imov_tp_neg.currentText().upper()}")

        if self.cmb_reg_imov_status.currentText() != "STATUS":
            caract_imovel.append(f"Status: {self.cmb_reg_imov_status.currentText().upper()}")
        
        if self.txt_reg_imov_preco.text() != "":
            caract_imovel.append(f"Preço: {self.txt_reg_imov_preco.text().upper()}")

        if self.txt_reg_imov_cond.text() != "":
            caract_imovel.append(f"Condições: {self.txt_reg_imov_cond.text().upper()}")
        
        if self.txt_reg_imov_cep.text() != "":
            caract_imovel.append(f"CEP: {self.txt_reg_imov_cep.text().upper()}")
        
        if self.txt_reg_imov_rua.text() != "":
            caract_imovel.append(f"RUA: {self.txt_reg_imov_rua.text().upper()}")
        
        if self.txt_reg_imov_n.text() != "":
            caract_imovel.append(f"N°: {self.txt_reg_imov_n.text().upper()}")
        
        if self.txt_reg_imov_comp.text() != "":
            caract_imovel.append(f"Complemento: {self.txt_reg_imov_comp.text().upper()}")
        
        if self.txt_reg_imov_bairro.text() != "":
            caract_imovel.append(f"Bairro: {self.txt_reg_imov_bairro.text().upper()}")

        if self.txt_reg_imov_cidade.text() != "":   
            caract_imovel.append(f"Cidade: {self.txt_reg_imov_cidade.text().upper()}")

        if self.txt_reg_imov_estado.text() != "":
            caract_imovel.append(f"Estado: {self.txt_reg_imov_estado.text().upper()}")

        self.ptxt_reg_imov_caract.setPlainText("\n".join(caract_imovel)) 

    def BTNRegistrarImoveis(self):
        valida_campos = []
        dados = []
        
        if self.txt_reg_imov_desc_imov.text() == "":
            valida_campos.append("Descrição do Imóvel")
        else:
            dados.append(self.txt_reg_imov_desc_imov.text().upper())

        if self.cmb_reg_imov_tp_imov.currentText() == "TIPO IMÓVEL":
            valida_campos.append("Tipo Imóvel")
        else:
            dados.append(self.cmb_reg_imov_tp_imov.currentText().upper())

        if self.cmb_reg_imov_tp_neg.currentText() == "TIPO DE NEGOCIAÇÃO":
            valida_campos.append("Tipo de Negociação")
        else:
            dados.append(self.cmb_reg_imov_tp_neg.currentText().upper())

        if self.cmb_reg_imov_status.currentText() == "STATUS":
            valida_campos.append("Status")
        else:
            dados.append(self.cmb_reg_imov_status.currentText().upper())
        
        if self.txt_reg_imov_preco.text() == "":
            valida_campos.append("Preço")
        else:
            dados.append(self.txt_reg_imov_preco.text())
                
        if self.txt_reg_imov_cond.text() == "":
            valida_campos.append("Condições")
        else:
            dados.append(self.txt_reg_imov_cond.text().upper())
        
        if self.txt_reg_imov_cep.text() == "":
            valida_campos.append("CEP")
        else:
            dados.append(self.txt_reg_imov_cep.text().upper())
        
        if self.txt_reg_imov_rua.text() == "":
            valida_campos.append("RUA")
        else:
            dados.append(self.txt_reg_imov_rua.text().upper())
        
        if self.txt_reg_imov_n.text() == "":
            valida_campos.append("N°")
        else:
            dados.append(self.txt_reg_imov_n.text().upper())
        
        if self.txt_reg_imov_comp.text() == "":
            dados.append("")
        else:
            dados.append(self.txt_reg_imov_comp.text().upper())
        
        if self.txt_reg_imov_bairro.text() == "":
            valida_campos.append("Bairro")
        else:
            dados.append(self.txt_reg_imov_bairro.text().upper())
        
        if self.txt_reg_imov_cidade.text() == "":
            valida_campos.append("Cidade")
        else:
            dados.append(self.txt_reg_imov_cidade.text().upper())

        if self.txt_reg_imov_estado.text() == "":
            valida_campos.append("Estado") 
        else:
            dados.append(self.txt_reg_imov_estado.text().upper())

        if self.ptxt_reg_imov_obs.toPlainText() == "":
            dados.append("") 
        else:
            dados.append(self.ptxt_reg_imov_obs.toPlainText().upper())
        
        if self.ptxt_reg_imov_caract.toPlainText() == "":
            valida_campos.append("Características do Imóvel")  
        else:
            dados.append(self.ptxt_reg_imov_caract.toPlainText().upper())
    
        

        if len(valida_campos) == 0:

            self.RegistrarImovel(dados)
            self.MsgFinalizado("Imóvel registrado com socesso...")
        else:
            '\n'.join(valida_campos)
            msg_info = "Por gentileza preencher todos os campos abaixo:\n"+'\n'.join(valida_campos)
            self.MsgErro(msg_info)


    def BTNAlterarRegistrarImoveis(self):
        valida_campos = []
        dados = []      

        if self.txt_alt_imov_desc_imov.text() == "":
            valida_campos.append("Descrição do Imóvel")
        else:
            dados.append(f"DESC_CURTA = '{self.txt_alt_imov_desc_imov.text().upper()}'")

        if self.cmb_alt_imov_tp_imov.currentText() == "TIPO IMÓVEL":
            valida_campos.append("Tipo Imóvel")
        else:
            dados.append(f"TIPO_IMOVEL = '{self.cmb_alt_imov_tp_imov.currentText().upper()}'")

        if self.cmb_alt_imov_tp_negoc.currentText() == "TIPO DE NEGOCIAÇÃO":
            valida_campos.append("Tipo de Negociação")
        else:
            dados.append(f"TIPO_NEGOCIACAO = '{self.cmb_alt_imov_tp_negoc.currentText().upper()}'")

        if self.cmb_alt_imov_status.currentText() == "STATUS":
            valida_campos.append("Status")
        else:
            dados.append(f"STATUS = '{self.cmb_alt_imov_status.currentText().upper()}'")
        
        if self.txt_alt_imov_preco.text() == "":
            valida_campos.append("Preço")
        else:
            dados.append(f"PRECO = {self.txt_alt_imov_preco.text()}")
                
        if self.txt_alt_imov_cond.text() == "":
            valida_campos.append("Condições")
        else:
            dados.append(f"CONDICOES = '{self.txt_alt_imov_cond.text().upper()}'")
        
        if self.txt_alt_imov_cep.text() == "":
            valida_campos.append("CEP")
        else:
            dados.append(f"CEP = '{self.txt_alt_imov_cep.text().upper()}'")
        
        if self.txt_alt_imov_rua.text() == "":
            valida_campos.append("RUA")
        else:
            dados.append(f"RUA = '{self.txt_alt_imov_rua.text().upper()}'")
        
        if self.txt_alt_imov_n.text() == "":
            valida_campos.append("N°")
        else:
            dados.append(f"NUMERO = '{self.txt_alt_imov_n.text().upper()}'")
        
        if self.txt_alt_imov_comp.text() == "":
            dados.append("")
        else:
            dados.append(f"COMPLEMENTO = '{self.txt_alt_imov_comp.text().upper()}'")
        
        if self.txt_alt_imov_bairro.text() == "":
            valida_campos.append("Bairro")
        else:
            dados.append(f"BAIRRO = '{self.txt_alt_imov_bairro.text().upper()}'")
        
        if self.txt_alt_imov_cidade.text() == "":
            valida_campos.append("Cidade")
        else:
            dados.append(f"CIDADE = '{self.txt_alt_imov_cidade.text().upper()}'")

        if self.txt_alt_imov_estado.text() == "":
            valida_campos.append("Estado") 
        else:
            dados.append(f"ESTADO = '{self.txt_alt_imov_estado.text().upper()}'")

        if self.ptxt_alt_imov_obs.toPlainText() == "":
            dados.append("") 
        else:
            dados.append(f"OBSERVACAO = '{self.ptxt_alt_imov_obs.toPlainText().upper()}'")
        
        if self.ptxt_alt_imov_caract.toPlainText() == "":
            valida_campos.append("Características do Imóvel")  
        else:
            dados.append(f"CARACTERISICAS_IMOVEL = '{self.ptxt_alt_imov_caract.toPlainText().upper()}'")
    
        

        if len(valida_campos) == 0:
            cod_imovel = self.txt_alt_imov_cod_imov.text()
            dados_alt = ", ".join(dados)
            # print(dados_alt)
            self.AlterarRegistroImovel(cod_imovel, dados_alt)
            self.MsgFinalizado("Registro imovel alterado com sucesso...")
        else:
            '\n'.join(valida_campos)
            msg_info = "Por gentileza preencher todos os campos abaixo:\n"+'\n'.join(valida_campos)
            self.MsgErro(msg_info)




    def FiltrosRegistrarImoveis(self):
        filtro = ""
        filtros = []
        if self.cmb_con_imv_tp_neg.currentText() != "TIPO DE NEGOCIAÇÃO":
            filtros.append(f"TIPO_NEGOCIACAO ='{self.cmb_con_imv_tp_neg.currentText().upper()}'")
        
        if self.cmb_con_imv_status.currentText() != "STATUS":
            filtros.append(f"STATUS ='{self.cmb_con_imv_status.currentText().upper()}'")

        if self.cmb_con_imv_tp_mov.currentText() != "TIPO IMÓVEL":
            filtros.append(f"TIPO_IMOVEL = '{self.cmb_con_imv_tp_mov.currentText().upper()}'")  

        if self.txt_con_imv_cep.text() != "":
            filtros.append(f"CEP ='{self.txt_con_imv_cep.text().upper()}'")
            
        if self.txt_con_imv_bairro.text() != "":
            filtros.append(f"BAIRRO ='{self.txt_con_imv_bairro.text().upper()}'")

        if self.txt_con_imv_cidade.text() != "":
            filtros.append(f"CIDADE ='{self.txt_con_imv_cidade.text().upper()}'")

        if self.txt_con_imv_estado.text() != "":
            filtros.append(f"ESTADO ='{self.txt_con_imv_estado.text().upper()}'")
        
        if len(filtros) > 0:
            filtro = f"WHERE {' AND '.join(filtros)}"

        self.ConsultarRegistroImovel(filtro)
    
    def CreateTable(self):
        self.conn = sqlite3.connect("DB_Registro_Imovel.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS REGISTRO_IMOVEIS ('COD_IMOVEL' INTEGER PRIMARY KEY AUTOINCREMENT, 'DESC_CURTA' TEXT,  'TIPO_IMOVEL' TEXT, 'TIPO_NEGOCIACAO' TEXT,'STATUS' TEXT, 'PRECO' REAL, 'CONDICOES' TEXT, 'CEP' TEXT, 'RUA' TEXT, 'NUMERO' TEXT, 'COMPLEMENTO' TEXT, 'BAIRRO' TEXT, 'CIDADE' TEXT, 'ESTADO' TEXT, 'CARACTERISICAS_IMOVEL' TEXT, 'OBSERVACAO' TEXT)")
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


    def RegistrarImovel(self, dados):
        self.conn = sqlite3.connect("DB_Registro_Imovel.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("INSERT INTO REGISTRO_IMOVEIS ('DESC_CURTA', 'TIPO_IMOVEL', 'TIPO_NEGOCIACAO', 'STATUS', 'PRECO', 'CONDICOES', 'CEP', 'RUA', 'NUMERO', 'COMPLEMENTO', 'BAIRRO', 'CIDADE', 'ESTADO', 'CARACTERISICAS_IMOVEL',  'OBSERVACAO') VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", dados)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


    def AlterarRegistroImovel(self, cod_imovel, dados):
        self.conn = sqlite3.connect("DB_Registro_Imovel.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
        UPDATE REGISTRO_IMOVEIS 
        SET {dados} 
        WHERE COD_IMOVEL = {int(cod_imovel)}""")
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
    
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

    
    def MsgQuestion(self, msg_info):      
        msg = QMessageBox()
        msg.setWindowTitle('Confirmar')        
        msg.setInformativeText(msg_info)
        msg.setIcon(msg.Question)            
        msg.setStyleSheet('color:rgb(255, 255, 255); font: bold 10pt \"Cambria\"; border-color:rgb(0, 0, 108); background-color: rgb(0, 98, 98);')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec() 

        return resp
    

    def MsgErro(self, msg_info):
        msg = QMessageBox()
        msg.setWindowTitle('Erro')        
        msg.setInformativeText(msg_info)
        msg.setStyleSheet('color:rgb(255, 255, 255); font: bold 10pt \"Cambria\"; border-color:rgb(0, 0, 108); background-color: rgb(0, 98, 98);')
        msg.setStandardButtons(msg.Ok)
        msg.setIcon(msg.Warning)
        msg.exec()

    def MsgFinalizado(self, msg_info):
        msg = QMessageBox()
        msg.setWindowTitle('Processo finalizado!') 
        msg.setInformativeText(msg_info)
        msg.setStyleSheet('color:rgb(255, 255, 255); font: bold 10pt \"Cambria\"; border-color:rgb(0, 0, 108); background-color: rgb(0, 98, 98);')
        msg.setIcon(msg.Information)
        msg.setStandardButtons(msg.Ok)
        msg.exec()
    


