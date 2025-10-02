import streamlit as st
import random

# --- BANCO DE PALABRAS (JUEGO B/V) ---
WORD_BANK_BV = {
    1: [
        {"display": "ama__le", "correct": "b", "answer": "amable"},
        {"display": "arri__a", "correct": "b", "answer": "arriba"},
        {"display": "a__ión", "correct": "v", "answer": "avión"},
        {"display": "a__rir", "correct": "b", "answer": "abrir"},
        {"display": "a__uelo", "correct": "b", "answer": "abuelo"},
        {"display": "a__entura", "correct": "v", "answer": "aventura"},
        {"display": "__arco", "correct": "b", "answer": "barco"},
        {"display": "__arrer", "correct": "b", "answer": "barrer"},
        {"display": "__einte", "correct": "v", "answer": "veinte"},
        {"display": "__estido", "correct": "v", "answer": "vestido"},
        {"display": "__lusa", "correct": "b", "answer": "blusa"},
        {"display": "__oca", "correct": "b", "answer": "boca"},
        {"display": "__otella", "correct": "b", "answer": "botella"},
        {"display": "__razo", "correct": "b", "answer": "brazo"},
        {"display": "__ueno", "correct": "b", "answer": "bueno"},
        {"display": "__ufanda", "correct": "b", "answer": "bufanda"},
        {"display": "__urla", "correct": "b", "answer": "burla"},
        {"display": "__uscar", "correct": "b", "answer": "buscar"},
        {"display": "ca__allo", "correct": "b", "answer": "caballo"},
        {"display": "ca__eza", "correct": "b", "answer": "cabeza"},
        {"display": "cam__io", "correct": "b", "answer": "cambio"},
        {"display": "ca__er", "correct": "b", "answer": "caber"},
        {"display": "cele__rar", "correct": "b", "answer": "celebrar"},
        {"display": "cepillo", "correct": "b", "answer": "cepillo"},
        {"display": "cer__eza", "correct": "v", "answer": "cerveza"},
        {"display": "ci__il", "correct": "v", "answer": "civil"},
        {"display": "cla__o", "correct": "v", "answer": "clavo"},
        {"display": "co__arde", "correct": "b", "answer": "cobarde"},
        {"display": "con__ersación", "correct": "v", "answer": "conversación"},
        {"display": "con__ento", "correct": "v", "answer": "convento"},
        {"display": "con__ivir", "correct": "v", "answer": "convivir"},
        {"display": "cur__a", "correct": "v", "answer": "curva"},
        {"display": "de__er", "correct": "b", "answer": "deber"},
        {"display": "descu__rir", "correct": "b", "answer": "descubrir"},
        {"display": "di__ertido", "correct": "v", "answer": "divertido"},
        {"display": "di__isión", "correct": "v", "answer": "división"},
        {"display": "do__le", "correct": "b", "answer": "doble"},
        {"display": "em__udo", "correct": "b", "answer": "embudo"},
        {"display": "en__ase", "correct": "v", "answer": "envase"},
        {"display": "en__iar", "correct": "v", "answer": "enviar"},
        {"display": "en__idia", "correct": "v", "answer": "envidia"},
        {"display": "equi__ocar", "correct": "v", "answer": "equivocar"},
        {"display": "escla__o", "correct": "v", "answer": "esclavo"},
        {"display": "escri__ir", "correct": "b", "answer": "escribir"},
        {"display": "fa__or", "correct": "v", "answer": "favor"},
        {"display": "fi__ra", "correct": "b", "answer": "fibra"},
        {"display": "fie__re", "correct": "b", "answer": "fiebre"},
        {"display": "fá__ula", "correct": "b", "answer": "fábula"},
        {"display": "go__ierno", "correct": "b", "answer": "gobierno"},
        {"display": "ha__er", "correct": "b", "answer": "haber"},
        {"display": "ha__lar", "correct": "b", "answer": "hablar"},
        {"display": "her__ir", "correct": "v", "answer": "hervir"},
        {"display": "hom__ro", "correct": "b", "answer": "hombro"},
        {"display": "hue__o", "correct": "v", "answer": "huevo"},
        {"display": "in__entar", "correct": "v", "answer": "inventar"},
        {"display": "in__ierno", "correct": "v", "answer": "invierno"},
        {"display": "in__itar", "correct": "v", "answer": "invitar"},
        {"display": "jo__en", "correct": "v", "answer": "joven"},
        {"display": "ju__ilar", "correct": "b", "answer": "jubilar"},
        {"display": "la__ar", "correct": "v", "answer": "lavar"},
        {"display": "li__ertad", "correct": "b", "answer": "libertad"},
        {"display": "li__ro", "correct": "b", "answer": "libro"},
        {"display": "lle__ar", "correct": "v", "answer": "llevar"},
        {"display": "llo__er", "correct": "v", "answer": "llover"},
        {"display": "mue__le", "correct": "b", "answer": "mueble"},
        {"display": "na__idad", "correct": "v", "answer": "navidad"},
        {"display": "na__ío", "correct": "v", "answer": "navío"},
        {"display": "ne__era", "correct": "v", "answer": "nevera"},
        {"display": "nie__la", "correct": "b", "answer": "niebla"},
        {"display": "no__ela", "correct": "v", "answer": "novela"},
        {"display": "no__io", "correct": "v", "answer": "novio"},
        {"display": "nu__e", "correct": "b", "answer": "nube"},
        {"display": "nue__e", "correct": "v", "answer": "nueve"},
        {"display": "nue__o", "correct": "v", "answer": "nuevo"},
        {"display": "o__jeto", "correct": "b", "answer": "objeto"},
        {"display": "obser__ar", "correct": "v", "answer": "observar"},
        {"display": "o__tener", "correct": "b", "answer": "obtener"},
        {"display": "ol__idar", "correct": "v", "answer": "olvidar"},
        {"display": "pala__ra", "correct": "b", "answer": "palabra"},
        {"display": "pa__o", "correct": "v", "answer": "pavo"},
        {"display": "po__re", "correct": "b", "answer": "pobre"},
        {"display": "pol__o", "correct": "v", "answer": "polvo"},
        {"display": "positi__o", "correct": "v", "answer": "positivo"},
        {"display": "pri__ado", "correct": "v", "answer": "privado"},
        {"display": "pro__ar", "correct": "b", "answer": "probar"},
        {"display": "pue__lo", "correct": "b", "answer": "pueblo"},
        {"display": "sa__er", "correct": "b", "answer": "saber"},
        {"display": "sel__a", "correct": "v", "answer": "selva"},
        {"display": "ser__ir", "correct": "v", "answer": "servir"},
        {"display": "so__re", "correct": "b", "answer": "sobre"},
        {"display": "sua__e", "correct": "v", "answer": "suave"},
        {"display": "su__ir", "correct": "b", "answer": "subir"},
        {"display": "ta__la", "correct": "b", "answer": "tabla"},
        {"display": "tam__or", "correct": "b", "answer": "tambor"},
        {"display": "ti__io", "correct": "b", "answer": "tibio"},
        {"display": "tra__ajo", "correct": "b", "answer": "trabajo"},
        {"display": "tri__u", "correct": "b", "answer": "tribu"},
        {"display": "tu__o", "correct": "b", "answer": "tubo"},
        {"display": "ur__ano", "correct": "b", "answer": "urbano"},
        {"display": "__aca", "correct": "v", "answer": "vaca"},
        {"display": "__acaciones", "correct": "v", "answer": "vacaciones"},
        {"display": "__aso", "correct": "v", "answer": "vaso"},
        {"display": "__ela", "correct": "v", "answer": "vela"},
        {"display": "__erde", "correct": "v", "answer": "verde"},
        {"display": "__iaje", "correct": "v", "answer": "viaje"},
        {"display": "__ida", "correct": "v", "answer": "vida"},
        {"display": "__iejo", "correct": "v", "answer": "viejo"},
        {"display": "__iento", "correct": "v", "answer": "viento"},
        {"display": "__ino", "correct": "v", "answer": "vino"},
        {"display": "__isita", "correct": "v", "answer": "visita"},
        {"display": "__i__ir", "correct": "v", "answer": "vivir"},
        {"display": "__oluntad", "correct": "v", "answer": "voluntad"},
        {"display": "__oto", "correct": "v", "answer": "voto"},
        {"display": "__uelo", "correct": "v", "answer": "vuelo"},
        {"display": "zum__ar", "correct": "b", "answer": "zumbar"},
    ],
    2: [
        {"display": "a__dicar", "correct": "b", "answer": "abdicar"},
        {"display": "ad__erbio", "correct": "v", "answer": "adverbio"},
        {"display": "ad__ertencia", "correct": "v", "answer": "advertencia"},
        {"display": "ad__ertir", "correct": "v", "answer": "advertir"},
        {"display": "ad__ersario", "correct": "v", "answer": "adversario"},
        {"display": "am__iguo", "correct": "b", "answer": "ambiguo"},
        {"display": "am__ulancia", "correct": "b", "answer": "ambulancia"},
        {"display": "atracti__o", "correct": "v", "answer": "atractivo"},
        {"display": "atri__uir", "correct": "b", "answer": "atribuir"},
        {"display": "a__soluto", "correct": "b", "answer": "absoluto"},
        {"display": "bene__olencia", "correct": "v", "answer": "benevolencia"},
        {"display": "bi__lioteca", "correct": "b", "answer": "biblioteca"},
        {"display": "bilingüe", "correct": "b", "answer": "bilingüe"},
        {"display": "biodegrada__le", "correct": "b", "answer": "biodegradable"},
        {"display": "biografía", "correct": "b", "answer": "biografía"},
        {"display": "bom__ardero", "correct": "b", "answer": "bombardero"},
        {"display": "bra__ucón", "correct": "v", "answer": "bravucón"},
        {"display": "bre__e", "correct": "v", "answer": "breve"},
        {"display": "bule__ar", "correct": "v", "answer": "bulevar"},
        {"display": "bur__ués", "correct": "g", "answer": "burgués"},
        {"display": "carita__tivo", "correct": "t", "answer": "caritativo"},
        {"display": "carni__oro", "correct": "v", "answer": "carnívoro"},
        {"display": "cla__ícula", "correct": "v", "answer": "clavícula"},
        {"display": "com__atir", "correct": "b", "answer": "combatir"},
        {"display": "com__inar", "correct": "b", "answer": "combinar"},
        {"display": "com__ustible", "correct": "b", "answer": "combustible"},
        {"display": "compasi__o", "correct": "v", "answer": "compasivo"},
        {"display": "competi__o", "correct": "t", "answer": "competitivo"},
        {"display": "contri__uir", "correct": "b", "answer": "contribuir"},
        {"display": "con__alidar", "correct": "v", "answer": "convalidar"},
        {"display": "con__encer", "correct": "v", "answer": "convencer"},
        {"display": "con__eniente", "correct": "v", "answer": "conveniente"},
        {"display": "con__ertir", "correct": "v", "answer": "convertir"},
        {"display": "con__ocar", "correct": "v", "answer": "convocar"},
        {"display": "creati__o", "correct": "v", "answer": "creativo"},
        {"display": "decisi__o", "correct": "v", "answer": "decisivo"},
        {"display": "decorati__o", "correct": "v", "answer": "decorativo"},
        {"display": "distri__uir", "correct": "b", "answer": "distribuir"},
        {"display": "di__agar", "correct": "v", "answer": "divagar"},
        {"display": "di__ergencia", "correct": "v", "answer": "divergencia"},
        {"display": "di__ulgar", "correct": "v", "answer": "divulgar"},
        {"display": "e__acuar", "correct": "v", "answer": "evacuar"},
        {"display": "e__aluar", "correct": "v", "answer": "evaluar"},
        {"display": "e__aporar", "correct": "v", "answer": "evaporar"},
        {"display": "e__asión", "correct": "v", "answer": "evasión"},
        {"display": "e__entual", "correct": "v", "answer": "eventual"},
        {"display": "e__idente", "correct": "v", "answer": "evidente"},
        {"display": "e__itar", "correct": "v", "answer": "evitar"},
        {"display": "e__ocar", "correct": "v", "answer": "evocar"},
        {"display": "e__olución", "correct": "v", "answer": "evolución"},
        {"display": "exhausi__o", "correct": "v", "answer": "exhaustivo"},
        {"display": "expansi__o", "correct": "v", "answer": "expansivo"},
        {"display": "explosi__o", "correct": "v", "answer": "explosivo"},
        {"display": "expresi__o", "correct": "v", "answer": "expresivo"},
        {"display": "extensi__o", "correct": "v", "answer": "extensivo"},
        {"display": "her__í__oro", "correct": "v", "answer": "herbívoro"},
        {"display": "informa__tivo", "correct": "t", "answer": "informativo"},
        {"display": "inno__ar", "correct": "v", "answer": "innovar"},
        {"display": "instinti__o", "correct": "v", "answer": "instintivo"},
        {"display": "in__adir", "correct": "v", "answer": "invadir"},
        {"display": "in__entariar", "correct": "v", "answer": "inventariar"},
        {"display": "in__ertir", "correct": "v", "answer": "invertir"},
        {"display": "in__estigar", "correct": "v", "answer": "investigar"},
        {"display": "la__anda", "correct": "v", "answer": "lavanda"},
        {"display": "legislati__o", "correct": "v", "answer": "legislativo"},
        {"display": "longe__o", "correct": "v", "answer": "longevo"},
        {"display": "medita__undo", "correct": "b", "answer": "meditabundo"},
        {"display": "moribundo", "correct": "b", "answer": "moribundo"},
        {"display": "nausea__undo", "correct": "b", "answer": "nauseabundo"},
        {"display": "na__egar", "correct": "v", "answer": "navegar"},
        {"display": "negati__o", "correct": "v", "answer": "negativo"},
        {"display": "normati__o", "correct": "v", "answer": "normativo"},
        {"display": "o__jetividad", "correct": "b", "answer": "objetividad"},
        {"display": "o__ligación", "correct": "b", "answer": "obligación"},
        {"display": "o__sequiar", "correct": "b", "answer": "obsequiar"},
        {"display": "o__stáculo", "correct": "b", "answer": "obstáculo"},
        {"display": "o__struir", "correct": "b", "answer": "obstruir"},
        {"display": "o__tuso", "correct": "b", "answer": "obtuso"},
        {"display": "o__vio", "correct": "b", "answer": "obvio"},
        {"display": "ofensi__o", "correct": "v", "answer": "ofensivo"},
        {"display": "operati__o", "correct": "v", "answer": "operativo"},
        {"display": "perspecti__a", "correct": "v", "answer": "perspectiva"},
        {"display": "persuasi__o", "correct": "v", "answer": "persuasivo"},
        {"display": "positi__o", "correct": "v", "answer": "positivo"},
        {"display": "preca__ido", "correct": "v", "answer": "precavido"},
        {"display": "pre__er", "correct": "v", "answer": "prever"},
        {"display": "pri__ilegio", "correct": "v", "answer": "privilegio"},
        {"display": "pro__ocar", "correct": "v", "answer": "provocar"},
        {"display": "renom__rar", "correct": "b", "answer": "renombrar"},
        {"display": "reno__ar", "correct": "v", "answer": "renovar"},
        {"display": "retri__uir", "correct": "b", "answer": "retribuir"},
        {"display": "re__isar", "correct": "v", "answer": "revisar"},
        {"display": "re__olución", "correct": "v", "answer": "revolución"},
        {"display": "sal__avidas", "correct": "v", "answer": "salvavidas"},
        {"display": "significati__o", "correct": "v", "answer": "significativo"},
        {"display": "so__erbio", "correct": "b", "answer": "soberbio"},
        {"display": "so__re__i__ir", "correct": "v", "answer": "sobrevivir"},
        {"display": "su__estimar", "correct": "b", "answer": "subestimar"},
        {"display": "su__marino", "correct": "b", "answer": "submarino"},
        {"display": "su__rayar", "correct": "b", "answer": "subrayar"},
        {"display": "su__sistir", "correct": "b", "answer": "subsistir"},
        {"display": "su__tituto", "correct": "s", "answer": "sustituto"},
        {"display": "super__i__encia", "correct": "v", "answer": "supervivencia"},
        {"display": "tur__ulencia", "correct": "b", "answer": "turbulencia"},
        {"display": "vaga__undo", "correct": "b", "answer": "vagabundo"},
        {"display": "valora__ción", "correct": "v", "answer": "valoración"},
        {"display": "ver__al", "correct": "b", "answer": "verbal"},
        {"display": "ver__ena", "correct": "b", "answer": "verbena"},
        {"display": "ver__iginoso", "correct": "t", "answer": "vertiginoso"},
        {"display": "vice__ersa", "correct": "v", "answer": "viceversa"},
        {"display": "vulnera__le", "correct": "b", "answer": "vulnerable"},
    ],
}

def initialize_bv_game():
    """Inicializa o resetea el estado del juego de B/V."""
    st.session_state.game_type = "bv"
    st.session_state.current_level = 1
    st.session_state.score = 0
    st.session_state.stars = 0
    st.session_state.used_words = []
    st.session_state.current_word = None
    st.session_state.answered = False
    st.session_state.feedback = ""
    st.session_state.show_rules = False
    load_new_word_bv()

def load_new_word_bv():
    """Carga una nueva palabra para el juego de B/V."""
    bank = WORD_BANK_BV
    available = [w for w in bank[st.session_state.current_level] if w["answer"] not in st.session_state.used_words]
    if not available:
        st.session_state.used_words = []
        available = bank[st.session_state.current_level]
    word = random.choice(available)
    st.session_state.current_word = word
    st.session_state.used_words.append(word["answer"])
    st.session_state.answered = False
    st.session_state.feedback = ""

def level_up_bv():
    """Gestiona el avance de nivel en el juego de B/V."""
    if st.session_state.current_level < max(WORD_BANK_BV.keys()):
        st.session_state.current_level += 1
        st.session_state.stars = 0
        st.session_state.used_words = []
        st.session_state.feedback = f"¡Felicidades! Has subido al nivel {st.session_state.current_level} 🚀"
    else:
        st.session_state.feedback = "¡Has completado todos los niveles de B/V! 🏆"
    load_new_word_bv()

def run_bv_game():
    """Ejecuta la interfaz y la lógica del juego de B/V."""
    st.markdown('<div class="game-container">', unsafe_allow_html=True)
    st.markdown("<h1>Juego de B o V</h1>", unsafe_allow_html=True)

    # Determinar el número total de palabras en el nivel actual
    total_words_in_level = len(WORD_BANK_BV[st.session_state.current_level])

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label=f"Nivel {st.session_state.current_level}", value=f"{st.session_state.stars} / {total_words_in_level} ★")
    with col2:
        st.metric(label="Puntuación", value=st.session_state.score)

    st.progress(min(1.0, st.session_state.stars / total_words_in_level))
    
    st.markdown(f'<div class="word-display">{st.session_state.current_word["display"]}</div>', unsafe_allow_html=True)

    # Opciones de respuesta
    cols = st.columns(2)
    options = ["b", "v"]
    for i, opt in enumerate(options):
        if cols[i].button(opt.upper(), key=f"opt_bv_{i}", disabled=st.session_state.answered, use_container_width=True):
            if opt == st.session_state.current_word["correct"]:
                st.session_state.feedback = f'¡Correcto! La palabra es "{st.session_state.current_word["answer"]}" 🎉'
                st.session_state.score += 10 * st.session_state.current_level
                st.session_state.stars += 1
                if st.session_state.stars >= total_words_in_level:
                    level_up_bv()
            else:
                st.session_state.feedback = f'Incorrecto. La palabra correcta es "{st.session_state.current_word["answer"]}"'
                if st.session_state.stars > 0:
                    st.session_state.stars -= 1
            st.session_state.answered = True
            st.rerun()

    if st.session_state.feedback:
        st.markdown(f'<div class="feedback">{st.session_state.feedback}</div>', unsafe_allow_html=True)

    # Botones de acción
    if st.session_state.answered:
        col1, col2 = st.columns(2)
        if col1.button("Siguiente", key="next_btn_bv", use_container_width=True):
            load_new_word_bv()
            st.rerun()
        if col2.button("Menú", key="menu_btn_bv", use_container_width=True):
            st.session_state.current_view = "menu"
            st.rerun()
    else:
        if st.button("Menú", key="menu_btn_bv_alt", use_container_width=True):
            st.session_state.current_view = "menu"
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
