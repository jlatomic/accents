import streamlit as st
import random

# Configuración inicial de la página
st.set_page_config(page_title="Juegos de Ortografía", layout="centered")

# Estilos CSS personalizados
st.markdown("""
<style>
    div[data-testid="stToolbar"] {
    visibility: hidden;
    height: 0%;
    position: fixed;
    }
    div[data-testid="stDecoration"] {
    visibility: hidden;
    height: 0%;
    position: fixed;
    }
    div[data-testid="stStatusWidget"] {
    visibility: hidden;
    height: 0%;
    position: fixed;
    }
    #MainMenu {
    visibility: hidden;
    height: 0%;
    }
    header {
    visibility: hidden;
    height: 0%;
    }
    .main {
        background: linear-gradient(135deg, #6e8efb, #a777e3);
        padding: 10px;
    }
    .game-container, .rules-container, .menu-container {
        background: white;
        border-radius: 12px;
        padding: 16px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
        text-align: center;
        max-width: 600px;
        margin: auto;
    }
    .word-display {
        font-size: 2rem;
        margin: 20px 0;
        font-weight: bold;
        color: #e7eb08;
        min-height: 2.5rem;
    }
    .feedback {
        margin: 12px 0;
        padding: 10px;
        border-radius: 6px;
        font-weight: bold;
        min-height: auto;
        text-align: center;
        font-size: 0.95rem;
    }
    h1 {
        color: #4a5568;
        margin-bottom: 8px;
        font-size: 1.6rem;
    }
    /* Estilos para el menú principal */
    .menu-container h1 {
        font-size: 2rem;
        margin-bottom: 24px;
    }
    .menu-container .stButton button {
        height: 80px;
        font-size: 1.2rem;
        font-weight: bold;
    }

    /* En móviles: usar una sola columna para botones */
    @media (max-width: 600px) {
        .word-display {
            font-size: 1.8rem;
        }
        .stButton > button {
            width: 100% !important;
            margin-bottom: 8px;
        }
        [data-testid="column"] {
            width: 100% !important;
            display: block !important;
            margin: 0 !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- BANCO DE PALABRAS (JUEGO DE ACENTOS) ---
WORD_BANK_ACCENTS = {
    1: [{"display": "arbol", "correct": "á", "answer": "árbol"}, {"display": "cafe", "correct": "é", "answer": "café"},],
    # ... (resto de palabras de acentos)
}

# --- BANCO DE PALABRAS (JUEGO B/V) ---
WORD_BANK_BV = {
    1: [
        {"display": "cam__ión", "correct": "b", "answer": "cambión"},
        {"display": "am__iguo", "correct": "b", "answer": "ambiguo"},
        {"display": "ad__ertir", "correct": "v", "answer": "advertir"},
        {"display": "in__ierno", "correct": "v", "answer": "invierno"},
        {"display": "tam__or", "correct": "b", "answer": "tambor"},
    ],
    2: [
        {"display": "o__vio", "correct": "b", "answer": "obvio"},
        {"display": "ad__erbio", "correct": "v", "answer": "adverbio"},
        {"display": "su__marino", "correct": "b", "answer": "submarino"},
        {"display": "en__idia", "correct": "v", "answer": "envidia"},
        {"display": "a__soluto", "correct": "b", "answer": "absoluto"},
    ],
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

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label=f"Nivel {st.session_state.current_level}", value=f"{st.session_state.stars} / 5 ★")
    with col2:
        st.metric(label="Puntuación", value=st.session_state.score)

    st.progress(min(1.0, st.session_state.stars / 5))
    
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
                if st.session_state.stars >= 5:
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

# --- LÓGICA DEL JUEGO B/V ---

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

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label=f"Nivel {st.session_state.current_level}", value=f"{st.session_state.stars} / 5 ★")
    with col2:
        st.metric(label="Puntuación", value=st.session_state.score)

    st.progress(min(1.0, st.session_state.stars / 5))
    
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
                if st.session_state.stars >= 5:
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


# --- MENÚ PRINCIPAL ---

def main_menu():
    """Muestra el menú principal para seleccionar el juego."""
    st.markdown('<div class="menu-container">', unsafe_allow_html=True)
    st.markdown("<h1>Juegos de Ortografía</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    if col1.button("Juego de Acentos", key="start_accents"):
        st.session_state.current_view = "accents_game"
        initialize_accents_game()
        st.rerun()
        
    if col2.button("Juego de B o V", key="start_bv"):
        st.session_state.current_view = "bv_game"
        initialize_bv_game()
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# --- INICIALIZACIÓN Y CONTROL DE VISTA ---

if "current_view" not in st.session_state:
    st.session_state.current_view = "menu"

# Decide qué vista mostrar
if st.session_state.current_view == "menu":
    main_menu()
elif st.session_state.current_view == "accents_game":
    run_accents_game()
elif st.session_state.current_view == "bv_game":
    run_bv_game()
