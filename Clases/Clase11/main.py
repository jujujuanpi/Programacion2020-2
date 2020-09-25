import persona as p
import estudiante as es
import egresado as eg

Laura = p.Persona ("Laura", 20, 1234567890)
Mario = p.Persona ("Mario", 20, 1122334455)
Valeria = es.Estudiante ("Valeria", 20, 5544332211, "Ingeniería Biomédica", 3)
Melany = eg.Egresado ("Melany", 21, 5566778899, "Ingeniería Biomédica", 2023)

Laura.hablar ("Tengo sueño.")
Mario.comer ("Tacos")
Valeria.estudiar ("Cálculo")
Melany.trabajar ("MIT")