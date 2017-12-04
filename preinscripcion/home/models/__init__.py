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

# Modelos Secundarios (Relaciones)

from .materiaInfo import MateriaInfo
from .alumnoMateriaInfo import AlumnoMateriaInfo
from .avanceMateria import AvanceMateria
from .kardex import Kardex
from .disponibilidad import Disponibilidad
from .perfil import Perfil
from .docenteMateriaInfo import DocenteMateriaInfo
