import pandas as pd
import sqlite3

def extrair():
    df = pd.read_csv("atendimentos.csv")
    return df

def transformar(df):
    df = df.dropna(subset=["cliente", "preco"])
    df["servico"] = df["servico"].str.title()
    df["data"] = pd.to_datetime(df["data"])
    return df

def analisar(df):
    print("=== RELATÓRIO DA BARBEARIA ===")
    print(f"Total de atedimentos: {len(df)}")
    print(f"Total geral: R$ {df["preco"].sum()}")
    print("\nPor servico:")
    print(df.groupby("servico")["preco"].sum())
    print("\nPor forma de pagamento:")
    print(df.groupby("forma_pagamento")["preco"].sum())


def carregar(df):
    conn = sqlite3.connect ("barbearia.db")
    df.to_sql("atendimentos", conn, if_exists="replace", index=False)
    conn.close()
    print("Dados carregados no banco com sucesso.")


def consultar():
    conn = sqlite3.connect("barbearia.db")
    query = "SELECT servico, SUM(preco) FROM atendimentos GROUP BY servico"
    resultado = pd.read_sql_query(query, conn)
    print(resultado)
    query2 = "SELECT cliente, COUNT(*) FROM atendimentos GROUP BY cliente ORDER BY COUNT(*) DESC"
    resultado2 = pd.read_sql(query2, conn)
    print(resultado2)
    query3 = "SELECT * FROM atendimentos WHERE preco > 30"
    resultado3 = pd.read_sql(query3, conn)
    print(resultado3)
    conn.close()

def exportar(df):
    df.to_csv("relatorio_final.csv", index=False, encoding="utf-8-sig")
    print("Relatório exportado com sucesso.")

# PIPELINE
df = extrair()
df = transformar(df)
analisar(df)
carregar(df)
consultar()
exportar(df)


