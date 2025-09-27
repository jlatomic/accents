import streamlit as st
import random

# Configuración inicial de la página
st.set_page_config(page_title="¡Acentos Game! - 1º ESO", layout="centered")

# Estilos CSS personalizados (similar al HTML original)
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #6e8efb, #a777e3);
        padding: 20px;
    }
    .game-container, .rules-container {
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        text-align: center;
        max-width: 600px;
        margin: auto;
    }
    .level-info {
        background: #edf2f7;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        font-weight: bold;
    }
    .word-display {
        font-size: 2.5rem;
        margin: 30px 0;
        font-weight: bold;
        color: #2d3748;
        min-height: 3rem;
    }
    .feedback {
        margin: 20px 0;
        padding: 15px;
        border-radius: 8px;
        font-weight: bold;
        min-height: 20px;
        text-align: center;
    }
    .correct {
        background: #c6f6d5;
        color: #276749;
    }
    .incorrect {
        background: #fed7d7;
        color: #9b2c2c;
    }
    .score {
        font-size: 1.2rem;
        font-weight: bold;
        margin: 20px 0;
    }
    .progress-bar {
        width: 100%;
        height: 20px;
        background: #edf2f7;
        border-radius: 10px;
        margin: 20px 0;
        overflow: hidden;
    }
    .progress {
        height: 100%;
        background: #48bb78;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    .stars {
        margin: 20px 0;
        color: #f6e05e;
        font-size: 1.5rem;
    }
    h1 {
        color: #4a5568;
        margin-bottom: 10px;
        font-size: 1.8rem;
    }
    .level-title {
        color: #2b6cb0;
        font-size: 1.3rem;
    }
    .rules-content {
        text-align: left;
        line-height: 1.6;
        font-size: 1rem;
    }
    .rules-content h2 {
        color: #2b6cb0;
        margin-top: 20px;
        border-bottom: 2px solid #ed8936;
        padding-bottom: 5px;
    }
    .rules-content ul {
        padding-left: 20px;
    }
    .rules-content li {
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Banco de palabras por niveles
WORD_BANK = {
    1: [
        {"display": "arbol", "correct": "á", "answer": "árbol"},
        {"display": "cafe", "correct": "é", "answer": "café"},
        {"display": "musica", "correct": "ú", "answer": "música"},
        {"display": "avion", "correct": "ó", "answer": "avión"},
        {"display": "dia", "correct": "í", "answer": "día"},
        {"display": "lapiz", "correct": "á", "answer": "lápiz"},
        {"display": "tunel", "correct": "ú", "answer": "túnel"},
        {"display": "telefono", "correct": "ó", "answer": "teléfono"},
        {"display": "carcel", "correct": "á", "answer": "cárcel"},
        {"display": "azucar", "correct": "ú", "answer": "azúcar"},
        {"display": "facil", "correct": "á", "answer": "fácil"},
        {"display": "bebe", "correct": "é", "answer": "bebé"},
        {"display": "jamas", "correct": "á", "answer": "jamás"},
        {"display": "ingles", "correct": "é", "answer": "inglés"},
        {"display": "camion", "correct": "ó", "answer": "camión"},
        {"display": "raton", "correct": "ó", "answer": "ratón"},
        {"display": "jabali", "correct": "í", "answer": "jabalí"},
        {"display": "buho", "correct": "ú", "answer": "búho"},
        {"display": "pais", "correct": "í", "answer": "país"},
        {"display": "sofa", "correct": "á", "answer": "sofá"},
    ],
    2: [
        {"display": "medico", "correct": "é", "answer": "médico"},
        {"display": "titulo", "correct": "í", "answer": "título"},
        {"display": "cesped", "correct": "é", "answer": "césped"},
        {"display": "angel", "correct": "á", "answer": "ángel"},
        {"display": "maquina", "correct": "á", "answer": "máquina"},
        {"display": "termino", "correct": "é", "answer": "término"},
        {"display": "pajaro", "correct": "á", "answer": "pájaro"},
        {"display": "record", "correct": "é", "answer": "récord"},
        {"display": "habil", "correct": "á", "answer": "hábil"},
        {"display": "centimo", "correct": "é", "answer": "céntimo"},
        {"display": "polvora", "correct": "ó", "answer": "pólvora"},
        {"display": "arbitro", "correct": "á", "answer": "árbitro"},
        {"display": "callate", "correct": "á", "answer": "cállate"},
        {"display": "martir", "correct": "á", "answer": "mártir"},
        {"display": "timido", "correct": "í", "answer": "tímido"},
        {"display": "fosil", "correct": "ó", "answer": "fósil"},
        {"display": "celebre", "correct": "é", "answer": "célebre"},
        {"display": "higado", "correct": "í", "answer": "hígado"},
    ],
    3: [
        {"display": "examenes", "correct": "á", "answer": "exámenes"},
        {"display": "jovenes", "correct": "ó", "answer": "jóvenes"},
        {"display": "regimen", "correct": "é", "answer": "régimen"},
        {"display": "caracter", "correct": "á", "answer": "carácter"},
        {"display": "compramelo", "correct": "ó", "answer": "cómpramelo"},
        {"display": "damelas", "correct": "á", "answer": "dámelas"},
        {"display": "rapidamente", "correct": "á", "answer": "rápidamente"},
        {"display": "logicamente", "correct": "ó", "answer": "lógicamente"},
        {"display": "fisicamente", "correct": "í", "answer": "físicamente"},
        {"display": "matematicas", "correct": "á", "answer": "matemáticas"},
        {"display": "politicas", "correct": "í", "answer": "políticas"},
        {"display": "economicas", "correct": "ó", "answer": "económicas"},
        {"display": "historicas", "correct": "ó", "answer": "históricas"},
        {"display": "geograficas", "correct": "á", "answer": "geográficas"},
        {"display": "cientificas", "correct": "í", "answer": "científicas"},
        {"display": "academicas", "correct": "é", "answer": "académicas"},
        {"display": "democraticas", "correct": "á", "answer": "democráticas"},
        {"display": "republica", "correct": "ú", "answer": "república"},
        {"display": "publico", "correct": "ú", "answer": "público"},
        {"display": "tecnicamente", "correct": "é", "answer": "técnicamente"},
    ],
    4: [
        {"display": "murcielago", "correct": "é", "answer": "murciélago"},
        {"display": "aereo", "correct": "é", "answer": "aéreo"},
        {"display": "heroe", "correct": "é", "answer": "héroe"},
        {"display": "rio", "correct": "í", "answer": "río"},
        {"display": "baul", "correct": "ú", "answer": "baúl"},
        {"display": "raiz", "correct": "í", "answer": "raíz"},
        {"display": "maiz", "correct": "í", "answer": "maíz"},
        {"display": "ataud", "correct": "ú", "answer": "ataúd"},
        {"display": "reir", "correct": "í", "answer": "reír"},
        {"display": "oir", "correct": "í", "answer": "oír"},
        {"display": "freir", "correct": "í", "answer": "freír"},
        {"display": "sonreir", "correct": "í", "answer": "sonreír"},
        {"display": "caidas", "correct": "í", "answer": "caídas"},
        {"display": "leismo", "correct": "í", "answer": "leísmo"},
        {"display": "tia", "correct": "í", "answer": "tía"},
        {"display": "pua", "correct": "ú", "answer": "púa"},
        {"display": "buho", "correct": "ú", "answer": "búho"},
        {"display": "pais", "correct": "í", "answer": "país"},
    ],
    5: [
        {"display": "cuidate", "correct": "í", "answer": "cuídate"},
        {"display": "apreciais", "correct": "á", "answer": "apreciáis"},
        {"display": "evaluais", "correct": "á", "answer": "evaluáis"},
        {"display": "actueis", "correct": "ú", "answer": "actuéis"},
        {"display": "continue", "correct": "ú", "answer": "continúe"},
        {"display": "evalue", "correct": "ú", "answer": "evalúe"},
        {"display": "guion", "correct": "sin acento", "answer": "guión"},
        {"display": "fie", "correct": "sin acento", "answer": "fié"},
        {"display": "liais", "correct": "sin acento", "answer": "liáis"},
        {"display": "truhan", "correct": "sin acento", "answer": "truhán"},
        {"display": "fuer", "correct": "sin acento", "answer": "fué"},
        {"display": "carmen", "correct": "sin acento", "answer": "Carmen"},
        {"display": "angel", "correct": "sin acento", "answer": "Ángel"},
        {"display": "album", "correct": "sin acento", "answer": "álbum"},
        {"display": "movil", "correct": "sin acento", "answer": "móvil"},
    ]
}

# Mapeo para mostrar botones
OPTION_LABELS = {
    "á": "Acento en á",
    "é": "Acento en é",
    "í": "Acento en í",
    "ó": "Acento en ó",
    "ú": "Acento en ú",
    "sin acento": "Sin acento"
}

# Inicializar estado de sesión
if "current_level" not in st.session_state:
    st.session_state.current_level = 1
    st.session_state.score = 0
    st.session_state.stars = 0
    st.session_state.used_words = []
    st.session_state.current_word = None
    st.session_state.answered = False
    st.session_state.feedback = ""
    st.session_state.feedback_class = ""
    st.session_state.show_rules = False

# Función para cargar nueva palabra
def load_new_word():
    available = [w for w in WORD_BANK[st.session_state.current_level] if w["display"] not in st.session_state.used_words]
    if not available:
        st.session_state.used_words = []
        available = WORD_BANK[st.session_state.current_level]
    word = random.choice(available)
    st.session_state.current_word = word
    st.session_state.used_words.append(word["display"])
    st.session_state.answered = False
    st.session_state.feedback = ""
    st.session_state.feedback_class = ""

# Función para subir de nivel
def level_up():
    if st.session_state.current_level < 5:
        st.session_state.current_level += 1
        st.session_state.stars = 0
        st.session_state.used_words = []
        st.session_state.feedback = f"¡Felicidades! Has subido al nivel {st.session_state.current_level} 🚀"
        st.session_state.feedback_class = "correct"
    else:
        st.session_state.feedback = "¡Has completado todos los niveles! ¡Eres un maestro de los acentos! 🏆"
        st.session_state.feedback_class = "correct"

# Cargar primera palabra si no hay
if st.session_state.current_word is None:
    load_new_word()

# Función para mostrar reglas
def show_rules():
    st.session_state.show_rules = True

def hide_rules():
    st.session_state.show_rules = False

# === INTERFAZ ===

if st.session_state.show_rules:
    # Pantalla de reglas
    st.markdown('<div class="rules-container">', unsafe_allow_html=True)
    st.markdown("<h1>Reglas de Acentuación</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="rules-content">
        <h2>1. Palabras Agudas</h2>
        <p>Llevan el acento en la última sílaba. Se acentúan cuando terminan en vocal, -n o -s.</p>
        <ul>
            <li>café, jamás, también, compás</li>
            <li>jabalí, marroquí, hindú</li>
        </ul>
        
        <h2>2. Palabras Llanas o Graves</h2>
        <p>Llevan el acento en la penúltima sílaba. Se acentúan cuando NO terminan en vocal, -n o -s.</p>
        <ul>
            <li>lápiz, árbol, fácil, cárcel</li>
            <li>mármol, ángel, Pérez</li>
        </ul>
        
        <h2>3. Palabras Esdrújulas</h2>
        <p>Llevan el acento en la antepenúltima sílaba. Siempre llevan tilde.</p>
        <ul>
            <li>música, teléfono, América</li>
            <li>cámara, médico, película</li>
        </ul>
        
        <h2>4. Palabras Sobreesdrújulas</h2>
        <p>Llevan el acento antes de la antepenúltima sílaba. Siempre llevan tilde.</p>
        <ul>
            <li>dígamelo, cómpraselo, llévamelo</li>
            <li>cuéntaselo, déjamelo</li>
        </ul>
        
        <h2>5. Diptongos, Triptongos y Hiatos</h2>
        <ul>
            <li><strong>Diptongos:</strong> Combinación de dos vocales en una misma sílaba (ai, au, ei, eu, oi, ou, ia, ie, io, iu, ua, ue, uo). Se acentúa según las reglas generales.</li>
            <li><strong>Triptongos:</strong> Combinación de tres vocales en una misma sílaba (iai, iau, uai, uei...). Se acentúa según las reglas generales.</li>
            <li><strong>Hiatos:</strong> Dos vocales juntas pero en sílabas diferentes. Siempre se acentúa la vocal cerrada (i, u) cuando va con vocal abierta (a, e, o).</li>
            <ul>
                <li>pa-ís, ba-úl, ra-íz, son-re-ír</li>
            </ul>
        </ul>
        
        <h2>6. Acento Diacrítico</h2>
        <p>Se usa para diferenciar palabras que se escriben igual pero tienen distinto significado.</p>
        <ul>
            <li>tú (pronombre) vs tu (posesivo)</li>
            <li>él (pronombre) vs el (artículo)</li>
            <li>sí (afirmación) vs si (condicional)</li>
            <li>mí (pronombre) vs mi (posesivo)</li>
            <li>té (bebida) vs te (pronombre)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Volver al juego", key="back_btn", use_container_width=True):
        hide_rules()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # Pantalla del juego
    st.markdown('<div class="game-container">', unsafe_allow_html=True)
    st.markdown("<h1>¡Acentos Game!</h1>", unsafe_allow_html=True)
    
    # Información del nivel
    st.markdown(f"""
    <div class="level-info">
        <div class="level-title">Nivel: {st.session_state.current_level}</div>
        <div class="stars">★ {st.session_state.stars} / 5</div>
    </div>
    <div class="score">Puntuación: {st.session_state.score}</div>
    """, unsafe_allow_html=True)
    
    # Barra de progreso
    progress = min(100, (st.session_state.stars / 5) * 100)
    st.markdown(f"""
    <div class="progress-bar">
        <div class="progress" style="width: {progress}%"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Palabra a acentuar
    st.markdown(f'<div class="word-display">{st.session_state.current_word["display"]}</div>', unsafe_allow_html=True)
    
    # Opciones
    cols = st.columns(2)
    options = ["á", "é", "í", "ó", "ú", "sin acento"]
    for i, opt in enumerate(options):
        col = cols[i % 2]
        if col.button(OPTION_LABELS[opt], key=f"opt_{i}", disabled=st.session_state.answered, use_container_width=True):
            # Verificar respuesta
            if opt == st.session_state.current_word["correct"]:
                st.session_state.feedback = f'¡Correcto! La palabra es "{st.session_state.current_word["answer"]}" 🎉'
                st.session_state.feedback_class = "correct"
                st.session_state.score += 10 * st.session_state.current_level
                st.session_state.stars += 1
                if st.session_state.stars >= 5:
                    level_up()
            else:
                st.session_state.feedback = f'Incorrecto. La respuesta correcta era: {OPTION_LABELS[st.session_state.current_word["correct"]]}. La palabra es "{st.session_state.current_word["answer"]}"'
                st.session_state.feedback_class = "incorrect"
                if st.session_state.stars > 0:
                    st.session_state.stars -= 1
            st.session_state.answered = True
            st.rerun()
    
    # Feedback
    if st.session_state.feedback:
        cls = st.session_state.feedback_class
        st.markdown(f'<div class="feedback {cls}">{st.session_state.feedback}</div>', unsafe_allow_html=True)
    
    # Botón "Siguiente palabra"
    if st.session_state.answered:
        if st.button("Siguiente palabra", key="next_btn", use_container_width=True):
            load_new_word()
            st.rerun()
    
    # Botón "Reglas"
    if st.button("Reglas de acentuación", key="rules_btn", use_container_width=True):
        show_rules()
    
    st.markdown('</div>', unsafe_allow_html=True)