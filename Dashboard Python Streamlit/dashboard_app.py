import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(layout="wide", page_title="Dashboard Agro Goiás")

# 2. CARREGAMENTO E TRATAMENTO DE DADOS (AGORA COM TODAS AS CIDADES)
@st.cache_data
def load_and_clean_data():
    df = pd.read_csv("financiamentoPecuaria.csv", encoding="utf-8", sep=";")
    df = df.replace('-', 0)
    
    # REMOVIDO .head(10) para exibir as 246 cidades
    
    # Limpeza da coluna de Localidade
    df.iloc[:, 0] = df.iloc[:, 0].astype(str).str.strip()
    
    # Tratamento numérico para todas as colunas de anos
    colunas_anos = df.columns[1:]
    for col in colunas_anos:
        if df[col].dtype == 'object':
            df[col] = df[col].str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    
    # Média por localidade (Md_Invest)
    df["Md_Invest"] = df[colunas_anos].mean(axis=1).round(2)
    return df

df = load_and_clean_data()

# 3. FILTROS NA SIDEBAR
st.sidebar.header("Filtros de Pesquisa")
localidades = df[df.columns[0]].unique().tolist()
opcoes_localidade = ["Todos"] + localidades
localidade_selecionada = st.sidebar.selectbox("Selecione a Localidade:", opcoes_localidade)

# Define colunas_anos (exclui a primeira de nomes e a última de Md_Invest)
colunas_anos = df.columns[1:-1]

# 4. TÍTULOS DO DASHBOARD
st.title('📊 Dashboard Financeiro - Agro Goiás (2014-2024)')
st.write(f"Exibindo dados de **{len(df)}** localidades.")
st.markdown("---")

# 5. DEFINIÇÃO DO LAYOUT EM COLUNAS (Conforme suas imagens)
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# --- PRIMEIRA LINHA ---

with col1:
    # Filtro para localidade escolhida (Gráfico de Barras)
    if localidade_selecionada == "Todos":
        df_plot = df[df[df.columns[0]] != "Média"]
        investimentos_ano = df_plot[colunas_anos].mean()
        st.write("### Média dos investimentos por ano (Todas as localidades):")
        st.bar_chart(investimentos_ano)
    else:
        df_local = df[df[df.columns[0]] == localidade_selecionada]
        st.write(f"### Dados filtrados para {localidade_selecionada}:")
        st.dataframe(df_local)
        if not df_local.empty:
            investimentos_local = df_local.iloc[0][colunas_anos]
            st.write(f"### Evolução dos investimentos para {localidade_selecionada}:")
            st.bar_chart(investimentos_local)

with col2:
    st.write("### Gráfico de Linhas: Evolução dos Investimentos")
    if localidade_selecionada == "Todos":
        investimentos_ano_lin = df[df[df.columns[0]] != "Média"].loc[:, colunas_anos].mean()
    else:
        # Reutiliza o df_local definido na col1
        investimentos_ano_lin = df_local.iloc[0][colunas_anos]
    st.line_chart(investimentos_ano_lin)

# --- SEGUNDA LINHA ---

with col3:
    st.write("### Comparação da Cidade com a Média Geral")
    if localidade_selecionada != "Todos" and not df_local.empty:
        investimentos_local_val = df_local.iloc[0][colunas_anos]
        investimentos_media_geral = df[df[df.columns[0]] != "Média"].loc[:, colunas_anos].mean()
        
        df_comparacao = pd.DataFrame({
            "Ano": colunas_anos,
            localidade_selecionada: investimentos_local_val.values,
            "Média Geral": investimentos_media_geral.values
        })
        df_comparacao.set_index("Ano", inplace=True)
        st.bar_chart(df_comparacao)
    else:
        st.info("Selecione uma localidade para visualizar a comparação.")

with col4:
    st.write("### Ano com Maior Investimento")
    if localidade_selecionada != "Todos" and not df_local.empty:
        investimentos_local_max = df_local.iloc[0][colunas_anos]
        ano_max = investimentos_local_max.idxmax()
        valor_max = investimentos_local_max.max()
        
        st.metric(label="Ano com Maior Investimento", 
                  value=ano_max, 
                  delta=f"Valor: R$ {valor_max:,.2f}")
    else:
        st.info("Selecione uma localidade para visualizar o pico de investimento.")

# 6. TABELA COMPLETA NO RODAPÉ
st.markdown("---")
st.subheader("Base de Dados Completa")
st.dataframe(df, use_container_width=True)