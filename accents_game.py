import streamlit as st
import random

# --- BANCO DE PALABRAS (JUEGO DE ACENTOS) ---
WORD_BANK_ACCENTS = {
    1: [
        {"display": "accion", "correct": "ó", "answer": "acción"},
        {"display": "ademas", "correct": "á", "answer": "además"},
        {"display": "avion", "correct": "ó", "answer": "avión"},
        {"display": "arbol", "correct": "á", "answer": "árbol"},
        {"display": "album", "correct": "á", "answer": "álbum"},
        {"display": "angel", "correct": "á", "answer": "ángel"},
        {"display": "azucar", "correct": "ú", "answer": "azúcar"},
        {"display": "bebe", "correct": "é", "answer": "bebé"},
        {"display": "cafe", "correct": "é", "answer": "café"},
        {"display": "camion", "correct": "ó", "answer": "camión"},
        {"display": "cancion", "correct": "ó", "answer": "canción"},
        {"display": "carcel", "correct": "á", "answer": "cárcel"},
        {"display": "cesped", "correct": "é", "answer": "césped"},
        {"display": "colibri", "correct": "í", "answer": "colibrí"},
        {"display": "compas", "correct": "á", "answer": "compás"},
        {"display": "corazon", "correct": "ó", "answer": "corazón"},
        {"display": "debil", "correct": "é", "answer": "débil"},
        {"display": "dificil", "correct": "í", "answer": "difícil"},
        {"display": "jamas", "correct": "á", "answer": "jamás"},
        {"display": "jardin", "correct": "í", "answer": "jardín"},
        {"display": "jesus", "correct": "ú", "answer": "jesús"},
        {"display": "lapiz", "correct": "á", "answer": "lápiz"},
        {"display": "leccion", "correct": "ó", "answer": "lección"},
        {"display": "leon", "correct": "ó", "answer": "león"},
        {"display": "mama", "correct": "á", "answer": "mamá"},
        {"display": "mani", "correct": "í", "answer": "maní"},
        {"display": "mastil", "correct": "á", "answer": "mástil"},
        {"display": "melon", "correct": "ó", "answer": "melón"},
        {"display": "menu", "correct": "ú", "answer": "menú"},
        {"display": "papa", "correct": "á", "answer": "papá"},
        {"display": "paris", "correct": "í", "answer": "parís"},
        {"display": "peru", "correct": "ú", "answer": "perú"},
        {"display": "raton", "correct": "ó", "answer": "ratón"},
        {"display": "rubi", "correct": "í", "answer": "rubí"},
        {"display": "segun", "correct": "ú", "answer": "según"},
        {"display": "sofa", "correct": "á", "answer": "sofá"},
        {"display": "tambien", "correct": "é", "answer": "también"},
        {"display": "Tunez", "correct": "ú", "answer": "Túnez"},
        {"display": "util", "correct": "ú", "answer": "útil"},
        {"display": "violin", "correct": "í", "answer": "violín"},
        {"display": "volcan", "correct": "á", "answer": "volcán"},
        {"display": "Ambar", "correct": "á", "answer": "Ámbar"},
        {"display": "America", "correct": "é", "answer": "América"},
        {"display": "Andres", "correct": "é", "answer": "Andrés"},
        {"display": "arabe", "correct": "á", "answer": "árabe"},
        {"display": "articulo", "correct": "í", "answer": "artículo"},
        {"display": "atun", "correct": "ú", "answer": "atún"},
        {"display": "automovil", "correct": "ó", "answer": "automóvil"},
        {"display": "beisbol", "correct": "é", "answer": "béisbol"},
        {"display": "belen", "correct": "é", "answer": "belén"},
        {"display": "boligrafo", "correct": "í", "answer": "bolígrafo"},
        {"display": "brujula", "correct": "ú", "answer": "brújula"},
        {"display": "camara", "correct": "á", "answer": "cámara"},
        {"display": "caracter", "correct": "á", "answer": "carácter"},
        {"display": "catolico", "correct": "ó", "answer": "católico"},
        {"display": "centimetro", "correct": "í", "answer": "centímetro"},
        {"display": "clasico", "correct": "á", "answer": "clásico"},
        {"display": "condor", "correct": "ó", "answer": "cóndor"},
        {"display": "cortes", "correct": "é", "answer": "cortés"},
        {"display": "crater", "correct": "á", "answer": "cráter"},
        {"display": "cristobal", "correct": "ó", "answer": "cristóbal"},
        {"display": "cupula", "correct": "ú", "answer": "cúpula"},
        {"display": "elastico", "correct": "á", "answer": "elástico"},
        {"display": "espectaculo", "correct": "á", "answer": "espectáculo"},
        {"display": "estomago", "correct": "ó", "answer": "estómago"},
        {"display": "exito", "correct": "é", "answer": "éxito"},
        {"display": "fantastico", "correct": "á", "answer": "fantástico"},
        {"display": "fernan", "correct": "á", "answer": "fernán"},
        {"display": "fosil", "correct": "ó", "answer": "fósil"},
        {"display": "futbol", "correct": "ú", "answer": "fútbol"},
        {"display": "gomez", "correct": "ó", "answer": "gómez"},
        {"display": "Hector", "correct": "é", "answer": "Héctor"},
        {"display": "heroe", "correct": "é", "answer": "héroe"},
        {"display": "habil", "correct": "á", "answer": "hábil"},
        {"display": "higado", "correct": "í", "answer": "hígado"},
        {"display": "hipopotamo", "correct": "ó", "answer": "hipopótamo"},
        {"display": "iberico", "correct": "é", "answer": "ibérico"},
        {"display": "idolo", "correct": "í", "answer": "ídolo"},
        {"display": "impetu", "correct": "í", "answer": "ímpetu"},
        {"display": "ingles", "correct": "é", "answer": "inglés"},
        {"display": "jabali", "correct": "í", "answer": "jabalí"},
        {"display": "jimenez", "correct": "é", "answer": "jiménez"},
        {"display": "lagrima", "correct": "á", "answer": "lágrima"},
        {"display": "lampara", "correct": "á", "answer": "lámpara"},
        {"display": "libelula", "correct": "é", "answer": "libélula"},
        {"display": "limite", "correct": "í", "answer": "límite"},
        {"display": "logico", "correct": "ó", "answer": "lógico"},
        {"display": "lopez", "correct": "ó", "answer": "lópez"},
        {"display": "marmol", "correct": "á", "answer": "mármol"},
        {"display": "martir", "correct": "á", "answer": "mártir"},
        {"display": "maquina", "correct": "á", "answer": "máquina"},
        {"display": "maximo", "correct": "á", "answer": "máximo"},
        {"display": "mecanico", "correct": "á", "answer": "mecánico"},
        {"display": "medico", "correct": "é", "answer": "médico"},
        {"display": "mexico", "correct": "é", "answer": "méxico"},
        {"display": "miercoles", "correct": "é", "answer": "miércoles"},
        {"display": "minimo", "correct": "í", "answer": "mínimo"},
        {"display": "musica", "correct": "ú", "answer": "música"},
        {"display": "nacar", "correct": "á", "answer": "nácar"},
        {"display": "numero", "correct": "ú", "answer": "número"},
        {"display": "oceano", "correct": "é", "answer": "océano"},
        {"display": "oxigeno", "correct": "í", "answer": "oxígeno"},
        {"display": "pajaro", "correct": "á", "answer": "pájaro"},
        {"display": "pagina", "correct": "á", "answer": "página"},
        {"display": "plastico", "correct": "á", "answer": "plástico"},
        {"display": "platano", "correct": "á", "answer": "plátano"},
        {"display": "publico", "correct": "ú", "answer": "público"},
        {"display": "sabado", "correct": "á", "answer": "sábado"},
        {"display": "silaba", "correct": "í", "answer": "sílaba"},
        {"display": "simbolo", "correct": "í", "answer": "símbolo"},
        {"display": "telefono", "correct": "é", "answer": "teléfono"},
        {"display": "termino", "correct": "é", "answer": "término"},
        {"display": "timido", "correct": "í", "answer": "tímido"},
        {"display": "titulo", "correct": "í", "answer": "título"},
        {"display": "trebol", "correct": "é", "answer": "trébol"},
        {"display": "ultimo", "correct": "ú", "answer": "último"},
        {"display": "valvula", "correct": "á", "answer": "válvula"},
        {"display": "victor", "correct": "í", "answer": "víctor"},
        {"display": "zoologico", "correct": "ó", "answer": "zoológico"},
    ],
    2: [
        {"display": "academico", "correct": "é", "answer": "académico"},
        {"display": "aeronautica", "correct": "á", "answer": "aeronáutica"},
        {"display": "anecdota", "correct": "é", "answer": "anécdota"},
        {"display": "antartida", "correct": "á", "answer": "antártida"},
        {"display": "apostolico", "correct": "ó", "answer": "apostólico"},
        {"display": "area", "correct": "á", "answer": "área"},
        {"display": "atmosfera", "correct": "ó", "answer": "atmósfera"},
        {"display": "atomo", "correct": "á", "answer": "átomo"},
        {"display": "aureo", "correct": "á", "answer": "áureo"},
        {"display": "autentico", "correct": "é", "answer": "auténtico"},
        {"display": "balsamo", "correct": "á", "answer": "bálsamo"},
        {"display": "barbaro", "correct": "á", "answer": "bárbaro"},
        {"display": "benefico", "correct": "é", "answer": "benéfico"},
        {"display": "biblico", "correct": "í", "answer": "bíblico"},
        {"display": "biceps", "correct": "í", "answer": "bíceps"},
        {"display": "boveda", "correct": "ó", "answer": "bóveda"},
        {"display": "calculo", "correct": "á", "answer": "cálculo"},
        {"display": "calido", "correct": "á", "answer": "cálido"},
        {"display": "cantaro", "correct": "á", "answer": "cántaro"},
        {"display": "capsula", "correct": "á", "answer": "cápsula"},
        {"display": "caratula", "correct": "á", "answer": "carátula"},
        {"display": "catastrofe", "correct": "á", "answer": "catástrofe"},
        {"display": "catedra", "correct": "á", "answer": "cátedra"},
        {"display": "celula", "correct": "é", "answer": "célula"},
        {"display": "ceramica", "correct": "á", "answer": "cerámica"},
        {"display": "cientifico", "correct": "í", "answer": "científico"},
        {"display": "circulo", "correct": "í", "answer": "círculo"},
        {"display": "citrico", "correct": "í", "answer": "cítrico"},
        {"display": "clinica", "correct": "í", "answer": "clínica"},
        {"display": "cobrese", "correct": "ó", "answer": "cóbrese"},
        {"display": "codice", "correct": "ó", "answer": "códice"},
        {"display": "colera", "correct": "ó", "answer": "cólera"},
        {"display": "comico", "correct": "ó", "answer": "cómico"},
        {"display": "complice", "correct": "ó", "answer": "cómplice"},
        {"display": "compraselo", "correct": "ó", "answer": "cómpraselo"},
        {"display": "comunmente", "correct": "ú", "answer": "comúnmente"},
        {"display": "concavo", "correct": "ó", "answer": "cóncavo"},
        {"display": "consola", "correct": "ó", "answer": "consola"},
        {"display": "cornea", "correct": "ó", "answer": "córnea"},
        {"display": "cosmetico", "correct": "é", "answer": "cosmético"},
        {"display": "credito", "correct": "é", "answer": "crédito"},
        {"display": "critica", "correct": "í", "answer": "crítica"},
        {"display": "cronica", "correct": "ó", "answer": "crónica"},
        {"display": "cuadrilatero", "correct": "á", "answer": "cuadrilátero"},
        {"display": "damelo", "correct": "á", "answer": "dámelo"},
        {"display": "decimo", "correct": "é", "answer": "décimo"},
        {"display": "deposito", "correct": "ó", "answer": "depósito"},
        {"display": "desanimo", "correct": "á", "answer": "desánimo"},
        {"display": "digamelo", "correct": "í", "answer": "dígamelo"},
        {"display": "dinamico", "correct": "á", "answer": "dinámico"},
        {"display": "diocesis", "correct": "ó", "answer": "diócesis"},
        {"display": "docil", "correct": "ó", "answer": "dócil"},
        {"display": "dolar", "correct": "ó", "answer": "dólar"},
        {"display": "domestico", "correct": "é", "answer": "doméstico"},
        {"display": "ebano", "correct": "é", "answer": "ébano"},
        {"display": "eclesiastico", "correct": "á", "answer": "eclesiástico"},
        {"display": "ecologico", "correct": "ó", "answer": "ecológico"},
        {"display": "ejercito", "correct": "é", "answer": "ejército"},
        {"display": "enfasis", "correct": "é", "answer": "énfasis"},
        {"display": "epico", "correct": "é", "answer": "épico"},
        {"display": "epoca", "correct": "é", "answer": "época"},
        {"display": "escandalo", "correct": "á", "answer": "escándalo"},
        {"display": "esceptico", "correct": "é", "answer": "escéptico"},
        {"display": "escrupulo", "correct": "ú", "answer": "escrúpulo"},
        {"display": "esdrujula", "correct": "ú", "answer": "esdrújula"},
        {"display": "esofago", "correct": "ó", "answer": "esófago"},
        {"display": "espatula", "correct": "á", "answer": "espátula"},
        {"display": "estadistica", "correct": "í", "answer": "estadística"},
        {"display": "estatico", "correct": "á", "answer": "estático"},
        {"display": "estiercol", "correct": "é", "answer": "estiércol"},
        {"display": "estimulo", "correct": "í", "answer": "estímulo"},
        {"display": "etica", "correct": "é", "answer": "ética"},
        {"display": "extasis", "correct": "é", "answer": "éxtasis"},
        {"display": "fabula", "correct": "á", "answer": "fábula"},
        {"display": "facil", "correct": "á", "answer": "fácil"},
        {"display": "factico", "correct": "á", "answer": "fáctico"},
        {"display": "farmaceutico", "correct": "é", "answer": "farmacéutico"},
        {"display": "femur", "correct": "é", "answer": "fémur"},
        {"display": "fenomeno", "correct": "ó", "answer": "fenómeno"},
        {"display": "fisica", "correct": "í", "answer": "física"},
        {"display": "formula", "correct": "ó", "answer": "fórmula"},
        {"display": "fornix", "correct": "ó", "answer": "fórnix"},
        {"display": "fosforo", "correct": "ó", "answer": "fósforo"},
        {"display": "fragil", "correct": "á", "answer": "frágil"},
        {"display": "gargola", "correct": "á", "answer": "gárgola"},
        {"display": "genero", "correct": "é", "answer": "género"},
        {"display": "genesis", "correct": "é", "answer": "génesis"},
        {"display": "geografico", "correct": "á", "answer": "geográfico"},
        {"display": "geologo", "correct": "ó", "answer": "geólogo"},
        {"display": "gondola", "correct": "ó", "answer": "góndola"},
        {"display": "gramatica", "correct": "á", "answer": "gramática"},
        {"display": "hercules", "correct": "é", "answer": "hércules"},
        {"display": "hibrido", "correct": "í", "answer": "híbrido"},
        {"display": "hipocrita", "correct": "ó", "answer": "hipócrita"},
        {"display": "humedo", "correct": "ú", "answer": "húmedo"},
        {"display": "identico", "correct": "é", "answer": "idéntico"},
        {"display": "implicito", "correct": "í", "answer": "implícito"},
        {"display": "indice", "correct": "í", "answer": "índice"},
        {"display": "indole", "correct": "í", "answer": "índole"},
        {"display": "informatico", "correct": "á", "answer": "informático"},
        {"display": "interes", "correct": "é", "answer": "interés"},
        {"display": "intrinseco", "correct": "í", "answer": "intrínseco"},
        {"display": "jerarquico", "correct": "á", "answer": "jerárquico"},
        {"display": "jubilo", "correct": "ú", "answer": "júbilo"},
        {"display": "jupiter", "correct": "ú", "answer": "júpiter"},
        {"display": "juridico", "correct": "í", "answer": "jurídico"},
        {"display": "kilometro", "correct": "ó", "answer": "kilómetro"},
        {"display": "lectura", "correct": "ú", "answer": "lectura"},
        {"display": "legitimo", "correct": "í", "answer": "legítimo"},
        {"display": "lexico", "correct": "é", "answer": "léxico"},
        {"display": "lider", "correct": "í", "answer": "líder"},
        {"display": "liquido", "correct": "í", "answer": "líquido"},
        {"display": "logistica", "correct": "í", "answer": "logística"},
        {"display": "ludico", "correct": "ú", "answer": "lúdico"},
        {"display": "magico", "correct": "á", "answer": "mágico"},
        {"display": "magnifico", "correct": "í", "answer": "magnífico"},
        {"display": "mayuscula", "correct": "ú", "answer": "mayúscula"},
        {"display": "metalico", "correct": "á", "answer": "metálico"},
        {"display": "metodo", "correct": "é", "answer": "método"},
        {"display": "microfono", "correct": "ó", "answer": "micrófono"},
        {"display": "milimetro", "correct": "í", "answer": "milímetro"},
        {"display": "minuscula", "correct": "ú", "answer": "minúscula"},
        {"display": "movil", "correct": "ó", "answer": "móvil"},
        {"display": "multiplo", "correct": "ú", "answer": "múltiplo"},
        {"display": "nectar", "correct": "é", "answer": "néctar"},
        {"display": "neumatico", "correct": "á", "answer": "neumático"},
        {"display": "nostalgico", "correct": "á", "answer": "nostálgico"},
        {"display": "notifico", "correct": "ó", "answer": "notificó"},
        {"display": "nucleo", "correct": "ú", "answer": "núcleo"},
        {"display": "obelisco", "correct": "é", "answer": "obelisco"},
        {"display": "obstaculo", "correct": "á", "answer": "obstáculo"},
        {"display": "onomatopeya", "correct": "é", "answer": "onomatopeya"},
        {"display": "opera", "correct": "ó", "answer": "ópera"},
        {"display": "optica", "correct": "ó", "answer": "óptica"},
        {"display": "optimo", "correct": "ó", "answer": "óptimo"},
        {"display": "orbita", "correct": "ó", "answer": "órbita"},
        {"display": "organico", "correct": "á", "answer": "orgánico"},
        {"display": "ortopedico", "correct": "é", "answer": "ortopédico"},
        {"display": "oxido", "correct": "ó", "answer": "óxido"},
        {"display": "pacifico", "correct": "í", "answer": "pacífico"},
        {"display": "pandemico", "correct": "é", "answer": "pandémico"},
        {"display": "panico", "correct": "á", "answer": "pánico"},
        {"display": "parabola", "correct": "á", "answer": "parábola"},
        {"display": "paralisis", "correct": "á", "answer": "parálisis"},
        {"display": "parametro", "correct": "á", "answer": "parámetro"},
        {"display": "parentesis", "correct": "é", "answer": "paréntesis"},
        {"display": "parpado", "correct": "á", "answer": "párpado"},
        {"display": "parrafo", "correct": "á", "answer": "párrafo"},
        {"display": "pauperrimo", "correct": "é", "answer": "paupérrimo"},
        {"display": "pelicula", "correct": "í", "answer": "película"},
        {"display": "pendulo", "correct": "é", "answer": "péndulo"},
        {"display": "peninsula", "correct": "í", "answer": "península"},
        {"display": "pentagono", "correct": "á", "answer": "pentágono"},
        {"display": "perdida", "correct": "é", "answer": "pérdida"},
        {"display": "periferico", "correct": "é", "answer": "periférico"},
        {"display": "periodico", "correct": "ó", "answer": "periódico"},
        {"display": "petalo", "correct": "é", "answer": "pétalo"},
        {"display": "petroleo", "correct": "ó", "answer": "petróleo"},
        {"display": "pindaro", "correct": "í", "answer": "píndaro"},
        {"display": "piramide", "correct": "á", "answer": "pirámide"},
        {"display": "piscis", "correct": "í", "answer": "piscis"},
        {"display": "polemica", "correct": "é", "answer": "polémica"},
        {"display": "polvora", "correct": "ó", "answer": "pólvora"},
        {"display": "portatil", "correct": "á", "answer": "portátil"},
        {"display": "practica", "correct": "á", "answer": "práctica"},
        {"display": "prestamo", "correct": "é", "answer": "préstamo"},
        {"display": "proposito", "correct": "ó", "answer": "propósito"},
        {"display": "proteina", "correct": "í", "answer": "proteína"},
        {"display": "proximo", "correct": "ó", "answer": "próximo"},
        {"display": "psicologo", "correct": "ó", "answer": "psicólogo"},
        {"display": "quimica", "correct": "í", "answer": "química"},
        {"display": "rabano", "correct": "á", "answer": "rábano"},
        {"display": "rapido", "correct": "á", "answer": "rápido"},
        {"display": "rectangulo", "correct": "á", "answer": "rectángulo"},
        {"display": "regimen", "correct": "é", "answer": "régimen"},
        {"display": "remoto", "correct": "ó", "answer": "remoto"},
        {"display": "reptil", "correct": "é", "answer": "réptil"},
        {"display": "republica", "correct": "ú", "answer": "república"},
        {"display": "retorica", "correct": "ó", "answer": "retórica"},
        {"display": "ridiculo", "correct": "í", "answer": "ridículo"},
        {"display": "rigido", "correct": "í", "answer": "rígido"},
        {"display": "romantico", "correct": "á", "answer": "romántico"},
        {"display": "rotula", "correct": "ó", "answer": "rótula"},
        {"display": "rustico", "correct": "ú", "answer": "rústico"},
        {"display": "sandalo", "correct": "á", "answer": "sándalo"},
        {"display": "sanguineo", "correct": "í", "answer": "sanguíneo"},
        {"display": "sarcasmo", "correct": "á", "answer": "sarcasmo"},
        {"display": "satelite", "correct": "é", "answer": "satélite"},
        {"display": "semaforo", "correct": "á", "answer": "semáforo"},
        {"display": "septimo", "correct": "é", "answer": "séptimo"},
        {"display": "sifilis", "correct": "í", "answer": "sífilis"},
        {"display": "silice", "correct": "í", "answer": "sílice"},
        {"display": "sintesis", "correct": "í", "answer": "síntesis"},
        {"display": "sintoma", "correct": "í", "answer": "síntoma"},
        {"display": "sismografo", "correct": "ó", "answer": "sismógrafo"},
        {"display": "sociologo", "correct": "ó", "answer": "sociólogo"},
        {"display": "sodio", "correct": "ó", "answer": "sodio"},
        {"display": "subdito", "correct": "ú", "answer": "súbdito"},
        {"display": "subito", "correct": "ú", "answer": "súbito"},
        {"display": "tecnica", "correct": "é", "answer": "técnica"},
        {"display": "tectil", "correct": "é", "answer": "téctil"},
        {"display": "termico", "correct": "é", "answer": "térmico"},
        {"display": "tarantula", "correct": "á", "answer": "tarántula"},
        {"display": "torax", "correct": "ó", "answer": "tórax"},
        {"display": "toxico", "correct": "ó", "answer": "tóxico"},
        {"display": "tragico", "correct": "á", "answer": "trágico"},
        {"display": "transito", "correct": "á", "answer": "tránsito"},
        {"display": "triangulo", "correct": "á", "answer": "triángulo"},
        {"display": "triptico", "correct": "í", "answer": "tríptico"},
        {"display": "tuberculo", "correct": "é", "answer": "tubérculo"},
        {"display": "tunel", "correct": "ú", "answer": "túnel"},
        {"display": "tunica", "correct": "ú", "answer": "túnica"},
        {"display": "uranio", "correct": "á", "answer": "uranio"},
        {"display": "utimo", "correct": "ú", "answer": "último"},
        {"display": "valido", "correct": "á", "answer": "válido"},
        {"display": "vandalo", "correct": "á", "answer": "vándalo"},
        {"display": "vencejo", "correct": "é", "answer": "vencejo"},
        {"display": "veridico", "correct": "í", "answer": "verídico"},
        {"display": "vertice", "correct": "é", "answer": "vértice"},
        {"display": "vibracion", "correct": "ó", "answer": "vibración"},
        {"display": "vinculo", "correct": "í", "answer": "vínculo"},
        {"display": "vispera", "correct": "í", "answer": "víspera"},
        {"display": "vitamina", "correct": "í", "answer": "vitamina"},
        {"display": "volumen", "correct": "ú", "answer": "volumen"},
        {"display": "vortice", "correct": "ó", "answer": "vórtice"},
        {"display": "zodiaco", "correct": "í", "answer": "zodíaco"},
    ]
}

# --- LÓGICA DEL JUEGO DE ACENTOS ---

def initialize_accents_game():
    """Inicializa o resetea el estado del juego de acentos."""
    st.session_state.game_type = "accents"
    st.session_state.current_level = 1
    st.session_state.score = 0
    st.session_state.stars = 0
    st.session_state.used_words = []
    st.session_state.current_word = None
    st.session_state.answered = False
    st.session_state.feedback = ""
    st.session_state.feedback_class = ""
    st.session_state.show_rules = False
    load_new_word_accents()

def load_new_word_accents():
    """Carga una nueva palabra para el juego de acentos."""
    bank = WORD_BANK_ACCENTS
    available = [w for w in bank[st.session_state.current_level] if w["answer"] not in st.session_state.used_words]
    if not available:
        st.session_state.used_words = []
        available = bank[st.session_state.current_level]
    word = random.choice(available)
    st.session_state.current_word = word
    st.session_state.used_words.append(word["answer"])
    st.session_state.answered = False
    st.session_state.feedback = ""

def level_up_accents():
    """Gestiona el avance de nivel en el juego de acentos."""
    if st.session_state.current_level < max(WORD_BANK_ACCENTS.keys()):
        st.session_state.current_level += 1
        st.session_state.stars = 0
        st.session_state.used_words = []
        st.session_state.feedback = f"¡Felicidades! Has subido al nivel {st.session_state.current_level} 🚀"
    else:
        st.session_state.feedback = "¡Has completado todos los niveles de acentos! 🏆"
    load_new_word_accents()

def run_accents_game():
    """Ejecuta la interfaz y la lógica del juego de acentos."""
    
    OPTION_LABELS_ACCENTS = {
        "á": "Acento en á", "é": "Acento en é", "í": "Acento en í",
        "ó": "Acento en ó", "ú": "Acento en ú", "sin acento": "Sin acento"
    }

    # --- PANTALLA DE REGLAS (ACENTOS) ---
    if st.session_state.get("show_rules", False):
        st.markdown('<div class="rules-container">', unsafe_allow_html=True)
        st.markdown("<h1>Reglas de Acentuación</h1>", unsafe_allow_html=True)
        st.markdown("""
        <div class="rules-content" style="text-align: left;">
            <h2>1. Palabras Agudas</h2>
            <p>Llevan el acento en la última sílaba. Se acentúan cuando terminan en <b>vocal, -n o -s</b>.</p>
            <h2>2. Palabras Llanas o Graves</h2>
            <p>Llevan el acento en la penúltima sílaba. Se acentúan cuando <b>NO</b> terminan en <b>vocal, -n o -s</b>.</p>
            <h2>3. Palabras Esdrújulas y Sobresdrújulas</h2>
            <p>Llevan el acento en la antepenúltima o anterior sílaba. <b>Siempre</b> llevan tilde.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Volver al juego", key="back_btn_accents"):
            st.session_state.show_rules = False
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        return

    # --- PANTALLA PRINCIPAL DEL JUEGO (ACENTOS) ---
    st.markdown('<div class="game-container">', unsafe_allow_html=True)
    st.markdown("<h1>¡Acentos Game!</h1>", unsafe_allow_html=True)

    total_words_in_level = len(WORD_BANK_ACCENTS[st.session_state.current_level])

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label=f"Nivel {st.session_state.current_level}", value=f"{st.session_state.stars} / {total_words_in_level} ★")
    with col2:
        st.metric(label="Puntuación", value=st.session_state.score)

    st.progress(min(1.0, st.session_state.stars / total_words_in_level))
    
    st.markdown(f'<div class="word-display">{st.session_state.current_word["display"]}</div>', unsafe_allow_html=True)

    # Opciones de respuesta
    options = ["á", "é", "í", "ó", "ú", "sin acento"]
    cols = st.columns(3)
    for i, opt in enumerate(options):
        if cols[i % 3].button(OPTION_LABELS_ACCENTS[opt], key=f"opt_accents_{i}", disabled=st.session_state.answered, use_container_width=True):
            if opt == st.session_state.current_word["correct"]:
                st.session_state.feedback = f'¡Correcto! La palabra es "{st.session_state.current_word["answer"]}" 🎉'
                st.session_state.score += 10 * st.session_state.current_level
                st.session_state.stars += 1
                if st.session_state.stars == total_words_in_level:
                    level_up_accents()
            else:
                st.session_state.feedback = f'Incorrecto. La respuesta correcta era: {st.session_state.current_word["answer"]}'
                if st.session_state.stars > 0:
                    st.session_state.stars -= 1
            st.session_state.answered = True
            st.rerun()

    if st.session_state.feedback:
        st.markdown(f'<div class="feedback">{st.session_state.feedback}</div>', unsafe_allow_html=True)

    # Botones de acción
    action_cols = st.columns(3) if st.session_state.answered else st.columns(2)
    
    if st.session_state.answered:
        if action_cols[0].button("Siguiente", key="next_btn_accents", use_container_width=True):
            load_new_word_accents()
            st.rerun()
        if action_cols[1].button("Reglas", key="rules_btn_accents", use_container_width=True):
            st.session_state.show_rules = True
            st.rerun()
        if action_cols[2].button("Menú", key="menu_btn_accents", use_container_width=True):
            st.session_state.current_view = "menu"
            st.rerun()
    else:
        if action_cols[0].button("Reglas", key="rules_btn_accents_alt", use_container_width=True):
            st.session_state.show_rules = True
            st.rerun()
        if action_cols[1].button("Menú", key="menu_btn_accents_alt", use_container_width=True):
            st.session_state.current_view = "menu"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
