from predicates import *


#Actions of example 1

class Encode(object):
        def precond(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent in agents:
                        for message in messages:
                                for agent1 in agents:
                                        for agent2 in agents:
                                                knows1 = Knows(agent, message)
                                                key = Key(agent1,agent2)
                                                knows2 = Knows(agent, key)
                                                if (knows1.listar() in knowledge) and (knows2.listar() in knowledge) and not(Enc(agent, message, key).listar() in actions):
                                                        return [True, Enc(agent, message, key).listar()]
                return [False]

        def action(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent in agents:
                        for message in messages:
                                for agent1 in agents:
                                        for agent2 in agents:
                                                knows1 = Knows(agent, message)
                                                key = Key(agent1,agent2)
                                                knows2 = Knows(agent, key)
                                                if (knows1.listar() in knowledge) and (knows2.listar() in knowledge):
                                                        enc = Encoded(message, key)
                                                        knowledge.append(Knows(agent, enc).listar())
                                                        actions.append(Enc(agent, message, key).listar())


encode = Encode()

class Decode(object):
        def precond(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent in agents:
                        for agent1 in agents:
                                for agent2 in agents:
                                        for message in messages:
                                                key = Key(agent1, agent2)
                                                enc = Encoded(message, key)
                                                knows1 = Knows(agent, enc)
                                                knows2 = Knows(agent, enc.key)
                                                if (knows1.listar() in knowledge) and (knows2.listar() in knowledge) and not(Dec(agent, enc).listar() in actions):
                                                        return [True, Dec(agent, enc).listar()]
                return [False]

        def action(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent in agents:
                        for agent1 in agents:
                                for agent2 in agents:
                                        for message in messages:
                                                key = Key(agent1, agent2)
                                                enc = Encoded(message, key)
                                                knows1 = Knows(agent, enc)
                                                knows2 = Knows(agent, enc.key)
                                                if (knows1.listar() in knowledge) and (knows2.listar() in knowledge):
                                                        knowledge.append(Knows(agent, message).listar())
                                                        actions.append(Dec(agent, enc).listar())


decode = Decode()

class Send(object):
        def precond(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent1 in agents:
                        for agent2 in agents:
                                if agent1 != agent2:
                                        for agent3 in agents:
                                                for agent4 in agents:
                                                        for message in messages:
                                                                key = Key(agent3, agent4)
                                                                enc = Encoded(message, key)
                                                                if Knows(agent1, enc).listar() in knowledge and not(Sent(enc, agent1, agent2).listar() in actions):
                                                                        if ((agent2 == enc.key.x1) or (agent2 == enc.key.x2)) or (Received(enc, agent1, agent2).listar() in actions):
                                                                                return [True, Sent(enc, agent1, agent2).listar()]
                return [False]

        def action(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent1 in agents:
                        for agent2 in agents:
                                if agent1 != agent2:
                                        for agent3 in agents:
                                                for agent4 in agents:
                                                        for message in messages:
                                                                key = Key(agent3, agent4)
                                                                enc = Encoded(message, key)
                                                                if Knows(agent1, enc).listar() in knowledge:
                                                                        if ((agent2 == enc.key.x1) or (agent2 == enc.key.x2)) or (Received(enc, agent1, agent2).listar() in actions):
                                                                                actions.append(Sent( enc, agent1, agent2).listar())

send = Send()

class Receive(object):

        def precond(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent1 in agents:
                        for agent2 in agents:
                                for agent3 in agents:
                                        if agent1 != agent2 and agent2 != agent3 and agent1 != agent3:
                                                for agent4 in agents:
                                                        for agent5 in agents:
                                                                for message in messages:
                                                                        key = Key(agent4, agent5)
                                                                        enc = Encoded(message, key)
                                                                        if (Sent(enc, agent1, agent2).listar() in actions) and not(Intercepted(agent3, enc, agent1, agent2).listar() in actions) and not(Received( enc, agent2, agent1).listar() in actions):
                                                                                return [True, Received( enc, agent2, agent1).listar()]
                return [False]

        def action(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent1 in agents:
                        for agent2 in agents:
                                for agent3 in agents:
                                        if agent1 != agent2 and agent2 != agent3 and agent1 != agent3:
                                                for agent4 in agents:
                                                        for agent5 in agents:
                                                                for message in messages:
                                                                        key = Key(agent4, agent5)
                                                                        enc = Encoded(message, key)
                                                                        if (Sent(enc, agent1, agent2).listar() in actions) and not(Intercepted(agent3, enc, agent1, agent2).listar() in actions):
                                                                                actions.append(Received( enc, agent2, agent1).listar())
                                                                                knowledge.append(Knows(agent2, enc).listar())

receive = Receive()

class Intercept(object):

        def precond(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent1 in agents:
                        for agent2 in agents:
                                for agent3 in agents:
                                        if agent1 != agent2 and agent2 != agent3 and agent1 != agent3:
                                                for agent4 in agents:
                                                        for agent5 in agents:
                                                                for message in messages:
                                                                        key = Key(agent4, agent5)
                                                                        enc = Encoded(message, key)
                                                                        if (Sent(enc, agent1, agent2).listar() in actions) and not(Received(enc, agent2, agent1).listar() in actions) and not(Intercepted(agent3, enc, agent1, agent2).listar() in actions):
                                                                                return [True, Intercepted(agent3, enc, agent1, agent2).listar()]
                return [False]

        def action(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent1 in agents:
                        for agent2 in agents:
                                for agent3 in agents:
                                        if agent1 != agent2 and agent2 != agent3 and agent1 != agent3:
                                                for agent4 in agents:
                                                        for agent5 in agents:
                                                                for message in messages:
                                                                        key = Key(agent4, agent5)
                                                                        enc = Encoded(message, key)
                                                                        if (Sent(enc, agent1, agent2).listar() in actions) and not(Received(enc, agent2, agent1).listar() in actions):
                                                                                actions.append(Intercepted(agent3, enc, agent1, agent2).listar())
                                                                                knowledge.append(Knows(agent3, enc).listar())

intercept = Intercept()

#Actions of example 2

class Encode2(object):
        def precond(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent in agents:
                        for message in messages:
                                for agent1 in agents:
                                        for agent2 in agents:
                                                key = Key(agent1,agent2)
                                                conc = Concat(message, key)
                                                knows1 = Knows(agent, conc)
                                                knows2 = Knows(agent, key)
                                                if (knows1.listar() in knowledge) and (knows2.listar() in knowledge) and not(Enc2(agent, message, key).listar() in actions):
                                                        return [True, Enc2(agent, conc, key).listar()]
                return [False]

        def action(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent in agents:
                        for message in messages:
                                for agent1 in agents:
                                        for agent2 in agents:
                                                key = Key(agent1,agent2)
                                                conc = Concat(message, key)
                                                knows1 = Knows(agent, conc)
                                                knows2 = Knows(agent, key)
                                                if (knows1.listar() in knowledge) and (knows2.listar() in knowledge) and not(Enc2(agent, message, key).listar() in actions):
                                                        enc = Encoded2(conc, key)
                                                        knowledge.append(Knows(agent, enc).listar())
                                                        actions.append(Enc(agent, conc, key).listar())


encode2 = Encode2()

class Decode2(object):
        def precond(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent in agents:
                        for agent1 in agents:
                                for agent2 in agents:
                                        for message in messages:
                                                key = Key(agent1, agent2)
                                                conc = Concat(message, key)
                                                enc = Encoded2(conc, key)
                                                knows1 = Knows(agent, enc)
                                                knows2 = Knows(agent, enc.key)
                                                if (knows1.listar() in knowledge) and (knows2.listar() in knowledge) and not(Dec(agent, enc).listar() in actions):
                                                        return [True, Dec(agent, enc).listar()]
                return [False]

        def action(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent in agents:
                        for agent1 in agents:
                                for agent2 in agents:
                                        for message in messages:
                                                key = Key(agent1, agent2)
                                                conc = Concat(message, key)
                                                enc = Encoded2(conc, key)
                                                knows1 = Knows(agent, enc)
                                                knows2 = Knows(agent, enc.key)
                                                if (knows1.listar() in knowledge) and (knows2.listar() in knowledge):
                                                        knowledge.append(Knows(agent, conc).listar())
                                                        actions.append(Dec(agent, enc).listar())


decode2 = Decode2()

class Concatenate(object):
        def precond(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent in agents:
                        for agent1 in agents:
                                for agent2 in agents:
                                        for message in messages:
                                                key = Key(agent1, agent2)
                                                conc = Concat(message, key)
                                                enc = Encoded2(conc, key)
                                                knows1 = Knows(agent, message)
                                                knows2 = Knows(agent, key)
                                                if (knows1.listar() in knowledge) and (knows2.listar() in knowledge) and not(Dec(agent, enc).listar() in actions):
                                                        return [True, Conc(agent, message, key).listar()]

                return [False]

        def action(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent in agents:
                        for agent1 in agents:
                                for agent2 in agents:
                                        for message in messages:
                                                key = Key(agent1, agent2)
                                                knows1 = Knows(agent, message)
                                                knows2 = Knows(agent, key)
                                                conc = Concat(message, key)
                                                enc = Encoded2(conc, key)
                                                if (knows1.listar() in knowledge) and (knows2.listar() in knowledge) and not(Dec(agent, enc).listar() in actions):
                                                        conc = Concat(message, key)
                                                        knowledge.append(Knows(agent, conc).listar())
                                                        actions.append(Conc(agent, message, key).listar())


concatenate = Concatenate()

class Deconcat(object):
        def precond(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent in agents:
                        for agent1 in agents:
                                for agent2 in agents:
                                        for message in messages:
                                                key = Key(agent1, agent2)
                                                conc = Concat(message, key)
                                                enc = Encoded2(conc, key)
                                                knows = Knows(agent, conc)
                                                if (knows.listar() in knowledge) and not(Dec(agent, enc).listar() in actions):
                                                        return [True, Deconc(agent, conc).listar()]

                return [False]

        def action(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent in agents:
                        for agent1 in agents:
                                for agent2 in agents:
                                        for message in messages:
                                                key = Key(agent1, agent2)
                                                conc = Concat(message, key)
                                                enc = Encoded2(conc, key)
                                                knows = Knows(agent, conc)
                                                if (knows.listar() in knowledge) and not(Dec(agent, enc).listar() in actions):
                                                        knowledge.append(Knows(agent, message).listar())
                                                        knowledge.append(Knows(agent, key).listar())
                                                        actions.append(Deconc(agent, conc).listar())

deconcat = Deconcat()

class Send2(object):
        def precond(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent1 in agents:
                        for agent2 in agents:
                                if agent1 != agent2:
                                        for agent3 in agents:
                                                for agent4 in agents:
                                                        for message in messages:
                                                                key = Key(agent3, agent4)
                                                                conc = Concat(message, key)
                                                                enc = Encoded2(conc, key)
                                                                if Knows(agent1, enc).listar() in knowledge and not(Sent(enc, agent1, agent2).listar() in actions):
                                                                        if ((agent2 == enc.key.x1) or (agent2 == enc.key.x2)) or (Received(enc, agent1, agent2).listar() in actions):
                                                                                return [True, Sent(enc, agent1, agent2).listar()]
                return [False]

        def action(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent1 in agents:
                        for agent2 in agents:
                                if agent1 != agent2:
                                        for agent3 in agents:
                                                for agent4 in agents:
                                                        for message in messages:
                                                                key = Key(agent3, agent4)
                                                                conc = Concat(message, key)
                                                                enc = Encoded2(conc, key)
                                                                if Knows(agent1, enc).listar() in knowledge:
                                                                        if ((agent2 == enc.key.x1) or (agent2 == enc.key.x2)) or (Received(enc, agent1, agent2).listar() in actions):
                                                                                actions.append(Sent( enc, agent1, agent2).listar())

send2 = Send2()

class Receive2(object):

        def precond(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent1 in agents:
                        for agent2 in agents:
                                for agent3 in agents:
                                        if agent1 != agent2 and agent2 != agent3 and agent1 != agent3:
                                                for agent4 in agents:
                                                        for agent5 in agents:
                                                                for message in messages:
                                                                        key = Key(agent4, agent5)
                                                                        conc = Concat(message, key)
                                                                        enc = Encoded2(conc, key)
                                                                        if (Sent(enc, agent1, agent2).listar() in actions) and not(Intercepted(agent3, enc, agent1, agent2).listar() in actions) and not(Received( enc, agent2, agent1).listar() in actions):
                                                                                return [True, Received( enc, agent2, agent1).listar()]
                return [False]

        def action(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent1 in agents:
                        for agent2 in agents:
                                for agent3 in agents:
                                        if agent1 != agent2 and agent2 != agent3 and agent1 != agent3:
                                                for agent4 in agents:
                                                        for agent5 in agents:
                                                                for message in messages:
                                                                        key = Key(agent4, agent5)
                                                                        conc = Concat(message, key)
                                                                        enc = Encoded2(conc, key)
                                                                        if (Sent(enc, agent1, agent2).listar() in actions) and not(Intercepted(agent3, enc, agent1, agent2).listar() in actions):
                                                                                actions.append(Received( enc, agent2, agent1).listar())
                                                                                knowledge.append(Knows(agent2, enc).listar())

receive2 = Receive2()

class Intercept2(object):

        def precond(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent1 in agents:
                        for agent2 in agents:
                                for agent3 in agents:
                                        if agent1 != agent2 and agent2 != agent3 and agent1 != agent3:
                                                for agent4 in agents:
                                                        for agent5 in agents:
                                                                for message in messages:
                                                                        key = Key(agent4, agent5)
                                                                        conc = Concat(message, key)
                                                                        enc = Encoded2(conc, key)
                                                                        if (Sent(enc, agent1, agent2).listar() in actions) and not(Received(enc, agent2, agent1).listar() in actions) and not(Intercepted(agent3, enc, agent1, agent2).listar() in actions):
                                                                                return [True, Intercepted(agent3, enc, agent1, agent2).listar()]
                return [False]

        def action(self):
                global agents
                global messages
                global knowledge
                global actions

                for agent1 in agents:
                        for agent2 in agents:
                                for agent3 in agents:
                                        if agent1 != agent2 and agent2 != agent3 and agent1 != agent3:
                                                for agent4 in agents:
                                                        for agent5 in agents:
                                                                for message in messages:
                                                                        key = Key(agent4, agent5)
                                                                        conc = Concat(message, key)
                                                                        enc = Encoded2(conc, key)
                                                                        if (Sent(enc, agent1, agent2).listar() in actions) and not(Received(enc, agent2, agent1).listar() in actions):
                                                                                actions.append(Intercepted(agent3, enc, agent1, agent2).listar())
                                                                                knowledge.append(Knows(agent3, enc).listar())

intercept2 = Intercept2()


#Provador

def Planner(Protocol, Knowledge, Goal, Agents, Messages):
         '''
         Planner(Protocol, Knowledge, Goal, Agents, messages)

          Protocol: actions possibles in protocol.
          Knowledge: initial knowledge.
          Goal:
          Agents: every agents in protocol, including the intruder.
          Messages: messages send in protocol.
         '''

         global protocol
         global knowledge
         global actions
         global goal
         global agents
         global messages

         actions = []
         goal = Goal
         agents = Agents
         messages = Messages

         l = len(Protocol)
         i = 0
         while i < l:
             j = i
             knowledge = Knowledge
             protocol = []
             while j < l:
                 protocol.append(Protocol[j])
                 j+=1
             j = 0
             while j < i:
                 protocol.append(Protocol[j])
                 j+=1

             stop = False

             while not(stop):
                     stop = True
                     for action in protocol:
                             a = action.precond()
                             if a[0]:
                                     if not(a[1] in actions):
                                             action.action()
                                             print knowledge
                                             stop = False

                             if goal in knowledge:
                                    print 'True'
                                    i = l
                                    stop = True
                                    break
                                   
             print 'False'
             i+=1
