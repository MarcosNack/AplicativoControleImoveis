from PySide6.QtWidgets import QMainWindow, QMessageBox

def MsgQuestion(self, msg_info):      
    msg = QMessageBox()
    msg.setWindowTitle('Confirmar')        
    msg.setInformativeText(msg_info)
    msg.setIcon(QMessageBox.Question)            
    msg.setStyleSheet('color:rgb(255, 255, 255); font: bold 10pt \"Cambria\"; border-color:rgb(0, 0, 108); background-color: rgb(0, 98, 98);')
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    resp = msg.exec() 

    return resp

def MsgErro(self, msg_info):
    msg = QMessageBox()
    msg.setWindowTitle('Erro')        
    msg.setInformativeText(msg_info)
    msg.setStyleSheet('color:rgb(255, 255, 255); font: bold 10pt \"Cambria\"; border-color:rgb(0, 0, 108); background-color: rgb(0, 98, 98);')
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setIcon(QMessageBox.Warning)
    msg.exec()

def MsgFinalizado(self, msg_info):
    msg = QMessageBox()
    msg.setWindowTitle('Processo finalizado!') 
    msg.setInformativeText(msg_info)
    msg.setStyleSheet('color:rgb(255, 255, 255); font: bold 10pt \"Cambria\"; border-color:rgb(0, 0, 108); background-color: rgb(0, 98, 98);')
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

