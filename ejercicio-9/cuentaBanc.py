#!/usr/bin/env python3

class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0.0
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
        else:
            print("Monto incorrecto")
    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Monto incorrecto")
    def mostrar_info(self):
        print(f"Titular: {self.titular}, saldo disponible: {self.__saldo}")

pablo = CuentaBancaria("tomas")
pablo.mostrar_info()
pablo.depositar(500)
pablo.mostrar_info()
pablo.retirar(200)
pablo.mostrar_info()
pablo.retirar(500)
pablo.mostrar_info()
