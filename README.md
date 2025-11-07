# Valorant Highlight Tracker v1

> Automação inteligente para detectar e salvar automaticamente seus **melhores momentos (ACE / CLUTCH)** no Valorant.

Este projeto utiliza **OCR** e **captura de tela em tempo real** para identificar quando uma jogada de destaque ocorre no jogo e gravar automaticamente os últimos segundos, salvando o clipe em uma pasta local.

---

## Funcionalidades

✅ Detecção automática de **ACE** e **CLUTCH** via OCR  
✅ Confirmação dupla para evitar falsos positivos  
✅ Pausa automática quando o jogo não está rodando  
✅ Gravação dos últimos segundos do gameplay  
✅ Configuração simples e totalmente offline  

---

## Pré-requisitos

- **Python 3.9+**
- **Tesseract OCR** (para reconhecimento de texto)
- Sistema operacional: **Windows 10/11**

 [Baixar Tesseract OCR (UB Mannheim Build)](https://github.com/UB-Mannheim/tesseract/wiki)

Durante a instalação, copie o caminho de instalação (exemplo):
C:\Program Files\Tesseract-OCR\tesseract.exe
Depois, substitua esse caminho na variável:
**pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"**
---

## Instalação

**1 - Clone o repositório**

**2 - Instale as dependências: pip install pyautogui opencv-python pytesseract pillow numpy psutil**

**3 - Crie uma pasta chamada highlights no mesmo diretório para armazenar as capturas.**

## Uso

**Execute o script:
python main.py**

**Durante o jogo:**

**O programa monitora sua tela.
Quando detectar um ACE ou CLUTCH, ele grava os últimos 30 segundos da partida.
O clipe será salvo automaticamente na pasta highlights criada anteriormente.**

---

| Tecnologia                                           | Função                              |
| ---------------------------------------------------- | ----------------------------------- |
| [Python](https://www.python.org/)                    | Linguagem principal                 |
| [OpenCV](https://opencv.org/)                        | Manipulação de imagem e vídeo       |
| [PyAutoGUI](https://pyautogui.readthedocs.io/)       | Captura de tela                     |
| [PyTesseract](https://pypi.org/project/pytesseract/) | OCR para detectar textos do jogo    |
| [Psutil](https://pypi.org/project/psutil/)           | Verificação do processo do Valorant |

---

## Observações.

O script não interfere no jogo (apenas lê a tela).

Não utiliza APIs ou dados internos do Valorant.

**Pode gerar falsos positivos em menus ou telas com textos similares, mas o sistema de confirmação dupla reduz bastante esses casos.**

---

## 🤝 Contribuindo

** Sinta-se à vontade para contribuir!**
**Abra uma issue para relatar bugs ou sugerir melhorias, ou envie um pull request.**
---

## 🧑‍💻 Autor

**Rafael Neves**
📧 Contato: rafahneves1@gmail.com

🌐 GitHub: https://github.com/RafaNeves1
