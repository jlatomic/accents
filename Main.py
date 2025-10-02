import streamlit as st
from accents_game import run_accents_game, initialize_accents_game
from bv_game import run_bv_game, initialize_bv_game

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
