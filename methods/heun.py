def heun(f, x0, y0, h, xtarget):

    n = int((xtarget - x0) / h)

    x = x0
    y = y0

    tabel = []
    langkah_perhitungan = []

    for i in range(n):

        k1 = f(x, y)

        y_prediksi = y + h * k1

        k2 = f(x + h, y_prediksi)

        y_baru = y + (h / 2) * (k1 + k2)

        langkah = f"""
        Iterasi {i+1}

        k1 = f({round(x,6)}, {round(y,6)})
        = {round(k1,6)}

        Prediksi y*
        = {round(y,6)} + ({h} × {round(k1,6)})
        = {round(y_prediksi,6)}

        k2 = f({round(x+h,6)}, {round(y_prediksi,6)})
        = {round(k2,6)}

        y{i+1}
        = {round(y,6)} + ({h}/2) × ({round(k1,6)} + {round(k2,6)})
        = {round(y_baru,6)}
        """


        tabel.append({
            "iterasi": i + 1,
            "x": round(x, 6),
            "y": round(y, 6),
            "k1": round(k1, 6),
            "k2": round(k2, 6),
            "y_baru": round(y_baru, 6)
        })

        langkah_perhitungan.append(langkah)
        y = y_baru
        x = x + h

    return y, tabel, langkah_perhitungan