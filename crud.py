from models import Livro
from database import conectar


def adicionar_livro(livro: Livro):
    """Adicionar"""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM livros WHERE id = ?",
        (livro.id,)
    )

    if cursor.fetchone() is not None:
        conn.close()
        return None

    cursor.execute(
        """
        INSERT INTO livros (id, titulo, autor, disponivel, ano)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            livro.id,
            livro.titulo,
            livro.autor,
            livro.disponivel,
            livro.ano
        )
    )

    conn.commit()
    conn.close()

    return livro


def excluir_livro(id):
    """Excluir"""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM livros WHERE id = ?",
        (id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return None

    conn.close()
    return True


def buscar_livro(id):
    """Buscar"""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, titulo, autor, disponivel, ano
        FROM livros
        WHERE id = ?
        """,
        (id,)
    )

    resultado = cursor.fetchone()
    conn.close()

    if resultado is None:
        return None

    return {
        "id": resultado[0],
        "titulo": resultado[1],
        "autor": resultado[2],
        "disponivel": bool(resultado[3]),
        "ano": resultado[4]
    }


def listar_livros():
    """Listar"""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, titulo, autor, disponivel, ano
        FROM livros
        """
    )

    resultados = cursor.fetchall()
    conn.close()

    livros = []

    for resultado in resultados:
        livros.append({
            "id": resultado[0],
            "titulo": resultado[1],
            "autor": resultado[2],
            "disponivel": bool(resultado[3]),
            "ano": resultado[4]
        })

    return livros


def atualizar_livro(id, livro_atualizado: Livro):
    """Atualizar"""
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE livros
        SET titulo = ?, autor = ?, disponivel = ?, ano = ?
        WHERE id = ?
        """,
        (
            livro_atualizado.titulo,
            livro_atualizado.autor,
            livro_atualizado.disponivel,
            livro_atualizado.ano,
            id
        )
    )

    conn.commit()

    if cursor.rowcount == 0:
        conn.close()
        return None

    conn.close()
    return livro_atualizado