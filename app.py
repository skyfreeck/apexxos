import streamlit as st
import pandas as pd

# ==========================================
# KONFIGURACE SYSTÉMU & F1 KARBONOVÝ DESIGN
# ==========================================
st.set_page_config(
    page_title="APEX OS // MICHAL KASTNER",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp {
        background-color: #0a0b0e;
        color: #f0f2f6;
    }
    h1, h2, h3 {
        font-family: 'Inter', 'Segoe UI', Roboto, sans-serif;
        font-weight: 800 !important;
        letter-spacing: -0.5px;
        text-transform: uppercase;
    }
    h1 {
        color: #ff2b2b !important;
        border-bottom: 2px solid #ff2b2b;
        padding-bottom: 10px;
    }
    div[data-testid="stMetric"] {
        background-color: #14171f;
        border: 1px solid #262b38;
        border-left: 4px solid #ff2b2b;
        padding: 15px;
        border-radius: 6px;
    }
    section[data-testid="stSidebar"] {
        background-color: #0f1117;
        border-right: 1px solid #262b38;
    }
    .apex-box {
        background-color: #14171f;
        border: 1px solid #2a3040;
        border-radius: 8px;
        padding: 18px;
        margin-bottom: 15px;
    }
    .chem-highlight {
        color: #00f2fe;
        font-weight: bold;
        font-size: 1.15rem;
    }
    .ego-quote {
        background: linear-gradient(90deg, #1f0a0a 0%, #14171f 100%);
        border-left: 4px solid #ff2b2b;
        padding: 12px 18px;
        font-style: italic;
        color: #ff9494;
        margin-bottom: 20px;
    }
    .rpg-card {
        background: linear-gradient(135deg, #14171f 0%, #1f141a 100%);
        border: 2px solid #ff2b2b;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR: OPERAČNÍ PROFIL & LIVE BIO-STATUS
# ==========================================
with st.sidebar:
    st.markdown("## ⚡ PROJEKT APEX // OS v1.0")
    st.caption("OPERÁTOR: **MICHAL KASTNER** (24. 8. 2008)")
    st.caption("LOKACE: **Lenešice / Most (ČR)**")
    st.divider()

    st.markdown("### 🧬 LIVE KALIBRACE ŠASI")
    current_weight = st.slider("Aktuální ranní váha (kg)", 74.0, 86.0, 82.5, 0.1)
    current_ftp = st.slider("Aktuální Bike FTP - LT2 (W)", 260, 340, 275, 1)
    target_cda = st.number_input("Aerodynamický koeficient CdA", value=0.193, step=0.001, format="%.3f")

    w_kg = round(current_ftp / current_weight, 2)
    lt1_watts = round(current_ftp * 0.81)

    st.metric("Aktuální poměr W/kg (LT2)", f"{w_kg} W/kg", f"{round((current_ftp/76.5) - w_kg, 2)} W/kg potenciál na 76.5 kg")
    st.metric("Závodní 70.3 LT1 strop", f"{lt1_watts} W", f"{round(lt1_watts / current_weight, 2)} W/kg")

    st.divider()
    st.markdown("### 🌙 NOČNÍ PROTOKOL (21:45)")
    c1, c2 = st.columns(2)
    c1.checkbox("5g Glycinu", value=False)
    c2.checkbox("400mg Mg", value=False)
    st.checkbox("Vycházka s Messíčkem (Z1)", value=False)
    st.checkbox("Anki Právo (PF UK)", value=False)

# ==========================================
# HLAVNÍ HLAVIČKA
# ==========================================
st.title("PROJEKT APEX // PERFORMANCE COMMAND CENTER")
st.markdown(
    '<div class="ego-quote">'
    '„Zatímco průměrní hledají výmluvy a spí, já s CdA 0.193 a chirurgickou přesností buduju impérium. '
    'Gamifikovaný motor opraven a spuštěn. Každý watt je XP.“'
    '</div>',
    unsafe_allow_html=True
)

tab0, tab1, tab2, tab3, tab4 = st.tabs([
    "🎮 0. APEX RPG & HABITS",
    "🔬 1. BIOCHEMIE & STRAVA",
    "📅 2. MĚSÍČNÍ KALENDÁŘ",
    "📊 3. TELEMETRIE & SIMULÁTOR",
    "⚖️ 4. PF UK & @KastnerTri"
])

# ==========================================
# TAB 0: GAMIFIKOVANÝ HABIT TRACKER & RPG
# ==========================================
with tab0:
    st.subheader("🎮 APEX RPG HABIT TRACKER // DOPAMINE ENGINE")
    st.caption("Za každý splněný protokol sbíráš XP. Za porušení disciplíny nebo lenost systém XP nekompromisně strhává.")

    st.markdown("#### ⚡ DNEŠNÍ OPERAČNÍ ÚKOLY (DOBÝVÁNÍ XP)")
    col_h1, col_h2 = st.columns(2)

    with col_h1:
        h_train = st.checkbox("🔥 Odjet hlavní trénink (Norská metoda / LT1 / LT2) [+250 XP]")
        h_chem = st.checkbox("🧪 Přesně namíchaná chemie v lahvích (Malto+Fruktóza+Citrát) [+100 XP]")
        h_diet = st.checkbox("🥩 Dodrženy denní kotvy stravy (185g B, 75g T, správné sacharidy) [+150 XP]")
        h_law = st.checkbox("⚖️ Anki kartičky / Kazuistika PF UK (min. 20 min) [+100 XP]")

    with col_h2:
        h_dog = st.checkbox("🐕 Svižná Z1 vycházka s Messíčkem [+75 XP]")
        h_night = st.checkbox("🌙 Noční protokol (Glycin + Mg) před spaním [+50 XP]")
        h_aero = st.checkbox("⏱️ 100% držení aero pozice v FastTT nástavcích [+100 XP]")
        h_fail = st.checkbox("⚠️ PORUŠENÍ DISCIPLÍNY (Jalové Z3, prokrastinace) [-200 XP]")

    gained_xp = 0
    if h_train: gained_xp += 250
    if h_chem: gained_xp += 100
    if h_diet: gained_xp += 150
    if h_law: gained_xp += 100
    if h_dog: gained_xp += 75
    if h_night: gained_xp += 50
    if h_aero: gained_xp += 100
    if h_fail: gained_xp -= 200

    base_xp = 1850 
    total_xp = base_xp + gained_xp

    level = (total_xp // 500) + 1
    xp_in_level = total_xp % 500
    progress_pct = min(1.0, xp_in_level / 500.0)

    if level < 3:
        title_rank = "Novice Rookie (Učedník z Mostu)"
    elif level < 6:
        title_rank = "Ironman Finisher (Sub-5h Breaker)"
    elif level < 9:
        title_rank = "Elite Age Grouper (Norský Prahový Drtič)"
    else:
        title_rank = "Apex Overlord (Kona World Championship Contender)"

    st.markdown(f"""
    <div class="rpg-card">
        <h3>🏆 STATUS OPERÁTORA: LEVEL {level}</h3>
        <p><b>Titul:</b> <span class="chem-highlight">{title_rank}</span></p>
        <p><b>Celkové XP:</b> {total_xp} XP &nbsp;|&nbsp; <b>Dnešní přírůstek:</b> {gained_xp} XP</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"**Progress do Levelu {level + 1} ({xp_in_level} / 500 XP):**")
    st.progress(progress_pct)

    st.divider()
    st.markdown("#### 🔥 DOPAMINOVÝ ARCHIV & STREAKY")
    col_s1, col_s2, col_s3 = st.columns(3)
    col_s1.metric("Aktivní Streak", "14 dní", "+2 dny od Erkneru")
    col_s2.metric("Norská Prahová Compliance", "98.5%", "Chirurgická přesnost")
    col_s3.metric("Závodní Připravenost Kona", "74%", "Cesta k 4:20:00")

# ==========================================
# TAB 1: BIOCHEMICKÁ LABORATOŘ & STRAVA
# ==========================================
with tab1:
    col_chem, col_food = st.columns([1.1, 1])

    with col_chem:
        st.subheader("🧪 SMART BOTTLE MIXER (PALIVOVÁ LABORATOŘ)")
        st.caption("Výpočet přesné gramáže pro maltodextrin, fruktózu, citrát sodný (23,5 % Na) a kyselinu citronovou.")

        with st.container():
            c_dur, c_carb = st.columns(2)
            workout_duration = c_dur.slider("Délka tréninku (minuty)", 30, 300, 90, 5)
            carbs_per_hour = c_carb.slider("Cílová dávka sacharidů (g / hod)", 0, 120, 90, 5)

            c_na, c_bot = st.columns(2)
            sodium_per_hour = c_na.slider("Cílový čistý sodík Na (mg / hod)", 300, 1500, 800, 50)
            bottles_count = c_bot.selectbox("Počet lahví (750 ml)", [1, 2, 3, 4], index=0)

            hours = workout_duration / 60.0
            total_carbs = round(carbs_per_hour * hours, 1)
            total_sodium_mg = round(sodium_per_hour * hours)

            if carbs_per_hour >= 75:
                ratio_label = "1 : 0.8 (Elitní vysokokapacitní absorpce SGLT1 + GLUT5)"
                malto_total = round(total_carbs * (1 / 1.8), 1)
                fructo_total = round(total_carbs * (0.8 / 1.8), 1)
            else:
                ratio_label = "2 : 1 (Standardní glukózo-fruktózový poměr)"
                malto_total = round(total_carbs * (2 / 3), 1)
                fructo_total = round(total_carbs * (1 / 3), 1)

            sodium_citrate_g = round(total_sodium_mg / 235.0, 2)
            citric_acid_g = round(max(1.0, sodium_citrate_g * 0.5), 1)

            st.markdown(f"""
            <div class="apex-box">
                <h4>📌 CELKOVÁ NAVÁŽKA NA TRÉNINK ({workout_duration} min | Poměr {ratio_label})</h4>
                <ul>
                    <li>Celkem sacharidů v tréninku: <span class="chem-highlight">{total_carbs} g</span></li>
                    <li><b>Maltodextrin:</b> <span class="chem-highlight">{malto_total} g</span> &nbsp;({round(malto_total/bottles_count, 1)} g / láhev)</li>
                    <li><b>Fruktóza:</b> <span class="chem-highlight">{fructo_total} g</span> &nbsp;({round(fructo_total/bottles_count, 1)} g / láhev)</li>
                    <li><b>Citrát sodný:</b> <span class="chem-highlight">{sodium_citrate_g} g</span> &nbsp;({round(sodium_citrate_g/bottles_count, 2)} g / láhev) ➡️ dodá <b>{total_sodium_mg} mg</b> čistého Na</li>
                    <li><b>Kyselina citronová:</b> <span class="chem-highlight">{citric_acid_g} g</span> &nbsp;({round(citric_acid_g/bottles_count, 1)} g / láhev)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    with col_food:
        st.subheader("🥩 MODULÁRNÍ STRAVA (2 KOTVY + 1 PROMĚNNÁ)")
        st.caption("Kalorický deficit -400 až -500 kcal/den směrem k závodní váze 76,5 kg.")

        day_type = st.radio(
            "Vyber typ dne podle tréninkové zátěže:",
            [
                "DEN A: Volno / Plavání / Krátký Z1 (2 350 kcal | 230 g S)",
                "DEN B: Střední Z2 objem / Posilovna (2 950 kcal | 380 g S)",
                "DEN C: Double-Threshold / Dlouhý blok (3 750 kcal | 580 g S)"
            ],
            index=2
        )

        if "DEN A" in day_type:
            target_day_carbs = 230
            target_kcal = 2350
            protocol_note = "Večer NULA komplexních sacharidů! Pouze bílkovina + tuk + zelenina."
        elif "DEN B" in day_type:
            target_day_carbs = 380
            target_kcal = 2950
            protocol_note = "Sacharidy soustřeď ke snídani, obědu a v okně kolem tréninku."
        else:
            target_day_carbs = 580
            target_kcal = 3750
            protocol_note = "Plné krytí prahové práce v kalorickém deficitu."

        remaining_solid_carbs = max(0.0, round(target_day_carbs - total_carbs, 1))
        equiv_rice_raw = round(remaining_solid_carbs / 0.78)
        equiv_potatoes = round(remaining_solid_carbs / 0.17)

        st.markdown(f"""
        <div class="apex-box">
            <h4>🎯 DENNÍ BILANCE MIMO TRÉNINKOVÉ LAHVE</h4>
            <p><b>Pevná Kotva 1 (Bílkoviny):</b> 185 g | <b>Pevná Kotva 2 (Tuky):</b> 75 g</p>
            <p><b>Celkový limit sacharidů:</b> {target_day_carbs} g ({target_kcal} kcal)</p>
            <p><b>Vypito v chemii:</b> -{total_carbs} g S</p>
            <hr style="border-color: #262b38;">
            <p>🍽️ <b>ZBÝVÁ SNÍST V PEVNÉM JÍDLE: <span class="chem-highlight">{remaining_solid_carbs} g sacharidů</span></b></p>
            <p style="font-size:0.9rem; color:#a0aab8;">
                Odpovídá např. <b>{equiv_rice_raw} g</b> rýže (suchý stav) NEBO <b>{equiv_potatoes} g</b> brambor.<br>
                <i>⚡ {protocol_note}</i>
            </p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# TAB 2: INTERAKTIVNÍ MĚSÍČNÍ KALENDÁŘ
# ==========================================
with tab2:
    st.subheader("📅 INTERAKTIVNÍ MĚSÍČNÍ KALENDÁŘ (16. ŘÍJNA – 15. LISTOPADU 2026)")
    st.caption("Přehledný kalendář tréninkových bloků, zátěže a akademických povinností.")

    calendar_data = [
        {"Datum": "Pá 16.10.", "Typ dne": "DEN C", "Hlavní blok": "Split-Threshold (Kolo LT1 + Běh LT2)", "Škola": "SŠDVS + Anki Právo"},
        {"Datum": "So 17.10.", "Typ dne": "DEN B", "Hlavní blok": "Plavání drily + 150 min Z2 Kolo", "Škola": "Víkend"},
        {"Datum": "Ne 18.10.", "Typ dne": "DEN B", "Hlavní blok": "90 min Z2 Běh + Max Strength Gym", "Škola": "Kazuistiky Trestní právo"},
        {"Datum": "Po 19.10.", "Typ dne": "DEN A", "Hlavní blok": "Plavání (Hypoxie) + Z1 Vycházka s Messíčkem", "Škola": "SŠDVS Most"},
        {"Datum": "Út 20.10.", "Typ dne": "DEN C", "Hlavní blok": "Norský Double-Threshold (Kolo LT2 + Běh LT1)", "Škola": "SŠDVS Most"},
        {"Datum": "St 21.10.", "Typ dne": "DEN B", "Hlavní blok": "90 min Z2 Kompenzace (Kolo)", "Škola": "SŠDVS + PF UK přednáška"},
        {"Datum": "Čt 22.10.", "Typ dne": "DEN A", "Hlavní blok": "Běh (Alphafly rovinky) + Core Gym", "Škola": "SŠDVS Most"},
        {"Datum": "Pá 23.10.", "Typ dne": "DEN C", "Hlavní blok": "Double-Threshold (Kolo LT1 + Běh LT2)", "Škola": "SŠDVS Most"},
        {"Datum": "So 24.10.", "Typ dne": "DEN B", "Hlavní blok": "2500 m Plavání + 3h Z2 Kolo", "Škola": "Víkend"},
        {"Datum": "Ne 25.10.", "Typ dne": "DEN A", "Hlavní blok": "45 min Z1 Regenerační klus + Mobilita", "Škola": "Víkend"},
        {"Datum": "Po 26.10.", "Typ dne": "DEN B", "Hlavní blok": "Kolo LT2 Intervaly (4× 10 min)", "Škola": "SŠDVS Most"},
        {"Datum": "Út 27.10.", "Typ dne": "DEN C", "Hlavní blok": "Norský Double-Threshold (Kolo + Běh)", "Škola": "SŠDVS Most"},
        {"Datum": "St 28.10.", "Typ dne": "DEN A", "Hlavní blok": "Státní svátek: 3500 m Plavání + Běh Z2", "Škola": "Volno (Svátek)"},
        {"Datum": "Čt 29.10.", "Typ dne": "DEN B", "Hlavní blok": "Běh LT2 intervaly + Gym", "Škola": "SŠDVS Most"},
        {"Datum": "Pá 30.10.", "Typ dne": "DEN C", "Hlavní blok": "Split-Threshold Brick", "Škola": "SŠDVS Most"},
        {"Datum": "So 31.10.", "Typ dne": "DEN B", "Hlavní blok": "CSS Plavecký test + 2.5h Kolo", "Škola": "Víkend"},
        {"Datum": "Ne 1.11.", "Typ dne": "DEN B", "Hlavní blok": "100 min Dlouhý běh + Síla", "Škola": "Víkend"},
        {"Datum": "Po 2.11.", "Typ dne": "DEN A", "Hlavní blok": "Plavání technika + Z1 Messíček", "Škola": "SŠDVS Most"},
        {"Datum": "Út 3.11.", "Typ dne": "DEN C", "Hlavní blok": "Norský Double-Threshold", "Škola": "SŠDVS Most"},
        {"Datum": "St 4.11.", "Typ dne": "DEN B", "Hlavní blok": "90 min Z2 Kolo", "Škola": "SŠDVS Most"},
        {"Datum": "Čt 5.11.", "Typ dne": "DEN A", "Hlavní blok": "Běh + Alphafly rovinky", "Škola": "SŠDVS Most"},
        {"Datum": "Pá 6.11.", "Typ dne": "DEN C", "Hlavní blok": "Split-Threshold Brick", "Škola": "SŠDVS Most"},
        {"Datum": "So 7.11.", "Typ dne": "DEN B", "Hlavní blok": "3h Kolo + Plavání vytrvalost", "Škola": "Víkend"},
        {"Datum": "Ne 8.11.", "Typ dne": "DEN B", "Hlavní blok": "105 min Dlouhý běh + Gym", "Škola": "Víkend"},
        {"Datum": "Po 9.11.", "Typ dne": "DEN A", "Hlavní blok": "Regenerace & Plavání", "Škola": "SŠDVS Most"},
        {"Datum": "Út 10.11.", "Typ dne": "DEN C", "Hlavní blok": "Norský Double-Threshold", "Škola": "SŠDVS Most"},
        {"Datum": "St 11.11.", "Typ dne": "DEN B", "Hlavní blok": "90 min Z2 Kolo", "Škola": "SŠDVS Most"},
        {"Datum": "Čt 12.11.", "Typ dne": "DEN A", "Hlavní blok": "Běh + Alphafly rovinky", "Škola": "SŠDVS Most"},
        {"Datum": "Pá 13.11.", "Typ dne": "DEN C", "Hlavní blok": "Split-Threshold Brick", "Škola": "SŠDVS Most"},
        {"Datum": "So 14.11.", "Typ dne": "DEN B", "Hlavní blok": "3.5h Z2 Kolo (Vrchol objemu)", "Škola": "Víkend"},
        {"Datum": "Ne 15.11.", "Typ dne": "DEN B", "Hlavní blok": "110 min Dlouhý běh + Síla", "Škola": "Víkend"}
    ]

    df_cal = pd.DataFrame(calendar_data)
    st.dataframe(df_cal, use_container_width=True, hide_index=True)

# ==========================================
# TAB 3: TELEMETRIE, ZÓNY & SIMULÁTOR KONY
# ==========================================
with tab3:
    st.subheader("📊 SIMULÁTOR DOMINANCE (PŘEPOČET ČASU IM 70.3 DLE VÁHY A FTP)")
    st.caption("Model vychází z tvé telemetrie IM 70.3 Erkner (04:48:20 | NP 229 W | Běh 1:49:28 | Depa 8:46).")

    weight_diff = 83.8 - current_weight
    ftp_diff = current_ftp - 275

    run_Minutes_saved_weight = (weight_diff * 46.4) / 60.0
    bike_minutes_saved = (ftp_diff * 0.22) + (weight_diff * 0.25)
    transition_saved = 5.0

    total_minutes_saved = round(run_Minutes_saved_weight + bike_minutes_saved + transition_saved, 1)
    erkner_total_min = 4 * 60 + 48.33
    projected_total_min = erkner_total_min - total_minutes_saved
    proj_h = int(projected_total_min // 60)
    proj_m = int(projected_total_min % 60)
    proj_s = int((projected_total_min - int(projected_total_min)) * 60)

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Erkner 70.3 Baseline", "04:48:20", "NP 229 W | 83.8 kg")
    m2.metric("Simulovaný 70.3 Čas", f"0{proj_h}:{proj_m:02d}:{proj_s:02d}", f"-{total_minutes_saved} min", delta_color="normal")
    m3.metric("Úspora na půlmaratonu", f"-{round(run_Minutes_saved_weight, 1)} min", f"Při váze {current_weight} kg v Alphafly 3")
    m4.metric("Úspora v depech", "-5.0 min", "Cíl pod 03:45 celkem")

    st.divider()
    col_z_bike, col_z_run = st.columns(2)

    with col_z_bike:
        st.markdown("#### 🚴‍♂️ DYNAMICKÉ ZÓNY – KOLO (Kú Cycle TF1)")
        df_bike = pd.DataFrame({
            "Zóna": ["Z1 (Recovery)", "Z2 (Norský LIT)", "LT1 (70.3 Aero Práh)", "LT2 (Norský Threshold)", "Z5 (VO2max)"],
            "Watty (W)": [
                f"< {round(current_ftp*0.55)} W",
                f"{round(current_ftp*0.56)} – {round(current_ftp*0.74)} W",
                f"{round(current_ftp*0.78)} – {round(current_ftp*0.84)} W",
                f"{round(current_ftp*0.93)} – {round(current_ftp*1.02)} W",
                f"{round(current_ftp*1.06)} – {round(current_ftp*1.20)} W"
            ],
            "TF (bpm)": ["< 130", "130 – 152", "158 – 170", "172 – 181", "> 182"],
            "Laktát": ["< 1.0 mmol/L", "1.0 – 1.4 mmol/L", "1.5 – 2.2 mmol/L", "2.8 – 3.8 mmol/L", "> 5.0 mmol/L"]
        })
        st.dataframe(df_bike, use_container_width=True, hide_index=True)

    with col_z_run:
        st.markdown("#### 👟 BĚŽECKÉ ZÓNY & PŘIŘAZENÍ ARZENÁLU")
        df_run = pd.DataFrame({
            "Zóna": ["Z1 (Recovery)", "Z2 (Norský LIT)", "LT1 (Spodní práh)", "LT2 (Horní práh)", "Z5 (VO2max)"],
            "Tempo (/km)": ["> 6:05", "5:40 – 6:00", "5:15 – 5:22", "4:42 – 4:50", "4:15 – 4:32"],
            "TF (bpm)": ["< 138", "138 – 155", "160 – 168", "174 – 181", "> 183"],
            "Předepsaná obuv": ["Asics Trabuco Max 4", "Asics Trabuco Max 4", "Adidas Boston 13", "Adidas Boston 13", "Nike Alphafly 3"]
        })
        st.dataframe(df_run, use_container_width=True, hide_index=True)

# ==========================================
# TAB 4: PF UK KRIMINALISTIKA & @KastnerTri
# ==========================================
with tab4:
    c_law, c_brand = st.columns(2)

    with c_law:
        st.subheader("⚖️ PF UK: DEDUKČNÍ & PRÁVNÍ TRENAŽÉR")
        case = st.selectbox("Vyber denní kazuistiku / dril:", [
            "Kazuistika #1: Nutná obrana vs. Krajní nouze (§ 28 a § 29 TZ)",
            "Kazuistika #2: Nepřímý úmysl (Dolus eventualis) vs. Vědomá nedbalost",
            "Kriminalistika #3: Taktika výslechu a detekce kognitivní zátěže"
        ])
        if "Kazuistika #1" in case:
            st.info("**Zadání:** Útočník s nožem vybíhá proti obránci. Obránce vytáhne legálně drženou zbraň a střelí útočníka do hrudníku, přestože měl možnost utéct do otevřených dveří za sebou. Jedná se o exces z nutné obrany?")
            if st.button("Zobrazit elitní právní argumentaci"):
                st.success("**Verdikt (Subsidiarita se neuplatní):** Nejedná se o exces. Na rozdíl od krajní nouze (§ 29 TZ) neplatí u nutné obrany (§ 28 TZ) podmínka subsidiarity. Obránce NENÍ povinen před útokem utíkat ani se vyhýbat – právo nemusí ustupovat bezpráví.")
        elif "Kazuistika #2" in case:
            st.info("**Zadání:** Řidič v noci předjíždí přes plnou čáru v nepřehledné zatáčce rychlostí 140 km/h. Spoléhá na to, že je špičkový řidič a že v noci nikdo nepojede. Dojde k čelnímu střetu. Jde o nepřímý úmysl nebo vědomou nedbalost?")
            if st.button("Zobrazit elitní právní argumentaci"):
                st.success("**Verdikt:** Rozhodující je kriterium 'rozumného důvodu' k spolehnutí se, že následek nenastane. Pokud řidič nemá absolutně žádnou vizuální kontrolu nad protisměrem, spolehnutí se na 'náhodu, že nikdo nejede' je natolik iracionální, že judikatura NS ČR přechází z vědomé nedbalosti do **nepřímého úmyslu (srozumění)**.")
        else:
            st.info("**Zadání:** Při výslechu podezřelého chceš odhalit vykonstruované alibi. Jak využiješ princip kognitivní zátěže?")
            if st.button("Zobrazit elitní kriminalistickou taktiku"):
                st.success("**Verdikt:** Lhaní vyžaduje 3× vyšší kapacitu pracovní paměti než vybavování reálné epizodické stopy. Přikaž vyslýchanému odvyprávět událost v **obráceném chronologickém pořadí** a současně udržovat oční kontakt.")

    with c_brand:
        st.subheader("📲 @KastnerTri // REELS SCÉNÁŘ ENGINE")
        reel_theme = st.selectbox("Vyber koncept pro Instagram Reels:", [
            "Reels #1: -45 kg Transformace -> Kú Cycle F1 Estetika",
            "Reels #2: Biochemická laboratoř v kuchyni (100g/h protokol)",
            "Reels #3: Erkner 4:48:20 Forenzní odhalení slabin"
        ])
        if "Reels #1" in reel_theme:
            st.code("""[HOOK - 0:00-0:02] (Záběr na starou fotku 135 kg -> tvrdý střih na Kú Cycle TF1)
TEXT NA OBRAZOVCE: "Říkali, že se 135 kily nikdy nebudu rychlý."
[BODY - 0:02-0:08] (Rychlé prostřihy: wattmetr Quarq, obouvání Shimano S-Phyre RC903)
TEXT: "-45 kg. 87 km ultramaraton. CdA 0.193 v Alkmaaru. Half-Ironman za 4:48 v 18 letech."
[CTA - 0:08-0:12]
TEXT: "Tohle byl jen tutoriál. Sleduj cestu do Kony. @KastnerTri x @KuCycle" """, language="markdown")
        elif "Reels #2" in reel_theme:
            st.code("""[HOOK - 0:00-0:02] (Pohled shora na digitální váhu, sypání prášku do lahve)
TEXT: "Proč 90 % triatletů na 15. kilometru běhu vytuhne?"
[BODY - 0:02-0:09]
TEXT: "Protože hádají, místo aby počítali. 100 g sacharidů a 1000 mg sodíku na hodinu v aero pozici."
[CTA - 0:09-0:12]
TEXT: "Tělo je Formule 1. Krm ho tak. @KastnerTri x @FSPerformance" """, language="markdown")
        else:
            st.code("""[HOOK - 0:00-0:02] (Záběr na graf z TrainingPeaks - 229 W NP a čas 4:48:20)
TEXT: "4:48:20 na Ironman 70.3 Erkner v 18 letech. Dobrý? Ne. Tady jsem nechal 25 minut."
[BODY - 0:02-0:09]
TEXT: "1. 176 tepů ve vodě. 2. Skoro 9 minut v depech. 3. 6 kg nad závodní váhou."
[CTA - 0:09-0:12]
TEXT: "Zima patří těm, co makají potmě. Příští rok jdeme pod 4:20." """, language="markdown")