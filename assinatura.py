import pandas as pd

excel_file = "banco-dados-pf.xlsx"

def convert_excel_to_txt(excel_file, sheet_name, txt_file):
    # Ler o arquivo Excel
    df = pd.read_excel(excel_file, sheet_name=sheet_name)

    # Abrir o arquivo txt para escrita
    with open(txt_file, 'w', encoding='utf-8') as f:
        # Escrever o cabeçalho
        f.write("Fiscalização de Produtos Químicos pela Polícia Federal no Brasil\n")
        f.write("="*63 + "\n\n")

        # Escrever cada seção com base nos dados do DataFrame
        f.write("1. Legislação e Regulamentação\n")
        f.write("-"*30 + "\n")
        f.write(f"- {df.loc[0, 'Legislação']}\n")
        f.write(f"- {df.loc[1, 'Legislação']}\n\n")

        f.write("2. Agentes Fiscalizadores\n")
        f.write("-"*30 + "\n")
        f.write(f"- {df.loc[0, 'Agentes']}\n")
        f.write(f"- {df.loc[1, 'Agentes']}\n\n")

        f.write("3. Procedimentos de Fiscalização\n")
        f.write("-"*30 + "\n")
        for i in range(len(df)):
            if not pd.isna(df.loc[i, 'Procedimentos']):
                f.write(f"- {df.loc[i, 'Procedimentos']}\n")
        f.write("\n")

        f.write("4. Penalidades\n")
        f.write("-"*30 + "\n")
        for i in range(len(df)):
            if not pd.isna(df.loc[i, 'Penalidades']):
                f.write(f"- {df.loc[i, 'Penalidades']}\n")
        f.write("\n")

        f.write("5. Importância da Fiscalização\n")
        f.write("-"*30 + "\n")
        for i in range(len(df)):
            if not pd.isna(df.loc[i, 'Importância']):
                f.write(f"- {df.loc[i, 'Importância']}\n")
        f.write("\n")

        f.write("Conclusão\n")
        f.write("-"*9 + "\n")
        f.write("A fiscalização de produtos químicos pela Polícia Federal é essencial para a segurança pública no Brasil, envolvendo procedimentos rigorosos e colaboração entre órgãos governamentais para garantir o uso seguro e legal dos produtos químicos.\n")

# Nome do arquivo Excel, nome da planilha, e nome do arquivo txt de saída
excel_file = 'dados_fiscalizacao.xlsx'
sheet_name = 'Sheet1'
txt_file = 'Fiscalizacao_Produtos_Quimicos_PF.txt'

convert_excel_to_txt(excel_file, sheet_name, txt_file)
