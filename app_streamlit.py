#PRINT 1 
import streamlit as st
from modules.conectar_bd import conectar_bd
from modules.validar_nome_produto import validar_nome_produto
from modules.validar_preco import validar_preco
from modules.validar_estoque import validar_estoque
from modules.cadastrar_produto import cadastrar_produto
from modules.listar_produtos import listar_produtos
from modules.atualizar_produto import atualizar_produto
from modules.deletar_produto import deletar_produto

st.set_page_config(page_title="sistema de produtos", layout="centered")

st.title("Sistema de Gerenciamento de produtos")
st.write("Bem-vindo! Escolha uma opção no menu lateral.")

menu = st.sidebar.radio("menu", ["Cadastrar", "Listar", "Atualizar", "Deletar"])


if menu == "cadastrar":
    st.subheader("Cadastrar Produto")


nome = st.text_input("Nome do produto:")
preco = st.text_input("Preço:")
estoque = st.text_input("Estoque:")


if st.button("Cadastrar"):
    nome_valido = validar_nome_produto(nome)
    preco_valido = validar_preco(preco)
    estoque_valido = validar_estoque(estoque)


    if nome_valido and preco_valido and estoque_valido is not None:
        cadastrar_produto(nome_valido, preco_valido, estoque_valido)
        st.success("Produto Cadastrado com sucesso!")

elif menu == "Listar":
    st.subheader("Lista de produtos")
    conexao, cursor = conectar_bd()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()

    if len(produtos) == 0:
        st.info("Nenhum produto cadastrado ainda.")
    else:
        for p in produtos:
         st.write(f"**ID:** {p[0]} | **Nome:** {p[1]} | **Preço:** R$ {p[2]:.2f} | **Estoque:** {p[3]}")

#PRINT 2
elif menu == "Atualizar":
    st.subheader("Atualizar produto")
    

    id_produto = st.number_input("ID do produto:", min_value=1, step=1)
    nome = st.text_input("Novo nome:")
    preco = st.text_input("Novo preço:")
    estoque = st.text_input("Novo estoque:")


    if st.button("Atualizar"):
        if nome and preco and estoque:
            atualizar_produto(id_produto, nome, preco, estoque)
            st.success("Produto atualizado com sucesso!")
        else:
            st.warning("Preencha todos os campos!")


elif menu == "Deletar":
    st.subheader("deletar produto")


    id_produto = st.number_input("ID do produto para deletar:", min_value=1, step=1 )
    if st.button("Deletar"):
        deletar_produto(id_produto)
        st.success("Produto deletado com sucesso!")




        



#