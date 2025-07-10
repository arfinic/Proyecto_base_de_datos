from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Asociacion(Base):
    __tablename__ = 'asociaciones'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    ciudad = Column(String)
    pais = Column(String)
    jugadores = relationship("Jugador", back_populates="asociacion")

class Jugador(Base):
    __tablename__ = 'jugadores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    fecha_nac = Column(Date)
    genero = Column(String)
    ciudad = Column(String)
    pais = Column(String)
    asociacion_id = Column(Integer, ForeignKey('asociaciones.id'), nullable=True)
    asociacion = relationship("Asociacion", back_populates="jugadores")

    equipos1 = relationship("EquipoDoble", foreign_keys='EquipoDoble.jugador1_id', back_populates="jugador1")
    equipos2 = relationship("EquipoDoble", foreign_keys='EquipoDoble.jugador2_id', back_populates="jugador2")
    participaciones = relationship("Participacion", back_populates="jugador")

class EquipoDoble(Base):
    __tablename__ = 'equipos_dobles'
    id = Column(Integer, primary_key=True)
    jugador1_id = Column(Integer, ForeignKey('jugadores.id'))
    jugador2_id = Column(Integer, ForeignKey('jugadores.id'))
    jugador1 = relationship("Jugador", foreign_keys=[jugador1_id], back_populates="equipos1")
    jugador2 = relationship("Jugador", foreign_keys=[jugador2_id], back_populates="equipos2")
    participaciones = relationship("Participacion", back_populates="equipo")

class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    edad_minima = Column(Integer)
    edad_maxima = Column(Integer)
    genero = Column(String)
    sets_por_partido = Column(Integer)
    puntos_por_set = Column(Integer)
    participaciones = relationship("Participacion", back_populates="categoria")
    partidos = relationship("Partido", back_populates="categoria")
    grupos = relationship("Grupo", back_populates="categoria")

class Torneo(Base):
    __tablename__ = 'torneos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    fecha_inscripcion_i = Column(Date)
    fecha_inscripcion_f = Column(Date)
    fecha_competencia_i = Column(Date)
    fecha_competencia_f = Column(Date)
    mesas_disponibles = Column(Integer)
    participaciones = relationship("Participacion", back_populates="torneo")
    partidos = relationship("Partido", back_populates="torneo")

class Grupo(Base):
    __tablename__ = 'grupos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    categoria = relationship("Categoria", back_populates="grupos")
    participaciones = relationship("Participacion", back_populates="grupo")

class Participacion(Base):
    __tablename__ = 'participaciones'
    id = Column(Integer, primary_key=True)
    jugador_id = Column(Integer, ForeignKey('jugadores.id'), nullable=True)
    equipo_id = Column(Integer, ForeignKey('equipos_dobles.id'), nullable=True)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    torneo_id = Column(Integer, ForeignKey('torneos.id'))
    grupo_id = Column(Integer, ForeignKey('grupos.id'), nullable=True)
    jugador = relationship("Jugador", back_populates="participaciones")
    equipo = relationship("EquipoDoble", back_populates="participaciones")
    categoria = relationship("Categoria", back_populates="participaciones")
    torneo = relationship("Torneo", back_populates="participaciones")
    grupo = relationship("Grupo", back_populates="participaciones")
    partidos = relationship("ParticipantePartido", back_populates="participacion")

class Partido(Base):
    __tablename__ = 'partidos'
    id = Column(Integer, primary_key=True)
    tipo_partido = Column(String) 
    horario_inicio = Column(DateTime)
    mesa_asignada = Column(Integer)
    fase = Column(String) 
    ronda_eliminacion = Column(String, nullable=True)
    ganador_id = Column(Integer, ForeignKey('participaciones.id'))
    perdedor_id = Column(Integer, ForeignKey('participaciones.id'))
    is_bye = Column(Boolean, default=False)
    torneo_id = Column(Integer, ForeignKey('torneos.id'))
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    participantes = relationship("ParticipantePartido", back_populates="partido")
    resultados = relationship("ResultadoSet", back_populates="partido")
    torneo = relationship("Torneo", back_populates="partidos")
    categoria = relationship("Categoria", back_populates="partidos")

class ParticipantePartido(Base):
    __tablename__ = 'participantes_partido'
    id = Column(Integer, primary_key=True)
    rol = Column(String) 
    participacion_id = Column(Integer, ForeignKey('participaciones.id'))
    partido_id = Column(Integer, ForeignKey('partidos.id'))
    participacion = relationship("Participacion", back_populates="partidos")
    partido = relationship("Partido", back_populates="participantes")

class ResultadoSet(Base):
    __tablename__ = 'resultados_sets'
    id = Column(Integer, primary_key=True)
    numero_set = Column(Integer)
    puntos_jugador1 = Column(Integer)
    puntos_jugador2 = Column(Integer)
    partido_id = Column(Integer, ForeignKey('partidos.id'))
    partido = relationship("Partido", back_populates="resultados")