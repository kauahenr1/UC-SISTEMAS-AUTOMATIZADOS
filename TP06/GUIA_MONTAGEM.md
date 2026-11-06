# Guia de montagem e validação — TP06 obrigatória

1. Abra https://plcsimulator.online e inicie um projeto vazio.
2. Crie as tags `START`, `STOP_OK`, `EMG_OK` e `MOTOR`.
3. Monte o rung ilustrado no README. `EMG_OK` e `STOP_OK` devem estar em série **antes** da divisão entre `START` e `MOTOR`.
4. Inicie a simulação com `START=0`, `STOP_OK=1` e `EMG_OK=1`: `MOTOR=0`.
5. Pressione `START`: `MOTOR=1` (T01). Solte `START`: `MOTOR=1` (T02).
6. Altere `STOP_OK=0`: `MOTOR=0` (T03). Restaure `STOP_OK=1` e confira que não há religamento sem novo `START`.
7. Parta novamente, depois altere `EMG_OK=0`: `MOTOR=0` (T04).
8. Com emergência ainda ativa, pressione `START`: `MOTOR=0` (T05).
9. Preencha `Obtido` e `Situacao` no CSV apenas com os resultados realmente observados. Salve o projeto/link e capturas de tela dos estados decisivos.

**Importante:** a interface do simulador pode mudar; localize os elementos por sua função. Não confunda o roteiro esperado com teste executado.
