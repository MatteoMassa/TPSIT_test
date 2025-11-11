from enum import Enum
from datetime import date, datetime
from typing import List, Dict, Optional
import uuid

class Moto(ar):
    def __init__(self, motore, cilindri, peso, quantita):
        self.qauntita = quantita
        self.motore : List[motori] = []
        self.cilindri = cilindri
        self.peso = peso
    
    def aggiungi_motore(self, motori) -> None:
        self.motore.append(motori)