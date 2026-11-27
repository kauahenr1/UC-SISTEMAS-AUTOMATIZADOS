"""Controle sequencial e de intertravamento da Celula 11 (TP11 / P11)."""

from dataclasses import dataclass, asdict
import json


@dataclass
class ControladorCelula11:
    e0_ok: bool = True
    g1_ok: bool = True
    b1: bool = False
    b2: bool = True
    b3: bool = False
    auto_mode: bool = True
    cmd_start: bool = False
    cmd_stop: bool = False
    cmd_reset: bool = False
    jog_avancar: bool = False
    jog_retornar: bool = False
    run: bool = False
    step_t: bool = False
    step_a: bool = False
    step_r: bool = False
    fault: bool = False
    alarme: str = ""
    rede_ativa: bool = True
    total_pecas: int = 0
    cronometro_s: float = 0.0
    limite_timeout_s: float = 3.0

    @property
    def safe(self) -> bool:
        return bool(self.e0_ok and self.g1_ok and (not self.fault))

    @property
    def m1(self) -> bool:
        return bool(self.safe and self.run and self.auto_mode and self.step_t and (not self.b1))

    @property
    def y1(self) -> bool:
        if not self.safe:
            return False
        if self.auto_mode:
            return bool(self.run and self.step_a and (not self.b3) and (not self.y2))
        return bool(self.jog_avancar and (not self.b3) and (not self.jog_retornar))

    @property
    def y2(self) -> bool:
        if not self.safe:
            return False
        if self.auto_mode:
            return bool(self.run and self.step_r and (not self.b2) and (not self.y1))
        return bool(self.jog_retornar and (not self.b2) and (not self.jog_avancar))

    def ciclo_scan(self, dt: float = 0.5) -> dict:
        if self.cmd_reset:
            self.fault = False
            self.alarme = ""
            self.cronometro_s = 0.0
            self.cmd_reset = False

        if (not self.e0_ok) or (not self.g1_ok) or self.fault:
            self.run = False
            self.step_t = False
            self.step_a = False
            self.step_r = False
            self.cronometro_s = 0.0
            self.cmd_start = False
            return self.estado_atual()

        if self.cmd_stop:
            self.run = False
            self.step_t = False
            self.step_a = False
            self.step_r = False
            self.cronometro_s = 0.0
            self.cmd_stop = False
        elif self.cmd_start and self.safe:
            self.run = True
            if self.auto_mode and not (self.step_t or self.step_a or self.step_r):
                self.step_t = True
                self.cronometro_s = 0.0
            self.cmd_start = False

        if self.run and self.auto_mode:
            if self.step_t and self.b1:
                self.step_t = False
                self.step_a = True
                self.cronometro_s = 0.0
            elif self.step_a:
                if self.b3:
                    self.step_a = False
                    self.step_r = True
                    self.cronometro_s = 0.0
                else:
                    self.cronometro_s += dt
                    if self.cronometro_s >= self.limite_timeout_s:
                        self.fault = True
                        self.alarme = "TIMEOUT_AVANCO_B3"
                        self.run = False
                        self.step_a = False
                        self.cronometro_s = 0.0
            elif self.step_r:
                if self.b2:
                    self.step_r = False
                    self.step_t = True
                    self.b1 = False
                    self.b3 = False
                    self.total_pecas += 1
                    self.cronometro_s = 0.0
                else:
                    self.cronometro_s += dt
                    if self.cronometro_s >= self.limite_timeout_s:
                        self.fault = True
                        self.alarme = "TIMEOUT_RETORNO_B2"
                        self.run = False
                        self.step_r = False
                        self.cronometro_s = 0.0

        return self.estado_atual()

    def estado_atual(self) -> dict:
        out = asdict(self)
        out["safe"] = self.safe
        out["m1"] = self.m1
        out["y1"] = self.y1
        out["y2"] = self.y2
        return out


def rodar_testes_t01_t06() -> list[dict]:
    logs = []

    # T01: start em condicao segura
    c = ControladorCelula11(e0_ok=True, g1_ok=True, auto_mode=True, b2=True, cmd_start=True)
    st = c.ciclo_scan(0.5)
    logs.append({
        "caso": "T01",
        "aprovado": st["step_t"] and st["m1"] and (not st["y1"]) and (not st["y2"]),
        "snapshot": st
    })

    # T02: peca detectada em B1
    c.b1 = True
    c.b2 = False
    st = c.ciclo_scan(0.5)
    logs.append({
        "caso": "T02",
        "aprovado": (not st["m1"]) and (not st["step_t"]) and st["step_a"] and st["y1"],
        "snapshot": st
    })

    # T03: abertura de G1 durante avanco
    c.g1_ok = False
    st = c.ciclo_scan(0.5)
    logs.append({
        "caso": "T03",
        "aprovado": (not st["safe"]) and (not st["run"]) and (not st["y1"]) and (not st["m1"]),
        "snapshot": st
    })

    # T04: timeout em avanco (3.0s sem B3)
    c = ControladorCelula11(e0_ok=True, g1_ok=True, auto_mode=True, b2=True, cmd_start=True)
    c.ciclo_scan(0.5)
    c.b1 = True
    c.b2 = False
    c.ciclo_scan(0.5)
    for _ in range(6):
        st = c.ciclo_scan(0.5)
    logs.append({
        "caso": "T04",
        "aprovado": st["fault"] and (st["alarme"] == "TIMEOUT_AVANCO_B3") and (not st["y1"]),
        "snapshot": st
    })

    # T05: reset limpa falha sem mover; novo start retoma
    c.cmd_reset = True
    st_reset = c.ciclo_scan(0.5)
    sem_partida_no_reset = (not st_reset["fault"]) and (not st_reset["run"]) and (not st_reset["m1"]) and (not st_reset["y1"])
    c.cmd_start = True
    st_start = c.ciclo_scan(0.5)
    logs.append({
        "caso": "T05",
        "aprovado": sem_partida_no_reset and st_start["run"] and st_start["step_a"] and st_start["y1"],
        "apos_reset": st_reset,
        "apos_start": st_start
    })

    # T06: queda de comunicacao HMI/rede
    c_rede = ControladorCelula11(e0_ok=True, g1_ok=True, auto_mode=True, b2=True, cmd_start=True, rede_ativa=False)
    st_rede = c_rede.ciclo_scan(0.5)
    logs.append({
        "caso": "T06",
        "aprovado": (not st_rede["rede_ativa"]) and st_rede["safe"] and st_rede["run"] and st_rede["m1"],
        "snapshot": st_rede
    })

    return logs


if __name__ == "__main__":
    print(json.dumps(rodar_testes_t01_t06(), indent=2, ensure_ascii=False))
