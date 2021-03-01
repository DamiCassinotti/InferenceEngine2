import engine.rules as rules
NADA = "NADA"

class RuleEngine():
	def __init__(self):
		self.RESPUESTA = [[],None]
		self.rules = rules.rules

	def reset(self):
		self.RESPUESTA = [[],None]

	def run(self, params):
		for key in self.rules.keys():
			success = 0
			fail = 0
			for condition in self.rules[key].keys():
				if params[condition] == NADA:
					continue
				elif all(item in params[condition] for item in self.rules[key][condition]):
					success += 1
				else:
					fail += 1
			if success == len(self.rules[key].keys()):
				self.RESPUESTA[1] = key
			elif fail > 0:
				continue
			elif success >= 0 and success < len(self.rules[key].keys()):
				self.RESPUESTA[0].append(key)

	def declare(self, bn=NADA,arq=NADA,canibalismo=NADA,n=NADA,nc=NADA,c=NADA,necro=NADA):
		return {
			"borde_nuclear": bn,
			"arq": arq,
			"canibalismo": canibalismo,
			"nucleo": n,
			"nucleo_citoplasma": nc,
			"citoplasma": c,
			"necrosis_tumoral": necro
		}
