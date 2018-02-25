#Exemplo 2 do Dolev-Yao

from dyel_strips3 import *


#Agents

Agents = ['a','b','z']

#Mensage

Messages = ['m']

#Protocol

Protocol = [encode2, decode2, concatenate, deconcat, send2, receive2, intercept2]

#Initial Knowledge

kab = Key('a', 'b').listar()
kbz = Key('b', 'z').listar()

Knowledge = [Knows('a', 'm').listar(), Knows('a', kab).listar(), Knows('b', kab).listar(), Knows('b', kbz).listar(), Knows('z', kbz).listar()]

#Goal

Goal = Knows('z', 'm').listar()
