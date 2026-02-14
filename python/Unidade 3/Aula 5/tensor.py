import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

produtos = [
    Produto('Camisa', 50.0, 'Roupas'),
    Produto('Calça', 80.0, 'Roupas'),
    Produto('Tênis', 120.0, 'Calçados'),
    Produto('Boné', 30.0, 'Acessórios'),
    Produto('Relógio', 200.0, 'Acessórios'),
    Produto('Mochila', 150.0, 'Acessórios'),
    Produto('Notebook', 3000.0, 'Eletrônicos'),
    Produto('Smartphone', 2500.0, 'Eletrônicos'),
    Produto('Tablet', 1800.0, 'Eletrônicos'),
]

nomes = tf.constant([p.nome for p in produtos])
precos = tf.constant([p.preco for p in produtos])
categorias = tf.constant([p.categoria for p in produtos])

media = tf.reduce_mean(precos)
eletronicos = tf.boolean_mask(nomes, tf.equal(categorias, 'Eletrônicos'))

print(media)
print(eletronicos)