# NOTA: Aqui se importan todos los viewsets para poder ser accesados importando "views"

# Catalogos

from .areaView import AreaViewSet
from .evidenciaView import EvidenciaViewSet
from .especialidadView import EspecialidadViewSet

# Modelos Principales

from .alumnoView import AlumnoViewSet
from .doncenteView import DocenteViewSet
from .materiaView import MateriaViewSet
from .carreraView import CarreraViewSet

# Modelos Secundarios - Relaciones (1,*)

from .avanceMateriaView import AvanceMateriaViewSet
from .disponibilidadView import DisponibilidadViewSet
from .perfilView import PerfilViewSet

# Modelos Secundarios - Relaciones (*,*)

from .alumnoMateriaView import AlumnoMateriaViewSet
