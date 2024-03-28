import copy
import unittest
import database as db
import helpers
import config
import csv

class TestDatabase(unittest.TestCase):
    
    def setUp(self):
        db.Clientes.lista = [
            db.Cliente('15J','juan','manolo'),
            db.Cliente('34F','fran','Garcia'),
            db.Cliente('23H','ana','Ramirez'),
        ]
        
    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar('15J')
        cliente_iexistente = db.Clientes.buscar('55K')
        self.assertIsNotNone(cliente_existente)  
        self.assertIsNone(cliente_iexistente)
        
    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear('88M','tarik','Gabriel') 
        self.assertEqual(len(db.Clientes.lista),4)
        self.assertCountEqual(nuevo_cliente.dni,'88M')    
        
    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar('15J'))
        cliente_modificado = db.Clientes.modificar('15J','pablo','mariana')
        self.assertEqual(cliente_a_modificar.nombre,'juan')
        self.assertEqual(cliente_modificado.nombre,'pablo')
        
    def test_borar_cliente(self):
        
        cliente_borrado = db.Clientes.borrar('23H')
        cliente_rebuscado = db.Clientes.buscar('23H')
        self.assertAlmostEqual(cliente_borrado.dni,'23H')
        self.assertIsNone(cliente_rebuscado)
        
    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('15M', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('123344H', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('H45', db.Clientes.lista))
        self.assertFalse(helpers.dni_valido('15J', db.Clientes.lista))
        
    def test_escritura_csv(self):
        db.Clientes.borrar('15J')
        db.Clientes.borrar('34F')
        db.Clientes.modificar('23H','toco','juanito')    
        
        dni,nombre,apellido = None,None,None
        with open(config.DATABAE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero ,delimiter=';')
            dni,nombre,apellido = next(reader)
            
        self.assertAlmostEqual(dni, '23H') 
        self.assertAlmostEqual(nombre, 'toco')
        self.assertAlmostEqual(apellido, 'juanito')   
        
        
            
            
             