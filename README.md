# qtile-ramz

Configuración personalizada de Qtile con Qtile Extras.

## Estructura del Proyecto

```
qtile/
├── config.py              # Punto de entrada - importa y combina todo
├── settings/
│   ├── layouts.py         # Configuración de layouts (MonadTall, Max)
│   └── groups.py          # Definición de 6 grupos de trabajo
├── theme/
│   ├── colors.py          # Paleta de colores Catppuccin Mocha
│   ├── decorations.py     # Estilos decorativos (RectDecoration)
│   └── icons.py           # Iconos para los grupos
├── shortcuts/
│   ├── __init__.py        # Combina todos los atajos de teclado
│   ├── config.py          # Configuración base (mod, terminal)
│   ├── keys_general.py    # Navegación de layouts y control de ventanas
│   ├── keys_groups.py     # Cambiar/mover ventanas entre grupos
│   ├── keys_apps.py       # Atajos de aplicaciones
│   ├── keys_media.py      # Volumen, brillo y teclas multimedia
│   ├── keys_rofi.py       # Menú Rofi y powermenu
│   └── mouse.py           # Acciones de arrastre y clic del ratón
└── bar/
    ├── bar.py             # Configuración de pantalla y barra
    └── widgets/
        ├── __init__.py    # Combina basic + custom + blocks
        ├── basics.py      # Widgets básicos (launcher, systray, updates, etc.)
        ├── customs.py     # Widgets personalizados (WindowName, GroupBox, Battery)
        ├── blocks.py      # Espaciadores y separadores
        └── extensions/    # Widgets personalizados (GroupBox, WindowName, Battery)
```

## Atajos de Teclado

### General
- `Mod + Space` - Alternar ventana flotante
- `Mod + Enter` - Abrir terminal
- `Mod + Tab` - Siguiente layout
- `Mod + w` - Cerrar ventana
- `Mod + Ctrl + r` - Reiniciar Qtile
- `Mod + Ctrl + q` - Salir de Qtile

### Navegación de Layouts
- `Mod + Left/Right/Down/Up` - Moverse entre ventanas
- `Mod + Shift + Left/Right/Down/Up` - Mover ventana
- `Mod + Ctrl + Arrow` - Redimensionar ventana
- `Mod + n` - Normalizar tamaño de ventanas
- `Mod + Shift + Return` - Alternar split en MonadTall

### Grupos
- `Mod + [1-6]` - Cambiar al grupo
- `Mod + Shift + [1-6]` - Mover ventana al grupo

### Aplicaciones
- `Mod + c` - Abrir Visual Studio Code
- `Mod + r` - Menú de aplicaciones (Rofi)
- `Mod + Alt + Tab` - Selector de ventanas (Rofi)
- `Mod + e` - Selector de emoji (Rofi)
- `Mod + p` - Menú de apagado

### Multimedia
- `Mod + i/k` - Aumentar/disminuir brillo
- `XF86Audio` - Controles de volumen y reproducción

### Ratón
- `Mod + Click 1` - Arrastrar ventana (posición)
- `Mod + Click 3` - Arrastrar ventana (tamaño)
- `Mod + Click 2` - Traer ventana al frente

## Paleta de Colores

Las paletas se encuentran en `theme/colors/` en formato JSON. Para cambiar de paleta, modifica la variable `PALETTE_FILE` en `theme/colors.py`.

Paletas disponibles:
- `tokyo-night-moon.json` (oscuro con tonos lavados)
- `tokyo-night-storm.json` (oscuro классик)
- `tokyo-night-night.json` (oscuro profundo)
- `tokyo-night-day.json` (versión clara)

### Tokyo Night Moon
- **Base**: `#222436` (fondo principal)
- **Mantle**: `#1e2030`
- **Crust**: `#1b1d2b`
- **Text**: `#c8d3f5`
- **Purple**: `#fca7ea` (acentos)
- **Blue**: `#82aaff`
- **Green**: `#c3e88d`
- **Red**: `#ff757f`
- **Yellow**: `#ffc777`
- **Orange**: `#ff966c`
- **Cyan**: `#86e1fc`
- **Magenta**: `#c099ff`

## Requisitos

- Qtile
- Qtile Extras
- Rofi
- pamixer (audio)
- brightnessctl (brillo)
- playerctl (reproducción)
- Papirus Icons

## Instalación

1. Copiar la carpeta `qtile` a `~/.config/`
2. Reiniciar Qtile: `Mod + Ctrl + r`
