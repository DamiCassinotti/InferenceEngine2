rules = {
	"cancer de mama lobulillar": {
		"borde_nuclear": ["irregular"],
		"arq": ["ductos rudimentarios", "conglomerados de celulas", "monomorfa"],
		"canibalismo": ["presente"]
	},
	"cancer de mama mucinoso": {
		"nucleo": ["mitosis en estallido"],
		"nucleo_citoplasma": ["aumentado"],
		"arq": ["lagos de mucinas"]
	},
	"cancer de mama ductal": {
		"nucleo": ["mitosis en estallido", "hipercromaticos", "irregulares", "amoldamiento"],
		"citoplasma": ["vacuolado", "pleomorfismo", "rosado"],
		"canibalismo": ["presente"],
		"borde_nuclear": ["irregular"],
		"arq": ["ductos rudimentarios"]
	},
	"cancer de mama papilar": {
		"nucleo": ["hipercromaticos", "irregulares", "amoldamiento"],
		"citoplasma": ["pleomorfismo", "rosado"],
		"canibalismo": ["presente"],
		"borde_nuclear": ["mal definido"],
		"arq": ["papila con microcalcificacion"],
		"nucleo_citoplasma": ["aumentado"]
	},
	"tumor phyllodes benigno": {
		"canibalismo": ["ausente"],
		"borde_nuclear": ["bien definido"],
		"necrosis_tumoral": ["normal"]
	},
	"tumor phyllodes maligno": {
		"nucleo": ["mitosis en estallido", "hipercromaticos", "irregulares", "amoldamiento"],
		"citoplasma": ["pleomorfismo"],
		"canibalismo": ["presente"],
		"borde_nuclear": ["irregular"],
		"arq": ["celulas fusocelulares"],
		"nucleo_citoplasma": ["aumentado"]
	}
}
