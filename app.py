import streamlit as st

st.title("Quiz, konwerter i lista zakupów")

quiz, konwerter, zakupy = st.tabs(["Quiz o grach", "Konwerter jednostek", "Lista zakupów"])

with quiz:
    st.header("Quiz o grach")
    st.write("Odpowiedz na 4 pytania. Za każdą poprawną odpowiedź dostajesz 1 punkt.")

    p1 = st.radio("1. Która postać jest hydraulikiem?", ["Sonic", "Mario", "Kratos"], index=None)
    p2 = st.multiselect("2. Które gry zostały wyprodukowane przez Valve? Zaznacz wszystkie.", ["Counter-Strike 1.6", "Counter-Strike 2", "Valorant", "Fortnite"])
    p3 = st.text_input("3. Jak nazywa się zielony, wybuchający potwór w Minecraft?")
    p4 = st.number_input("4. Ilu graczy liczy jedna drużyna w standardowym meczu League of Legends?", min_value=0, max_value=20, step=1)

    if st.button("Sprawdź wynik"):
        punkty = 0
        if p1 == "Mario":
            punkty += 1
        if sorted(p2) == ["Counter-Strike 1.6", "Counter-Strike 2"]:
            punkty += 1
        if p3.strip().lower() == "creeper":
            punkty += 1
        if p4 == 5:
            punkty += 1

        st.success(f"Twój wynik: {punkty}/4 punktów")
        st.write("Poprawne odpowiedzi:")
        st.write("1. Mario")
        st.write("2. Counter-Strike 1.6 i Counter-Strike 2")
        st.write("3. Creeper")
        st.write("4. 5 graczy")

with konwerter:
    st.header("Konwerter jednostek")
    rodzaj = st.selectbox("Co chcesz przeliczyć?", ["Kilogramy na funty", "Funty na kilogramy", "Kilometry na mile", "Mile na kilometry", "Celsjusz na Fahrenheit", "Fahrenheit na Celsjusz"])
    wartosc = st.number_input("Wartość w jednostce początkowej", value=0.0)

    if st.button("Przelicz"):
        if wartosc < 0 and rodzaj in ["Kilogramy na funty", "Funty na kilogramy", "Kilometry na mile", "Mile na kilometry"]:
            st.error("Masa i odległość nie mogą być ujemne.")
        else:
            if rodzaj == "Kilogramy na funty":
                wynik = wartosc / 0.45359237
                jednostka = "lb"
            elif rodzaj == "Funty na kilogramy":
                wynik = wartosc * 0.45359237
                jednostka = "kg"
            elif rodzaj == "Kilometry na mile":
                wynik = wartosc / 1.609344
                jednostka = "mi"
            elif rodzaj == "Mile na kilometry":
                wynik = wartosc * 1.609344
                jednostka = "km"
            elif rodzaj == "Celsjusz na Fahrenheit":
                wynik = wartosc * 9 / 5 + 32
                jednostka = "°F"
            else:
                wynik = (wartosc - 32) * 5 / 9
                jednostka = "°C"

            st.success(f"Wynik: {wynik:.2f} {jednostka}")

with zakupy:
    st.header("Lista zakupów")

    if "koszyk" not in st.session_state:
        st.session_state.koszyk = {}

    produkt = st.text_input("Nazwa produktu").strip()
    if st.button("Dodaj") and produkt:
        if produkt in st.session_state.koszyk:
            st.session_state.koszyk[produkt] += 1
        else:
            st.session_state.koszyk[produkt] = 1

    if st.session_state.koszyk:
        for nazwa, ilosc in st.session_state.koszyk.items():
            st.write(f"{nazwa}: {ilosc} szt.")

        wybrany = st.selectbox("Wybierz produkt do usunięcia", list(st.session_state.koszyk))
        if st.button("Usuń"):
            st.session_state.koszyk[wybrany] -= 1
            if st.session_state.koszyk[wybrany] == 0:
                del st.session_state.koszyk[wybrany]
            st.rerun()
    else:
        st.info("Lista zakupów jest pusta.")
