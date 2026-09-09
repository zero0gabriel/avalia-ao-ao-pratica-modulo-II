from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Jogo(Base):
    __tablename__ = "jogos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    genero: Mapped[str] = mapped_column(String(50), nullable=False)
    nota: Mapped[int] = mapped_column(nullable=False)
    imagem_url: Mapped[str] = mapped_column(String(1024), default="")

    def __rep__(self):
        return f"Jogo(id={self.id!r}), nome={self.nome!r}"