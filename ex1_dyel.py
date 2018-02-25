#Example 1 of Dolev-Yao

from dyel_strips3 import *

#Agents

Agents = ['a','b','z']

#Mensage

Messages = ['m']

#Protocol

Protocol = [encode, decode, send, receive, intercept]

#Initial Knowledge

kab = Key('a', 'b').listar()
kbz = Key('b', 'z').listar()

Knowledge = [Knows('a', 'm').listar(), Knows('a', kab).listar(), Knows('b', kab).listar(), Knows('b', kbz).listar(), Knows('z', kbz).listar()]

#Goal

Goal = Knows('z', 'm').listar()
