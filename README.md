### Renomeador em Massa de PDFs

**Descrição:**
Este script Python foi desenvolvido para facilitar a renomeação em massa de arquivos PDF, especialmente útil para setores como o de Recursos Humanos. Ele permite selecionar uma área específica de um PDF para extrair texto e usar esse texto como o novo nome do arquivo. Isso é particularmente útil para renomear arquivos de folha de pagamento, que são exportados com códigos aleatórios, dificultando a identificação.

**Funcionalidade:**
- **Interface Gráfica (GUI):** Utiliza o Tkinter para criar uma interface gráfica amigável.
- **Visualização de PDF:** Permite visualizar PDFs e selecionar uma área específica para extrair o texto.
- **Zoom:** Inclui um slider para ajustar o nível de zoom da visualização do PDF.
- **Renomeação Automática:** Renomeia os arquivos PDF com base no texto extraído da área selecionada.
- **Tratamento de Conflitos:** Verifica se o nome do arquivo já existe e ajusta automaticamente para evitar conflitos.

**Principais Bibliotecas Utilizadas:**
- `tkinter`: Para a criação da interface gráfica.
- `fitz` (PyMuPDF): Para manipulação e visualização de arquivos PDF.
- `PIL` (Python Imaging Library): Para manipulação de imagens dentro do Tkinter.
- `os`: Para operações com o sistema de arquivos, como renomeação e verificação de existência de arquivos.

### Código Principal:
1. **Importação das Bibliotecas:**
   ```python
   import tkinter as tk
   from tkinter import filedialog, messagebox, ttk, Scale
   import fitz  # PyMuPDF
   from PIL import Image, ImageTk
   import os
   ```

2. **Visualização e Seleção de Área do PDF:**
   - Implementação da classe `PDFViewer` que permite visualizar e selecionar uma área específica do PDF.

3. **Funções de Extração e Renomeação:**
   - `extrair_texto_da_area_selecionada()`: Extrai o texto da área selecionada no PDF.
   - `renomear_arquivo()`: Renomeia o arquivo PDF com o texto extraído.

4. **Função Principal:**
   - `iniciar_processo()`: Inicia o processo de renomeação em massa, iterando sobre os arquivos PDF no diretório de origem e renomeando-os com base na seleção.

5. **Interface Gráfica Principal:**
   - Botões e entradas para selecionar diretórios de origem e destino e iniciar o processo de renomeação.

### Exemplo de Uso:
- O usuário seleciona um diretório de origem contendo os arquivos PDF.
- Abre um PDF e seleciona uma área que contém o nome ou identificador desejado.
- O script extrai o texto dessa área e renomeia os arquivos no diretório de origem, salvando-os no diretório de destino com os novos nomes.

Esta ferramenta simplifica o processo de organização e identificação de arquivos PDF, especialmente em ambientes com grande volume de documentos.
