from engine.engine import *

def ask_expert(bn=NADA,arq=NADA,canibalismo=NADA,n=NADA,nc=NADA,c=NADA,necro=NADA):
    engine = RuleEngine()
    engine.reset()
    engine.run(engine.declare(bn=bn, arq=arq, canibalismo=canibalismo, n=n, nc=nc, c=c, necro=necro))
    if engine.RESPUESTA[1]==None and len(engine.RESPUESTA[0])==0:
        print("Dadas las caracteristicas no logramos distinguir si el tumor corresponde a los tipos de cancer conocidos por el experto.")
    else:
        if engine.RESPUESTA[1] != None:
            print(f"El paciente padece de {engine.RESPUESTA[1]}")
        else:
            for n in set(engine.RESPUESTA[0]):
                print(f"Existe la posibilidad de que el paciente padezca {n}")
