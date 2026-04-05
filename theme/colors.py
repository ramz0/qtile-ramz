import json
import os

PALETTE_FILE = "colors/tokyo-night-storm.json"

palette_path = os.path.join(os.path.dirname(__file__), PALETTE_FILE)

with open(palette_path, "r") as f:
    palette_data = json.load(f)

colores = palette_data["colors"]
border_focus = palette_data.get("border_focus", "#fca7ea")

colorMoradoIntenso = colores["purple"]
colorAmarilloIntenso = colores["yellow"]

colorBarra = colores["base"]

colorMenuRofi = colores["blue"]
colorIndicadorDeActualizaciones = colores["red"]
colorVolumen = colores["cyan"]
colorBrillo = colores["yellow"]
colorBateria = colores["green"]
colorFechaYHora = colores["purple"]

colorDeTextos = colores["text"]

listaDeColoresGrupos = [
  colores["pink"],
  colores["orange"],
  colores["cyan"], 
  colores["red"], 
  colores["blue"], 
  colores["blue"], 
]

colorBarraGrupos = colores["crust"]
colorDelGrupoActivo = colorMoradoIntenso
colorDeGruposActivos = listaDeColoresGrupos
colorDelGrupoActual = colores["yellow"]
