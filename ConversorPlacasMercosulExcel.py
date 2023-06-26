import pandas as pd

conversor = {
    "A": "0",
    "B": "1",
    "C": "2",
    "D": "3",
    "E": "4",
    "F": "5",
    "G": "6",
    "H": "7",
    "I": "8",
    "J": "9"
}

# Ler o arquivo Excel
df = pd.read_excel(r"C:\Users\Willian\OneDrive\Área de Trabalho\ANPV\python\análiseDadosVeículosComRastreadores\relatorioAtivos.xlsx")

# Aplicar a conversão da placa para cada valor na coluna "Placa"
df["Placa"] = df["Placa"].apply(lambda placa: placa[:4] + conversor.get(placa[4], placa[4]) + placa[5:] if isinstance(placa, str) else placa)

# Salvar o dataframe modificado em um novo arquivo Excel
df.to_excel(r"C:\Users\Willian\OneDrive\Área de Trabalho\ANPV\python\análiseDadosVeículosComRastreadores\placasConvertidasSGA3.xlsx", index=False)

print("Placas convertidas com sucesso no arquivo Excel.")