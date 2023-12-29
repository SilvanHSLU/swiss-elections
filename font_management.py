import matplotlib.font_manager as fm

# Load the "PT-Sans" font needed for the project
font_dir = ['fonts']
for font in fm.findSystemFonts(font_dir):
    fm.fontManager.addfont(font)

TITLE_FONT = {
    'fontname': 'PT Sans',
    'size': '28',
    'color': 'black',
    'weight': 'bold',
    'verticalalignment': 'bottom'
}
SUBTITLE_FONT = {
    'fontname': 'PT Sans',
    'size': '18',
    'color': 'black',
    'weight': 'bold',
    'verticalalignment': 'bottom'
}
DESCRIPTION_FONT = {
    'fontname': 'PT Sans',
    'size': '16',
    'color': 'black',
    'weight': 'normal',
    'verticalalignment': 'bottom'
}
ANNOTATION_FONT = {
    'fontname': 'PT Sans',
    'size': '12',
    'color': 'dimgrey',
    'weight': 'normal',
    'verticalalignment': 'bottom'
}