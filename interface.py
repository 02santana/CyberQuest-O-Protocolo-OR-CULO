import sys
import time


def digitar_texto(texto, velocidade=0.02):
  for letra in texto:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(velocidade)
  print()


def mostrar_pistas():
  print("\n" + "=" * 48)
  print("         BANCO DE DADOS DE PISTAS (MOCK)")
  print("=" * 48)

  pistas = {
      "Mensagem 03h17": (
          "Aviso anónimo recebido no terminal: 'O ORÁCULO não falhou.'"
      ),
      "Ficheiro Incompleto": (
          "Contém 3 nomes e coordenadas do antigo centro de dados."
      ),
      "Dante Moreau": (
          "Investigador independente. Informações úteis, intenções incertas."
      ),
  }

  for titulo, descricao in pistas.items():
    digitar_texto(f"[*] {titulo}: {descricao}", velocidade=0.01)

  print("=" * 48)
  input("\nPressione ENTER para voltar ao menu...")


def menu_principal():
  while True:
    print("\n" + "#" * 48)
    print("    CYBERQUEST: O PROTOCOLO ORÁCULO - TERMINAL")
    print("#" * 48)
    print("1. Aceder ao Terminal NEXUS (Iniciar Investigação)")
    print("2. Ver Banco de Pistas Coletadas")
    print("3. Desconectar (Sair)")
    print("#" * 48)

    opcao = input("\nEscolha uma opção (1-3): ").strip()

    if opcao == "1":
      print("\n--- INICIANDO CONEXÃO SEGURA ---")
      digitar_texto(
          "PHANTOM, acesso concedido. A investigar centro de dados...", 0.02
      )
      digitar_texto("Sinal detetado às 03h17. Prazo: 72 horas.", 0.02)
      input("\nPressione ENTER para continuar...")
    elif opcao == "2":
      mostrar_pistas()
    elif opcao == "3":
      digitar_texto("\nA encerrar sessão... Até à próxima, PHANTOM.", 0.02)
      break
    else:
      print("\n[ERRO] Opção inválida! Digite apenas 1, 2 ou 3.")


if __name__ == "__main__":
  menu_principal()