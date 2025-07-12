# import scipy.stats as st
# from create_graphics import bp
# import read_data as rd
# 
# nome_arq_series = "ipeadata[02-07-2025-09-51] (1).xlsx - Séries.csv"
# def main():
#     dados1, dados2 = rd.readData(nome_arq_series)
# 
#     bp(dados1, dados2, "São Paulo", "Minas Gerais")
# 
#     # EXEMPLO DE TESTE T COM OS DADOS ACHATADOS (bagulho q o Gemini criou)
#     if dados1.size > 1 and dados2.size > 1: # Precisa de pelo menos 2 pontos para t-test
#         estatistica_t, valor_p = st.ttest_ind(dados1, dados2, equal_var=False, nan_policy='omit')
#         print(f"\nResultado do Teste T de Independência:")
#         print(f"Estatística T: {estatistica_t}")
#         print(f"Valor P: {valor_p}")
#         if valor_p < 0.05: # Considerando um nível de significância de 5%
#             print("Há uma diferença estatisticamente significativa no número de pequenas empresas entre os dois estados.")
#         else:
#             print("Não há evidências estatisticamente significativas de uma diferença no número de pequenas empresas entre os dois estados.")
#     else:
#         print("\nNão há dados suficientes para realizar o Teste T (cada grupo precisa de mais de um ponto de dados).")
# 
# if __name__ == "__main__":
#     main()