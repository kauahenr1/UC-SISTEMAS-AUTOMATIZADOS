# TP05 — Sistemas Sequenciais e GRAFCET/SFC
## Atividade 24 — Semáforo temporizado (obrigatória)

**Disciplina:** Sistemas Automatizados — USJT, 2026.2  
**Referência:** Prof. Calvetti, TP05 — Gabarito detalhado, páginas 12–13.

## Objetivo
Modelar um semáforo cíclico em GRAFCET, com etapas, ações, transições e receptividades temporais verificáveis.

## Etapas e ações
| Etapa | Situação | Ação | Duração |
|---|---|---|---|
| E0 (inicial) | Sinal vermelho | VERMELHO = 1 | 8 s |
| E1 | Sinal verde | VERDE = 1 | 10 s |
| E2 | Sinal amarelo | AMARELO = 1 | 3 s |

Apenas uma cor deve estar ligada por etapa; as outras permanecem desligadas.

## Transições
| Transição | Origem → destino | Receptividade |
|---|---|---|
| T0 | E0 → E1 | Tempo de E0 ≥ 8 s |
| T1 | E1 → E2 | Tempo de E1 ≥ 10 s |
| T2 | E2 → E0 | Tempo de E2 ≥ 3 s |

Os tempos são medidos **desde a ativação da respectiva etapa**. O ciclo completo dura 21 s, desconsiderando atrasos de implementação.

## Arquivos
- `semaforo.drawio`: diagrama-fonte editável no https://app.diagrams.net/
- `semaforo.png`: visualização de referência do diagrama; **não é evidência de teste executado**.
- `casos_teste.csv`: roteiro de testes com resultados reais ainda não preenchidos.

## Procedimento de validação manual (pendente)
1. Abrir o arquivo `.drawio` no diagrams.net e conferir a notação.
2. Percorrer as etapas com tempos 7,9 s; 8,0 s; 9,9 s; 10,0 s; 3,0 s.
3. Registrar a etapa obtida e a situação (PASSA/FALHA) no CSV.
4. Exportar a evidência final e atualizar esta seção.

## Hipóteses e limites
O diagrams.net é um editor gráfico e **não executa o GRAFCET automaticamente**. A validação prevista é por percurso manual. O modelo representa um semáforo didático sem controlador físico.

## Resultados
**Pendente de validação manual.** Nenhum resultado experimental foi declarado como executado.
