import streamlit as st
import random

# --- BANCO DE PALABRAS (JUEGO DE ACENTOS) ---
WORD_BANK_ACCENTS = {
    1: [{"display": "arbol", "correct": "á", "answer": "árbol"}, {"display": "cafe", "correct": "é", "answer": "café"},],
    # ... (resto de palabras de acentos)
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

    # --- PANTALLA PRINCIPAL DEL Juego (ACENTOS) ---
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
