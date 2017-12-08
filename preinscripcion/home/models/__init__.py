# NOTA: El orden de los modelos es importante para generar las migraciones

# Catalogos

from .area import Area
from .evidencia import Evidencia
from .especialidad import Especialidad

# Modelos Principales

from .alumno import Alumno
from .docente import Docente
from .materia import Materia
from .carrera import Carrera

# Modelos Secundarios - Relaciones (1,*)

from .avanceMateria import AvanceMateria
from .kardex import Kardex
from .disponibilidad import Disponibilidad
from .perfil import Perfil

# Modelos Secundarios - Relaciones (*,*)

from .alumnoMateria import AlumnoMateria
from .docenteMateria import DocenteMateria
from .materiaCarrera import MateriaCarrera
from .materiaArea import MateriaArea
