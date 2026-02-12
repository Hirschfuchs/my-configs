from base import SubModule


# Die meisten nicht mehr benötigten Pakete wurden entfernt
# Manche werden vorerst übernommen, langfristig muss aber eine Entscheidung über
# Einsortierung oder dauerhafte Entfernung getroffen werden
class Legacy(SubModule):
    def __init__(self):
        super().__init__(
            "legacy",
            native_packages=[
                # Obsidian Notizen (könnte durch Typst ersetzt werden (wie auch TeX))
                "obsidian",
                # Automationstool für X11 (bisher nicht aktiv genutzt, aber könnte cool sein)
                "xdotool"
                # Festlegung von Tastenkombinationen zur Ausführung von Befehlen (i.V.m. xdotool)
                "xbindkeys"
            ]
        )
