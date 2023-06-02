######################################################
# Title: Search Engine Application
# Author: Natalie Eversole
# Date: April 28th, 2022
#
# Description: This code creates the application for
# the search engine using PyQt.
#######################################################

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon, QPixmap
import psycopg2

qtCreatorFile = "milestone1App.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class milestone1(QMainWindow):
    def __init__(self):
        super(milestone1, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadStateList()
        self.ui.stateList.currentTextChanged.connect(self.stateChanged)
        self.ui.cityList.itemSelectionChanged.connect(self.cityChanged)
        self.ui.zipCodeList.itemSelectionChanged.connect(self.zipCodeChanged)
        self.ui.zipCodeList.itemSelectionChanged.connect(self.loadTotalPopulation)
        self.ui.zipCodeList.itemSelectionChanged.connect(self.loadAverageIncome)
        self.ui.zipCodeList.itemSelectionChanged.connect(self.loadNumberOfBusinesses)


    def executeQuery(self,sql_str):
        try:
            conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' password='***'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()
        cur.execute(sql_str)
        conn.commit()
        result = cur.fetchall()
        conn.close()
        return result

    def loadStateList(self):
        #clears items in combo box initially. before adding below data
        self.ui.stateList.clear()
        self.ui.cityList.clear()
        self.ui.zipCodeList.clear()
        sql_str = "SELECT distinct state FROM businesstable ORDER BY state;"
        try:
            results = self.executeQuery(sql_str)
            for row in results:
                self.ui.stateList.addItem(row[0])
        except:
            print("Query1 failed!")
        self.ui.stateList.setCurrentIndex(-1)
        self.ui.stateList.clearEditText()

    def stateChanged(self):
        self.ui.cityList.clear()
        self.ui.zipCodeList.clear()
        state = self.ui.stateList.currentText()
        if (self.ui.stateList.currentIndex()>=0):
            sql_str = "SELECT distinct city FROM businesstable WHERE state ='" + state + "' ORDER BY city;"
            try:
                results = self.executeQuery(sql_str)
                for row in results:
                    self.ui.cityList.addItem(row[0])
            except:
                print("Query2 failed!")

            for i in reversed(range(self.ui.businessTable.rowCount())):
                self.ui.businessTable.removeRow(i)
            sql_str = "SELECT name, address, city, stars, review_count FROM businesstable WHERE state = '" + state + "' ORDER BY name;"
            try:
                results = self.executeQuery(sql_str)
                #Add header color and style
                style = "::section {""background-color: #f3f3f3; }"
                self.ui.businessTable.horizontalHeader().setStyleSheet(style)
                self.ui.businessTable.setColumnCount(len(results[0]))
                self.ui.businessTable.setRowCount(len(results))
                #Add header titles and column width
                self.ui.businessTable.setHorizontalHeaderLabels(['Business Name', 'Address', 'City', 'Stars', 'Review Count'])
                self.ui.businessTable.resizeColumnsToContents()
                self.ui.businessTable.setColumnWidth(0, 280)
                self.ui.businessTable.setColumnWidth(1, 200)
                self.ui.businessTable.setColumnWidth(2, 100)
                self.ui.businessTable.setColumnWidth(3, 80)
                currentRowCount = 0
                for row in results:
                    for colCount in range (0,len(results[0])):
                        self.ui.businessTable.setItem(currentRowCount,colCount,QTableWidgetItem(row[colCount]))
                    currentRowCount += 1
            except:
                print("Query3 failed!")

    def cityChanged(self):
        self.ui.zipCodeList.clear()
        state = self.ui.stateList.currentText()
        city = self.ui.cityList.selectedItems()[0].text()
        if (self.ui.stateList.currentIndex()>=0):
            sql_str = "SELECT distinct postal_code FROM businesstable WHERE city ='" + city + "' ORDER BY postal_code;"
            try:
                results = self.executeQuery(sql_str)
                for row in results:
                    self.ui.zipCodeList.addItem(row[0])
            except:
                print("Query4 failed!")

            for i in reversed(range(self.ui.businessTable.rowCount())):
                self.ui.businessTable.removeRow(i)
            sql_str = "SELECT name, address, city, stars, review_count FROM businesstable WHERE state = '" + state + "' AND city='" + city + "' ORDER BY name ;"
            try:
                results = self.executeQuery(sql_str)
                #Add header color and style
                style = "::section {""background-color: #f3f3f3; }"
                self.ui.businessTable.horizontalHeader().setStyleSheet(style)
                self.ui.businessTable.setColumnCount(len(results[0]))
                self.ui.businessTable.setRowCount(len(results))
                #Add header titles and column width
                self.ui.businessTable.setHorizontalHeaderLabels(['Business Name', 'Address', 'City', 'Stars', 'Review Count'])
                self.ui.businessTable.resizeColumnsToContents()
                self.ui.businessTable.setColumnWidth(0, 280)
                self.ui.businessTable.setColumnWidth(1, 200)
                self.ui.businessTable.setColumnWidth(2, 100)
                self.ui.businessTable.setColumnWidth(3, 80)
                currentRowCount = 0
                for row in results:
                    for colCount in range (0,len(results[0])):
                        self.ui.businessTable.setItem(currentRowCount,colCount,QTableWidgetItem(row[colCount]))
                    currentRowCount += 1
            except:
                print("Query5 failed!")

    #New Zip Code Mehtod
    def zipCodeChanged(self):
        if (self.ui.stateList.currentIndex() >= 0) and (len(self.ui.zipCodeList.selectedItems()) > 0):
            state = self.ui.stateList.currentText()
            city = self.ui.cityList.selectedItems()[0].text()
            zipCode = self.ui.zipCodeList.selectedItems()[0].text()
            sql_str = "SELECT name, address, city, stars, review_count FROM businesstable WHERE postal_code='" + zipCode + "' ORDER BY name ;"
            #sql_str2 = "SELECT review_count FROM review_count WHERE postal_code='" + zipCode + "' ORDER BY name ;"
            results = self.executeQuery(sql_str)
            try:
                results = self.executeQuery(sql_str)
                #Add header color and style
                style = "::section {""background-color: #f3f3f3; }"
                self.ui.businessTable.horizontalHeader().setStyleSheet(style)
                self.ui.businessTable.setColumnCount(len(results[0]))
                self.ui.businessTable.setRowCount(len(results))
                #Add header titles and column width
                self.ui.businessTable.setHorizontalHeaderLabels(['Business Name', 'Address', 'City', 'Stars', 'Review Count'])
                self.ui.businessTable.resizeColumnsToContents()
                self.ui.businessTable.setColumnWidth(0, 280)
                self.ui.businessTable.setColumnWidth(1, 200)
                self.ui.businessTable.setColumnWidth(2, 100)
                self.ui.businessTable.setColumnWidth(3, 80)
                currentRowCount = 0
                for row in results:
                    for colCount in range (0,len(results[0])):
                        self.ui.businessTable.setItem(currentRowCount,colCount,QTableWidgetItem(row[colCount]))
                    currentRowCount += 1
            except:
                print("Query6 failed!")


    def loadNumberOfBusinesses(self):
        self.ui.NumOfBusinessesBox.clear()
        zipCode = self.ui.zipCodeList.selectedItems()[0].text()
        sql_str = "SELECT business_count FROM business_count_table WHERE postalcode='" + zipCode + "';"
        try:
            results = self.executeQuery(sql_str)
            self.ui.NumOfBusinessesBox.setText(results[0][0])
        except:
            print("Query7 failed!")


    def loadTotalPopulation(self):
        self.ui.TotalPopBox.clear()
        zipCode = self.ui.zipCodeList.selectedItems()[0].text()
        sql_str = "SELECT population FROM zipcodedata WHERE zipcode='" + zipCode + "';"
        try:
            results = self.executeQuery(sql_str)
            self.ui.TotalPopBox.setText(results[0][0])
        except:
            print("Query8 failed!")


    def loadAverageIncome(self):
        self.ui.AvgIncomeBox.clear()
        zipCode = self.ui.zipCodeList.selectedItems()[0].text()
        sql_str = "SELECT meanincome FROM zipcodedata WHERE zipcode='" + zipCode + "';"
        try:
            results = self.executeQuery(sql_str)
            self.ui.AvgIncomeBox.setText(results[0][0])
        except:
            print("Query9 failed!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = milestone1()
    window.show()
    sys.exit(app.exec_())
