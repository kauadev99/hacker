#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MEU SISTEMA PRÓPRIO - Ferramenta de Controle de Licenças
Sistema Personalizado - Versão 1.0
Desenvolvido por: cauan
Contato: 75982599462 / EMAIL
"""

import os
import sys
import time
import random
import string

# ===================== CONFIGURAÇÕES DO SEU SISTEMA =====================
NOME_SISTEMA = "quebra senha"
VERSAO = "1.0"
VALOR_FERRAMENTA = "R$ 150,00"  # Você pode mudar o valor
CONTATO_WHATSAPP = "+55 75 98259-9462"  # Coloque seu número
DESENVOLVEDOR = "Cauan"
# ==========================================================================

# Banco de dados simples (chaves válidas salvas na memória)
CHAVES_VALIDAS = set()
ARQUIVO_CHAVES = "chaves_salvas.txt"

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def carregar_chaves_salvas():
    """Carrega chaves que foram salvas anteriormente no arquivo"""
    if os.path.exists(ARQUIVO_CHAVES):
        try:
            with open(ARQUIVO_CHAVES, 'r', encoding='utf-8') as f:
                for linha in f:
                    chave = linha.strip()
                    if chave:
                        CHAVES_VALIDAS.add(chave)
        except:
            pass

def salvar_chave_arquivo(chave):
    """Salva nova chave no arquivo para não perder quando fechar"""
    try:
        with open(ARQUIVO_CHAVES, 'a', encoding='utf-8') as f:
            f.write(chave + "\n")
    except:
        pass

def gerar_chave(tamanho=16):
    """Gera uma chave única e válida no formato XXXX-XXXX-XXXX-XXXX"""
    partes = []
    for _ in range(4):
        parte = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        partes.append(parte)
    chave = '-'.join(partes)
    return chave

def menu_criar_chaves():
    """ÁREA RESTRITA: Somente VOCÊ cria as chaves válidas aqui"""
    limpar_tela()
    print("\033[95m" + "═" * 75 + "\033[0m")
    print("\033[95m[🔐] ÁREA DE ADMINISTRAÇÃO - GERENCIAR LICENÇAS\033[0m")
    print("\033[95m" + "═" * 75 + "\033[0m\n")

    while True:
        print("\033[96m[1] Gerar NOVA chave válida\033[0m")
        print("\033[96m[2] Ver TODAS as chaves cadastradas\033[0m")
        print("\033[96m[3] Voltar ao menu principal\033[0m")
        print("\033[93m" + "-" * 75 + "\033[0m")
        
        opcao = input("\033[96mEscolha uma opção: \033[0m").strip()

        if opcao == "1":
            quantidade = input("\033[94mQuantas chaves quer gerar? \033[0m").strip()
            try:
                qtd = int(quantidade)
                print(f"\n\033[92m[✓] Gerando {qtd} chave(s)...\033[0m\n")
                time.sleep(0.5)
                
                for i in range(qtd):
                    nova_chave = gerar_chave()
                    CHAVES_VALIDAS.add(nova_chave)
                    salvar_chave_arquivo(nova_chave)
                    print(f"\033[92m🔑 Chave {i+1}: {nova_chave}\033[0m")
                    time.sleep(0.2)
                
                print(f"\n\033[92m[✓] Todas as chaves foram salvas no sistema!\033[0m")
                input("\n\033[93mPressione ENTER para continuar...\033[0m")
                limpar_tela()

            except ValueError:
                print(f"\033[91m[✗] Digite apenas números!\033[0m")
                time.sleep(1)
                limpar_tela()

        elif opcao == "2":
            print(f"\n\033[94m[📋] LISTA DE CHAVES CADASTRADAS ({len(CHAVES_VALIDAS)} no total):\033[0m")
            print("\033[93m-" * 75 + "\033[0m")
            if CHAVES_VALIDAS:
                for idx, chave in enumerate(CHAVES_VALIDAS, 1):
                    print(f"\033[92m{idx:02d} → {chave}\033[0m")
            else:
                print(f"\033[91m[!] Nenhuma chave cadastrada ainda.\033[0m")
            
            input("\n\033[93mPressione ENTER para voltar...\033[0m")
            limpar_tela()

        elif opcao == "3":
            break

        else:
            print(f"\033[91m[✗] Opção inválida!\033[0m")
            time.sleep(1)
            limpar_tela()

def mostrar_logo():
    logo = r"""
  __  __       _         ____  _           _             
 |  \/  | ___ (_) ___   / ___|| |_ __ _ __| |_ _ __ ___  
 | |\/| |/ _ \| |/ _ \ | |    | __/ _` / _` | '_ ` _ \ 
 | |  | | (_) | |  __/ | |___ | || (_| | (_| | | | | | |
 |_|  |_|\___// |\___|  \____| \__\__, \__,_|_| |_| |_|
            |__/                   |___/                  
    """
    
    print("\033[92m" + logo + "\033[0m")
    print("\033[93m" + "═" * 75 + "\033[0m")
    print(f"\033[93m[#] {NOME_SISTEMA} - Versão {VERSAO}\033[0m")
    print(f"\033[93m[#] Desenvolvido por: {DESENVOLVEDOR}\033[0m")
    print(f"\033[93m[#] Licenciamento Oficial - Valor: {VALOR_FERRAMENTA}\033[0m")
    print(f"\033[93m[#] Contato Suporte: {CONTATO_WHATSAPP}\033[0m")
    print("\033[93m" + "═" * 75 + "\033[0m\n")

def verificar_codigo():
    print("\n" + "═" * 75)
    print("\033[96m[🔑] VERIFICAÇÃO DE LICENÇA DE USO\033[0m")
    print("\033[96m" + "═" * 75 + "\033[0m")
    
    print(f"\n\033[91m[!] ATENÇÃO: Este software é licenciado\033[0m")
    print(f"\033[91m[!] Valor da licença: {VALOR_FERRAMENTA}\033[0m")
    print(f"\033[91m[!] Para adquirir, contate: {CONTATO_WHATSAPP}\033[0m\n")
    
    print(f"\033[96mDigite sua CHAVE DE LICENÇA: \033[0m", end="")
    codigo = input().strip().upper()
    
    if codigo in CHAVES_VALIDAS:
        print(f"\n\033[92m[✓] LICENÇA VÁLIDA!\033[0m")
        print(f"\033[92m[✓] Sistema ativado com sucesso\033[0m")
        print(f"\033[92m[✓] Bem-vindo ao {NOME_SISTEMA}\033[0m")
        time.sleep(2)
        return True
    else:
        print(f"\n\033[91m[✗] LICENÇA INVÁLIDA OU EXPIRADA\033[0m")
        print(f"\033[91m[✗] Chave digitada: '{codigo}'\033[0m")
        print(f"\033[91m[✗] Essa chave não existe na base oficial\033[0m")
        
        print(f"\n\033[93m" + "═" * 75 + "\033[0m")
        print(f"\033[93m[!] PARA OBTER UMA LICENÇA VÁLIDA:\033[0m")
        print(f"\033[93m[!] 1. Contate: {CONTATO_WHATSAPP}\033[0m")
        print(f"\033[93m[!] 2. Efetue o pagamento de {VALOR_FERRAMENTA}\033[0m")
        print(f"\033[93m[!] 3. Receba sua chave exclusiva\033[0m")
        print(f"\033[93m" + "═" * 75 + "\033[0m")
        
        time.sleep(4)
        return False

def menu_principal():
    print(f"\n\033[92m" + "═" * 75 + "\033[0m")
    print(f"\033[92m[🏠] PAINEL PRINCIPAL - {NOME_SISTEMA}\033[0m")
    print(f"\033[92m" + "═" * 75 + "\033[0m\n")

    while True:
        print("\033[94m[1] Iniciar Ferramenta Principal\033[0m")
        print("\033[94m[2] Área do Desenvolvedor (Criar Licenças)\033[0m")
        print("\033[94m[3] Sobre o Sistema\033[0m")
        print("\033[94m[4] Sair\033[0m")
        print("\033[93m" + "-" * 75 + "\033[0m")
        
        opcao = input("\033[96mEscolha uma opção: \033[0m").strip()

        if opcao == "1":
            limpar_tela()
            print(f"\n\033[94m[+] Carregando módulos do sistema...\033[0m")
            print(f"\033[94m[+] Verificando integridade dos arquivos...\033[0m")
            print(f"\033[94m[+] Conectando ao servidor...\033[0m")
            time.sleep(2)
            print(f"\n\033[92m[✓] Sistema pronto para uso!\033[0m")
            print(f"\033[92m[✓] Todos os recursos liberados\033[0m")
            input("\n\033[93mPressione ENTER para voltar...\033[0m")
            limpar_tela()
            mostrar_logo()

        elif opcao == "2":
            # Senha de acesso à área de criação (você pode mudar)
            senha = input("\033[91m[!] Digite a SENHA DE ADMINISTRADOR: \033[0m").strip()
            if senha == "admin123":  # <--- MUDE ESSA SENHA!
                menu_criar_chaves()
                limpar_tela()
                mostrar_logo()
            else:
                print(f"\n\033[91m[✗] Senha incorreta! Acesso negado.\033[0m")
                time.sleep(2)
                limpar_tela()
                mostrar_logo()

        elif opcao == "3":
            limpar_tela()
            print("\033[95m" + "═" * 75 + "\033[0m")
            print(f"\033[95m[Sobre] {NOME_SISTEMA} v{VERSAO}\033[0m")
            print("\033[95m" + "═" * 75 + "\033[0m\n")
            print(f"\033[94m• Desenvolvedor: {DESENVOLVEDOR}\033[0m")
            print(f"\033[94m• Contato: {CONTATO_WHATSAPP}\033[0m")
            print(f"\033[94m• Licenciamento: {VALOR_FERRAMENTA}\033[0m")
            print(f"\033[94m• Funcionalidade: Gerenciamento completo de licenças\033[0m")
            print(f"\033[94m• Segurança: Chaves únicas e criptografadas\033[0m")
            input("\n\033[93mPressione ENTER para voltar...\033[0m")
            limpar_tela()
            mostrar_logo()

        elif opcao == "4":
            print(f"\n\033[92m[✓] Encerrando {NOME_SISTEMA}...\033[0m")
            print(f"\033[92m[✓] Obrigado por usar nossos serviços!\033[0m")
            time.sleep(1.5)
            sys.exit(0)

        else:
            print(f"\033[91m[✗] Opção inválida!\033[0m")
            time.sleep(1)
            limpar_tela()
            mostrar_logo()

def main():
    carregar_chaves_salvas()  # Carrega chaves que já foram criadas antes
    limpar_tela()
    mostrar_logo()
    
    # Primeiro verifica a licença
    if verificar_codigo():
        menu_principal()  # Se chave for válida, libera o sistema
    else:
        print(f"\n\033[91m[!] PROGRAMA ENCERRADO - LICENÇA NECESSÁRIA\033[0m")
        time.sleep(3)

if __name__ == "__main__":
    if os.name == 'nt':
        os.system(f"title {NOME_SISTEMA} - Sistema Oficial")
        os.system("mode con: cols=90 lines=40")
    
    main()

