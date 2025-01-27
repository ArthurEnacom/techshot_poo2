from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from techshot.orm.base import Base

class Postagem(Base):
    """
    Classe que representa uma postagem na rede
    social Piui, mapeado para o banco de dados.
    """

    # Nome da tabela no banco de dados.
    __tablename__ = 'tb_postagem'

    # Coluna que representa o id da postagem.
    id = Column(Integer, primary_key=True)
    # Coluna que representa a data em que o objeto foi criado.
    data_criacao = Column(Date, nullable=False)
    # Coluna que representa a data em que o objeto foi atualizado.
    data_atualizacao = Column(Date, nullable=False)
    # Coluna que representa a versao em que o objeto se encontra.
    versao = Column(Integer, nullable=False, autoincrement=True)

    # Coluna que representa o texto da postagem.
    texto = Column(String(255), nullable=False)
    # Coluna que representa o id do usuário que postou.
    id_usuario = Column(Integer, ForeignKey('tb_usuario.id'))
    # Coluna que representa o relacionamento com a tabela de usuários.
    usuario = relationship('Usuario', back_populates='postagens')